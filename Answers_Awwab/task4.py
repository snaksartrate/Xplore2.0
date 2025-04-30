import cv2 as cv
img = cv.imread("Task4.png")
res =0
cnt =0
r2=1
g2=-1
b2=-1
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r,g,b = img[i,j]
        if(r!=255 or g!=255 or b !=255):
            if(r2!=r or b2 != b or g2!=g):
                res = max(res,cnt)
                cnt=1
                r2=r
                g2=g
                b2=b
            else:
                cnt=cnt+1
        else:
            r2=1
            g2=-1
            b2=-1
            res = max(res,cnt)
            cnt=0
print(f"Side length: {res}")
print(f"Area: {res**2}")
