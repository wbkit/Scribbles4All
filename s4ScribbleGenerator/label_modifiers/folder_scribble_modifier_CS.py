""" Script to update/modify the scribble labels for ADE20K according to the HDF5 label files """

import os

import cv2
import tqdm

from utils.image_from_hdf import scribble_image_from_hdf

SEQ_TRAIN_VAL = [
    "aachen",
    "bochum",
    "bremen",
    "cologne",
    "darmstadt",
    "dusseldorf",
    "erfurt",
    "hamburg",
    "hanover",
    "jena",
    "krefeld",
    "monchengladbach",
    "strasbourg",
    "stuttgart",
    "tubingen",
    "ulm",
    "weimar",
    "zurich",
]

CS_PATH = "/scratch/inf0/user/wboettche/datasets/Cityscapes/scribbles08/gtFine/train/"
NEW_THIKNESS = 5
NEW_SCALING = 0.8


def main():
    assert len(SEQ_TRAIN_VAL) > 0, "No sequences to process"
    assert os.path.exists(CS_PATH), "CS path does not exist"

    for seq in SEQ_TRAIN_VAL:
        # Base dir
        sequence = seq
        base_dir = os.path.join(CS_PATH, sequence)
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
