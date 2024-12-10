""" Visualises all semantic images in a folder with the scribbles overlaid on top of them. """
# %%
import json
import os

import cv2
import h5py
import numpy as np
from matplotlib import pyplot as plt

from utils.visualiser import plot_scribbles

SEQ = 6
FOLDER = "directory with scribble labels"
SEG_DIR = "directory with the dense labels"


# Get all files in the folder
files = os.listdir(FOLDER)

# Loop through all files in the folder
for i, file_name in enumerate(files):
    # Check if the file is an HDF5 file
    if not file_name.endswith(".h5"):
        continue
    # if (i % 4) != 0:
    #     continue

    # Grab a specific file
    if int(file_name[:-3]) != 4573:
        continue

    print(file_name)

    # Load the scribbles from the HDF5 file
    with h5py.File(FOLDER + file_name, "r") as hdf_file:
        if (
            "scribble" in hdf_file
            and "scribble_values" in hdf_file
            and "image_dims" in hdf_file
            and "config" in hdf_file
        ):
            scribble = np.array(hdf_file["scribble"])
            scribble_values = np.array(hdf_file["scribble_values"])
            image_dims = np.array(hdf_file["image_dims"])
            config = json.loads(hdf_file["config"][()])
        else:
            raise ValueError(
                "Datasets 'scribble' and/or 'scribble_value' and/or 'image_dims' not "
                "found in the HDF5 file."
            )

    LABEL_PATH = SEG_DIR + os.path.basename(file_name)[:-3] + ".png"

    plot_scribbles(
        scribble,
        scribble_values,
        image_dims,
        set_red=False,
        background_image=LABEL_PATH,
        thickness=3,  # config["line_thickness"],
        use_class_color_scale=True,
    )

    ##################
    background = cv2.imread(LABEL_PATH, cv2.IMREAD_GRAYSCALE)
    scribble_png = cv2.imread((FOLDER + file_name)[:-3] + ".png", cv2.IMREAD_GRAYSCALE)

    plt.imshow(background)
    plt.show()
    plt.imshow(scribble_png)
    plt.show()

    ##################

    # Delay for 3 seconds
    plt.pause(0.5)
