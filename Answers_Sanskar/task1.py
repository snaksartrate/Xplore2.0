import cv2 as cv
import numpy as np

image = cv.imread('Task1.png')

# print(image.shape)

count = 0
locations = []

if len(image.shape) == 2:
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] != 255:
                count += 1
                locations.append([i,j])
else:
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # checking for each pixel now:
            countThisPixel = False
            for k in range(image.shape[2]):
                if image[i,j,k] != 255:
                    countThisPixel = True
            if countThisPixel:
                count += 1
                locations.append([i,j])

print(count, "non-white pixels were found")
if count > 0:
    print("their locations are:", locations)