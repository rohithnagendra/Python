import numpy as np
import cv2 as cv

img = np.zeros((512,512,3),np.uint8)

cv.line(img,(69,23),(511,511),(255,20,30),9)
##
cv.rectangle (img,(384,500),(510,198),(0,225,0),5)
##
cv.circle(img,(100,53),93,(0,0,225),-8)
##
pts = np.array([[190,150],[240,800],[79,220],[690,169],[60,200],[70,400]],np.int32)
cv.polylines(img,[pts],True,(0,255,255),3)
##
##font = cv.FONT_ITALIC
##cv.putText(img,'Welcome',(0,480),font,2,(255,255,255),2)

cv.imshow('Image',img)

cv.waitKey(0)
cv.destroyAllWindows()
