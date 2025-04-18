import cv2 as cv
img = cv.imread('Task5.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY_INV)[1]
contours, _ = cv.findContours(thresh.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
map = {
    "circle": 0,
    "square": 0,
    "rectangle": 0,
    "triangle":0
}
for cnt in contours:
    perimeter = cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, 0.04 * perimeter, True)
    if len(approx) == 3:
            map["triangle"]+=1
    elif len(approx) == 4:
            x, y, w, h = cv.boundingRect(approx)
            aspect_ratio = float(w) / h
            if 0.95 <= aspect_ratio <= 1.05:
                map["square"]+=1 
            else:
                map["rectangle"]+=1
    else:
            map["circle"]+=1
print(f"Number of shapes found: {len(contours)}")
for key,value in map.items():
      print(f"Shape: {key}\nCount: {value}")