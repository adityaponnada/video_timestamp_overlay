import sys
import os
from os import sep
from overlay_time_stamp import add_timestamp_overlay
from multiprocessing import Pool

if __name__ == "__main__":

    in_folder = sys.argv[1]

    cores = int(sys.argv[2])

    video_file_list = os.listdir(in_folder)
    video_file_list = list(
        filter(lambda f: f.endswith('mp4'), video_file_list))

    print('Video files found: ' + str(video_file_list))

    with Pool(processes=cores) as pp:
        for video_file in video_file_list:
            print('processing: ' + str(video_file))
            stamped_video_file = os.path.join(in_folder, 'stamped', os.path.basename(
                video_file).replace('.mp4', '_stamped.mp4'))
            print(stamped_video_file)
            if os.path.exists(stamped_video_file):
                print(f'{stamped_video_file} was already stamped, skip it')
            else:
                p = pp.apply_async(add_timestamp_overlay, args=(
                    in_folder, video_file, None, False, True))
        # os.system('python overlay_time_stamp.py ' + in_folder + ' ' + str(video_file))
        pp.close()
        pp.join()
    # Call video stitching
    os.system('python stitch_videos.py ' + str(in_folder))
