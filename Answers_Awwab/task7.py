import cv2 as cv
import numpy as np
img = np.zeros((400,800,3),np.uint8)
cv.rectangle(img,(0,0),(img.shape[1],img.shape[0]),(225,221,185),-1)
cv.circle(img, (int(img.shape[1]*5/6),int(img.shape[0]/6)),50,(79,244,255),-1)
cv.rectangle(img,(0,int(img.shape[0]*19/20)),(img.shape[1],img.shape[0]),(0,75,150),-1)
cv.rectangle(img,(int(img.shape[1]*35/100),int(img.shape[0]*3/5)),(int(img.shape[1]*65/100),img.shape[0]),(185,218,255),-1)
cv.rectangle(img,(int(img.shape[1]*48/100),int(img.shape[0]*78/100)),(int(img.shape[1]*52/100),img.shape[0]),(113,62,90),-1)
cv.rectangle(img,(int(img.shape[1]*40/100),int(img.shape[0]*65/100)),(int(img.shape[1]*44/100),int(img.shape[0]*73/100)),(255,255,255),-1)
cv.rectangle(img,(int(img.shape[1]*56/100),int(img.shape[0]*65/100)),(int(img.shape[1]*60/100),int(img.shape[0]*73/100)),(255,255,255),-1)
vertices = np.array([[int(img.shape[1]*35/100),int(img.shape[0]*3/5)], [int(img.shape[1]*65/100),int(img.shape[0]*3/5)], [int(img.shape[1]/2), int(img.shape[0]/4)]], np.int32)
pts=vertices.reshape((-1,1,2))
cv.fillPoly(img, [pts], (113,62,90))
text = "Awwab's House"
font = cv.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
color = (0, 0, 0) 
thickness = 1
position = (int(img.shape[1]*41/100),int(img.shape[0]*48/100))
cv.putText(img, text, position, font, font_scale, color, thickness)
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()