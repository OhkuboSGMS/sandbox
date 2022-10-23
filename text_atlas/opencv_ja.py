# opencv-freetype2を使うと日本語が描画できるかも？
# https://fireant.github.io/misc/2017/01/28/ttf-opencv.html
import cv2
import numpy as np

img = np.zeros((100, 300, 3), dtype=np.uint8)

ft = cv2.freetype.createFreeType2()
ft.loadFontData(fontFileName='Ubuntu-R.ttf',
                id=0)
ft.putText(img=img,
           text='いろはにほへとちりぬるを',
           org=(15, 70),
           fontHeight=60,
           color=(255,  255, 255),
           thickness=-1,
           line_type=cv2.LINE_AA,
           bottomLeftOrigin=True)

cv2.imwrite('image.png', img)