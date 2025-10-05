"""
Merged demos: OpenCV image/video + Python basics
One-file script containing functions for each functionality from the user's snippets.
Usage examples:
  python merged_opencv_and_python_demos.py --show-image hazard10.jpg
  python merged_opencv_and_python_demos.py --capture-video
  python merged_opencv_and_python_demos.py --list-demo
  python merged_opencv_and_python_demos.py --all
"""

import cv2 as cv
import numpy as np
import argparse
import sys

# ------------------------- Image utilities -------------------------

def load_image(path: str):
    """Load image with OpenCV. Returns image or None."""
    img = cv.imread(path)
    if img is None:
        print(f"[load_image] Failed to load image: {path}")
    return img


def show_image(winname: str, img, wait: bool = True):
    """Show image in a window and optionally wait until keypress."""
    if img is None:
        print(f"[show_image] No image to show for window '{winname}'.")
        return
    cv.imshow(winname, img)
    if wait:
        cv.waitKey(0)
        cv.destroyWindow(winname)


def print_image_info(img, name: str = "image"):
    """Print basic properties of an image (shape, size, dtype)."""
    if img is None:
        print(f"[print_image_info] No image named {name}.")
        return
    print(f"[{name}] shape: {img.shape}")
    print(f"[{name}] size: {img.size}")
    print(f"[{name}] dtype: {img.dtype}")


def access_pixel(img, x: int, y: int):
    """Return full BGR pixel and its blue channel at (x,y)."""
    if img is None:
        print("[access_pixel] image is None")
        return None
    h, w = img.shape[:2]
    if not (0 <= y < h and 0 <= x < w):
        print(f"[access_pixel] Coordinates ({x},{y}) out of range for image {w}x{h}")
        return None
    px = img[y, x]
    blue = px[0]
    print(f"Pixel at ({x},{y}) = {px} (B,G,R)")
    print(f"Blue channel at ({x},{y}) = {blue}")
    return px


def modify_pixels(img, modifications: dict):
    """Modify multiple pixel coordinates in-place.
    modifications: {(x,y): (B,G,R), ...}
    Returns the modified image.
    """
    if img is None:
        print("[modify_pixels] image is None")
        return None
    h, w = img.shape[:2]
    for (x, y), color in modifications.items():
        if 0 <= y < h and 0 <= x < w:
            img[y, x] = np.array(color, dtype=img.dtype)
            print(f"Modified pixel ({x},{y}) -> {color}")
        else:
            print(f"Skipping ({x},{y}) - out of bounds")
    return img


# ------------------------- Video capture -------------------------

def capture_video(device: int = 0):
    """Capture video from camera and show frames until ESC is pressed."""
    cam = cv.VideoCapture(device)
    if not cam.isOpened():
        print(f"[capture_video] Cannot open camera device {device}")
        return
    print("Press ESC to exit video capture.")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("[capture_video] Failed to read frame")
            break
        cv.imshow('frame', frame)
        key = cv.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break
    cam.release()
    cv.destroyAllWindows()


# ------------------------- Python list demos -------------------------

def list_demo():
    print("\n--- list_demo ---")
    number = [1,2,3,4,5]
    mix_list = [1, "myself", 3.14, True]
    nested_list = [1, 2, [3,4]]

    value = [13,15,34,55,77,99,32,234]
    mix_value = [1233, "yourself", 4.13, True]
    nested_value = [13,14,[23,54]]

    print(value)
    print(mix_value)
    print(nested_value)

    print(value[0])
    print(mix_list[1])

    value[1] = 89
    print(value)

    mix_list.append(784)
    print(mix_list)

    nested_list.insert(2, 5423)
    print(nested_list)

    mix_value.remove(4.13)
    print(mix_value)

    del value[3]
    print(value)

    valu_list = [1,2,3,4,5,5,66,7,47,57]
    sub_list = valu_list[1:9]
    print(sub_list)
    print(valu_list[-3:-1])
    print(valu_list[::2])

    list_val = list(range(1,11))
    print(len(list_val))

    listl = [1,2,3,45,567]
    friut = ['orange','apple','banana','guava']
    for fruits in friut:
        print(fruits)
    for l in listl:
        print(l)


