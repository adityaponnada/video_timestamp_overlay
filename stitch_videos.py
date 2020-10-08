import os
import sys
from os import sep
import time
import subprocess

in_file = sys.argv[1]
stamped_folder = in_file + sep + 'stamped'
file_list_txt = open(stamped_folder + sep + 'file_list.txt', 'w')
stitched_output_name = 'stitched.mp4'
stamped_files = []
final_output_loc = stamped_folder + sep + 'stitched'
if not os.path.exists(final_output_loc):
    os.makedirs(final_output_loc)

final_output = final_output_loc + sep + stitched_output_name

try:
    os.remove(final_output_loc + sep + stitched_output_name)
except OSError:
    pass

start = time.time()
for root, dirs, files in os.walk(stamped_folder):
    for file in files:
        if file.endswith('.mp4'):
            file_to_add = os.path.join(os.path.abspath(root), file)
            print("File to add: " + str(file_to_add))
            file_list_txt.write("file '%s'\n" % file_to_add)
file_list_txt.close()
video_files = stamped_folder + sep + 'file_list.txt'

print("Input text file: " + str(video_files))

# merge the video files
cmd = ["ffmpeg",
       "-f",
       "concat",
       "-safe",
       "0",
       # "-loglevel",
       # "quiet",
       "-i",
       "%s" % video_files,
       "-c",
       "copy",
       "%s" % final_output
       ]

print("Command is: " + str(cmd))
p = subprocess.run(cmd, capture_output=True, shell=True)

if p.returncode != 0:
    raise subprocess.CalledProcessError(p.returncode, cmd)

end = time.time()
print("Merging videos took", end - start, " seconds.")

# Remvoe the temp file.txt
os.remove(video_files)
