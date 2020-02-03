import json
import os

# something2_train_json = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something-something-v2-train.json'
# something2_validation_json = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something-something-v2-validation.json'
something2_test_json = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something-something-v2-test.json'
# something2_labels_json = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something-something-v2-labels.json'

# something2_trainlist = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something_v2_trainlist.txt'
# something2_vallist = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something_v2_vallist.txt'
something2_testlist = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something_v2_testlist.txt'

something2_vids_dir = '/home/xqzhu/something_v2_dataset/videos/20bn-sth-sth-v2-jpg/'


with open(something2_test_json, 'r') as f:
    sth2_test = json.load(f)

test_clean = []
sth2_vids = os.listdir(something2_vids_dir)

for x in sth2_test:
    temp_dict = {}
    temp_dict['id'] = x['id']
    temp_dict['label_id'] = '0'
    temp_dict['vid_dir'] = os.path.join(something2_vids_dir, temp_dict['id'])
    temp_dict['n_frames'] = len(os.listdir(temp_dict['vid_dir']))
    test_clean.append(' '.join([temp_dict['vid_dir'], 
                                str(temp_dict['n_frames']), 
                                temp_dict['label_id']]))

with open(something2_testlist, 'w') as f:
    for line in test_clean:
        f.write(line+'\n')
