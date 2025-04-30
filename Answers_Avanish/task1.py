# You have have been given an image with a white canvas containing few non white pixels. The task is to use OpenCV to find the number of non white pixels and also return the positions of the pixels you have found.

import cv2
import numpy as np

#ahhhh this step tooo ahhhhhh,, read the image and already convert in and read it in gray form cause we dont want 3 diff channels ka scene n all that
img = cv2.imread("D:\OPEN CV\OPEN CV Workshop\OPENCV TASKS\Answers_Avanish\OPENCV\Answers_Avanish\Task1.png", cv2.IMREAD_GRAYSCALE)
#in the above one i had to put the path directly cause just the name of the image file gave error.


#now time to apply invert threshold cause for the contour ditection path, it does not do well with the white background and black dots so reversed it!
_, thresh = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY_INV)

#to find the contours, RETR_EXTERNAL cause in this case we need to find just the outer contour and its not a looped contours the black dots.
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Simple for loop to write the position of each contour using the centroid method.

for i, contour in enumerate(contours):
    x, y = contour[0][0]
    print(f"Dot {i+1} at: ({x}, {y})")



# len(contours function to print the total number of contours
print("Total black dots:", len(contours))
