import numpy
import cv2

panda_image=cv2.imread("./images/panda.jpg")
panda_grey_image = cv2.cvtColor(panda_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey panda", panda_grey_image)
cv2.imshow("Color panda", panda_image)
cv2.imwrite("grey_panda", panda_grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



