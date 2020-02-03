from __future__ import print_function, division
import os
import sys
import subprocess

def class_process(dir_path, dst_dir_path):
  if not os.path.exists(dst_dir_path):
    os.mkdir(dst_dir_path)

  num_files = 0
  for file_name in os.listdir(dir_path):
    # if ('.avi' not in file_name) and ('.mp4' not in file_name):
      # continue
    name, ext = os.path.splitext(file_name)
    dst_directory_path = os.path.join(dst_dir_path, name)

    video_file_path = os.path.join(dir_path, file_name)
    try:
      if os.path.exists(dst_directory_path):
        if not os.path.exists(os.path.join(dst_directory_path, '00001.jpg')):
          subprocess.call('rm -r \"{}\"'.format(dst_directory_path), shell=True)
          print('remove {}'.format(dst_directory_path))
          os.mkdir(dst_directory_path)
        else:
          continue
      else:
        os.mkdir(dst_directory_path)
    except:
      print(dst_directory_path, 'problem')
      continue
    cmd = 'ffmpeg -i \"{}\" \"{}/%05d.jpg\"'.format(video_file_path, dst_directory_path)
    # cmd = 'ffmpeg -i \"{}\" -vf scale=-1:256 \"{}/image_%05d.jpg\"'.format(video_file_path, dst_directory_path)
    print(cmd)
    num_files += 1
    subprocess.call(cmd, shell=True)
    print('\n')
  num_out = len(os.listdir(dst_class_path))
  with open('vids_count.txt', 'a') as f:
    f.write('in_vids: '+str(num_files)+'\n')
  with open('out_count.txt', 'a') as f:
    f.write('out_vids: '+str(num_out)+'\n')


if __name__=="__main__":
  dir_path = sys.argv[1]
  dst_dir_path = sys.argv[2]

  with open('vids_count.txt', 'w') as f:
    f.write('')
  with open('out_count.txt', 'w') as f:
    f.write('')

class_process(dir_path, dst_dir_path)