# ------------------------- Functions demo -------------------------

def functions_demo():
    print("\n--- functions_demo ---")

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
        for k, v in kwargs.items():
            print(f"{k}:{v}")

    nmana()
    aB("rohith")
    aB("ronith")
    print(square(4))
    greet()
    greet("hhdhdhh")
    introduce(name="Rohith.N", age=14)
    print(add_numbers(1,2,3,4))
    describe_person(key="ss", value="rr")
    sq = lambda x: x * x
    print(sq(5))


# ------------------------- Loop demos -------------------------

def while_loop_demo():
    print("\n--- while_loop_demo ---")
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


def for_loop_demo():
    print("\n--- for_loop_demo ---")
    for i in range(5):
        print(i)

    fruits = ['orange','apple','banana','guava']
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

    for i in range(5,11,3):
        print(i, end="  ")
    print()


# ------------------------- If/Else and brightness -------------------------

def check_image_load_and_show(path: str):
    img = load_image(path)
    if img is not None:
        print("image loaded successfully")
        show_image('loaded image', img)
    else:
        print("error error error")


def classify_brightness(path: str):
    img = load_image(path)
    if img is None:
        print("error could not load the image")
        return
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    avg_brightness = img.mean()  # mean of all channels
    show_image('gray', gray)
    print(f"Average brightness: {avg_brightness}")
    if avg_brightness < 50:
        print("the image is dark")
    elif 50 <= avg_brightness < 150:
        print("the image is medium")
    else:
        print("the image is bright")


# ------------------------- Small convenience wrappers -------------------------

def image_demo(path: str = 'hazard10.jpg'):
    img = load_image(path)
    print_image_info(img, name=path)
    access_pixel(img, 100, 100)
    modifications = {(100, 100): (212, 255, 249), (135, 134): (255,255,255)}
    modified = modify_pixels(img, modifications)
    show_image('modified', modified)


# ------------------------- CLI / main -------------------------

def parse_args():
    p = argparse.ArgumentParser(description='Merged OpenCV + Python demos')
    p.add_argument('--show-image', nargs='?', const='hazard10.jpg', help='Load and show image')
    p.add_argument('--image-info', nargs='?', const='hazard10.jpg', help='Print image info and pixel access/modify')
    p.add_argument('--capture-video', action='store_true', help='Open webcam and show video')
    p.add_argument('--list-demo', action='store_true', help='Run list demo')
    p.add_argument('--functions-demo', action='store_true', help='Run functions demo')
    p.add_argument('--while-demo', action='store_true', help='Run while loop demo')
    p.add_argument('--for-demo', action='store_true', help='Run for loop demo')
    p.add_argument('--check-load', nargs='?', const='hazard10.jpg', help='Check image load and show')
    p.add_argument('--classify-brightness', nargs='?', const='gradient.png', help='Classify brightness of an image')
    p.add_argument('--all', action='store_true', help='Run all demos (image, lists, functions, loops).')
    return p.parse_args()


def main():
    args = parse_args()

    if args.all:
        image_demo()
        list_demo()
        functions_demo()
        while_loop_demo()
        for_loop_demo()
        return

    if args.show_image:
        img = load_image(args.show_image)
        show_image('image', img)

    if args.image_info:
        image_demo(args.image_info)

    if args.capture_video:
        capture_video(0)

    if args.list_demo:
        list_demo()

    if args.functions_demo:
        functions_demo()

    if args.while_demo:
        while_loop_demo()

    if args.for_demo:
        for_loop_demo()

    if args.check_load:
        check_image_load_and_show(args.check_load)

    if args.classify_brightness:
        classify_brightness(args.classify_brightness)

    # If user provided no args, print help
    if len(sys.argv) == 1:
        print("No arguments provided. Use --help to see usage. Running a small image check (hazard10.jpg) if available.")
        image_demo()


if __name__ == '__main__':
    main()
