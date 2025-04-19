import numpy as np
import cv2 as cv
img=cv.imread('Task2.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

flat = img.flatten()
morse_array = np.where(flat == 255, '.',
                   np.where(flat == 0, '-', 
                   np.where((flat >= 120) & (flat <= 220), ' ', '')))

morse_code = ''.join(morse_array)
print(morse_code)
