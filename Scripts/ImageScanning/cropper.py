import cv2
import numpy as np

#img = cv2.imread('ImageCroppingTest.jpg', 0)
img = cv2.imread('ImageCroppingTest.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

re, thresh = cv2.threshold(gray, 127, 255, 0)
_, countours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = countours[0]

M = cv2.moments(cnt)
#print M


rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0,0,255), 2)


cv2.imshow('dst_rt', img)
cv2.waitKey(0)