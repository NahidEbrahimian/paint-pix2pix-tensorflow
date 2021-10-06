
import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", default='input/maps/02.jpg', type=str)
args = parser.parse_args()

IMG_WIDTH = 256
IMG_HEIGHT = 256

gen = load_model('models/maps_model.h5')

image =cv2.imread(args.input)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
input_image = cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH)).astype('float32')
input_image = input_image[tf.newaxis, ...]
input_image = (input_image / 127.5) - 1 

gen_output = gen(input_image, training=True)
gen_output = np.array((gen_output[0,:, :, :] + 1) * 127.5).astype('uint8')

file_name, file_ext = os.path.splitext(os.path.basename(args.input))
cv2.imwrite(f'output/maps/{file_name}.jpg', gen_output)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.title('Input Image')
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title('Predicted Image')
plt.imshow(gen_output)
plt.show()