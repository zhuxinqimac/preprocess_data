import os
import argparse

parser = argparse.ArgumentParser(
        description='modify ucf101 lists from devcube3 to DEVBOX')
parser.add_argument('old_list', type=str)
parser.add_argument('new_list', type=str)
args = parser.parse_args()

old_vid_path = '/home/xinqizhu/UCF101_frames/'
new_vid_path = '/home/xqzhu/ucf101_dataset/UCF101_frames/'

with open(args.old_list, 'r') as f:
    data = f.readlines()

with open(args.new_list, 'w') as f:
    for line in data:
        temp_items = line.strip().split()
        old_path, n_frames, label = temp_items[0], temp_items[1], temp_items[2]
        new_path = old_path.replace(old_vid_path, new_vid_path)
        new_line = ' '.join([new_path, n_frames, label])
        f.write(new_line+'\n')
