import cv2 
import numpy as np 

image = cv2.imread('D:\OPEN CV\OPEN CV Workshop\OPENCV TASKS\Answers_Avanish\OPENCV\Answers_Avanish\Task4.png',cv2.IMREAD_GRAYSCALE)

_,thresh = cv2.threshold(image,254,255,cv2.THRESH_BINARY)

maximum_side = 0

for row in thresh:
    count = 0
    for pixel in row:
        if pixel == 0:
            count = count + 1
            maximum_side = count
        else:
            count = 0
            
print(maximum_side*maximum_side)
            
    