from pytorch_lightning import seed_everything
import argparse

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
        "--model",
        type=str,
        help="backbone model",
    )
    parser.add_argument(
        "--config",
        type=str,
        default="configs/stable-diffusion/v2-inference.yaml",
        help="path to config which constructs model",
    )
    parser.add_argument(
        "--ckpt",
        type=str,
        help="path to checkpoint of model",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="the seed (for reproducible sampling)",
    )
    parser.add_argument(
        "--precision",
        type=str,
        help="evaluate at this precision",
        choices=["full", "autocast"],
        default="autocast"
    )
    opt = parser.parse_args()
    return opt

def main(opt):
    seed_everything(opt.seed)

