import argparse

parser = argparse.ArgumentParser(description="Change something file path")
parser.add_argument('old_rgb_list', type=str)
parser.add_argument('new_rgb_list', type=str)
args = parser.parse_args()

old_dir = '/home/xqzhu/something_v1_dataset/videos/' + \
    '20bn-something-something-v1/'
new_dir = '/home/yjz/xqzhu_proj/abilip_key/dataset/' + \
    '20bn-something-something-v1/'

# old_dir = '/home/xqzhu/something_v2_dataset/videos/20bn-sth-sth-v2-jpg/'
# new_dir = '/home/xqzhu/something_v2_dataset/flow/'

with open(args.old_rgb_list, 'r') as f:
    data = f.readlines()

new_data = []
for line in data:
    rgb_d, rgb_f, rgb_l = line.strip().split()
    flow_d = rgb_d.replace(old_dir, new_dir)
    flow_f = rgb_f
    flow_l = rgb_l
    new_line = ' '.join((flow_d, flow_f, flow_l))
    new_data.append(new_line)

with open(args.new_rgb_list, 'w') as f:
    for line in new_data:
        f.write(line + '\n')
