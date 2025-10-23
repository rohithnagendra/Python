import cv2 as cv
import numpy as np

img = cv.imread('hazard10.jpg')
cv.imshow('image',img)

print('the shape of the image is')
print(img.shape)

print('the size of a image')
print(img.size)

print('the data type of the pixel values in the image is ')
print(img.dtype)

px = img[100,100]
print('the value of the pixel 100,100 is')
print(px)

blue = img[100,100,0]
print('the value of the blue colour in pixel at 100x100')
print(blue)

img[100,100] = [212,255,249]
img[135,134] = [255,255,255]
cv.imshow('image1',img)

cv.waitKey(0)
cv.destroyAllWindows()
