import sys
import os
from os import sep
from overlay_time_stamp import add_timestamp_overlay

in_folder = sys.argv[1]

video_file_list = os.listdir(in_folder)

print('Video files found: ' + str(video_file_list))

for video_file in video_file_list:
    print('processing: ' + str(video_file))
    add_timestamp_overlay(in_folder, video_file, None, False, True)
    # os.system('python overlay_time_stamp.py ' + in_folder + ' ' + str(video_file))

# Call video stitching
os.system('python stitch_videos.py ' + str(in_folder))
