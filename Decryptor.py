# coding=utf-8

from PIL.Image import *
from math import *
from random import *

image = open("result.bmp")
width, height = image.size
result = ""

threshold = image.getpixel((0, 0))[1]
for x in range(1, width):
    flag, one, two = image.getpixel((x, 0))

    if (one | two) == 0:
        break

    if flag < threshold:
        unicode = (one << 8) + two
    else:
        unicode = (two << 8) + one

    result += chr(unicode)
for y in range(1, height):
    for x in range(width):
        flag, one, two = image.getpixel((x, y))

        if (one | two) == 0:
            break

        if flag < threshold:
            unicode = (one << 8) + two
        else:
            unicode = (two << 8) + one

        result += chr(unicode)

print(result)
