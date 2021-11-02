# pix2pix-tensorflow
Image-to-Image Translation Using Conditional Adversarial Networks

![download](https://user-images.githubusercontent.com/82975802/136291775-3603ee00-442c-4dea-a76c-319c75e73245.png)
![facades](https://user-images.githubusercontent.com/82975802/139734285-b37c1997-d388-4cf1-8772-e3fdc5085373.png)

#


- [ ] train.py
- [x] inference.py

#

| Dataset  | Model |
| ------------- | ------------- |
|maps|[download]( https://drive.google.com/file/d/1-aGQ78qFieai5CkBiUhz3Hw1b-EudpO4/view?usp=sharing)|
|cityscapes|[download]( https://drive.google.com/file/d/1-EMn9piSvsYnLnlcH1HyODeyqbC9FjRb/view?usp=sharing)      |
|edges2handbags|[download]( https://drive.google.com/file/d/10MStW9oQ3R591G_SWi9fdLQQ5ikwQtUZ/view?usp=sharing)      |
|edges2shoes|[download]( https://drive.google.com/file/d/1-XypWpkrefi-rmRRXFDHbvHWAyADDvqc/view?usp=sharing)     |
|facades|[download]( https://drive.google.com/file/d/1-r1C9hrm0rDo9h7odbjc85SIbxbFitaz/view?usp=sharing)     |
|night2day|      |

#

### Train

#

### Inference

1- for inference, first clone this repository using the following command:

```
git clone https://github.com/NahidEbrahimian/pix2pix-tensorflow
```

2- Then, download pre-trained model from the table and put in `./pix2pix-tensorflow` directory.

3- Put your input images in `./input/maps` directory and run the following command. generated images will be saved under `./output/maps` directory. 

```
!python3 inference.py --input input/maps/03.jpg
```
