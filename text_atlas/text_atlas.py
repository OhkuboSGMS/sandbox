from PIL import ImageDraw, ImageFont, Image
import string

# https://github.com/python-pillow/Pillow/issues/3921#issuecomment-508567914
abc = 'あいうえお'

img = Image.new('RGB', (600, 600))
draw = ImageDraw.Draw(img)

text_size = 32
font = ImageFont.truetype('NotoSansJP-Regular.otf', text_size)
# bbox = draw.multiline_textbbox((0, 0), abc, font=font)
# print(bbox)

# (x,y,w,h) = (0,0,100,100)
text_color = (255, 255, 255)
draw.text((0, 0), abc, text_color, font=font)

x, y = 0, 0
for i, c in enumerate(abc):
    w, h = font.getsize(c)
    # w, h = font.getmask(c)
    print(f"c:{c},x:{x},y:{y} w:{w} h:{h}")
    draw.rectangle((x, y, x+w, y+h), None, '#f00')
    img.save(f'text-{i}.png')
    x += w

    # draw.rectangle((left, top, right, bottom), None, '#f00')
# bbox = draw.multiline_textbbox((0, 0), abc, font=font)
# print(bbox)

img.save('text.png')
