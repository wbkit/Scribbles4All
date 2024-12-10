"""
    Evaluates the scribbles and full annotations in the respective folders
    and outputs the ratio of boundary pixels that are labeled in the
    scribbles and the percentage of pixels that are scribbled.
"""
# pylint: disable=no-member
import os

import cv2
import numpy as np
from scipy import ndimage
from tqdm import tqdm

from helpers.labels import ID2TRAINID

IMAGE_DIR = "/scratch/wboet/datasets/urss_data/VOC2012/SegmentationClassAug/"
SCRIBBLE_DIR = "/scratch/wboet/datasets/VOCScribble_aug_auto_085/"
# SCRIBBLE_DIR = "/scratch/wboet/datasets/urss_data2/VOC2012/pascal_2012_scribble/"
IS_KITTI360 = True

config = {
    "validation_erosion_it": 5,
    "num_classes": 21,
}


def process_frame(image_file, scribble_file, boundary=5):
    """Processes a single pair of scribble and full semantics images with the given boundary"""
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    scribble = cv2.imread(scribble_file, cv2.IMREAD_GRAYSCALE)

    # Convert to label
    if IS_KITTI360:
        image = ID2TRAINID[image]
        scribble = ID2TRAINID[scribble]

    # Get values
    class_boundary = np.zeros((config["num_classes"],))
    class_label = np.zeros((config["num_classes"],))
    class_blob = np.zeros((config["num_classes"],))

    scribble_values = np.unique(scribble)
    for value in scribble_values:
        if value == 255:
            continue

        # Get the image blob
        full_blob = image == value
        # Get the eroded blob
        eroded_blob = ndimage.binary_erosion(full_blob, iterations=boundary)
        # Get the boundary blob
        boundary_blob = full_blob ^ eroded_blob
        assert np.sum(boundary_blob) == np.sum(full_blob) - np.sum(eroded_blob)

        # Get the scribble mask
        scribble_mask = scribble == value

        # Get the overlap
        overlap = scribble_mask & boundary_blob
        overlap_count = np.sum(overlap)

        class_boundary[value] = overlap_count
        class_label[value] = np.sum(scribble_mask)
        class_blob[value] = np.sum(full_blob)

    return class_boundary, class_label, class_blob


def main():
    """Main function"""
    boundary_list = []
    label_list = []
    blob_list = []

    # Get all files in the directory
    scribble_files = os.listdir(SCRIBBLE_DIR)
    scribble_paths = [os.path.join(SCRIBBLE_DIR, file) for file in scribble_files]
    label_paths = [os.path.join(IMAGE_DIR, file) for file in scribble_files]

    # Process all files
    for scribble_path, label_path in tqdm(
        zip(scribble_paths, label_paths), total=len(scribble_paths)
    ):
        # Check that the image exists
        if not os.path.exists(label_path):
            raise FileNotFoundError(f"Label file {label_path} does not exist")
        class_boundary, class_label, class_blob = process_frame(
            label_path, scribble_path, boundary=config["validation_erosion_it"]
        )

        boundary_list.append(class_boundary)
        label_list.append(class_label)
        blob_list.append(class_blob)

    print("__________________________________________________________")
    print("Label boundary stats")

    boundary_list = np.array(boundary_list)
    label_list = np.array(label_list)
    blob_list = np.array(blob_list)
    # Overall stats
    mean = np.sum(boundary_list) / np.sum(label_list) * 100
    print(f"Overall: {mean:.2f}")
    # Class wise stats
    for i in range(config["num_classes"]):
        mean = np.sum(boundary_list[:, i]) / np.sum(label_list[:, i]) * 100
        print(f"Class {i}: {mean:.2f}")
    print("__________________________________________________________")
    print("Scribble share of labels")
    mean = np.sum(label_list) / np.sum(blob_list) * 100
    print(f"Overall: {mean:.2f}")
    # Class wise stats
    for i in range(config["num_classes"]):
        mean = np.sum(label_list[:, i]) / np.sum(blob_list[:, i]) * 100
        print(f"Class {i}: {mean:.2f}")
    print("__________________________________________________________")


if __name__ == "__main__":
    main()
