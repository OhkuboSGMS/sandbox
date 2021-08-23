import warnings
from typing import Optional, Tuple

import cv2
import numpy as np

"""
width,height両方指定されたら : まずサイズのキャンバスを作成し、その中にfitするように画像をリサイズする
width,height一方のみ指定されたら : 一方のサイズに合わせてリサイズ
scale:が与えられたら :スケールでリサイズ
"""


def resize_with_aspect(image: np.ndarray, width: Optional[int] = None, height: Optional[int] = None, scale=None,
                       bg_color=(255, 255, 255), inter=cv2.INTER_NEAREST) -> np.ndarray:
    """
    https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
    width , heightいずれかのサイズを指定して、そのサイズを固定して、他方のサイズをアスペクト維持される形のリサイズ値を求める
    :param image: resize image
    :type image: np.ndarray
    :param width: resize width
    :type width: int
    :param height: resize height
    :type height: int
    :param scale:
    :type scale: float
    :param bg_color: RGB Color(0~255)
    :type bg_color: Tuple[int,int,int]
    :param inter: Interpolation
    :type inter:
    :return: resized or not fix image
    :rtype: np.ndarray
    """
    (h, w) = image.shape[:2]
    # if both the width and height are None, then return the
    # original image
    if width is None and height is None and scale is None:
        return image
    if width is not None and height is not None and scale is not None:
        warnings.warn("リサイズはwidth,heightが優先されます、scale指定したい場合はwidth,heightはNoneにしてください")

    # 画像サイズを事前に決定し、サイズに収まるように指定した画像をリサイズする
    if width and height:
        canvas = np.full((height, width, len(bg_color)), list(reversed(bg_color)), dtype=np.uint8)
        # print("canvas", width, height)
        # print("original", w, h)
        # キャンバスとの比が小さい方に合わせる
        c_w, c_h = width, height
        i_w, i_h = w, h
        a_w, a_h = c_w / i_w, c_h / i_h
        # print("scale", a_w, a_h)
        if a_w < a_h:
            r_i_x, r_i_y = int(i_w * a_w), int(i_h * a_w)  # resize image size
        else:
            r_i_x, r_i_y = int(i_w * a_h), int(i_h * a_h)  # resize image size
        pad_x, pad_y = (c_w - r_i_x) // 2, (c_h - r_i_y) // 2
        # print("resize", r_i_x, r_i_y)
        # print("pad", pad_x, pad_y)
        resized_img = cv2.resize(image, (r_i_x, r_i_y), interpolation=inter)
        canvas[pad_y:pad_y + r_i_y, pad_x:pad_x + r_i_x, :] = resized_img
        return canvas

        pass
    # check to see if the width is None
    elif width is None and height is not None:
        r = height / float(h)
        dim = (int(w * r), height)
        resized = cv2.resize(image, dim, interpolation=inter)
        return resized

    # otherwise, the height is None
    elif width is not None and height is None:
        r = width / float(w)
        dim = (width, int(h * r))
        resized = cv2.resize(image, dim, interpolation=inter)
        return resized
    elif scale is not None:
        return cv2.resize(image, dsize=None, fx=scale, fy=scale, interpolation=inter)

    else:
        return image
