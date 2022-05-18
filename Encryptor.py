# coding=utf-8

import PIL.Image as img
from math import *
from random import *

with open("textSource.txt", encoding="utf8") as textFile:
    text = textFile.read()
length = ceil(sqrt(len(text) + 1))

image = img.new("RGB", (length, length), 0x0)
x = 1
y = 0

threshold = randint(120, 140)
image.putpixel((0, 0), (randint(0, threshold), threshold, randint(threshold, 255)))
for char in text:
    unicode = ord(char)
    if randint(0, 1) == 0:
        color = (randint(0, (threshold - 1 if randint(1, 3) == 2 else 100)),
                 (unicode & 0xFF00) >> 8, unicode & 0xFF)
    else:
        color = (randint(threshold, (255 if randint(1, 3) == 2 else 228)),
                 (unicode & 0xFF), (unicode & 0xFF00) >> 8)

    image.putpixel((x, y), color)

    if x == length - 1:
        x = 0
        y += 1
    else:
        x += 1

image.save("result.bmp")
