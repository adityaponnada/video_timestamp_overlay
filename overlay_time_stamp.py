import sys
import os
from os import sep
import cv2
import datetime
from datetime import datetime, timedelta
import tqdm


def add_timestamp_overlay(in_path, file_name, out_path=None, preview=True, progress_bar=True):
    # keep the outpath same as the input path
    out_path = out_path or in_path

    # get the full path of the input file
    in_file_name = in_path + sep + file_name

    # Get the video file into openCV
    cap = cv2.VideoCapture(in_file_name)

    # Get the frame rate of the file
    video_frame_rate = cap.get(cv2.CAP_PROP_FPS)

    # Get the number of frames of the file
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get frame size of the file
    frame_width, frame_height = int(cap.get(3)), int(cap.get(4))

    # File name length
    file_name_len = len(file_name)

    # remove extension
    video_start_time = file_name[:- 4]

    # Remove the begining QVR_ type string
    video_start_time = video_start_time[4:]

    # Split the file name by '_' to get date time components
    video_name_string_list = video_start_time.split("_")

    # Stitch a timestamp
    video_start_time = video_name_string_list[0] + "-" + video_name_string_list[1] + "-" + video_name_string_list[2] + \
        " " + \
        video_name_string_list[3] + ":" + video_name_string_list[4] + ":" + video_name_string_list[5] + \
        ".000"

    # Convert to a datetime object
    video_start_time = datetime.strptime(
        video_start_time, '%Y-%m-%d %H:%M:%S.%f')

    print("Start time is: " + str(video_start_time))

    # This line below may not be working. Might be a codec problem
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')

    # Create an output file name
    out_put_dir = out_path + sep + 'stamped'
    if not os.path.exists(out_put_dir):
        os.makedirs(out_put_dir)
    output_file = out_put_dir + sep + f'{file_name[:- 4]}_stamped.mp4'

    # Create a video writer buffer
    out = cv2.VideoWriter(output_file, fourcc,
                          video_frame_rate, (frame_height, frame_width))

    # Initialize the frame count
    frame_count = 0

    print("Video frame rate is: " + str(video_frame_rate))

    with tqdm.tqdm(total=frame_count, disable=not progress_bar) as bar:

        while cap.isOpened():

            # Capture frames in the video
            ret, frame = cap.read()

            # rotate 90 degree counter-clockwise
            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

            if ret:
                bar.update()
                # describe the type of font
                # to be used.
                font = cv2.FONT_HERSHEY_SIMPLEX

                # Use putText() method for
                # inserting text on video

                # Get number of seconds to ad to the start time fetched from file name
                secs_add = frame_count / video_frame_rate
                secs_to_add = timedelta(seconds=secs_add)
                frame_time = (video_start_time +
                              secs_to_add).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                frame_count = frame_count + 1
                frame = cv2.putText(frame,
                                    str(frame_time),
                                    (50, 50),
                                    font, 1,
                                    (0, 255, 255),
                                    2,
                                    cv2.LINE_4)
                bar.set_description(frame_time)
                # Display the resulting frame
                # if end of the frame, exit
                if not ret:
                    break

                out.write(frame)

                if preview:
                    cv2.imshow('video', frame)

                # creating 'q' as the quit
                # button for the video
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            else:
                break

    # release the cap object
    cap.release()
    out.release()
    # close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":

    # Get the input file folder path
    in_path = sys.argv[1]

    # get the file name of the video file
    file_name = sys.argv[2]

    add_timestamp_overlay(in_path, file_name, preview=False, progress_bar=True)
