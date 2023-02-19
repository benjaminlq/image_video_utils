# Utility Scripts for image and video data preparation, pre &amp; post processing
------------------------------------------------------------------------------
Scripts for image and video data preparation, pre &amp; post processing

## 1. Prepare YOLO Annotations
`python3 utils/prepare_data_folder.py -i <input_folder:str> -f <format:str>` 

## 2. Convert Videos to Frames for annotations and training with sample rate.
`python3 utils/convert_video_to_frames.py -i <input_video:str> -o <output_folder:str> -r <sample_rate:float>`
