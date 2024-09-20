# Scribbles4All

The paper preprint is available on arXiv under:

### [Scribbles4All](http://arxiv.org/abs/2408.12489)

## Roadmap
- [x] Publish the s4 datasets
- [x] Move dataset location to GitHub
- [ ] Publish the scribbble generation code
- [x] Add Croissant metadata standard
- [x] Provide download helper tools


## Dataset extraction
The s4Pascal dataset can be extracted directly by calling 
`tar -xzf s4Pascal.tar.gz`.
For the other datasets we recommend calling the respective unpacking scripts. Those will unpack the multiple tarballs and create the proper folder structure to copy-paste the scribble labels into the maind-dataset folder structure.

    ./extractADE.sh
    ./extractCityscapes.sh 
    ./extractKITTI360.sh 


## License

The code in this repository an the datasets linked by this repository are published under the  CC BY 4.0 license.