import cv2 as cv
import numpy as np

img = cv.imread('Task6.png')

# creating mask using thresholding over `red` channel (use better use histogram to get thresholding value)
ret, mask = cv.threshold(img[:, :,2], 254, 255, cv.THRESH_BINARY)

mask3 = np.zeros_like(img)
mask3[:, :, 0] = mask
mask3[:, :, 1] = mask
mask3[:, :, 2] = mask

# extracting `red` region using `bitewise_and`
red = cv.bitwise_and(img, mask3)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img  = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

# extracting non-red region
gray = cv.bitwise_and(img, 255 - mask3)

# red masked output
out = gray + red
cv.imshow('mask', mask3)
cv.imshow('red', red)
cv.imshow('gray', gray)
cv.imshow("final_output.png", out)
cv.waitKey(0)
cv.destroyAllWindows()