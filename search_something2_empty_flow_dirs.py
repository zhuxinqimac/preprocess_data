import os

flow_dir = '/home/xqzhu/something_v2_dataset/flow/'

out_file = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/empty_flow_vids.txt'
vids_names = os.listdir(flow_dir)

empty_vids = []
for vid in vids_names:
    temp_path = os.path.join(flow_dir, vid)
    if len(os.listdir(temp_path)) == 0:
        empty_vids.append(vid)

with open(out_file, 'w') as f:
    for line in empty_vids:
        f.write(line+'\n')
