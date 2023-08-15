import numpy as np
import cv2 as cv
cap = cv.VideoCapture('/home/precyxyne/Downloads/holdon.mp4')
lower1 = np.array([170, 100, 20])
upper1 = np.array([180, 255, 255])
while cap.isOpened():
 ret, frame = cap.read()
 # if frame is read correctly ret is True
 if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break
 gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 cv.imshow('frame', gray)
 lower_mask = cv.inRange(gray, lower1, upper1)
 frame = cv.bitwise_and(frame, frame, mask=lower_mask)

 if cv.waitKey(25) == ord('q'):
    break
cap.release()
cv.destroyAllWindows()