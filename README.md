# pix2pix-tensorflow
Image-to-Image Translation Using Conditional Adversarial Networks

![download](https://user-images.githubusercontent.com/82975802/136291775-3603ee00-442c-4dea-a76c-319c75e73245.png)

#


- [x] train.py
- [x] inference.py

#

| Dataset  | Model |
| ------------- | ------------- |
|maps|[download]( https://drive.google.com/file/d/1-aGQ78qFieai5CkBiUhz3Hw1b-EudpO4/view?usp=sharing)|
|cityscapes|      |
|edges2handbags|      |
|edges2shoes|      |
|facades|     |
|night2day|      |

#

### Train

#

### Inference

1- for inference, first clone this repository using following command:

```
git clone https://github.com/NahidEbrahimian/pix2pix-tensorflow
```

2- then, download pretraned model from the table and put in `./pix2pix-tensorflow` directory

3- put your input images in `./input/maps` directory and run the following command. generated images will be saved under `./output/maps` directory. 

```
!python3 inference.py --input input/maps/03.jpg
```
