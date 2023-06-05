import os
import sys
import argparse
import numpy as np 

import torch 
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.utils.data.distributed import DistributedSampler
from torch.cuda.amp import autocast

from dataset.dataloader_train import TrainDataAugmentation, TrainData
from dataset.dataloader_test import TestDataAugmentation, TestData

import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
torch.multiprocessing.set_sharing_strategy('file_system')


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--gpus', type=int, default=1, help='Number of gpus')
    parser.add_argument('--local_rank', type=int, default=0, help='local rank')
    parser.add_argument('--world_size', default=1, type=int, help='number of distributed processes')
    return parser.parse_args()

def get_model(args):

    return

def setup(local_rank):
    torch.cuda.set_device(local_rank)
    dist.init_process_group(backend='nccl',init_method='env://')

def cleanup():
    dist.destroy_process_group()

def train_process(args, local_rank):
    seed = args.seed
    torch.manual_seed(seed)

    train_transform= TrainDataAugmentation(args)
    test_transform= TestDataAugmentation(args)
    train_dataset=TrainData(args,transform=train_transform)
    train_sampler= DistributedSampler(train_dataset)
    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, sampler=train_sampler, num_workers=8)
    test_dataset=TestData(args,transform=test_transform)
    test_sampler = DistributedSampler(test_dataset)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size, sampler=test_sampler, num_workers=8)
    
    model = get_model(args)
    model = torch.nn.SyncBatchNorm.convert_sync_batchnorm(model) # 全局同步BN
    model = DDP(model.cuda(),device_ids=[local_rank], output_device=local_rank, find_unused_parameters=False)
    
    train_loop(args, model, train_loader, test_loader)

def train_loop(args, model, trainloader, testloader):
    local_rank = dist.get_rank()
    scaler = torch.cuda.amp.GradScaler()

    if args.optim=='adam':
        optimizer = torch.optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=args.lr, betas=(0.9,0.98), weight_decay=0.0005, eps=1e-5)
    if args.optim == 'adagrad':
        optimizer = torch.optim.Adagrad(filter(lambda p: p.requires_grad, model.parameters()), lr=args.lr, weight_decay=0.0005)
        
    if args.lr_schedule=='milestone':
        milestones = [i for i in range(50, args.epochs, 50)]
        scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=milestones, gamma=0.8)  # three step decay
    elif args.lr_schedule=='cosine':
        scheduler =  torch.optim.lr_scheduler.CosineAnnealingLR(optimizer = optimizer, T_max =  args.epochs) #  * iters 

    if dist.get_rank() == 0 and ckpt_path is not None:
        model.load_state_dict(torch.load(ckpt_path))

    for epoch in range(args.currEpoch, args.epochs + args.currEpoch):
        if args.train:
            trainLosses=[]
            model.train()
            trainloader.sampler.set_epoch(epoch)
            pbar = enumerate(trainloader)
            for iters, (_, _, data, _) in pbar:
                # print(data.shape)
                with autocast():
                    data = data.to(local_rank, non_blocking=True)
                    optimizer.zero_grad()
                    outputs=model(data)
                    rec_loss = nn.MSELoss(reduction='none')
                    rec = rec_loss(outputs, data)
                    loss = 0.5 * rec.sum(dim=(1,2,3,4)).mean()
                    
                scaler.scale(loss).backward()
                scaler.step(optimizer)
                scaler.update()
                dist.all_reduce(loss.div_(torch.cuda.device_count()))

                train_loss =loss.cpu().detach().numpy()
                trainLosses.append(train_loss)
                if iters % args.log_intv == 0 and local_rank==0:
                    print('epoch:', epoch, 
                          iters, "/", len(trainloader) ,
                          "loss: ",np.mean(trainLosses),
                          "lr: ", optimizer.state_dict()['param_groups'][0]['lr'])
            torch.cuda.empty_cache()
            scheduler.step()    

        if dist.get_rank() == 0:
            torch.save(model.module.state_dict(), "%d.ckpt" % epoch)

def main(args):
    n_gpus = torch.cuda.device_count()
    device_ids =list(range(n_gpus))
    os.environ["CUDA_VISIBLE_DEVICES"] = ",".join(map(str, device_ids))
    local_rank=int(os.getenv('LOCAL_RANK', -1))
    setup(local_rank)
    train_process(args, local_rank)
    cleanup()


if __name__ == '__main__':
    args = get_args()
    main(args)
