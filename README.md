# Scribbles4All

This is the GitHub repository for the NeurIPS spotilight Paper [Scribbles for All: Benchmarking Scribble Supervised Segmentation Across Datasets](http://arxiv.org/abs/2408.12489) containing the s4Datasets and the universal scribble generator code.

## Roadmap
- [x] Publish the s4 datasets
- [x] Move dataset location to GitHub
- [x] Publish the scribbble generation code
- [x] Add Croissant metadata standard
- [x] Provide download helper tools


## Dataset extraction
The s4Pascal dataset can be extracted directly by calling 
`tar -xzf s4Pascal.tar.gz`.
For the other datasets we recommend calling the respective unpacking scripts. Those will unpack the multiple tarballs and create the proper folder structure to copy-paste the scribble labels into the maind-dataset folder structure.

    bash ./extractADE.sh
    bash ./extractCityscapes.sh 
    bash ./extractKITTI360.sh 

## Scribble Generation/Modification
The code to generate scribble labels from fully supervised segmentation labels or modify existing scribble datasets can be found in the subfolder [s4ScribbleGenerator](./s4ScribbleGenerator/). To get started, refer to the separate [README](./s4ScribbleGenerator/README.MD).

## License

The code in this repository an the datasets linked by this repository are published under the  CC BY 4.0 license.