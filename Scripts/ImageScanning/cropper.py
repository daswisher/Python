import cv2
import numpy as np

img = cv2.imread('ImageCroppingTest.jpg', 0)

re, thresh = cv2.threshhold(img, 127, 255, 0)
countours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

M = cv2.moments(cn2)
print M
