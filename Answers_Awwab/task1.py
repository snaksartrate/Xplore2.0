import cv2 as cv
img = cv.imread("Task1 copy.png")
answer =[]
count =0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r,g,b = img[i,j]
        if r!=255 or g!= 255 or b !=255:
            count=count+1
            answer.append([i,j])

print(f"Count of non white pixels is:{count} ")
print("Positions of pixels are: ")
for y,x in answer:
    print(f"{x} {y}")
