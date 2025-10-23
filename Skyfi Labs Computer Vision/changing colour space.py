import cv2 as cv
import numpy as np

img = cv.imread('opencv-logo.png')
cv.imshow('BGR',img)
print('the shape of the image is ')
print(img.shape)
print('the size of the image')
print(img.size)

img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Color',img_gray)
print('the shape of the image is')
print(img_gray.shape)
print('the size of the image is')
print(img_gray.size)

RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('3 color',RGB)
print('the shape of the image is')
print(RGB.shape)
print('the size of the image is')
print(RGB.size)

IG_HSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('4 color',IG_HSV)
print('the shape of the image is')
print(IG_HSV.shape)
print('the size of the image is')
print(IG_HSV.size)
cv.waitKey(0)
cv.destroyAllWindows()
