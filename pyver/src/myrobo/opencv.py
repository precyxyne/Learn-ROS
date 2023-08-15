import cv2 as cv
import numpy as np
image = cv.imread("/home/precyxyne/Downloads/ems.jpg")
cv.imshow("test",image)
result= image.copy()
image = cv.cvtColor(image, cv.COLOR_BGR2HSV) 
cv.imshow("test",result)
cv.waitKey(10)
lower1 = np.array([170, 100, 20])
upper1 = np.array([180, 255, 255])
lower_mask = cv.inRange(image, lower1, upper1)
result = cv.bitwise_and(result, result, mask=lower_mask)
print(result)
cv.imshow('mask', lower_mask)
cv.imshow('result', result)
cv.waitKey(0)