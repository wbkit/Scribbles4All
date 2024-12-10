""" Plotting function for the visualiser scripts"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# from helpers.labels import ID2TRAINID, OBJECT_COLOR

IS_KITTI360 = False


def plot_scribbles(
    scribble,
    scribble_colors,
    image_dims,
    background_color=None,
    background_image=None,
    set_red=False,
    thickness=3,
    use_class_color_scale=False,
):
    if background_image is None and background_color is None:
        raise ValueError("Either background_image or background_color must be given.")
    if background_image is not None:
        if use_class_color_scale:
            background = cv2.imread(background_image, cv2.IMREAD_GRAYSCALE) % 20
        else:
            background = cv2.imread(background_image, cv2.IMREAD_GRAYSCALE)
            # if IS_KITTI360:
            #     background = ID2TRAINID[background]
            #     backgr_idx = np.where(background == 255)
            #     background[background == 255] = 0
            #     background = OBJECT_COLOR[background]
            #     background[backgr_idx] = (0, 0, 0)

    else:
        background = np.ones((image_dims)) * background_color / 255

    if set_red:
        scribble_colors[:, 0] = 0
        scribble_colors[:, 1] = 1
        scribble_colors[:, 2] = 0
    else:
        scribble_colors = scribble_colors / 255

    for i in range(scribble.shape[0]):
        plt.imshow(background, cmap="tab20")
        plt.plot(
            scribble[i, :, 0],
            scribble[i, :, 1],
            color=(scribble_colors[i, 0], scribble_colors[i, 1], scribble_colors[i, 2]),
            linewidth=thickness - 4,
        )

    plt.savefig("visualise_scribbles.png", dpi=300)
    plt.show()
