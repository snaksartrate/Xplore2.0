import cv2 

image = cv2.imread("D:\OPEN CV\OPEN CV Workshop\OPENCV TASKS\Answers_Avanish\OPENCV\Answers_Avanish\Task2.png",cv2.IMREAD_GRAYSCALE)

row = image[0]

for pixel in row:
    if pixel == 255:
        print(".",end="")
    
    
    elif pixel == 0:
        print("_",end= "")

    elif 120 <= pixel <= 220 :
        print(" ", end = "")
    