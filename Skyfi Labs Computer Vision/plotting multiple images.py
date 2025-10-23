import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')
cv.imshow('BGR',img)
img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

img_HSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',img_HSV)
img_hsv_RGB = cv.cvtColor(img_HSV,cv.COLOR_BGR2RGB)

titles = ['original','hsv']
images = [img_RGB,img_hsv_RGB]

plt.axis("off")
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


cv.waitKey(0)
cv.destroyAllWindows()
