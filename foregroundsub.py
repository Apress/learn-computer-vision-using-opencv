import cv2
import numpy as np

# Initalize webacam and store first frame
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Create a flaot numpy array with frame values
average = np.float32(frame)

while True:
    # Get webcam frmae
    ret, frame = cap.read()
    
    # 0.01 is the weight of image, play around to see how it changes
    cv2.accumulateWeighted(frame, average, 0.01)
    
    # Scales, calculates absolute values, and converts the result to 8-bit
    background = cv2.convertScaleAbs(average)

    cv2.imshow('Input', frame)
    cv2.imshow('Disapearing Background', background)
    
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cv2.destroyAllWindows()
cap.release()