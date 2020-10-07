import ffmpeg
import os
import sys
from os import sep

in_file = sys.argv[1]
stamped_folder = in_file + sep + 'stamped'
# stamped_files = os.listdir(stamped_folder)
stamped_files = []
final_output = stamped_folder + sep + 'combined'
file_list_txt = open(stamped_folder + sep + 'file_list.txt', 'w')

for dirpath, dirnmaes, filenames in os.walk(stamped_folder):
    for file in filenames:
        stamped_files.append(os.path.join(os.path.abspath(dirpath), file))

final_video_files = []

# Save the files into a text file
for file_name in stamped_files:
    if not file_name.endswith('.txt'):
        final_video_files.append(file_name)
        print("file " + "'" + file_name + "'", file=file_list_txt)

# ffmpeg.concat(stamped_files).output(final_output + sep + 'combined.mp4').run()

# file_1 = ffmpeg.input(final_video_files[0])
# file_2 = ffmpeg.input(final_video_files[1])
#
# ffmpeg.concat(file_1, file_2).output(stamped_folder + sep + 'output.mp4')

print("Input folder: " + str(stamped_folder + sep + 'file_list.txt'))

# Run the os command for ffmpeg concatination
os.system('ffmpeg -f concat -safe 0 -i ' + str(stamped_folder + sep + 'file_list.txt') + ' -c copy ' +
          str(stamped_folder + sep + 'output.mp4'))
