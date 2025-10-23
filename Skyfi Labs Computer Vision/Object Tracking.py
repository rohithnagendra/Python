import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

cam = cv.VideoCapture(0)
## WE NEED MINIMUM VALUE OF INTENSITY OF PIXELS AND MAXIMUM
## LOWEST INTENSITY OF YELLOW
lower_yellow = np.array([20,100,100])
##HIGH INTENSITY OF YELLOW
upper_yellow = np.array([40,255,255])

while(True):
    ret,frame = cam.read()
    cv.imshow('Frame',frame)
    key = cv.waitKey(10)
    if key == 27:
        break

img_RGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
plt.imshow(img_RGB)
plt.show()

cam.release()
cv.destroyAllWindows()
