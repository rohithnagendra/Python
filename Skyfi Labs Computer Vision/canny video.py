import cv2 as cv
import numpy as np

cam =cv.VideoCapture(0)

while(1):
    ret,frame = cam.read()
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(frame,100,150)
    cv.imshow('edges',edges)

    key = cv.waitKey(20)
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()
