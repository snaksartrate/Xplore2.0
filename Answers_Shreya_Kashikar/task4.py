import numpy as np
import cv2 as cv
img=cv.imread('Task4.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

ret,binary= cv.threshold(img,127,255,cv.THRESH_BINARY)
max=0
for i in range(binary.shape[0]):
    side=0
    for j in range(binary.shape[1]):
        if binary[i][j]==0:
            side+=1
        else:
            if side>max:
                max=side

print(max**2)
            
