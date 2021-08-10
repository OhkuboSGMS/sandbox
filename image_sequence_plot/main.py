import argparse
from fnmatch import fnmatch
from typing import Iterable
from pathlib import Path
import cv2
import numpy as np

ext = ["*.jpg", "*.png", "*.webp"]


def file_ext_match(file: str, extensions: Iterable[str]):
    return any(map(lambda e: fnmatch(file, e) is not None, extensions))


def generate(im_dir: str, size=(512, 512), bg_color=255):
    canvas = np.full((size[1], size[0], 3), bg_color, np.uint8)
    img_files = [str(f) for f in Path(im_dir).iterdir() if file_ext_match(f, ext)]
    print(img_files)
    imgs = [cv2.imread(f) for f in img_files]
    anchor = size[0] // 4, size[1] // 4  # width,height
    unit = 20
    print(anchor)
    for idx, img in enumerate(imgs):
        img =cv2.resize(img, dsize=None, fx=0.1, fy=0.1)
        left, right = anchor[1] + idx * unit, anchor[1]+ idx * unit + img.shape[1]
        top, bottom = anchor[0] + idx * unit, anchor[0]+ idx * unit + img.shape[0]
        print(left, right, top, bottom)
        canvas[top:bottom, left:right, :] = img

    cv2.imshow("Test", canvas)
    cv2.waitKey(-1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=str)
    parser.add_argument("output_path", type=str)
    args = parser.parse_args()
    generate(args.input_dir)
