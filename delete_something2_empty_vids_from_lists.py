import os
import argparse

parser = argparse.ArgumentParser(description="delete_something2_empty_vids_from_lists")
parser.add_argument('origin_flow_list', type=str)
parser.add_argument('new_list', type=str)
args = parser.parse_args()

empty_txt = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/empty_flow_vids.txt'

with open(args.origin_flow_list, 'r') as f:
    data = f.readlines()

with open(empty_txt, 'r') as f:
    empty_list_origin = f.readlines()
empty_list = []
for line in empty_list_origin:
    empty_list.append(line.strip())

new_lines = []
for line in data:
    path, n_frames, label = line.strip().split()
    if not(path.split('/')[-1] in empty_list):
        new_lines.append(line)

with open(args.new_list, 'w') as f:
    for line in new_lines:
        f.write(line)
