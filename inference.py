import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import argparse
from google_drive_downloader import GoogleDriveDownloader as gdd

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str)
parser.add_argument("--model", type=str)
args = parser.parse_args()

IMG_WIDTH = 256
IMG_HEIGHT = 256

models_url = {
    "cityscapes": "1-EMn9piSvsYnLnlcH1HyODeyqbC9FjRb",
    "edges2handbags": "h10MStW9oQ3R591G_SWi9fdLQQ5ikwQtUZ",
    'edges2shoes' : "1-XypWpkrefi-rmRRXFDHbvHWAyADDvqc",
    "night2day" : "1-Yex8Ujb7fDW_SGYR_yrhK9Tu3GykrCy",
    "facades" : "1-r1C9hrm0rDo9h7odbjc85SIbxbFitaz",
    "maps" : "1-aGQ78qFieai5CkBiUhz3Hw1b-EudpO4"}

id = models_url[args.model]
# gdd.download_file_from_google_drive(file_id=id,
#                                     dest_path='model/{}.h5'.format(args.model))
gen = load_model('model/{}.h5'.format(args.model))

image =cv2.imread(args.input)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
input_image = cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH)).astype('float32')
input_image = input_image[tf.newaxis, ...]
input_image = (input_image / 127.5) - 1

gen_output = gen(input_image, training=True)
gen_output = np.array((gen_output[0,:, :, :] + 1) * 127.5).astype('uint8')

file_name, file_ext = os.path.splitext(os.path.basename(args.input))
cv2.imwrite(f'{file_name}.jpg', gen_output)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.title('Input Image')
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title('Predicted Image')
plt.imshow(gen_output)
plt.show()