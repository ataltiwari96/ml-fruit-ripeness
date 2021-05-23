import cv2
import tensorflow as tf
from tensorflow.python.keras.models import load_model
import os
import sys

CATEGORIES = ["ripened apple", "unripened apple"]


def prepare(filepath):
    IMG_SIZE = 250  
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = load_model("64x31-CNN.model")

while True:
    a=input("Enter 1 to Capture Image & 2 to Exit: ")
    if a==1:
        os.system("fswebcam --no-banner image.jpg")
        prediction = model.predict([prepare('image.jpg')])
        print(prediction)
        print(CATEGORIES[int(prediction[0][0])])

    else:
        print "Goodbye!"
        break
