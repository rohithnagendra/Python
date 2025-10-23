import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('hazard10.jpg',0)

edges = cv.Canny(img,100,200)

plt.subplot(121)
plt.imshow(img,'gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(edges,'gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])

plt.show()
