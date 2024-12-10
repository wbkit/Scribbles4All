""" Drawing related functions """
import numpy as np


def get_2nd_order_polynomial(center_of_m, first_pt, max_pt, preferred_axis):
    """
    Fit a 2nd order polynomial to the points

    Parameters
    ----------
    center_of_m : tuple center of mass of blob
    first_pt : tuple first point
    max_pt : tuple furthest point
    preferred_axis : str 'x' or 'y'
    """
    # Fit polynomial
    x_coords = [center_of_m[1], first_pt[1], max_pt[1]]
    y_coords = [center_of_m[0], first_pt[0], max_pt[0]]

    if preferred_axis == "x":
        y_min = np.min(y_coords)
        y_max = np.max(y_coords)
        poly_params = np.polyfit(y_coords, x_coords, 2)
        polynomial_fctn = np.poly1d(poly_params)
        x_new = np.linspace(y_min, y_max, 100)
        y_poly = polynomial_fctn(x_new)
    else:
        x_min = np.min(x_coords)
        x_max = np.max(x_coords)
        poly_params = np.polyfit(x_coords, y_coords, 2)
        polynomial_fctn = np.poly1d(poly_params)
        y_poly = np.linspace(x_min, x_max, 100)
        x_new = polynomial_fctn(y_poly)

    return polynomial_fctn, x_new, y_poly


def get_4th_order_polynomial(
    center_of_m, first_pt, max_pt, x_1, x_2, y_1, y_2, preferred_axis
):
    """
    Fit 4th order polynomial to the provided points

    Parameters
    ----------
    center_of_m : tuple center of mass of blob
    first_pt : tuple first point of blob
    max_pt : tuple point with max distance to first point
    x_1 : int x coordinate of third point
    x_2 : int x coordinate of fourth point
    y_1 : int y coordinate of third point
    y_2 : int y coordinate of fourth point
    preferred_axis : str 'x' or 'y'
    """
    # Fit polynomial
    if preferred_axis == "x":
        x_coords = [center_of_m[1], first_pt[1], max_pt[1], y_1, y_2]
        y_coords = [center_of_m[0], first_pt[0], max_pt[0], x_1, x_2]
        y_min = np.min(y_coords)
        y_max = np.max(y_coords)
        poly_params = np.polyfit(y_coords, x_coords, 2)
        polynomial_fctn = np.poly1d(poly_params)
        x_new = np.linspace(y_min, y_max, 100)
        y_poly = polynomial_fctn(x_new)
    else:
        x_coords = [center_of_m[1], first_pt[1], max_pt[1], y_1, y_2]
        y_coords = [center_of_m[0], first_pt[0], max_pt[0], x_1, x_2]
        x_min = np.min(x_coords)
        x_max = np.max(x_coords)
        poly_params = np.polyfit(x_coords, y_coords, 2)
        polynomial_fctn = np.poly1d(poly_params)
        y_poly = np.linspace(x_min, x_max, 100)
        x_new = polynomial_fctn(y_poly)

    return polynomial_fctn, x_new, y_poly
