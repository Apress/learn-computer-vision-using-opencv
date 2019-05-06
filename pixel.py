import numpy 
import cv2

#read the flower image and load it into a variable flower_image
flower_image=cv2.imread("./images/flower_pink.jpg")

#access a specific pixel using the coordinate based access from the matrix
pixel=flower_image[200,250]

#see what color space this pixel represents - this is an RBG representation
print(pixel)

#lets change the pixel color value to blue
flower_image[200,250]=(255,0,0)

#lets change the pixel color value to blue in a region range as against 
flower_image[200:250,200:350]=(0,255,0)
