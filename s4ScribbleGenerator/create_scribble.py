"""
    This file contains functions to create scribbles from semantic segmentation images.
"""

# %%
# pylint: disable=no-member
import json
import os

import cv2
import h5py
import numpy as np
from scipy import ndimage
from skimage.morphology import skeletonize
from skimage.measure import label, regionprops

from utils.drawing_scribble import get_2nd_order_polynomial, get_4th_order_polynomial
from utils.utils_scribble import (
    check_axis,
    check_curve_validity,
    check_point_validity,
    get_furthest_points,
    sample_points,
)

# Configuration Parameters
# ________________________________________________________________________________
CONFIG_PATH = "./configs/configWaymo.json"
SEG_PATH = "path of label file to load"
SAVE_PATH = "path of saved file"
# ________________________________________________________________________________


def blob_erosion_processing(blob, iterations=10, config=None):
    """
    Takes a binary blob and removes fine details from it.
    """
    # revove fine details
    # Undistort image
    if config is not None:
        height, width = blob.shape[:2]
        scale = 1 / config["height_distortion"]
        blob = cv2.resize(
            blob, (int(width), int(height * scale)), interpolation=cv2.INTER_NEAREST
        )
    # Perform erosion and closing
    blob = ndimage.binary_erosion(blob, iterations=iterations)
    # Convert from bool to int
    blob = blob.astype(int)
    # Distort image again
    if config is not None:
        blob = cv2.resize(
            blob, (int(width), int(height)), interpolation=cv2.INTER_NEAREST
        )

    # Check if the blob contains multiple blobs
    # If so separate blobs
    labeled_array, num_features = ndimage.label(blob)
    if num_features > 1:
        # Obtain the biggest blob
        biggest_blob = np.zeros(blob.shape)
        biggest_blob[labeled_array == 1] = 1
        for i in range(2, num_features + 1):
            blob_i = np.zeros(blob.shape)
            blob_i[labeled_array == i] = 1
            if np.sum(blob_i) > np.sum(biggest_blob):
                biggest_blob = blob_i
        blob = biggest_blob

    # Process edges and calculate center of mass
    # Create new arrays
    edge = np.zeros((blob.shape[0], blob.shape[1]))
    center_of_mass = np.zeros((2))

    # Icrease image size by 2 pixel per dinmension
    # Makes sure that edge detection works on image boundaries
    ext_edge = np.pad(blob, 1, "constant", constant_values=0)

    # get edge of blob
    edge = cv2.Canny(np.uint8(ext_edge * 255), 100, 200)[1:-1, 1:-1]
    edge[edge > 0] = 1

    # get center of mass of blob
    center_of_mass = np.array(ndimage.center_of_mass(blob))

    return blob, edge, center_of_mass


def image_to_blob(color_image, config):
    """
    Takes an image with semantic segmentation and separates it into individual
    images tha each contain one blob. Also removes fine details from the blobs.
    Further, returns the center of mass of each blob and an edge image of each blob.

    Parameters
    ----------
    color_image : numpy array
    """
    image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    unique_values = np.unique(image)

    blob_list = []
    edge_list = []
    center_of_mass_list = []
    unique_val_list = []
    color_val_list = []

    image_area = image.shape[0] * image.shape[1]

    for value in unique_values:
        # Get mask of current value
        mask = image == value

        # Perform connected component labeling
        labeled_mask = label(mask)

        for region in regionprops(labeled_mask):
            # Skip small regions
            if region.area < config["min_blob_area"]:
                continue

            # Extract region mask
            region_mask = (labeled_mask == region.label)

            # Remove fine details by erosion
            area_share = region.area / image_area
            if area_share < config["min_erosion_area_share"]:
                erosion_value = config["min_binary_erosion"]
            elif area_share > config["max_erosion_area_share"]:
                erosion_value = config["max_binary_erosion"]
            else:
                erosion_value = config["min_binary_erosion"] + int(
                    (area_share - config["min_erosion_area_share"])
                    / (config["max_erosion_area_share"] - config["min_erosion_area_share"])
                    * (config["max_binary_erosion"] - config["min_binary_erosion"])
                )

            eroded_region_mask = ndimage.binary_erosion(region_mask, iterations=erosion_value)

            # Skip if erosion removes the region
            if np.sum(eroded_region_mask) == 0:
                continue

            # Relabel the eroded mask to separate any disconnected components
            eroded_labeled_mask = label(eroded_region_mask)

            for eroded_region in regionprops(eroded_labeled_mask):
                # Skip small regions
                if eroded_region.area < config["min_blob_area"]:
                    continue

                eroded_region_mask = (eroded_labeled_mask == eroded_region.label)

                # Edge detection
                ext_eroded_mask = np.pad(eroded_region_mask, 1, 'constant', constant_values=0)
                edge = cv2.Canny(np.uint8(ext_eroded_mask * 255), 100, 200)[1:-1, 1:-1]
                edge[edge > 0] = 1

                # Center of mass
                com = ndimage.center_of_mass(eroded_region_mask)

                # Color value from the original image
                coords = np.argwhere(eroded_region_mask)
                color_value = color_image[coords[0][0], coords[0][1], :]

                # Ensure color_value is a NumPy array of integers
                color_value = color_value.astype(np.int32)

                # Append results to lists
                blob_list.append(eroded_region_mask.astype(np.uint8))
                edge_list.append(edge)
                center_of_mass_list.append(com)
                unique_val_list.append(value)
                color_val_list.append(color_value)

    # Convert lists to arrays
    blob_array = np.array(blob_list)
    edge_array = np.array(edge_list)
    center_of_mass = np.array(center_of_mass_list)
    unique_val_array = np.array(unique_val_list)
    color_val_array = np.array(color_val_list, dtype=np.int32)

    return blob_array, edge_array, center_of_mass, unique_val_array, color_val_array


