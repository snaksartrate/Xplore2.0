import cv2
import numpy as np


img = cv2.imread("D:\OPEN CV\OPEN CV Workshop\OPENCV TASKS\Answers_Avanish\OPENCV\Answers_Avanish\Task5.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

shape_counts = {
    "triangle": 0,
    "square": 0,
    "circle": 0
}

for contour in contours:
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    vertices = len(approx)

    x, y, w, h = cv2.boundingRect(approx)

    shape_type = "unknown"

    if vertices == 3:
        shape_type = "triangle"
        shape_counts["triangle"] += 1
    elif vertices == 4:
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape_type = "square"
            shape_counts["square"] += 1
    elif vertices > 5:
        shape_type = "circle"
        shape_counts["circle"] += 1

    cv2.drawContours(img, [approx], 0, (0, 255, 0), 15)
    cv2.putText(img, shape_type, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

print("Total shapes:", len(contours))
print("Shape Counts:", shape_counts)

cv2.imshow("Detected Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
