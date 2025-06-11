import cv2 as cv
from google.colab.patches import cv2_imshow
import numpy as np

from google.colab import files
uploaded = files.upload()

# Import image into variable img
img6 = cv.imread("Task6.png")
# Save height and width for traversal
height, width = img6.shape[:2]

# Accessing pixels
for i in range(height):
  for j in range(width):
    b, g, r = img6[i][j]
    if not (img6[i][j] == [ 0, 0, 255]).all():
      g = int(0.114 * b + 0.587 * g + 0.299 * r)
      img6[i][j] = [g, g, g]

# Display Image
cv2_imshow(img6)
cv.waitKey(0)
cv.destroyAllWindows()