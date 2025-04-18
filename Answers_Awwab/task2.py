import cv2 as cv
def apply_grayscale(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return gray
img = cv.imread("Task2.png")
img = apply_grayscale(img)
s=""
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j] == 0:
            s+='-'
        elif img[i,j]==255:
            s+='.'
        else:
            s+=' '
print(s)