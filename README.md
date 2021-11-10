# pix2pix-tensorflow
Image-to-Image Translation Using Conditional Adversarial Networks

|night2day![1_83_to_60](https://user-images.githubusercontent.com/82975802/140188194-9168b7a0-c83a-467e-b26a-2dad7868a235.jpg)|edges2shoes![ba9ea360-d563-4cbb-8d2e-7f54b1f8cc44](https://user-images.githubusercontent.com/82975802/140188431-16737fc6-3d02-4d7a-b0f5-4f228cb6f467.jpeg)|facades![11](https://user-images.githubusercontent.com/82975802/140188508-3b505b02-dbc2-4826-a0f4-37727502b4b7.jpg)|
| ------------- | ------------- | ------------- |

|edges2handbags![103_AB](https://user-images.githubusercontent.com/82975802/140189363-99aa1203-10e1-4f87-92e3-e3283cf077d3.jpg)| cityscapes![10](https://user-images.githubusercontent.com/82975802/140188577-c6936293-9a7f-4301-8e93-79cc08b9525c.jpg)|maps![1002](https://user-images.githubusercontent.com/82975802/140189945-fd63e667-093d-48be-abab-69526bb8df88.jpg)|
| ------------- | ------------- | ------------- |


#

- [ ] train.py
- [x] inference.py

#
### Trained Models

You can download the trained model from the table below

| Dataset Name  | Model |
| ------------- | ------------- |
|maps|[download]( https://drive.google.com/file/d/1-aGQ78qFieai5CkBiUhz3Hw1b-EudpO4/view?usp=sharing)|
|cityscapes|[download]( https://drive.google.com/file/d/1-EMn9piSvsYnLnlcH1HyODeyqbC9FjRb/view?usp=sharing)      |
|edges2handbags|[download]( https://drive.google.com/file/d/10MStW9oQ3R591G_SWi9fdLQQ5ikwQtUZ/view?usp=sharing)      |
|edges2shoes|[download]( https://drive.google.com/file/d/1-XypWpkrefi-rmRRXFDHbvHWAyADDvqc/view?usp=sharing)     |
|facades|[download]( https://drive.google.com/file/d/1-r1C9hrm0rDo9h7odbjc85SIbxbFitaz/view?usp=sharing)     |
|night2day|[download]( https://drive.google.com/file/d/1-Yex8Ujb7fDW_SGYR_yrhK9Tu3GykrCy/view?usp=sharing)      |

#

### Train

- In Google Colaboratory with 12GB ram

- For all datasets, model trained on 5K images of training set and in 40k steps
 
For training:

1-  You can run `pix2pix-cGAN-on-maps-dataset.ipynb` file

2- OR run the following command:

```
```
#

### Inference on Image

1- for inference, first clone this repository using the following command:

```
git clone https://github.com/NahidEbrahimian/pix2pix-tensorflow
```

2- Then, according to the pictures above, select your favorite dataset name that you want to run inference(for example: maps, cityscapes or ...)

3- Put your input images in `./input/dataset_name` directory(dataset_name refers to favorite dataset name that you selected in previous step)

4- run the following command

dataset_name: favorite dataset name that selected in step2

input: your input images

```
python3 inference.py --input input/maps/01.jpg --dataset_name maps

```
