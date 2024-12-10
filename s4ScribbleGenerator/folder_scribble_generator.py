""" This module generates scribbles for all the segmentation images in a folder. """

import os
import random

from joblib import Parallel, delayed
from tqdm import tqdm

from create_scribble import main as create_scribble

# Configuration Parameters
# ________________________________________________________________________________
SEG_DIR = "directory with the dense segmentation labels"
OUTPUT_DIR = "folder for scribble outputs"
# ________________________________________________________________________________

NR_JOBS = 2


def split_list(lst, nr_sublists):
    """
    Splits a given list `lst` into `n` sublists.

    Args:
    lst (list): The list to split
    n (int): The number of sublists to create

    Returns:
    list: A list of `n` sublists that contains all elements of the original list `lst`.
    """
    if nr_sublists > len(lst):
        raise ValueError("Cannot split list into more sublists than there are elements")

    quotient = len(lst) // nr_sublists
    remainder = len(lst) % nr_sublists

    result = []
    start = 0
    for i in range(nr_sublists):
        end = start + quotient
        if i < remainder:
            end += 1
        result.append(lst[start:end])
        start = end

    return result


if __name__ == "__main__":
    seg_paths = []
    # Loop through all files in the folder
    for file_name in os.listdir(SEG_DIR):
        # Check if the file is a PNG file
        if file_name.endswith(".png"):
            # If it is, add its path to the list
            seg_paths.append(os.path.join(SEG_DIR, file_name))

    # Randomly shuffle the list of segmentation images
    seg_paths = random.sample(seg_paths, len(seg_paths))

    # Call the scribble genereation function for each segmentation image
    print(f"Starting {NR_JOBS} jobs")
    image_filenames = Parallel(n_jobs=NR_JOBS, prefer="threads")(
        delayed(create_scribble)(
            seg_path,
            os.path.join(OUTPUT_DIR, os.path.basename(seg_path)),
            os.path.join(OUTPUT_DIR, os.path.basename(seg_path))[:-4] + ".h5",
            overwrite_files=False,
        )
        for seg_path in tqdm(seg_paths)
    )
    # NOTE Option that works without joblib
    # for seg_path in tqdm(seg_paths):
    #     print("Start a new image")
    #     create_scribble(
    #             seg_path,
    #             os.path.join(OUTPUT_DIR, os.path.basename(seg_path)),
    #             os.path.join(OUTPUT_DIR, os.path.basename(seg_path))[:-4] + ".h5",
    #             overwrite_files=False
    #         )
