import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create FAST detector object
fast = cv2.FastFeatureDetector()

# Create BRIEF extractor object
brief = cv2.DescriptorExtractor_create("BRIEF")

# Determine key points
keypoints = fast.detect(gray, None)

# Obtain descriptors and new final keypoints using BRIEF
keypoints, descriptors = brief.compute(gray, keypoints)
print "Number of keypoints Detected: ", len(keypoints)

# Draw rich keypoints on input image
image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                                    
cv2.imshow('Feature Method - BRIEF', image)
cv2.waitKey()
cv2.destroyAllWindows()