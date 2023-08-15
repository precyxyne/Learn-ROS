import numpy as np
import cv2 as cv
import imutils
cap = cv.VideoCapture('/home/precyxyne/Downloads/holdon.mp4')
lower = np.array([40,0,200])
upper = np.array([120,180,255])
center =None
while cap.isOpened():
 ret, frame = cap.read()
 if not ret:
    print("Can't receive frame")
    break
 result= frame.copy()
 gra = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 blurred = cv.GaussianBlur(gra, (3, 3), 0)

 edged = cv.Canny(blurred, 10, 100)

 cv.imshow("Edged image", edged)
 res = cv.bitwise_and(frame, frame, mask=edged)
 lower_mask = cv.inRange(gra, lower, upper)
 red= cv.bitwise_and(res, res, mask=lower_mask)
 cv.imshow("Edged imae", red)
 
 cnts,hier = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
 if len(cnts) > 0:
   c0 = sorted(cnts, key=cv.contourArea)
   c=c0[1]
   M = cv.moments(c)
   if(M["m00"]!=0):
      center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
   print(center)
		
 lower_mask = cv.inRange(gra, lower, upper)
 res = cv.bitwise_and(frame, frame, mask=lower_mask)
 cv.imshow('mask', res)
 if cv.waitKey(25) == ord('q'):
  break
cap.release()
cv.destroyAllWindows()