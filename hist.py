import numpy as np
import cv2

from matplotlib import pyplot as plt

image=cv2.imread("./images/panda.jpg")
#plot a histogram
histogram_image= cv2.calcHist([image], [0], none, [256], [0,256])
#flatten the histogram
plt.hist(imagel.ravel(), 256, [0,256]; plt.show();



panda_grey_image = cv2.cvtColor(panda_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey panda", panda_grey_image)
cv2.imshow("Color panda", panda_image)
cv2.imwrite("grey_panda", panda_grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

