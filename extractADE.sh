#!/bin/sh
tar -xzf ./s4ADE20K/scribbles/training/0.tar.gz -C ./s4ADE20K/scribbles/training/
tar -xzf ./s4ADE20K/scribbles/training/1.tar.gz -C ./s4ADE20K/scribbles/training/
tar -xzf ./s4ADE20K/scribbles/training/2.tar.gz -C ./s4ADE20K/scribbles/training/
tar -xzf ./s4ADE20K/scribbles/training/3.tar.gz -C ./s4ADE20K/scribbles/training/
tar -xzf ./s4ADE20K/scribbles/training/4.tar.gz -C ./s4ADE20K/scribbles/training/
tar -xzf ./s4ADE20K/scribbles/training/5.tar.gz -C ./s4ADE20K/scribbles/training/
tar -xzf ./s4ADE20K/scribbles/training/6.tar.gz -C ./s4ADE20K/scribbles/training/

rm ./s4ADE20K/scribbles/training/0.tar.gz
rm ./s4ADE20K/scribbles/training/1.tar.gz
rm ./s4ADE20K/scribbles/training/2.tar.gz
rm ./s4ADE20K/scribbles/training/3.tar.gz
rm ./s4ADE20K/scribbles/training/4.tar.gz
rm ./s4ADE20K/scribbles/training/5.tar.gz
rm ./s4ADE20K/scribbles/training/6.tar.gz

mv ./s4ADE20K/scribbles/training/0/* ./s4ADE20K/scribbles/training
mv ./s4ADE20K/scribbles/training/1/* ./s4ADE20K/scribbles/training
mv ./s4ADE20K/scribbles/training/2/* ./s4ADE20K/scribbles/training
mv ./s4ADE20K/scribbles/training/3/* ./s4ADE20K/scribbles/training
mv ./s4ADE20K/scribbles/training/4/* ./s4ADE20K/scribbles/training
mv ./s4ADE20K/scribbles/training/5/* ./s4ADE20K/scribbles/training
mv ./s4ADE20K/scribbles/training/6/* ./s4ADE20K/scribbles/training

rm -r ./s4ADE20K/scribbles/training/0/
rm -r ./s4ADE20K/scribbles/training/1/
rm -r ./s4ADE20K/scribbles/training/2/
rm -r ./s4ADE20K/scribbles/training/3/
rm -r ./s4ADE20K/scribbles/training/4/
rm -r ./s4ADE20K/scribbles/training/5/
rm -r ./s4ADE20K/scribbles/training/6/
