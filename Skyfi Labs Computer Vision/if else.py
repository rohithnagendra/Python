import cv2 as cv
import numpy as np

image = cv.imread('hazard10.jpg')

if image is not None :
    print (" image loaded sucssesfully")
    cv.imshow('loaded image',image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("error error error")
