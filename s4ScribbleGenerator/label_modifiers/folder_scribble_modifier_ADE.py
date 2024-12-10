""" Script to update/modify the scribble labels for ADE20K according to the HDF5 label files """

import os

import cv2
import tqdm

from utils.image_from_hdf import scribble_image_from_hdf


ADE_PATH = "/scratch/inf0/user/wboettche/datasets/ADE20K/ADEChallengeData2016/scribbles08/training"
NEW_THIKNESS = 3
NEW_SCALING = 0.8


def main():
    assert os.path.exists(ADE_PATH), "CS path does not exist"
    # Base dir
    base_dir = ADE_PATH
    # Get all files in the folder
    seg_paths = []
    # Loop through all files in the folder
    for file_name in os.listdir(base_dir):
        # Check if the file is an HDF5 file
        if file_name.endswith(".h5"):
            # If it is, add its path to the list
            seg_paths.append(os.path.join(base_dir, file_name))

    print("Processing sequence ADE20K")

    for file_path in tqdm.tqdm(seg_paths):
        cv_image = scribble_image_from_hdf(
            file_path, line_thickness=NEW_THIKNESS, scribble_scale=NEW_SCALING
        )
        out_path = file_path[:-3] + ".png"
        cv2.imwrite(out_path, cv_image)


if __name__ == "__main__":
    main()
