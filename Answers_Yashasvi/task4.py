import cv2 as cv
from google.colab.patches import cv2_imshow
import numpy as np

from google.colab import files
uploaded = files.upload()

# Import image into variable img
img4 = cv.imread("Task4.png")

# Convert to grayscale
gray = cv.cvtColor(img4, cv.COLOR_BGR2GRAY)

# Threshold to binary (black and white)
_, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY_INV)

# Save height and width for traversal
height, width = img4.shape[:2]

# Counters
c, side = 0, 0

# Accessing pixels
for i in range(height):
  c=0
  for j in range(width):
    if thresh[i,j]==255:
      c+=1
      if c > side :
        side = c
    elif thresh[i,j]==0:
      c=0

print(f"Area of largest square : {side*side}")
