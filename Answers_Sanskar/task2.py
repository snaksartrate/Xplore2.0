import cv2 as cv
import numpy as np

image = cv.imread('Task2.png')

image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

s = ""

# print(image.shape)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i,j] == 255:
            s += '.'
        elif image[i,j] == 0:
            s += '_'
        elif 120 <= image[i,j] and image[i,j] <= 220:
            s += ' '

print(s) # XFACTOR