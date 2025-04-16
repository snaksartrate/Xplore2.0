import cv2
import numpy as np

#as far as i remember we used something something like this for the cloth task and the pen detection task using webcam on the 2nd and 3rd day respectively

# why is it like that when we put \ sometimes in the path it works while sometimes when we put / in the path it works sometimes?
image = cv2.imread("D:/OPEN CV/OPEN CV Workshop/OPENCV TASKS/Answers_Avanish/OPENCV/Answers_Avanish/ball.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#here, i used 2 types of ranges since single mai it was not detecting
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])
mask_red = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)


lower_white = np.array([0, 0, 180])
upper_white = np.array([180, 80, 255])
mask_white = cv2.inRange(hsv, lower_white, upper_white)
mask_white = cv2.dilate(mask_white, None, iterations=2)  


lower_blue = np.array([100, 150, 100])
upper_blue = np.array([130, 255, 255])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

#had to take tha above values from google cause i didnt knew them
#khudse values leke try kiye but phir woh span nai horah tha acchese


masks = [mask_red, mask_white, mask_blue]


for mask in masks:
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Insane 3 BALLS! ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
 