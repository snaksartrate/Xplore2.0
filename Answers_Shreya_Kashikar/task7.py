import cv2 as cv
import numpy as np

height, width = 135, 216
img=np.zeros((height,width,3), dtype=np.uint8)
img[:] = [235, 206, 135]

house_w, house_h = width // 3, height // 2
house_x = (width - house_w) // 2
house_y = height - house_h - 4

cv.rectangle(img, (0, height - 4), (width, height), (42, 42, 165), -1)
cv.rectangle(img,(house_x, house_y), (house_x + house_w, house_y + house_h),(125, 180, 255),-1)
cv.rectangle(img,(house_x+27, house_y+35), (house_x + house_w - 27, house_y + house_h),(128, 128, 200),-1)
cv.rectangle(img,(house_x+10, house_y+10), (house_x + 24, house_y + 23),(150, 255, 255),-1)
cv.rectangle(img,(house_x+house_w-24, house_y+10), (house_x + house_w-10, house_y + 23),(150, 255, 255),-1)
cv.circle(img,(width - 30, 30), width // 15,(0, 255, 255),-1)

points = np.array([(house_x, house_y),(house_x+house_w, house_y),(house_x+(house_w//2), house_y-50)])
points = points.reshape((-1, 1, 2))
cv.fillPoly(img,[points],(250, 100, 200))
cv.putText(img,"My House",(house_x + 14, house_y - 5),cv.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))

cv.imshow("Output", img)
cv.waitKey(0)
cv.destroyAllWindows()