def get_valid_com(center_of_m, blob_image):
    """
    Get a valid point from the blob that is closest to the center of mass.
    This is needed for non-convex blobs.

    Parameters
    ----------
    center_of_m : tuple
    blob_image : np.array
    """
    # Skeletonize blob
    skeleton = skeletonize(blob_image)
    skeleton_idx = np.argwhere(skeleton == True)  # pylint: disable=singleton-comparison

    # Sample points from skeleton
    sample_size = 10
    sample_indices = np.random.randint(0, skeleton_idx.shape[0], sample_size)

    # Get closest point to center of mass
    distances = np.linalg.norm(skeleton_idx[sample_indices] - center_of_m, axis=1)
    # Get index of closest point
    min_distance_idx = np.argmin(distances)
    # Get closest point
    closest_point = skeleton_idx[sample_indices][min_distance_idx]

    return closest_point


def draw_polynom(blob_image, edge_image, center_of_m, blob_image_initial, tolerance=5):
    """
    Draws a polynomial scribble on the blob image

    Parameters
    ----------
    blob_image : np.array Image of the blob
    edge_image : np.array Image of the edges of the blob
    center_of_m : np.array Center of mass of the blob
    tolerance : int Tolerance for the number of pixels of the polynom
                    that can violate the blob boundary
    """
    center_of_m_old = center_of_m
    # Add randomness to points
    sigm = np.sqrt(np.sum(blob_image)) / 20
    center_of_m[0] = center_of_m[0] + sigm * np.random.randn()
    center_of_m[1] = center_of_m[1] + sigm * np.random.randn()
    # check if center of mass is within blob
    # If not, sample for up to tolerance times new center of mass
    if not check_point_validity(center_of_m, blob_image):
        center_of_m = get_valid_com(center_of_m_old, blob_image)

    old_first_pt, max_pt, first_pt = get_furthest_points(
        sample_points(edge_image, sample_size=25)
    )

    pref_axis = check_axis(center_of_m, first_pt, max_pt)

    # Fit polynomial
    _, x_new, y_poly = get_2nd_order_polynomial(
        center_of_m, first_pt, max_pt, pref_axis
    )

    # Extract 2 extra points
    idx1 = np.random.randint(0.2 * x_new.shape[0], x_new.shape[0] * 0.8)
    idx2 = np.random.randint(0.2 * x_new.shape[0], x_new.shape[0] * 0.8)

    add_x1 = x_new[idx1]
    add_x2 = x_new[idx2]
    add_y1 = y_poly[idx1]
    add_y2 = y_poly[idx2]

    # Add randomness
    add_x1 += sigm * np.random.randn()
    add_x2 += sigm * np.random.randn()
    add_y1 += sigm * np.random.randn()
    add_y2 += sigm * np.random.randn()

    # use skeleton to refine points
    add_1 = np.array([add_x1, add_y1])
    add_2 = np.array([add_x2, add_y2])

    add_1 = get_valid_com(add_1, blob_image)
    add_2 = get_valid_com(add_2, blob_image)

    add_x1 = add_1[0]
    add_x2 = add_2[0]
    add_y1 = add_1[1]
    add_y2 = add_2[1]

    # Fit polynomial again
    _, x_new, y_poly = get_4th_order_polynomial(
        center_of_m, first_pt, max_pt, add_x1, add_x2, add_y1, add_y2, pref_axis
    )
    # Basic validity check
    check_result = check_curve_validity(
        x_new, y_poly, blob_image_initial, tolerance=tolerance
    )

    return (
        check_result,
        old_first_pt,
        max_pt,
        first_pt,
        x_new,
        y_poly,
        add_x1,
        add_x2,
        add_y1,
        add_y2,
    )


