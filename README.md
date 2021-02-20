## About this repo
Use this repo to add time stamp overlays to videos for annotation. The script first adds time stamp overlay from the file name and then stitches the videos together into a single mp4 file.

## Install dependencies
Make sure to install all the dependencies using the following command.

`pip install -r requirements.txt`

## Run the script
To run the script, type the following command.
`python overlay_multiple_videos.py folder_path_with_multiple_videos number_of_cores`


The folder path is the path to folder that contains all the mp4 videos collected during data collection. For paralellel processing please provide the number of cores to be used (e.g., 4 or 8)
