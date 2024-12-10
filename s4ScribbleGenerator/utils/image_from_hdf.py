""" Method to generate a label image from HDF file"""

import json

import cv2
import h5py
import numpy as np


def scribble_image_from_hdf(file_path, **kwargs):
    """
    Generates a scribble image from the HDF5 file provided with the changed
    parameters as specified above

    Parameters
    ----------
    file_path: String
    """
    # Check if file ending is .h5 or .hdf5
    if not (file_path.endswith(".h5") or file_path.endswith(".hdf5")):
        raise ValueError("File ending is not .h5 or .hdf5")

    # Load the scribbles from the HDF5 file
    with h5py.File(file_path, "r") as hdf_file:
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
                "Datasets 'scribble' and/or 'scribble_value' and/or 'image_dims' \
                    not found in the HDF5 file."
            )

    ## Override config
    if "line_thickness" in kwargs:
        config["line_thickness"] = kwargs["line_thickness"]
    if "scribble_scale" in kwargs:
        config["scribble_scale"] = kwargs["scribble_scale"]
    if "background_px_value" in kwargs:
        config["background_px_value"] = kwargs["background_px_value"]

    ## Draw the scribbles
    cv_image = np.zeros((image_dims), dtype=np.uint8)
    # Set image to background color
    cv_image[:] = (
        config["background_px_value"][0],
        config["background_px_value"][1],
        config["background_px_value"][2],
    )
    for scribble_line, color in zip(scribble, scribble_values):
        if config["scribble_scale"] != 1:
            length_of_x = scribble_line.shape[0]
            new_start = int(length_of_x * (1 - config["scribble_scale"]) / 2)
            new_stop = int(length_of_x - new_start)
            scribble_line = scribble_line[new_start:new_stop]
        # Draw the scribbles
        cv_image = cv2.polylines(
            cv_image,
            [scribble_line.astype(np.int32)],
            False,
            tuple(color),
            config["line_thickness"],
        )

    return cv_image