def main(path_to_image, path_to_save, path_to_save_h5=None, overwrite_files=False):
    """
    Main function
    """
    # NOTE This is to prevent double computation if the file already exists
    if overwrite_files is False and os.path.exists(path_to_save):
        print("File already exists")
        return

    # Read the config file
    with open(CONFIG_PATH, "r") as f_stream:
        config = json.load(f_stream)
    image_undist = cv2.imread(path_to_image, cv2.IMREAD_COLOR)

    # Perfrom image distortion
    height, width = image_undist.shape[:2]
    scale = config["height_distortion"]
    image = cv2.resize(
        image_undist, (int(width), int(height * scale)), interpolation=cv2.INTER_NEAREST
    )

    (
        blob_array,
        edge_array,
        center_of_mass,
        unique_val_array,
        color_array,
    ) = image_to_blob(image, config)

    # Create image for drawing in color
    cv_image = image_undist.copy()
    # Set image to background color
    cv_image[:] = (
        config["background_px_value"][0],
        config["background_px_value"][1],
        config["background_px_value"][2],
    )
    # Create array for scribble lines to save to HDF5
    scribble_array = []
    scribble_value_array = []

    for i in range(0, blob_array.shape[0]):
        # Just use one image
        blob_image = blob_array[i]
        edge_image = edge_array[i]
        center_of_m = center_of_mass[i]

        blob_image_ = blob_image.copy()

        # Background blob ususally has a weird shape
        # Do some extra eroding
        if unique_val_array[i] in config["background_input_values"]:
            blob_image, edge_image, center_of_m = blob_erosion_processing(
                blob_image, iterations=config["max_binary_erosion"]
            )

        # Check for empty blobs
        if np.sum(blob_image) < config["min_blob_area"]:
            continue
        if np.sum(edge_image) == 0:
            continue
        if unique_val_array[i] in config["ignore_values"]:
            continue

        check_result = False
        empty_blob = False
        while not check_result:
            for _ in range(0, config["patience"]):
                check_result, _, _, _, x_new, y_poly, _, _, _, _ = draw_polynom(
                    blob_image,
                    edge_image,
                    center_of_m,
                    blob_image_,
                    tolerance=config["error_tolerance_px"],
                )
                if check_result:
                    break

            # Extra erosion
            blob_image, edge_image, center_of_m = blob_erosion_processing(
                blob_image, iterations=config["it_extra_erosion"], config=config
            )
            if np.sum(blob_image) == 0:
                empty_blob = True
                break
            if np.sum(edge_image) == 0:
                empty_blob = True
                break
        if empty_blob:
            continue

        # Undo the distortion
        x_new = x_new / scale

        # NOTE Scaling of the scribble labels
        if config["scribble_scale"] != 1:
            length_of_x = x_new.shape[0]
            new_start = int(length_of_x * (1 - config["scribble_scale"]) / 2)
            new_stop = int(length_of_x - new_start)
            x_new = x_new[new_start:new_stop]
            y_poly = y_poly[new_start:new_stop]

        # Drawing with cv2
        draw = np.stack((y_poly, x_new), axis=-1)
        cv_color = tuple(map(int, color_array[i]))
        cv_image = cv2.polylines(
            cv_image,
            [draw.astype(np.int32)],
            False,
            cv_color,
            config["line_thickness"],
        )

        # Save scribble to array
        scribble_array.append(draw)
        scribble_value_array.append(color_array[i])

    cv2.imwrite(path_to_save, cv_image)
    # Save scribble to HDF5
    if path_to_save_h5 is not None:
        scribble_array = np.array(scribble_array)
        scribble_value_array = np.array(scribble_value_array)
        with h5py.File(path_to_save_h5, "w") as f_stream:
            f_stream.create_dataset("scribble", data=scribble_array)  # Scribbles
            f_stream.create_dataset(
                "scribble_values", data=scribble_value_array
            )  # Scribble color
            f_stream.create_dataset(
                "image_dims", data=image_undist.shape
            )  # Original image
            f_stream.create_dataset(
                "config", data=json.dumps(config).encode("utf-8")
            )  # Config


if __name__ == "__main__":
    main(
        SEG_PATH,
        SAVE_PATH,
        path_to_save_h5=SAVE_PATH[:-4] + ".h5",
        overwrite_files=True,
    )
