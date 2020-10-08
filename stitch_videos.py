import ffmpeg
import os
import sys
from os import sep
import time
import subprocess

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
print("# All the files to be stitched here", file=file_list_txt)
for file_name in stamped_files:
    if not file_name.endswith('.txt'):
        final_video_files.append(file_name)
        print("file " + "'" + file_name + "'", file=file_list_txt)


print("Input folder: " + str(stamped_folder + sep + 'file_list.txt'))

file_list = open(stamped_folder + sep + 'file_list.txt', 'w')
video_files = stamped_folder + sep + 'file_list.txt'
final_output_loc = stamped_folder + sep + 'stitched'
if not os.path.exists(final_output_loc):
    os.makedirs(final_output_loc)

final_output = final_output_loc + sep + 'stitched.mp4'

try:
    os.remove(final_output_loc + sep + 'stitched.mp4')
except OSError:
    pass

# merge the video files
cmd = ["ffmpeg",
       "-f",
       "concat",
       "-safe",
       "0",
       "-loglevel",
       "quiet",
       "-i",
       "%s" % video_files,
       "-c",
       "copy",
       "%s" % final_output
       ]


start = time.time()

p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

fout = p.stdin
fout.close()

print(p.returncode)
if p.returncode != 0:
    raise subprocess.CalledProcessError(p.returncode, cmd)

end = time.time()
print("Merging videos took", end - start, " seconds.")


# print("test command:::: " + 'ffmpeg -f concat -safe 0 -i ' + str(stamped_folder + sep + 'file_list.txt') + ' -c copy ' +
#       str(stamped_folder + sep + 'output.mp4'))
#
# # Run the os command for ffmpeg concatination
# os.system('ffmpeg -f concat -safe 0 -i ' + str(stamped_folder + sep + 'file_list.txt') + ' -c copy ' +
#           str(stamped_folder + sep + 'output.mp4'))
