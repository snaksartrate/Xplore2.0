import cv2 as cv
import numpy as np

img = cv.imread('Task6.png')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower1 = np.array([0, 120, 70])  
upper1 = np.array([10, 255, 255]) 
lower2 = np.array([170, 120, 70]) 
upper2 = np.array([180, 255, 255])  

mask1 = cv.inRange(hsv, lower1, upper1)
mask2 = cv.inRange(hsv, lower2, upper2)
red_mask = mask1 + mask2 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray2bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

result = img.copy() 
result[red_mask == 0] = gray2bgr[red_mask == 0] 

cv.imshow("Output", result)
cv.waitKey(0)
cv.destroyAllWindows()
