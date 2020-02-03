import os

something_v1_labels_path = '/home/xqzhu/repo/tsn-bilinear/something_v1_list/something-something-v1-labels.csv'
dataset_path = '/home/xqzhu/something_v1_dataset/videos/20bn-something-something-v1'

files_input = '/home/xqzhu/repo/tsn-bilinear/something_v1_list/something-something-v1-test.csv'
files_output = '/home/xqzhu/repo/tsn-bilinear/something_v1_list/something_v1_testlist.txt'

with open(files_input) as f:
    lines = f.readlines()

folders = []
idx_categories = []
for line in lines:
    line = line.strip()
    folders.append(line)
    idx_categories.append(0)

output = []
for i in range(len(folders)):
    curFolder = folders[i]
    curIDX = idx_categories[i]
    out_dir_name = os.path.join(dataset_path, curFolder)
    dir_files = os.listdir(out_dir_name)
    output.append('%s %d %d'%(out_dir_name, len(dir_files), curIDX))

with open(files_output, 'w') as f:
    f.write('\n'.join(output))
