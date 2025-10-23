import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('ellipses.jpg')

##                   size = width , length
blur = cv.blur (img,(6,6))

gauss_blur = cv.GaussianBlur(img,(5,7),1)

median = cv.medianBlur(img,5)

bilateral = cv.bilateralFilter(img,9,75,75)


plt.subplot(121)
plt.imshow(img)
plt.title('original')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(blur)
plt.title('Averaging')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(gauss_blur)
plt.title('gauss_blur')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(median)
plt.title('median')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(bilateral)
plt.title('bilateral')
plt.xticks([])
plt.yticks([])


plt.show()
