import cv2 as cv
import numpy as np

img = cv.imread('pic1.png')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 
ret, thresh = cv.threshold (img_gray, 127,255,0)
##                                                   outline
contours, hierachy = cv.findContours (thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
##cv.drawContours (img, contours, -1, (0,255,0),3)
##      2)no of obj in img      3)obj
cv.drawContours (img, contours, 3, (0,255,0),3)

cnt =  contours [8]
cv.drawContours (img, [cnt], 0, (0,212,0),3)

cv.imshow('Contours', img)

cv.waitKey (0)
cv.destroyAllWindows ()
