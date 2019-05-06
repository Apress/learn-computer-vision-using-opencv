import numpy 
import cv2

#read the flower image and load it into a variable image
image=cv2.imread("./images/input1.jpg")

#kernel value of 3 3x3 matrix neighbourhood is used
noisereduced_version = cv2.medianBlur(image,3)

cv2.imshow("Original",image)
cv2.imshow("Corrected",noisereduced_version)

cv2.waitKey(0)