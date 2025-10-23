import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('hazard10.jpg')
cv.imshow('image',img)



img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

plt.axis('OFF')
plt.imshow(img_RGB)
plt.show()

ball = img[235:295,465:530]

#ball = ([255,255,255])
img[235:295,465:530]= ball

img [235:295,555:620]=ball
img [235:295,380:445] = ball
head = img[30:80,260:315]
head = ([255,255,0])
img [30:92,265:325]= head



cv.imshow('ROI',img)

cv.waitKey(0)
cv.destroyAllWindows()
