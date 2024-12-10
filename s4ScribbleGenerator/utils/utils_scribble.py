"""	Utils for scribble generation """
import numpy as np


def sample_points(edge_image, sample_size=20):
    """
    Sample points from edge image.
    Genereally this function will randomly draw coordinates of all one-valued pixels

    Parameters
    ----------
    edge_image : np.array
        Binary image with one-valued pixels on the edge
    sample_size : int
    """
    # Get relevant point for one blob
    edge_coords = np.argwhere(edge_image == 1)
    sample_indices = np.random.randint(0, edge_coords.shape[0], sample_size)

    return edge_coords[sample_indices]


def get_furthest_points(sampled_points):
    """
    Get furthest point from sampled input point. Moreover, this is refined by
    getting the furthest point from the initial furthest point.

    Parameters
    ----------
    sampled_points : np.array
        Array of sampled points from edge image
    """
    # Select first point
    first_point_idx = np.random.randint(0, sampled_points.shape[0])
    # Get furthest point from first point
    distances = np.linalg.norm(sampled_points - sampled_points[first_point_idx], axis=1)
    max_distance_idx = np.argmax(distances)

    # Refine furthest point
    distances = np.linalg.norm(sampled_points - sampled_points[max_distance_idx], axis=1)
    first_point2_idx = np.argmax(distances)

    return (
        sampled_points[first_point_idx],
        sampled_points[max_distance_idx],
        sampled_points[first_point2_idx],
    )


def check_axis(center_of_m, first_pt, max_pt):
    """
    Check if x or y axis is preferred for scribble generation.
    Specifically: Check if the first point is on the left side of the center of mass
        Second point is on the right side of the center of mass or vice versa.

    Parameters
    ----------
    center_of_m : tuple
        Center of mass of the blob
    first_pt : tuple
        First point of the polynomial
    max_pt : tuple
        Second point of the polynomial
    """
    preferred_axis = None

    if (center_of_m[0] > first_pt[0]) and (center_of_m[0] < max_pt[0]):
        preferred_axis = "x"
    elif (center_of_m[0] < first_pt[0]) and (center_of_m[0] > max_pt[0]):
        preferred_axis = "x"
    else:
        preferred_axis = "y"

    return preferred_axis


def check_point_validity(point, blob_image):
    """
    Checks if a point is inside the blob.

    Parameters:
    __________
    point: tuple of shape (2,) with x and y coordinates of the point
    blob_image: np.array image of the blob
    """
    if (
        (point[0] > blob_image.shape[0])
        or (point[1] > blob_image.shape[1])
        or (point[0] < 0)
        or (point[1] < 0)
    ):
        return False
    # Check if point is inside blob
    if blob_image[int(point[0]), int(point[1])] == 0:
        return False
    else:
        return True


def check_curve_validity(x_new, y_poly, blob_image, tolerance=5):
    """
    Checks if the curve is valid by checking if all points are inside the blob.
    There is a small tolerance for points that are outside the blob.

    Parameters:
    __________
    x_new: np.array of shape (n,) with x coordinates of the curve
    y_poly: np.array of shape (n,) with y coordinates of the curve
    blob_image: np.array image of the blob
    """
    # Check value range
    x_max = np.max(x_new)
    y_max = np.max(y_poly)
    x_min = np.min(x_new)
    y_min = np.min(y_poly)
    if (x_max > blob_image.shape[0]) or (y_max > blob_image.shape[1]) or (x_min < 0) or (y_min < 0):
        return False

    # Basic validity check
    check_mask = np.zeros(blob_image.shape, dtype=int)
    x_new = np.floor(x_new).astype(int)
    y_poly = np.floor(y_poly).astype(int)
    check_mask[x_new, y_poly] = 1
    checked = np.logical_and(blob_image, check_mask)
    checked = checked.astype(int)

    diff_masks = np.sum(np.abs(check_mask - checked))

    if diff_masks > tolerance:
        return False
    else:
        return True
