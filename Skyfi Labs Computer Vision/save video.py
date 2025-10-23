import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
## video_writer is a function to encode the video file of cam variable
## *XVID allows to add multiple arguements
fourcc = cv.VideoWriter_fourcc(*'XVID')
##file to be saved in the documents          fps    pixel value for fps
output = cv.VideoWriter('Output.avi',fourcc,20.0,(640,480))

while (cam.isOpened()):
    ret, frame = cam.read()
    if ret ==True:
        cv.imshow('frame',frame)
        output.write(frame)

        if cv.waitKey(1) == ord('s'):
            print('saved video')
            break
    else:
        print('Error in Capturing Video')
        break



cam.release()
output.release()

