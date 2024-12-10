# Guide to Scribble Generator configs

## Major settings
- **line_thickness** - Thickness of the line drawn for the image scribbles in pixels.
- **scribble_scale** - Scales the inital scribble down by a certain factor. Scaling happens equallly from both ends. The original scribble is always preserved in the HDF5 scribble file
- **min_blob_area** - Minimum area of a blob to be considered for labelling in pixels
- **patience** - Max. numers of tries to generate a valid scribble before performing another erosion step. Denoted in the paper as *N*.
- **ignore_values** - Imnage values that are ignored and not labelled.
- **min_binary_erosion** - Minimum erosion for the initial erosion round. (See definition of epsilon1 in the paper.)
- **max_binary_erosion** - Maximum erosion for the initial erosion round. (See definition of epsilon1 in the paper.)
- **min_erosion_area_share** - Threshold below which min_binary_erosion is applied.
- **max_erosion_area_share** - Threshold above which max_binary_erosion is applied. In between min and max the erosion value is linearly interpolated.
- **it_extra_erosion** - Additional erosion if patience runs out. (See epsilon2 in the paper.)

## Further Settings
- **error_tolerance_px** - Number of pixels of a different class that a scribble can cover. ALWAYS keep the value at 0 when generating production ready scribble datasets!
- **background_px_value** - Grayscale value that is used as the background color for the scribble label images.
- **background_input_values** - Defines an input channel that is treated as a background class which is subjected to extra erosion steps by max_binary_erosion. If the dataset contains no background class, set this value to the value of the ignore classes.
- **height_distortion** - A factor that elongates the image vertically if greater 1. This is no longer used but can be set in order to incentivise vertically oriented scribble labels.