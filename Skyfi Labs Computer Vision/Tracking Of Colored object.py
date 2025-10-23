import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])

lower_red = np.array([0,125,125])
upper_red = np.array([10,255,255])

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Smooth the image
    image_smooth = cv.GaussianBlur(frame, (7, 7), 0)

    # Convert to HSV
    image_hsv = cv.cvtColor(image_smooth, cv.COLOR_BGR2HSV)


    cv.imshow('HSV IMAGE',image_hsv)
    # Create mask for yellow color #in range = work for range for color from lower to upper range and hold the thresholded image
    image_threshold = cv.inRange(image_hsv,lower_red, upper_red )#upper_red,lower_red )

    cv.imshow('hsv',image_threshold)
    
    # Find contours
    contours, hierarchy = cv.findContours(image_threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        areas = [cv.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt = contours[max_index]
        x_bound, y_bound, w_bound, h_bound = cv.boundingRect(cnt)
        cv.rectangle(frame, (x_bound, y_bound), (x_bound + w_bound, y_bound + h_bound), (255, 0, 0), 2)

    cv.imshow('Frames', frame)
    key = cv.waitKey(100)
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()
