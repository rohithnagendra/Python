import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('sudoku.png',0)

img = cv.medianBlur(img,5)
cv.imshow('Original Image', img)

ret,TH1 = cv.threshold(img , 127,255,cv.THRESH_BINARY)
TH2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                           cv.THRESH_BINARY,11,2)
TH3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                           cv.THRESH_BINARY,11,2)

titles = ['Original Image','Global Thresholding (v = 127)','Adaptive Mean Thresholding','Adaptive Gaussian Thresholding']
images = [img , TH1 , TH2, TH3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
