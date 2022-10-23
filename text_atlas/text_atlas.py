from typing import Dict

from PIL import ImageDraw, ImageFont, Image
import string
import cv2
import numpy as np
from ja_unicode import cjk
from more_itertools import sliced

# https://github.com/python-pillow/Pillow/issues/3921#issuecomment-508567914
abc = ''.join(list(cjk())[0:100])
print(abc)
text_size = 32  # one character width
n_row_char = 600 // 32
print(f'一行の文字数:{n_row_char}')
img = Image.new('RGB', (600, 600))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype('NotoSansJP-Black.otf', text_size)
# bbox = draw.multiline_textbbox((0, 0), abc, font=font)
# print(bbox)
area_map: Dict[str, np.ndarray] = {}
text_color = (255, 255, 255)
ml_text = '\n'.join(sliced(abc, n_row_char))
draw.multiline_text((0, 0), ml_text, font=font)
# draw.text((0, 0), abc, text_color, font=font)
np_img = np.array(img)
x, y = 0, 0
for i, c in enumerate(abc):
    w, h = font.getsize(c)
    # w, h = font.getmask(c)
    code: str = ord(c)
    print(type(c.encode('unicode-escape')))
    print(np.array(c.encode('unicode-escape')))
    print(f"c:{c},x:{x},y:{y} w:{w} h:{h} unicode:{code}")
    r = (x, y, x + w, y + h)
    area_map[code] = np.array(r)
    # print(np_img[r[1]:r[3],r[0]:r[2]].shape)
    # cv2.imshow('Test', np_img[r[1]:r[3], r[0]:r[2]])
    # cv2.waitKey(-1)
    draw.rectangle((x, y, x + w, y + h), None, '#f00')
    x += w
print(area_map)
area_code = np.array(list(map(int, area_map.keys())))
area_list = np.array(list(area_map.values()))
print(area_code)
print(area_list.shape)
# bbox = draw.multiline_textbbox((0, 0), abc, font=font)
# print(bbox)

img.save('text.png')
