"""	Code to analyse the label distribution in semantic masks
    We assume that the labels are in grayscale in a certain range of values
"""

# %%
import os

import cv2
import numpy as np
from scipy import ndimage
from scipy.ndimage import label as ndlabel
from tqdm import tqdm


LABEL_DIR = "label directory"
SUP_DIR = "dense label directory"
MAX_LABEL = 20
SAVE_PLOT = "path to save a plot image"


def analyse_label(label):
    """
    Analyses one label image and returns the statistics.
    """
    # Get overall image pixels
    total_pixels = label.shape[0] * label.shape[1]
    # Get the unique values
    unique, counts = np.unique(label, return_counts=True)

    # Create label based statistics
    label_stats = np.array([0] * (MAX_LABEL + 1))
    for i, unique_value in enumerate(unique):
        if unique_value <= MAX_LABEL:
            label_stats[unique_value] = counts[i]

    # Get relative values
    label_stats_rel = label_stats / total_pixels * 100

    return label_stats, label_stats_rel


def classify_closeness(label, seg_label, closeness=30):
    """
    Classifies the label based on the closeness to the border
    """
    label_stats = np.array([0] * (MAX_LABEL + 1))
    boundary_label_stats = np.array([0] * (MAX_LABEL + 1))
    rel_boundary_label_stats = np.array([0] * (MAX_LABEL + 1))
    # Get the unique values
    unique, counts = np.unique(label, return_counts=True)
    for i, unique_value in enumerate(unique):
        if unique_value <= MAX_LABEL:
            label_stats[unique_value] = counts[i]

            # Get all parts of the segmentation mask that are of the current class
            # and erode them by the boundary size
            one_class_image = seg_label == unique_value
            eroded_image = ndimage.binary_erosion(one_class_image, iterations=closeness)
            # Get the difference between the original and the eroded image
            boundary_image = one_class_image ^ eroded_image

            # Get the label values of the boundary pixels
            boundary_labels = label[boundary_image]
            # get the number of pixels in the boundary labels
            idx = np.where(boundary_labels == unique_value)
            boundary_label_stats[unique_value] = len(idx[0])

            rel_boundary_label_stats[unique_value] = (
                boundary_label_stats[unique_value] / label_stats[unique_value] * 100
            )

    return rel_boundary_label_stats, boundary_label_stats


def main():
    """Calculates the label distribution in the given folder"""
    label_paths = []
    # Loop through all files in the folder
    for file_name in os.listdir(LABEL_DIR):
        # Check if the file is a PNG file
        if file_name.endswith(".png"):
            # If it is, add its path to the list
            label_paths.append(os.path.join(LABEL_DIR, file_name))

    stats_list = []
    stats_rel_list = []
    boundary_stats_list = []
    abs_closeness_stats_list = []
    nr_scribble_list = []
    for label_path in tqdm(label_paths):
        # Read the label image
        label = cv2.imread(
            label_path, cv2.IMREAD_GRAYSCALE
        )  # pylint: disable=no-member
        seg_path = os.path.join(SUP_DIR, os.path.basename(label_path))
        seg_label = cv2.imread(
            seg_path, cv2.IMREAD_GRAYSCALE
        )  # pylint: disable=no-member

        # Get nr. of scribbles through label
        count_label = np.array(label)
        count_label[count_label < 21] = 1
        count_label[count_label > 21] = 0
        # count_label[count_label < 0] = 0
        _, nr_scribbles = ndlabel(count_label)
        nr_scribble_list.append(nr_scribbles)

        # Pascal remove the 255 label
        label[label == 255] = 21

        label_stats, label_stats_rel = analyse_label(label)
        closeness_stats, abs_closeness_stats = classify_closeness(label, seg_label)
        stats_list.append(label_stats)
        stats_rel_list.append(label_stats_rel)
        boundary_stats_list.append(closeness_stats)
        abs_closeness_stats_list.append(abs_closeness_stats)

    # Get the mean of the label statistics
    stats_mean = np.mean(stats_list, axis=0)
    stats_rel_mean = np.mean(stats_rel_list, axis=0)
    closeness_stats_mean = np.mean(boundary_stats_list, axis=0)
    share_labelled = np.sum(stats_rel_mean)

    abs_closeness_stats_list = np.array(abs_closeness_stats_list).sum(axis=0)
    abs_labbelded = np.array(stats_list).sum(axis=0)
    complete_boundary_mean = (
        np.sum(abs_closeness_stats_list) / np.sum(abs_labbelded) * 100
    )

    avg_scribbles_per_image = np.mean(nr_scribble_list)

    # Create label based statistics
    print("______________________________________________________")
    for i in range(MAX_LABEL + 1):
        print(
            f"Label {i:02d}: {stats_mean[i]:05.1f} ({stats_rel_mean[i]:02.4f}%), \
                closeness: {closeness_stats_mean[i]:02.4f}%"
        )

    # Get the share of labelled pixels
    print("______________________________________________________")
    print(f"Share of labelled pixels: {share_labelled}%")
    print(f"Share of closeness: {complete_boundary_mean}%")
    print(f"Average scribbles per image: {avg_scribbles_per_image}")

    # Save data for plotting in numpy format
    np.savez(
        SAVE_PLOT,
        stats_rel_mean=stats_rel_mean,
        closeness_stats_mean=closeness_stats_mean,
    )


if __name__ == "__main__":
    main()
