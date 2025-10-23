import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg')
cv.imshow('rol',img)

b,g,r = cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

img_merge_bgr = cv.merge([b,g,r])
cv.imshow('merge_bgr',img_merge_bgr)

img_HSV =cv.cvtColor(img,cv.COLOR_BGR2HSV)

h,s,v = cv.split(img_HSV)
cv.imshow('hsv',img_HSV)
cv.imshow('hue',h)
cv.imshow('saturation',s)
cv.imshow('value',v)

img_merge_HSV = cv.merge([h,s,v])
cv.imshow('merge_hsv',img_merge_HSV)

cv.waitKey(0)
cv.destroyAllWindows()
