import cv2 as cv
from google.colab.patches import cv2_imshow

from google.colab import files
uploaded = files.upload()

# Import image into variable img
img2 = cv.imread("Task2.png" , cv.IMREAD_GRAYSCALE)
# Save height and width for traversal
height, width = img2.shape[:2]
# To save morse string
morse = ""
# Accessing pixels
for i in range(height):
  for j in range(width):
    if img2[i,j]==255:
      morse+="."
    elif img2[i,j]==0:
      morse+="-"
    elif 120 < img2[i,j] < 220 :
      morse+=" "

print(f"Morse Code : {morse}")