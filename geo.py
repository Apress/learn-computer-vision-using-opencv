import numpy 
import cv2

#read the flower image and load it into a variable flower_image
flower_image=cv2.imread("./images/flower_pink.jpg")

cv2.line(flower_image,(25,21),(100,100),(255,0,0),5)
cv2.rectangle(flower_image,(25,21),(200,200),(0,255,0),2)
cv2.circle(flower_image,(50,50),50,(0,0,255),-1)

cv2.imshow("Geometry",flower_image)
cv2.waitKey(0)