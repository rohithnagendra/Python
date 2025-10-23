"""
OpenCV All-in-One Functions
===========================
This script contains multiple OpenCV-based image and video processing examples:
1. Save Video
2. Play Video
3. Changing Color Space
4. Smoothing
5. Simple Threshold
6. Adaptive Threshold
7. Canny Video
8. Canny Edge Detection
9. Finding Contours
10. Contour Properties
11. Object Tracking (Basic)
12. Tracking of Coloured Object
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# ============================================================
# 1. SAVE VIDEO
# ============================================================
def save_video():
    cam = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    output = cv.VideoWriter('Output.avi', fourcc, 20.0, (640, 480))

    while cam.isOpened():
        ret, frame = cam.read()
        if ret:
            cv.imshow('frame', frame)
            output.write(frame)
            if cv.waitKey(1) == ord('s'):
                print('saved video')
                break
        else:
            print('Error in Capturing Video')
            break

    cam.release()
    output.release()
    cv.destroyAllWindows()


# ============================================================
# 2. PLAY VIDEO
# ============================================================
def play_video():
    vid = cv.VideoCapture('vtest.avi')

    while vid.isOpened():
        ret, frame = vid.read()
        if not ret:
            break
        cv.imshow('frame', frame)
        key = cv.waitKey(10)
        if key == 27:
            break

    cv.destroyAllWindows()


# ============================================================
# 3. CHANGING COLOR SPACE
# ============================================================
def changing_color_space():
    img = cv.imread('opencv-logo.png')
    cv.imshow('BGR', img)
    print('Shape:', img.shape, 'Size:', img.size)

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', img_gray)
    print('Gray Shape:', img_gray.shape, 'Size:', img_gray.size)

    RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow('RGB', RGB)
    print('RGB Shape:', RGB.shape, 'Size:', RGB.size)

    HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow('HSV', HSV)
    print('HSV Shape:', HSV.shape, 'Size:', HSV.size)

    cv.waitKey(0)
    cv.destroyAllWindows()


# ============================================================
# 4. SMOOTHING
# ============================================================
def smoothing():
    img = cv.imread('ellipses.jpg')
    blur = cv.blur(img, (6, 6))
    gauss_blur = cv.GaussianBlur(img, (5, 7), 1)
    median = cv.medianBlur(img, 5)
    bilateral = cv.bilateralFilter(img, 9, 75, 75)

    plt.subplot(151), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
    plt.subplot(152), plt.imshow(cv.cvtColor(blur, cv.COLOR_BGR2RGB)), plt.title('Blur')
    plt.subplot(153), plt.imshow(cv.cvtColor(gauss_blur, cv.COLOR_BGR2RGB)), plt.title('Gaussian')
    plt.subplot(154), plt.imshow(cv.cvtColor(median, cv.COLOR_BGR2RGB)), plt.title('Median')
    plt.subplot(155), plt.imshow(cv.cvtColor(bilateral, cv.COLOR_BGR2RGB)), plt.title('Bilateral')
    plt.show()


# ============================================================
# 5. SIMPLE THRESHOLD
# ============================================================
def simple_threshold():
    img = cv.imread('gradient.png', 0)
    cv.imshow('original', img)
    ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
    ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
    ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
    ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

    titles = ['Original', 'Binary', 'Binary_INV', 'Trunc', 'ToZero', 'ToZero_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray'), plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()


# ============================================================
# 6. ADAPTIVE THRESHOLD
# ============================================================
def adaptive_threshold():
    img = cv.imread('sudoku.png', 0)
    img = cv.medianBlur(img, 5)
    cv.imshow('Original Image', img)

    ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

    titles = ['Original', 'Global Threshold', 'Adaptive Mean', 'Adaptive Gaussian']
    images = [img, th1, th2, th3]

    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray'), plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

    cv.waitKey(0)
    cv.destroyAllWindows()


# ============================================================
# 7. CANNY VIDEO
# ============================================================
def canny_video():
    cam = cv.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, 100, 150)
        cv.imshow('edges', edges)
        if cv.waitKey(20) == 27:
            break
    cam.release()
    cv.destroyAllWindows()


# ============================================================
# 8. CANNY EDGE DETECTION
# ============================================================
def canny_edge_detection():
    img = cv.imread('hazard10.jpg', 0)
    edges = cv.Canny(img, 100, 200)

    plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original')
    plt.subplot(122), plt.imshow(edges, 'gray'), plt.title('Canny Edges')
    plt.show()


# ============================================================
# 9. FINDING CONTOURS
# ============================================================
def finding_contours():
    img = cv.imread('pic1.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) > 8:
        cv.drawContours(img, contours, 3, (0, 255, 0), 3)
        cnt = contours[8]
        cv.drawContours(img, [cnt], 0, (0, 212, 0), 3)
    else:
        print("Not enough contours found.")

    cv.imshow('Contours', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# ============================================================
# 10. CONTOURS PROPERTIES
# ============================================================
def contours_properties():
    img = cv.imread('pic1.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) > 7:
        cnt = contours[7]
        cv.drawContours(img, [cnt], 0, (0, 235, 0), 3)
        M = cv.moments(cnt)
        cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
        print('Centroid:', (cx, cy))
        print('Area:', cv.contourArea(cnt))
        print('Perimeter:', cv.arcLength(cnt, True))

        x, y, w, h = cv.boundingRect(cnt)
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        (x, y), radius = cv.minEnclosingCircle(cnt)
        center, radius = (int(x), int(y)), int(radius)
        cv.circle(img, center, radius, (255, 0, 0), 2)

        cv.imshow('Contours', img)
        cv.waitKey(0)
    else:
        print("Not enough contours found.")
    cv.destroyAllWindows()


# ============================================================
# 11. OBJECT TRACKING (Frame Display)
# ============================================================
def object_tracking():
    cam = cv.VideoCapture(0)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])

    while True:
        ret, frame = cam.read()
        cv.imshow('Frame', frame)
        if cv.waitKey(10) == 27:
            break

    img_RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    plt.imshow(img_RGB)
    plt.show()
    cam.release()
    cv.destroyAllWindows()


# ============================================================
# 12. TRACKING OF COLOURED OBJECT
# ============================================================
def tracking_coloured_object():
    cam = cv.VideoCapture(0)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        image_smooth = cv.GaussianBlur(frame, (7, 7), 0)
        image_hsv = cv.cvtColor(image_smooth, cv.COLOR_BGR2HSV)
        mask = cv.inRange(image_hsv, lower_yellow, upper_yellow)

        contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        if len(contours) != 0:
            cnt = max(contours, key=cv.contourArea)
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv.imshow('Frames', frame)
        if cv.waitKey(100) == 27:
            break

    cam.release()
    cv.destroyAllWindows()


# ============================================================
# MAIN EXECUTION
# ============================================================
if __name__ == "__main__":
    print("Select a function to run:")
    print("""
1. save_video()
2. play_video()
3. changing_color_space()
4. smoothing()
5. simple_threshold()
6. adaptive_threshold()
7. canny_video()
8. canny_edge_detection()
9. finding_contours()
10. contours_properties()
11. object_tracking()
12. tracking_coloured_object()
    """)

    choice = input("Enter function number (1-12): ").strip()

    funcs = {
        "1": save_video,
        "2": play_video,
        "3": changing_color_space,
        "4": smoothing,
        "5": simple_threshold,
        "6": adaptive_threshold,
        "7": canny_video,
        "8": canny_edge_detection,
        "9": finding_contours,
        "10": contours_properties,
        "11": object_tracking,
        "12": tracking_coloured_object,
    }

    func = funcs.get(choice)
    if func:
        func()
    else:
        print("Invalid choice.")
