## About this repo
Use this repo to add time stamp overlays to videos for annotation. The script first adds time stamp overlay from the file name and then stitches the videos together into a single mp4 file.

## Insert blank videos
The video capturing tool might have lags when it stops recording the current video and starts recording the sibsequent video. Thus, to add blank frames in between to make labeling more convinint, run the following command.


`python insert_blank_videos.py path_to_blank_video.mp4 folder_path_with_multiple_videos`


Please perform this step first if there are gaps between multiple videos. This script will save the right sized blank mp4 videos with appropriate file names in the folder with multiple videos. Once done, you can run the script below to add time stamp overlays and stitch them together.


## Install dependencies
Make sure to install all the dependencies using the following command.

`pip install -r requirements.txt`

## Run the script
To run the script, type the following command.


`python overlay_multiple_videos.py folder_path_with_multiple_videos number_of_cores`


The folder path is the path to folder that contains all the mp4 videos collected during data collection. For paralellel processing please provide the number of cores to be used (e.g., 4 or 8). The output is saved in multiple_videos_folder/stamped/stitched/

