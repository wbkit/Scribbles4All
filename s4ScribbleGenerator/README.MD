# s4ScribbleGenerator
## Setup
To install a suitable python environment, please follow the subsequent commands.

    mamba create -n scribble_env python=3.12
    mamba activate scribble_env
    pip install -f requirements.txt


## General Remarks
The general scribble generation process is controlled by a config.json file. Script specific settings are located in the header of the respective .py files as global variables. This applies specifically for the scribble modification scripts.

## Generate New Scribble Labels
The generation of new datasets is done through the create_scribble.py which operates on a single file. To convert a whole dataset, we recommend writing a wrapper script that handles the dataset's folder structure and calls the create scribble function. This function can also contain multiprocessing capababilities. We provide an example folder wrapper(folder_scribble_generator.py).

Configuration files for the pre-generated s4Datasets are located in [/configs](./configs/). NOTE: To maintain comparability of methods trained on s4Datasets, please only create your own datasets if there is no publsihed s4Dataset for your dataset available.

## Adapt/Modify Existing Scribble Datasets
We provide scripts to modify the scribbles of the s4Dataset family in [/label_modifiers](./label_modifiers/). These scripts take the scribble information stored in the HDF5 files of the scribble dataset and generate a new PNG version of the dataset. Such a setup ensures, that the HDF5 files always maintain the original scribble information while the PNG files can be updated/modified. This is mainly intended to enable scribble length and width ablations. For this purpose, set the NEW_SCALING and NEW_THIKNESS values in the modifier scripts. Lenght scaling preserves the center of the scribbles. NEVER modifiy the HDF5 files when performing ablations.
