# Final Project

Kin Loh, kmloh@ucsd.edu

## Abstract Proposal

In this final project, we continue to explore futher on one of our past project which transforms a cat into a tiger using cycleGAN. We continue to explore different technique to do the transformation of a cat into a tiger. Our idea is to use HED model to generate contour images of cats, and at the same time, pix2pix model is used to train sketches of tiger. The generated contour images of cats are then used as the input test for the generator of pix2pix tiger trained model.

## Project Report

Upload your project report (4 pages) as a pdf with your repository, following this template: [google docs](https://docs.google.com/document/d/133H59WZBmH6MlAgFSskFLMQITeIC5d9b2iuzsOfa4E8/edit?usp=sharing).

## Model/Data
-pretrained_model/ -- contained a zipped sketch2tiger_pretrained_3 folder 

##  Raw Data
- raw_data/ -- contained images and sketches of tiger and cat 

## Code

0. get the repo from [here](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
```
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
```
1. Before training the data with your own dataset
- place your own data_images into a new folder into datasets folder in the repo above
- make sure the data_images folder contains these subfolder 
    - trainA  ===> real images of tiger
    - trainB  ===> sketches of a tiger
    - testA   ===> real images of tiger
    - testB   ===> sketches of cat
- run the following script that is in the datasets folder in the repo
```
python make_dataset_aligned.py --dataset-path ./path/to/folder_name
```
_NOTE_: 
This script will combine the images from trainA and trainB, allign them and merge them into a images. The alligned images will be placed in folder call train which is lated used for training.

2. Train the data using dataset given / your own dataset
```
python train.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --direction BtoA
```
_NOTE_: 
After training is done. The trained model will be generated in checkpoints folder. Move the latest_net_G.pth to a new directory folder named _pretrained_3

3. Generate the picture using pretained model / your own trained model
```
python test.py --dataroot ./datasets/tes_set --direction BtoA --model pix2pix --name sketch2tiger_pretrained_3
```

## Results

## Others
- my_util_tools -- python script to rename/copy the images


## Technical Notes

Any implementation details or notes we need to repeat your work. 
- Does this code require other pip packages, software, etc?
- Does it run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

- [pip2pix in pytorch](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
- dataset from sketchyGAN [Link1](http://sketchy.eye.gatech.edu/) [Link2](https://goo.gl/SNpMmK)
- [dataset from cyclegan pytorch](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)
- [ImageNet](www.image-net.org/)