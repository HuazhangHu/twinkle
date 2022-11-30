from pytorch_lightning import seed_everything
import argparse
import yaml
from omegaconf import OmegaConf

def read_yaml2(yaml_path):
    '''
    using omegaconf to read yaml file
    '''
    config = OmegaConf.load(yaml_path)
    # print('type:{type(conf)}')
    # print(config.model.optimization)
    # print(config.params.learning_rate)
    # print(config.model.model_name)
    
    return config

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--batch",
        type=int,
        default="16",
        help="batchsize"
    )
    parser.add_argument(
        "--GPU",
        type=int,
        default=2,
        help="num of frame",
    )
    parser.add_argument(
        "--config",
        type=str,
        default="test.yaml",
        help="path to config which constructs model",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="seed everything"
    )
    opt = parser.parse_args()
    return opt

def main(opt):
    seed_everything(opt.seed)
    config=read_yaml2(opt.config)
    print(config.model.optimization)
    print(config.params.learning_rate)
    print(config.model.model_name)


if __name__ == "__main__":
    opt=parse_args()
    main(opt)
