import cv2 as cv
from google.colab.patches import cv2_imshow

from google.colab import files
uploaded = files.upload()

# Import image into variable img
img1 = cv.imread("Task1.png")
# Save height and width for traversal
height, width = img1.shape[:2]
# Counter to count total number of non white pixels
c=0
# Accessing pixels
for i in range(height):
  for j in range(width):
    b,g,r=img1[i,j]
    if b!=255 or g!=255 or r!=255:
      print(f"({j}, {i})")
      c+=1

print(f"\nTotal number of non white pixels: {c}")