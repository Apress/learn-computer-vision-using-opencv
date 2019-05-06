import numpy as np
import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# take first frame of the video
ret, frame = cap.read()

# setup default location of window
r, h, c, w = 240, 100, 400, 160 
track_window = (c, r, w, h)

# Crop region of interest for tracking
roi = frame[r:r+h, c:c+w]

# Convert cropped window to HSV color space
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Create a mask between the HSV bounds
lower_purple = np.array([130,60,60])
upper_purple = np.array([175,255,255])
mask = cv2.inRange(hsv_roi, lower_purple, upper_purple)

# Obtain the color histogram of the ROI
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])

# Normalize values to lie between the range 0, 255
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria
# We stop calculating the centroid shift after ten iterations 
# or if the centroid has moved at least 1 pixel
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while True:
    
    # Read webcam frame
    ret, frame = cap.read()

    if ret == True:
        # Convert to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Calculate the histogram back projection 
        # Each pixel's value is it's probability
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply Camshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        # Draw it on image 
        # We use polylines to represent Adaptive box 
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame,[pts],True, 255,2)
        
        cv2.imshow('Camshift Tracking', img2)
        
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break

    else:
        break

cv2.destroyAllWindows()
cap.release()