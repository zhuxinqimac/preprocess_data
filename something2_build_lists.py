import json
import os

something2_train_json = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something-something-v2-train.json'
something2_validation_json = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something-something-v2-validation.json'
something2_labels_json = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something-something-v2-labels.json'

something2_trainlist = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something_v2_trainlist.txt'
something2_vallist = '/home/xqzhu/repo/tsn-bilinear/something_v2_list/something_v2_vallist.txt'

something2_vids_dir = '/home/xqzhu/something_v2_dataset/videos/20bn-sth-sth-v2-jpg/'


with open(something2_labels_json, 'r') as f:
    sth2_labels = json.load(f)

with open(something2_validation_json, 'r') as f:
    sth2_val = json.load(f)

with open(something2_train_json, 'r') as f:
    sth2_train = json.load(f)

train_clean = []
val_clean = []
sth2_vids = os.listdir(something2_vids_dir)

for x in sth2_train:
    temp_template = x['template']
    temp_template = temp_template.replace('[', '')
    temp_template = temp_template.replace(']', '')
    temp_dict = {'id':x['id'], 'template':temp_template}
    if not (temp_dict['id'] in sth2_vids):
        print('in train processing, vid ', temp_dict['id'], ' is not missed!')
    else:
        temp_dict['label_id'] = sth2_labels[temp_dict['template']]
        temp_dict['vid_dir'] = os.path.join(something2_vids_dir, temp_dict['id'])
        temp_dict['n_frames'] = len(os.listdir(temp_dict['vid_dir']))
        train_clean.append(' '.join([temp_dict['vid_dir'], 
                                    str(temp_dict['n_frames']), 
                                    temp_dict['label_id']]))

with open(something2_trainlist, 'w') as f:
    for line in train_clean:
        f.write(line+'\n')

        
for x in sth2_val:
    temp_template = x['template']
    temp_template = temp_template.replace('[', '')
    temp_template = temp_template.replace(']', '')
    temp_dict = {'id':x['id'], 'template':temp_template}
    if not (temp_dict['id'] in sth2_vids):
        print('in val processing, vid ', temp_dict['id'], ' is not missed!')
    else:
        temp_dict['label_id'] = sth2_labels[temp_dict['template']]
        temp_dict['vid_dir'] = os.path.join(something2_vids_dir, temp_dict['id'])
        temp_dict['n_frames'] = len(os.listdir(temp_dict['vid_dir']))
        val_clean.append(' '.join([temp_dict['vid_dir'], 
                                    str(temp_dict['n_frames']), 
                                    temp_dict['label_id']]))

with open(something2_vallist, 'w') as f:
    for line in val_clean:
        f.write(line+'\n')

