import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create FAST Detector object
fast = cv2.FastFeatureDetector()

# Obtain Key points, by default non max suppression is On
# to turn off set fast.setBool('nonmaxSuppression', False)
keypoints = fast.detect(gray, None)
print "Number of keypoints Detected: ", len(keypoints)

# Draw rich keypoints on input image
image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Feature Method - FAST', image)
cv2.waitKey()
cv2.destroyAllWindows()