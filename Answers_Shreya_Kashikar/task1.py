import numpy as np
import cv2 as cv
img=cv.imread('Task1.png')
if img is None:
    print("Error: Image not found or unable to load.")
    exit()
non_white=np.where(np.any(img!=[255,255,255],axis=-1))
count=len(non_white[0])
print("The total no. of non-white pixels are",count)
print("There co-ordinates are:")
y_index,x_index=non_white
for i in range(count):
    print(f"({y_index[i]},{x_index[i]})")
