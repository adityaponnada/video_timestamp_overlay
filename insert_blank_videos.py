import sys
import os
from os import sep, path
import datetime
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Path to the blank video
blank_video_path = 'blank.mp4'

# path to the list of video files
video_files_path = sys.argv[1]

FIXED_VIDEO_LENGTH = 10 * 60

video_files_list = os.listdir(video_files_path)


def get_time_from_filename(file):
    # first remove extension
    filename = file[: -4]
    # split by components
    file_name_parts = filename.split('_')
    init_letters = file_name_parts[0]
    date_time_string = file_name_parts[1] + '-' + file_name_parts[2] + '-' + file_name_parts[3] + ' ' + \
                       file_name_parts[4] + ':' + file_name_parts[5] + ':' + file_name_parts[6]
    date_time_obj = datetime.datetime.strptime(date_time_string, '%Y-%m-%d %H:%M:%S')
    return init_letters, date_time_obj


def generate_file_name(init_chars, date_time):
    date_time_string = date_time.strftime('%Y_%m_%d_%H_%M_%S')
    file_name = init_chars + '_' + date_time_string + '.mp4'
    return file_name


def trim_video(video_file, trim_time, output_loc):
    ffmpeg_extract_subclip(video_file, 0, trim_time, targetname=output_loc)


for i in range(len(video_files_list)):
    print(video_files_list[i])
    if i < len(video_files_list) - 1:
        file_1_init, file_1_time = get_time_from_filename(video_files_list[i])
        file_2_init, file_2_time = get_time_from_filename(video_files_list[i + 1])
        time_lag = file_2_time - (file_1_time + datetime.timedelta(seconds=FIXED_VIDEO_LENGTH))
        time_lag = time_lag.total_seconds()
        blank_start_time = file_1_time + datetime.timedelta(seconds=FIXED_VIDEO_LENGTH)
        blank_video_loc = video_files_path + sep + generate_file_name(file_1_init, blank_start_time)
        trim_video(blank_video_path, time_lag, blank_video_loc)


