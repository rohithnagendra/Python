import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('lena.jpg')
cv.imshow('origin',img)
img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
