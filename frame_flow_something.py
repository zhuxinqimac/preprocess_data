__author__ = 'yjxiong'
# modified by Xinqi Zhu

import os
import glob
import sys
from pipes import quote
from multiprocessing import Pool, current_process

import argparse
out_path = ''


def run_optical_flow(vid_item, dev_id=0):
    vid_path = vid_item[0]
    vid_id = vid_item[1]
    vid_name = vid_path.split('/')[-1]
    out_full_path = os.path.join(out_path, vid_name)
    try:
        os.mkdir(out_full_path)
    except OSError:
        pass

    current = current_process()
    dev_id = (int(current._identity[0]) - 1) % NUM_GPU
    image_path = '{}/img'.format(out_full_path)
    flow_x_path = '{}/flow_x'.format(out_full_path)
    flow_y_path = '{}/flow_y'.format(out_full_path)

    cmd = os.path.join(df_path, 'denseFlow_gpu')+' -f {}/%05d.jpg -x {} -y {} -i {} -b 20 -t 1 -d {} -s 1 -w {} -h {}'.format(
        quote(vid_path), quote(flow_x_path), quote(flow_y_path), quote(image_path), dev_id, new_size[0], new_size[1])

    os.system(cmd)
    print( '{} {} done'.format(vid_id, vid_name))
    sys.stdout.flush()
    return True


# def run_warp_optical_flow(vid_item, dev_id=0):
    # vid_path = vid_item[0]
    # vid_id = vid_item[1]
    # vid_name = vid_path.split('/')[-1].split('.')[0]
    # out_full_path = os.path.join(out_path, vid_name)
    # try:
        # os.mkdir(out_full_path)
    # except OSError:
        # pass

    # current = current_process()
    # dev_id = (int(current._identity[0]) - 1) % NUM_GPU
    # flow_x_path = '{}/flow_x'.format(out_full_path)
    # flow_y_path = '{}/flow_y'.format(out_full_path)

    # cmd = os.path.join(df_path + 'build/extract_warp_gpu')+' -f {} -x {} -y {} -b 20 -t 1 -d {} -s 1'.format(
        # vid_path, flow_x_path, flow_y_path, dev_id)

    # os.system(cmd)
    # print( 'warp on {} {} done'.format(vid_id, vid_name))
    # sys.stdout.flush()
    # return True


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
        print( "creating folder: "+out_path)
        os.makedirs(out_path)

    vid_list = glob.glob(os.path.join(src_path, '*'))
    print( len(vid_list))
    pool = Pool(num_worker)
    if mode == 'debug':
        if flow_type == 'tvl1':
            pool.map(run_optical_flow, zip(vid_list[:2], range(2)))
        elif flow_type == 'warp_tvl1':
            pool.map(run_warp_optical_flow, zip(vid_list[:2], range(2)))
    else:
        if flow_type == 'tvl1':
            pool.map(run_optical_flow, zip(vid_list, range(len(vid_list))))
        elif flow_type == 'warp_tvl1':
            pool.map(run_warp_optical_flow, zip(vid_list, range(len(vid_list))))
