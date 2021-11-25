def inference(input):
    import os
    import numpy as np
    import cv2
    import tensorflow as tf
    from tensorflow.keras.models import load_model
    from google_drive_downloader import GoogleDriveDownloader as gdd

    IMG_WIDTH = 256
    IMG_HEIGHT = 256

    model_path = 'model'
    if not os.path.exists(model_path):
        os.makedirs(model_path)
        gdd.download_file_from_google_drive(file_id='1-XypWpkrefi-rmRRXFDHbvHWAyADDvqc',
                                        dest_path=os.path.join(model_path, 'edges2shoes.h5'))
    gen = load_model(os.path.join(model_path, 'edges2shoes.h5'))

    input_image = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
    input_image = cv2.resize(input_image, (IMG_HEIGHT, IMG_WIDTH)).astype('float32')
    input_image = input_image[tf.newaxis, ...]
    input_image = (input_image / 127.5) - 1

    gen_output = gen(input_image, training=True)
    gen_output = np.array((gen_output[0,:, :, :] + 1) * 127.5).astype('uint8')

    cv2.imshow('gen_output', gen_output)
    cv2.waitKey()

    return gen_output