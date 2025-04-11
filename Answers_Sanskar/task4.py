import cv2 as cv
import numpy as np

image = cv.imread('Task4.png')
h, w = image.shape[0], image.shape[1]

pixelcount = 0
maxlength = 0

white = np.array([255,255,255], dtype = np.uint8)

for i in range(h):
    for j in range(w):
        if image[i,j].all() != white.all():
            pixelcount += 1
        if image[i,j].all() != image[i,j-1].all():
            countCompleted = True
            if image[i,j].all() == white.all():
                maxlength = max(pixelcount, maxlength)
                pixelcount = 0
            else:
                maxlength = max(pixelcount - 1, maxlength)
                pixelcount = 1

print("largest area =", maxlength ** 2)