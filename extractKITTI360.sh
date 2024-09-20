#!/bin/sh

tar -xzf ./s4KITTI360/train/2013_05_28_drive_0003_sync.tar.gz -C ./s4KITTI360/train/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0007_sync.tar.gz -C ./s4KITTI360/train/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0010_sync.tar.gz -C ./s4KITTI360/train/
rm ./s4KITTI360/train/2013_05_28_drive_0003_sync.tar.gz
rm ./s4KITTI360/train/2013_05_28_drive_0007_sync.tar.gz
rm ./s4KITTI360/train/2013_05_28_drive_0010_sync.tar.gz

tar -xzf ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/0.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/1.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/2.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/3.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/0/* ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/1/* ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/2/* ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/3/* ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/
rm -r ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/0/
rm -r ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/1/
rm -r ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/2/
rm -r ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/3/
rm -r ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/0.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/1.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/2.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0000_sync/image_00/scribble/3.tar.gz

tar -xzf ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/0.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/1.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/2.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/3.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/0/* ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/1/* ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/2/* ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/3/* ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/
rm -r ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/0/
rm -r ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/1/
rm -r ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/2/
rm -r ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/3/
rm -r ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/0.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/1.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/2.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0002_sync/image_00/scribble/3.tar.gz

tar -xzf ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/0.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/1.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/2.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/3.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/0/* ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/1/* ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/2/* ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/3/* ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/
rm -r ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/0/
rm -r ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/1/
rm -r ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/2/
rm -r ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/3/
rm -r ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/0.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/1.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/2.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0004_sync/image_00/scribble/3.tar.gz

tar -xzf ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/0.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/1.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/2.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/0/* ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/1/* ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/2/* ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/
rm -r ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/0/
rm -r ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/1/
rm -r ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/2/
rm -r ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/0.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/1.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0005_sync/image_00/scribble/2.tar.gz

tar -xzf ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/0.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/1.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/2.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/0/* ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/1/* ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/2/* ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/
rm -r ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/0/
rm -r ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/1/
rm -r ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/2/
rm -r ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/0.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/1.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0006_sync/image_00/scribble/2.tar.gz

tar -xzf ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/0.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/1.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/2.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/3.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
tar -xzf ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/4.tar.gz -C ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/0/* ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/1/* ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/2/* ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/3/* ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
mv ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/4/* ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/0/
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/1/
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/2/
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/3/
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/4/
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/0.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/1.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/2.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/3.tar.gz
rm -r ./s4KITTI360/train/2013_05_28_drive_0009_sync/image_00/scribble/4.tar.gz
