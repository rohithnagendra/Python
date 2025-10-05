"""
opencv_matplotlib_master.py
A single-file "master" script combining common OpenCV + Matplotlib examples.
Functions:
 - play_video
 - show_image_rgb_plot
 - roi_copy_paste_example
 - show_hsv_conversion_and_plot
 - split_and_show_channels
 - show_image_info_and_conversions
 - draw_shapes_example
 - several matplotlib demo plots (line, bar, sine, scatter)

Usage examples:
    python opencv_matplotlib_master.py --video vtest.avi
    python opencv_matplotlib_master.py --roi hazard10.jpg
    python opencv_matplotlib_master.py --lena
    python opencv_matplotlib_master.py --draw
    python opencv_matplotlib_master.py --plot line
"""

import argparse
import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
import time


# -------------------------
# Utility helpers
# -------------------------
def safe_imread(path):
    """Read an image and raise a helpful error if not found."""
    img = cv.imread(path)
    if img is None:
        raise FileNotFoundError(f"Could not read image file: {path}")
    return img


def safe_videocapture(path):
    """Open a video file or device; raise if fails."""
    cap = cv.VideoCapture(path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Could not open video source: {path}")
    return cap


# -------------------------
# OpenCV examples
# -------------------------
def play_video(video_path: str = "vtest.avi", delay_ms: int = 10):
    """
    Play a video using OpenCV.
    - video_path: path to video file or integer for webcam (e.g., "0")
    - delay_ms: waitKey delay between frames in milliseconds
    """
    # allow numeric webcam id
    if str(video_path).isdigit():
        video_src = int(video_path)
    else:
        video_src = video_path

    cap = safe_videocapture(video_src)
    print(f"Playing: {video_path}  — press ESC to exit")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("End of stream or can't fetch frame.")
            break

        cv.imshow("Video - press ESC to exit", frame)
        key = cv.waitKey(delay_ms) & 0xFF
        if key == 27:  # ESC
            break

    cap.release()
    cv.destroyAllWindows()


def show_image_rgb_plot(img_path: str = "lena.jpg"):
    """
    Show an image using both OpenCV (BGR) and Matplotlib (RGB).
    """
    img = safe_imread(img_path)
    cv.imshow("OpenCV - BGR view", img)
    # Convert to RGB for matplotlib
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.axis("off")
    plt.imshow(img_rgb)
    plt.title(f"Matplotlib RGB view: {os.path.basename(img_path)}")
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()


def roi_copy_paste_example(img_path: str = "hazard10.jpg"):
    """
    Example of extracting/copying/pasting regions of interest (ROI).
    The snippet uses sample coordinates matching the user's original code.
    You can adapt coordinates to different images.
    """
    img = safe_imread(img_path)
    h, w = img.shape[:2]
    print(f"Image size: {w}x{h}")

    # Coordinates used in the original snippet (may need adjustment per image)
    try:
        ball = img[235:295, 465:530].copy()
        img[235:295, 555:620] = ball
        img[235:295, 380:445] = ball

        head = np.array([255, 255, 0], dtype=np.uint8)  # BGR scalar
        # Make a rectangle region and set to 'head' color (clamped inside image)
        img[30:92, 265:325] = head

        cv.imshow("ROI copy & paste result", img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except Exception as e:
        print("ROI operation failed (likely coordinates out of bounds for this image).")
        print("Error:", e)
        cv.destroyAllWindows()


def show_hsv_conversion_and_plot(img_path: str = "lena.jpg"):
    """
    Convert image to HSV, show both BGR/HSV using OpenCV and Matplotlib.
    """
    img = safe_imread(img_path)
    cv.imshow("Original (BGR)", img)

    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    img_hsv_rgb = cv.cvtColor(img_hsv, cv.COLOR_HSV2RGB)

    titles = ["Original (RGB)", "HSV (converted to RGB for display)"]
    images = [img_rgb, img_hsv_rgb]

    plt.figure(figsize=(8, 4))
    for i, im in enumerate(images):
        plt.subplot(1, 2, i + 1)
        plt.imshow(im)
        plt.title(titles[i])
        plt.axis("off")
    plt.tight_layout()
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()


def split_and_show_channels(img_path: str = "lena.jpg"):
    """
    Split image into B, G, R (and HSV channels) and show them with OpenCV.
    """
    img = safe_imread(img_path)
    cv.imshow("Original", img)

    b, g, r = cv.split(img)
    cv.imshow("Blue channel", b)
    cv.imshow("Green channel", g)
    cv.imshow("Red channel", r)

    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(img_hsv)
    cv.imshow("HSV image", img_hsv)
    cv.imshow("Hue channel", h)
    cv.imshow("Saturation channel", s)
    cv.imshow("Value channel", v)

    # Merge back to show correctness
    merged_bgr = cv.merge([b, g, r])
    merged_hsv = cv.merge([h, s, v])
    cv.imshow("Merged BGR", merged_bgr)
    # Convert merged_hsv to BGR for display to avoid seeing HSV interpreted as BGR
    cv.imshow("Merged HSV -> visualized", cv.cvtColor(merged_hsv, cv.COLOR_HSV2BGR))

    cv.waitKey(0)
    cv.destroyAllWindows()


def show_image_info_and_conversions(img_path: str = "opencv-logo.png"):
    """
    Prints shape/size info and shows grayscale, RGB, HSV conversions.
    """
    img = safe_imread(img_path)
    print("Original shape:", img.shape)
    print("Original size (num elements):", img.size)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    print("Gray shape:", gray.shape, "size:", gray.size)
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    cv.imshow("Original (BGR)", img)
    cv.imshow("Gray", gray)
    cv.imshow("RGB (as BGR for window)", cv.cvtColor(rgb, cv.COLOR_RGB2BGR))
    cv.imshow("HSV (visualized)", cv.cvtColor(hsv, cv.COLOR_HSV2BGR))

    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_shapes_example(save_to: str = None):
    """
    Draw shapes (line, rectangle, circle, polygon) on a blank image.
    Optionally save result to a file.
    """
    img = np.zeros((512, 512, 3), np.uint8)

    # Line
    cv.line(img, (69, 23), (511, 511), (255, 20, 30), 9)
    # Rectangle (top-left and bottom-right)
    cv.rectangle(img, (384, 198), (510, 500), (0, 225, 0), 5)
    # Circle
    cv.circle(img, (100, 53), 93, (0, 0, 225), -1)
    # Polygon (pts must be integer coordinates)
    pts = np.array([[190, 150], [240, 250], [79, 220], [300, 169], [60, 200]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], True, (0, 255, 255), 3)

    cv.putText(img, "Shapes Demo", (10, 500), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv.imshow("Drawing shapes", img)

    if save_to:
        cv.imwrite(save_to, img)
        print(f"Saved drawing to {save_to}")

    cv.waitKey(0)
    cv.destroyAllWindows()


# -------------------------
# Matplotlib plotting examples
# -------------------------
def plot_line_example():
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]
    plt.plot(x, y, marker='x', linestyle='--', label='y = x^2')
    plt.title('Simple Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()


def plot_bar_example():
    categories = ['A', 'B', 'C', 'D']
    values = [5, 7, 3, 8]
    plt.bar(categories, values)
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.title("Bar Chart Example")
    plt.show()


def plot_sine_example():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y, linestyle='--', label='Sine Wave')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.title("Sine Wave Example")
    plt.grid()
    plt.show()


def plot_scatter_example():
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.scatter(x, y, alpha=0.6, edgecolors='black')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("Scatter Plot Example")
    plt.show()


# -------------------------
# CLI / main runner
# -------------------------
def build_argparser():
    p = argparse.ArgumentParser(description="OpenCV + Matplotlib Master Script")
    p.add_argument("--video", "-v", nargs='?', const="vtest.avi",
                   help="Play video. Provide file path or webcam id (0,1...). Use just --video to play default 'vtest.avi'")
    p.add_argument("--roi", help="Run ROI copy/paste example with image path (default: hazard10.jpg)", nargs='?', const="hazard10.jpg")
    p.add_argument("--hsv", help="Show HSV conversion & plot for image (default: lena.jpg)", nargs='?', const="lena.jpg")
    p.add_argument("--split", help="Split and show channels for image (default: lena.jpg)", nargs='?', const="lena.jpg")
    p.add_argument("--info", help="Show image info and conversions (default: opencv-logo.png)", nargs='?', const="opencv-logo.png")
    p.add_argument("--draw", help="Draw shapes demo (optionally provide save path)", nargs='?', const=None)
    p.add_argument("--plot", help="Plot examples: line|bar|sine|scatter (example: --plot line)", choices=['line', 'bar', 'sine', 'scatter'])
    p.add_argument("--all", help="Run a series of demos sequentially (will show windows and plots).", action='store_true')
    return p


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = build_argparser()
    args = parser.parse_args(argv)

    try:
        if args.all:
            print("Running all demos in sequence (may open windows and plots)...")
            try:
                draw_shapes_example()
            except Exception as e:
                print("draw_shapes_example failed:", e)

            try:
                show_image_rgb_plot("lena.jpg")
            except Exception as e:
                print("show_image_rgb_plot failed:", e)

            try:
                show_hsv_conversion_and_plot("lena.jpg")
            except Exception as e:
                print("show_hsv_conversion_and_plot failed:", e)

            try:
                split_and_show_channels("lena.jpg")
            except Exception as e:
                print("split_and_show_channels failed:", e)

            try:
                roi_copy_paste_example("hazard10.jpg")
            except Exception as e:
                print("roi_copy_paste_example failed:", e)

            print("All done.")
            return

        if args.video is not None:
            play_video(args.video)

        if args.roi is not None:
            roi_copy_paste_example(args.roi)

        if args.hsv is not None:
            show_hsv_conversion_and_plot(args.hsv)

        if args.split is not None:
            split_and_show_channels(args.split)

        if args.info is not None:
            show_image_info_and_conversions(args.info)

        if args.draw is not None:
            # if the user provided a path string, use it to save; otherwise just display
            save_path = args.draw if args.draw is not None else None
            draw_shapes_example(save_to=save_path)

        if args.plot:
            if args.plot == "line":
                plot_line_example()
            elif args.plot == "bar":
                plot_bar_example()
            elif args.plot == "sine":
                plot_sine_example()
            elif args.plot == "scatter":
                plot_scatter_example()

        # If no arguments given, print help
        if len(argv) == 0:
            parser.print_help()

    except FileNotFoundError as e:
        print("File error:", e)
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
