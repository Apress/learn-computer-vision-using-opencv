import cv2
import numpy as np
 
mountains_video = cv2.VideoCapture("mountains.mp4")
 
fcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("new_mountains.avi", fcc, 28, (640, 360))
 
while True:
    ret, f = mountains_video.read()
    f2 = cv2.flip(f, 1)
    
    cv2.imshow("frame2", f2)
    cv2.imshow("frame", f)
    
    out.write(f2)
    
    key = cv2.waitKey(20)
    if key == 27:
        break
 
out.release()
mountains_video.release()
cv2.destroyAllWindows()