import os
import cv2
import argparse
import numpy as np

def convert_video_to_frames(video_path, outfolder, sample_rate = 1.0):
    if not os.path.exists(outfolder):
        os.makedirs(outfolder, exist_ok=True)
    capture = cv2.VideoCapture(video_path)
    video_name = video_path.split("/")[-1]
    frameNr = 0
    while True:
        success, frame = capture.read()
        if success:
            seed = np.random.random()
            if seed >= (1 - sample_rate):
                img_path = os.path.join(outfolder, f"{video_name}#frame={frameNr}.jpg")
                cv2.imwrite(img_path, frame)
                print(f"Successfully print frame {frameNr} at path {img_path}")
        else:
            break
        frameNr+=1
    capture.release()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, help="Input Video Path")
    parser.add_argument("--output", "-o", type=str, help="Output Folder")
    parser.add_argument("--sample_rate", "-r", type=float, default=1.0, help="Sampling Rate for frames")
    args = parser.parse_args()
    
    convert_video_to_frames(args.input, args.output, args.sample_rate)