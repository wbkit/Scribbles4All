""" Script to update/modify the scribble labels for KITTI360 according to the HDF5 label files """

import os

import cv2
import tqdm

from utils.image_from_hdf import scribble_image_from_hdf


SEQ_TRAIN_VAL = [0, 2, 3, 4, 5, 6, 7, 9, 10]

KITTI360_PATH = "/scratch/wboet/datasets/KITTI360/"
SUBFOLDER = "data_2d_semantics/train"
NEW_THIKNESS = 3
NEW_SCALING = 0.9


def main():
    assert len(SEQ_TRAIN_VAL) > 0, "No sequences to process"
    assert os.path.exists(KITTI360_PATH), "KITTI360 path does not exist"

    for seq in SEQ_TRAIN_VAL:
        # Base dir
        sequence = "2013_05_28_drive_%04d_sync" % seq
        base_dir = os.path.join(
            KITTI360_PATH, SUBFOLDER, sequence, "image_00/scribble/"
        )
        # Get all files in the folder
        seg_paths = []
        # Loop through all files in the folder
        for file_name in os.listdir(base_dir):
            # Check if the file is an HDF5 file
            if file_name.endswith(".h5"):
                # If it is, add its path to the list
                seg_paths.append(os.path.join(base_dir, file_name))

        print(f"Processing sequence {sequence}")

        for file_path in tqdm.tqdm(seg_paths):
            cv_image = scribble_image_from_hdf(
                file_path, line_thickness=NEW_THIKNESS, scribble_scale=NEW_SCALING
            )
            out_path = file_path[:-3] + ".png"
            cv2.imwrite(out_path, cv_image)


if __name__ == "__main__":
    main()
