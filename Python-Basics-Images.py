"""
Combined Python Program
Author: Rohith N
Description:
This single Python file contains multiple functions demonstrating different Python and OpenCV concepts:
1. Accessing and Changing Pixel
2. Capturing Video
3. List Operations
4. Functions Demonstration
5. While Loop
6. For Loop
7. If-Else Condition
8. If-Else Ladder
9. Reading Images
"""

import cv2 as cv
import numpy as np

# 1️⃣ ACCESSING AND CHANGING PIXEL
def access_and_change_pixel():
    img = cv.imread('hazard10.jpg')
    if img is None:
        print("Error: Image not found.")
        return

    cv.imshow('Original Image', img)
    print('Shape:', img.shape)
    print('Size:', img.size)
    print('Data type:', img.dtype)

    px = img[100, 100]
    print('Pixel value at (100,100):', px)
    print('Blue channel value at (100,100):', img[100, 100, 0])

    img[100, 100] = [212, 255, 249]
    img[135, 134] = [255, 255, 255]
    cv.imshow('Modified Image', img)

    cv.waitKey(0)
    cv.destroyAllWindows()


# 2️⃣ CAPTURE VIDEO
def capture_video():
    cam = cv.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press ESC to stop video capture.")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error capturing frame.")
            break
        cv.imshow('Live Video', frame)
        key = cv.waitKey(1)
        if key == 27:  # ESC key
            break

    cam.release()
    cv.destroyAllWindows()


# 3️⃣ LIST OPERATIONS
def list_operations():
    number = [1, 2, 3, 4, 5]
    mix_list = [1, "myself", 3.14, True]
    nested_list = [1, 2, [3, 4]]
    value = [13, 15, 34, 55, 77, 99, 32, 234]
    mix_value = [1233, "yourself", 4.13, True]
    nested_value = [13, 14, [23, 54]]

    print(value)
    print(mix_value)
    print(nested_value)

    print(value[0])
    print(mix_list[1])

    value[1] = 89
    print("Updated value list:", value)

    mix_list.append(784)
    nested_list.insert(2, 5423)
    mix_value.remove(4.13)
    del value[3]

    print("Modified Lists:")
    print("mix_list:", mix_list)
    print("nested_list:", nested_list)
    print("mix_value:", mix_value)
    print("value:", value)

    valu_list = [1, 2, 3, 4, 5, 5, 66, 7, 47, 57]
    print("Sub-list (1:9):", valu_list[1:9])
    print("Negative index slice (-3:-1):", valu_list[-3:-1])
    print("Step slicing (::2):", valu_list[::2])

    print("Length of list_val:", len(valu_list))
    friut = ['orange', 'apple', 'banana', 'guava']
    for fruits in friut:
        print(fruits)


# 4️⃣ FUNCTION TYPES
def function_examples():
    def nmana():
        print("er")

    def aB(name):
        print(f"hello, {name}")

    def square(x):
        return x * x

    def greet(name="guest"):
        print(f"hello, {name}")

    def introduce(name, age):
        print(f"Name: {name}")
        print(f"Age: {age}")

    def add_numbers(*args):
        return sum(args)

    def describe_person(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    nmana()
    aB("rohith")
    aB("ronith")
    print(square(4))
    greet()
    greet("hhdhdhh")
    introduce(age=14, name="Rohith.N")
    print(add_numbers(1, 2, 3, 4, (19876 % 3235) ^ 23423))
    describe_person(key="ss", value="rr")

    square_lambda = lambda x: x * x
    print(square_lambda(5))


# 5️⃣ WHILE LOOP
def while_loop_demo():
    i = 1
    while i <= 10:
        print(i)
        i += 10

    count = 0
    while count < 3:
        print(count)
        count += 1
    else:
        print("loop finished")


# 6️⃣ FOR LOOP
def for_loop_demo():
    for i in range(5):
        print(i)

    fruits = ['orange', 'apple', 'banana', 'guava']
    for f in fruits:
        print(f)

    text = "my name is yipeeeee"
    for b in text:
        print(b)

    for i in range(5):
        if i == 3:
            continue
        print(i)

    for i in range(5):
        print(i)
    else:
        print("loop finished")

    for i in range(5, 11, 3):
        print(i, end="  ")
    print()


# 7️⃣ IF ELSE (Image Loading)
def if_else_image():
    image = cv.imread('hazard10.jpg')
    if image is not None:
        print("Image loaded successfully")
        cv.imshow('Loaded Image', image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Error: Could not load image.")


# 8️⃣ IF ELSE LADDER (Brightness Detection)
def if_else_ladder():
    image = cv.imread("gradient.png")
    if image is None:
        print("Error: Could not load the image")
        return

    gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    avg_brightness = gray_img.mean()
    cv.imshow('Gray Image', gray_img)

    if avg_brightness < 50:
        print("The image is dark")
    elif 50 <= avg_brightness < 150:
        print("The image is medium")
    else:
        print("The image is bright")

    cv.waitKey(0)
    cv.destroyAllWindows()


# 9️⃣ READING IMAGE
def reading_image():
    image = cv.imread('hazard10.jpg')
    if image is None:
        print("Error: Could not read image.")
        return
    cv.imshow('Football', image)
    cv.waitKey(0)
    cv.destroyAllWindows()


# 🧠 MAIN MENU
if __name__ == "__main__":
    print("=== Combined Python Demo Program ===")
    print("Select a function to run:")
    print("1. Access and Change Pixel")
    print("2. Capture Video")
    print("3. List Operations")
    print("4. Function Examples")
    print("5. While Loop Demo")
    print("6. For Loop Demo")
    print("7. If-Else Image")
    print("8. If-Else Ladder")
    print("9. Reading Image")

    choice = input("Enter your choice (1-9): ")

    functions = {
        "1": access_and_change_pixel,
        "2": capture_video,
        "3": list_operations,
        "4": function_examples,
        "5": while_loop_demo,
        "6": for_loop_demo,
        "7": if_else_image,
        "8": if_else_ladder,
        "9": reading_image
    }

    func = functions.get(choice)
    if func:
        func()
    else:
        print("Invalid choice.")
