import cv2 as cv
import numpy as p

img =cv.imread('pic1.png')

img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img_gray, 127, 255, 0)

contours, hierachy = cv.findContours (thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cnt =  contours [7]
## highlight the object
cv.drawContours (img, [cnt], 0, (0,235,0),3)

M = cv.moments(cnt)
cx = int(M['m10']/M['m00'])## these are spacial movement that represent area of the object
cy = int(M['m01']/M['m00'])##m00 will be total area inside contour

print('Centroid of the face is ',(cx,cy))

area = cv.contourArea(cnt)
print('Area of the Face is ', area)

perimeter = cv.arcLength(cnt,True)
print('Perimeter of the Face is ', perimeter)

## helps to draw rectangle and circle accourding to the object
x,y,w,h = cv.boundingRect(cnt)
#             Source img,value respect to x and y axis,width and height,color,thickness
cv.rectangle(img , (x,y),(x+w,y+h),(255,0,0),2)


## help us by taking radius to draw circle
(x,y),radius = cv.minEnclosingCircle(cnt)
##aware of the center before to draw circle
center = (int(x),int(y))
radius = int(radius)
##        source img,center,radius value,color,thickness
cv.circle(img,center,radius,(255,0,0),2)
## showing the image
cv.imshow('Contours',img)

cv.waitKey(0)
cv.destroyAllWindows()
