import cv2 as cv
img=cv.imread('Task5.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
dic = {"square": 0, "triangle": 0, "circle": 0}
for cnt in contours:
    epsilon = 0.04 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    if len(approx) == 4 and cv.contourArea(cnt) < 50000:
        dic["square"]+=1
    elif len(approx) == 3:
        dic["triangle"]+=1
    else:
        (x, y), radius = cv.minEnclosingCircle(cnt)
        ratio = float(cv.contourArea(cnt)) / (3.14 * radius * radius)
        if 0.7 < ratio < 1.3:
            dic["circle"]+=1
for shape,num in dic.items():
    print(shape,":",num)
