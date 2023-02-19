import os
import os.path as osp
import argparse

def organize_images(input_folder, format: str = "YOLOV8"):
    if format == "YOLOV8":
        source_folder = osp.join(input_folder, "src_images")
        train_folder = osp.join(input_folder, "training")
        val_folder = osp.join(input_folder, "validation")
        source_files = os.listdir(source_folder)
        train_anns = os.listdir(train_folder)
        val_anns = os.listdir(val_folder)
        for train_ann in train_anns:
            img_name = train_ann[:-4] + ".jpg"
            if not os.path.exists(osp.join(train_folder, img_name)):
                assert img_name in source_files, "Image file not inside source folder"
                os.rename(osp.join(source_folder, img_name), osp.join(train_folder, img_name))
            
        for val_ann in val_anns:
            img_name = val_ann[:-4] + ".jpg"
            if not os.path.exists(osp.join(val_folder, img_name)):
                assert img_name in source_files, "Image file not inside source folder"
                os.rename(osp.join(source_folder, img_name), osp.join(val_folder, img_name))
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, help="Input Folder")
    parser.add_argument("--format", "--f", type=str, default = "YOLOV8" , help="Output Format")
    args = parser.parse_args()
    
    organize_images(args.input, args.format)