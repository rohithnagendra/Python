import cv2 as cv
import numpy as np

image = cv.imread("gradient.png")

if image is None:
    print("error could not load the image")
else:
    gray_ing = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
  #  avg_brightness = gray_ing.mean()
    avg_brightness = image.mean()
    cv.imshow('gray',gray_ing)
if avg_brightness < 50 :
    print ("the image is dark")
elif 50 <= avg_brightness < 150:
    print("the image is medium")
else:
    print("the image is bright")
    
