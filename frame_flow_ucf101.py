from __future__ import print_function

import os
import sys
import glob
import time
import argparse
from pipes import quote
from multiprocessing import Pool, current_process


# def run_optical_flow(vid_item):
    # vid_path = vid_item[0]
    # vid_id = vid_item[1]
    # vid_class_name = vid_path.split('/')[-2]
    # vid_name = vid_path.split('/')[-1]
    # out_full_path = os.path.join(out_path, vid_class_name, vid_name)
    # try:
        # os.mkdir(out_full_path)
    # except OSError:
        # pass

    # current = current_process()
    # dev_id = (int(current._identity[0]) - 1) % NUM_GPU
    # # flow_x_path = '{}/flow_x'.format(out_full_path)
    # # flow_y_path = '{}/flow_y'.format(out_full_path)

    # # cmd = os.path.join(df_path + 'build/extract_gpu')+' -f {} -x {} -y {} -i {} -b 20 -t 1 -d {} -s 1 -o {} -w {} -h {}'.format(
        # # quote(vid_path), quote(flow_x_path), quote(flow_y_path), quote(image_path), dev_id, out_format, new_size[0], new_size[1])
    # # cmd = os.path.join(df_path, 'flow_video ')+'-p {} -o {} {}/image_%05d.jpg'.format(
            # # quote(proc_type), quote(out_full_path), quote(vid_path))
    # cmd = os.path.join(df_path, 'denseFlow_gpu')+' -f {}/image_%05d.jpg -x {} -y {} -i {} -b 20 -t 1 -d {} -s 1 -w {} -h {}'.format(
        # quote(vid_path), quote(flow_x_path), quote(flow_y_path), quote(image_path), dev_id, new_size[0], new_size[1])

    # os.system(cmd)
    # print('{} {} done'.format(vid_id, vid_name))
    # sys.stdout.flush()
    # return True

def run_optical_flow(vid_item, dev_id=0):
    vid_path = vid_item[0]
    vid_id = vid_item[1]
    vid_name = vid_path.split('/')[-1]
    vid_category = vid_path.split('/')[-2]
    out_full_path = os.path.join(out_path, vid_category, vid_name)
    try:
        # os.mkdir(out_full_path)
        os.makedirs(out_full_path)
    except OSError:
        pass

    current = current_process()
    dev_id = (int(current._identity[0]) - 1) % NUM_GPU
    image_path = '{}/image'.format(out_full_path)
    flow_x_path = '{}/flow_x'.format(out_full_path)
    flow_y_path = '{}/flow_y'.format(out_full_path)

    cmd = os.path.join(df_path, 'denseFlow_gpu')+' -f {}/image_%05d.jpg -x {} -y {} -i {} -b 20 -t 1 -d {} -s 1 -w {} -h {}'.format(
        quote(vid_path), quote(flow_x_path), quote(flow_y_path), quote(image_path), dev_id, new_size[0], new_size[1])

    os.system(cmd)
    print( '{} {} done'.format(vid_id, vid_name))
    sys.stdout.flush()
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="extract optical flows")
    parser.add_argument("src_dir")
    parser.add_argument("out_dir")
    parser.add_argument("--num_worker", type=int, default=32)
    parser.add_argument("--flow_type", type=str, default='tvl1', choices=['tvl1', 'warp_tvl1'])
    parser.add_argument("--df_path", type=str, default='/home/xqzhu/repo/denseFlow_gpu/', help='path to the dense_flow toolbox')
    parser.add_argument("--new_width", type=int, default=0, help='resize image width')
    parser.add_argument("--new_height", type=int, default=0, help='resize image height')
    parser.add_argument("--num_gpu", type=int, default=4, help='number of GPU')
    parser.add_argument("--mode", type=str, default='debug', choices=['debug', 'run'])

    args = parser.parse_args()

    out_path = args.out_dir
    src_path = args.src_dir
    num_worker = args.num_worker
    flow_type = args.flow_type
    df_path = args.df_path
    new_size = (args.new_width, args.new_height)
    NUM_GPU = args.num_gpu
    mode = args.mode

    if not os.path.isdir(out_path):
        print("creating folder: "+out_path)
        os.makedirs(out_path)

    vid_list = glob.glob(src_path+'/*/*')
    print('no. videos:', len(vid_list))
    pool = Pool(num_worker)
    start_time = time.time()
    pool.map(run_optical_flow, zip(vid_list, range(len(vid_list))))
    end_time = time.time()
    print('processing time:', end_time-start_time)

