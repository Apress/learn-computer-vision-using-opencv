import cv2
import numpy as np

iamge = cv2.imread('.images/input1.jpg')
num_rows, num_cols = iamge.shape[:2]

translation_matrix = np.float32([ [1,0,70], [0,1,110] ])
image_translation = cv2.warpAffine(iamge, translation_matrix, (num_cols, num_rows))
cv2.imshow('Translation', image_translation)
cv2.waitKey()