#!/usr/bin/python
#-*- coding: utf-8 -*-

# >.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.
# Licensed under the Apache License, Version 2.0 (the "License")
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# --- File Name: CelebA_crop.py
# --- Creation Date: 03-02-2020
# --- Last Modified: Mon 03 Feb 2020 17:42:09 AEDT
# --- Author: Xinqi Zhu
# .<.<.<.<.<.<.<.<.<.<.<.<.<.<.<.<
"""
Crop CelebA aligned version to a certain size.
* The original image dimension is: [178 x 218].
"""

import os
import argparse
import os
import pdb
import glob

from PIL import Image


def main():
    parser = argparse.ArgumentParser(description='Crop CelebA images.')
    parser.add_argument('--source_dir',
                        help='Source directory.',
                        type=str,
                        default='/mnt/hdd/Datasets/CelebA_dataset/celeba_img')
    parser.add_argument('--result_dir',
                        help='Results directory.',
                        type=str,
                        default='/mnt/hdd/Datasets/CelebA_dataset/celeba_128')
    parser.add_argument('--height',
                        help='Height and width of new images.',
                        type=int,
                        default=128)
    args = parser.parse_args()
    args.width = args.height

    if not os.path.exists(args.result_dir):
        os.makedirs(args.result_dir)

    orig_img_names = os.listdir(args.source_dir)
    # orig_img_names = glob.glob(os.path.join(args.source_dir, '*.jpg'))
    for orig_img_name in orig_img_names:
        # with open(orig_img_name, 'r') as f:
        image = Image.open(os.path.join(args.source_dir, orig_img_name))
        x_0 = (178 - args.width) // 2
        y_0 = (218 - args.height) // 2
        cropped_image = image.crop(
            (x_0, y_0, x_0 + args.width, y_0 + args.height))
        new_img_name = orig_img_name
        cropped_image.save(os.path.join(args.result_dir, new_img_name))


if __name__ == "__main__":
    main()
