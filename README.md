# Final Project

Kin Loh, kmloh@ucsd.edu
Zhuoqun Xu, zhx068@ucsd.edu

## Abstract Proposal

In this final project, we continue to explore futher on one of our past project which transforms a cat into a tiger using cycleGAN. We continue to explore different technique to do the transformation of a cat into a tiger. Our idea is to use HED model to generate contour images of cats, and at the same time, pix2pix model is used to train sketches of tiger. The generated contour images of cats are then used as the input test for the generator of pix2pix tiger trained model.

## Project Report

Upload your project report (4 pages) as a pdf with your repository, following this template: [google docs](https://docs.google.com/document/d/133H59WZBmH6MlAgFSskFLMQITeIC5d9b2iuzsOfa4E8/edit?usp=sharing).

## Model/Data
- pretrained_model/countour2tiger  --- zipped version of contour2tiger model
- pretrained_model/sketch2tiger   --- zipped version of sketch2tiger model

##  Raw Data
### contained images/sketches/contour of tiger and cat
- data(from_sketchy)
- generated_contour
- cat zipped dataset 

## Code
### part A


0. get the HED repository
```
git clone https://github.com/moabitcoin/holy-edge.git
```
1. requirements
```
cd holy-edge
pip install -r requirements.txt
export OMP_NUM_THREADS=1
```

2. download pretrained model [here](https://mega.nz/#!YU1FWJrA!O1ywiCS2IiOlUCtCpI6HTJOMrneN-Qdv3ywQP5poecM)

3. Use this to verify the pretrained model
```
19ff134af12b6ea0c0ff35664b031ba5 hed/models/vgg16.npy
```
4. manually download the HED model that is trained on augmented training set created by the authors if necessery [here](http://vcl.ucsd.edu/hed/HED-BSDS.tar)

5. set up the config file located at hed/configs/hed.yaml

```
# location where training data : http://vcl.ucsd.edu/hed/HED-BSDS.tar would be downloaded and decompressed
download_path: '<path>'
# location of snapshot and tensorbaord summary events
save_dir: '<path>'
# location where to put the generated edgemaps during testing
test_output: '<path>'
```

6. put images into a test folder in HED-BSDS(from step 4)
7. update the filename in the test folder accordingly in test.lst
8. edit the config yml based on the input dimension of the file in test folder.

_testing with the pretrained model_
9. edit your config file located at hed/configs/hed.yaml to change the location of the pre-trained HED model
```
save_dir: <path_to_repo_on_disk>/hed
test_snapshot: 5000
# location where to put the generated edgemaps during testing
test_output: '<path>'
```
_run prediction_
```
CUDA_VISIBLE_DEVICES=1 python run-hed.py --test --config-file hed/configs/hed.yaml --gpu-limit 0.4
feh <test_output>
```

### Part B

0. get the pix2pix repo from [here](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
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
 - More details are in the report
 - Sample generated image 
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained/small_dataset/html_imgs/01.PNG)
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained/small_dataset/html_imgs/02.PNG)
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained/small_dataset/html_imgs/03.PNG)
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained/small_dataset/html_imgs/04.PNG)
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained/small_dataset/html_imgs/05.PNG)

 Trained with larger datasets
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained_3/test_latest/html_img/01.PNG)
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained_3/test_latest/html_img/02.PNG)
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained_3/test_latest/html_img/03.PNG)
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained_3/test_latest/html_img/04.PNG)
![](https://github.com/ucsd-ml-arts/ml-art-final2-amcda-anymlcandoart/blob/kin/results/sketch2tiger_pretrained_3/test_latest/html_img/05.PNG)


## Others
- my_util_tool -- python script to rename/copy/remove the images


## Technical Notes
- pix2pix model in pytorch runs on datahub but it failed to setup the web localhost. Anyway, the models can train the images and generate the images
- HED model runs on my own machine due to some dependency issue

## Reference

- [pip2pix in pytorch](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
- dataset from sketchyGAN [Link1](http://sketchy.eye.gatech.edu/) [Link2](https://goo.gl/SNpMmK)
- [dataset from cyclegan pytorch](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)
- [ImageNet](www.image-net.org/)