import os
import argparse

parser = argparse.ArgumentParser(description="Convert something rgblist to flowlist")
parser.add_argument('rgb_list', type=str)
parser.add_argument('flow_list', type=str)
args = parser.parse_args()

# rgb_dir = '/home/xqzhu/something_v1_dataset/videos/20bn-something-something-v1/'
# flow_dir = '/home/xqzhu/something_v1_dataset/flows/'

rgb_dir = '/home/xqzhu/something_v2_dataset/videos/20bn-sth-sth-v2-jpg/'
flow_dir = '/home/xqzhu/something_v2_dataset/flow/'

with open(args.rgb_list, 'r') as f:
    data = f.readlines()

flow_data = []
for line in data:
    rgb_d, rgb_f, rgb_l = line.strip().split()
    flow_d = rgb_d.replace(rgb_dir, flow_dir)
    flow_f = str(int(rgb_f)-1)
    flow_l = rgb_l
    new_line = ' '.join((flow_d, flow_f, flow_l))
    flow_data.append(new_line)

with open(args.flow_list, 'w') as f:
    for line in flow_data:
        f.write(line+'\n')
