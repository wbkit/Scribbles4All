""" Visualises scribble labels over the corresponding dense label image """

# %% [markdown]
# # Inspect Scribbles
import json
import os

import cv2
import h5py
import numpy as np
from matplotlib import pyplot as plt

from utils.visualiser import plot_scribbles

# Configuration Parameters
# ________________________________________________________________________________
LABEL_PATH = "dense label image"
SCRIBBLE_PATH = "folder for scribbles" + os.path.basename(LABEL_PATH)
FILE_NAME = "folder for scribble HDF files" + os.path.basename(LABEL_PATH)[:-4] + ".h5"
# ________________________________________________________________________________

scribbles = cv2.imread(SCRIBBLE_PATH, cv2.IMREAD_GRAYSCALE) % 10
labels = cv2.imread(LABEL_PATH, cv2.IMREAD_GRAYSCALE) % 10

# %% [markdown]
# # PNG - Plot the scribbles and labels
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

ax1.imshow(labels, cmap="tab10")
ax2.imshow(scribbles, cmap="tab10")

plt.tight_layout()
plt.show()

# %% [markdown]
# # HDF5 - Plot the scribbles on the labels
with h5py.File(FILE_NAME, "r") as hdf_file:
    # Assuming the datasets are named 'array1' and 'array2'
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
            "Datasets 'scribble' and/or 'scribble_value' and/or 'image_dims' not found \
                in the HDF5 file."
        )

print(f"scribble: {scribble.shape}")
print(f"scribble_values: {scribble_values.shape}")

plot_scribbles(
    scribble,
    scribble_values,
    image_dims,
    set_red=True,
    background_image=LABEL_PATH,
    thickness=config["line_thickness"],
    use_class_color_scale=True,
)

# %%
