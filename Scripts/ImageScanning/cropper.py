import argparse
import imutils


import cv2
import numpy as np



'''
#img = cv2.imread('ImageCroppingTest.jpg', 0)
img = cv2.imread('ImageCroppingTest.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#re, thresh = cv2.threshold(gray, 127, 255, 0)
re, thresh = cv2.threshold(gray, 127, 255, 0)
_, countours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = countours[0]

M = cv2.moments(cnt)
#print M


rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
box = box.tolist()
print type(box[0])
print box[0]
print rect[0]
#cv2.drawContours(img, [box], 0, (0,0,255), 2)
cv2.rectangle(img, (box[0][0],box[0][1]), (100,100), (0,255,0), 2)
#x,y,w,h = cv2.boundingRect(cnt)
#cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 200)

cv2.namedWindow('image', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
cv2.imshow('image', img)
cv2.waitKey(0)
'''


def detect(c):
	# initialize the shape name and approximate the contour
	shape = "unidentified"
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.04 * peri, True)

	# if the shape is a triangle, it will have 3 vertices
	if len(approx) == 3:
		shape = "triangle"

	# if the shape has 4 vertices, it is either a square or
	# a rectangle
	elif len(approx) == 4:
		# compute the bounding box of the contour and use the
		# bounding box to compute the aspect ratio
		(x, y, w, h) = cv2.boundingRect(approx)
		ar = w / float(h)

		# a square will have an aspect ratio that is approximately
		# equal to one, otherwise, the shape is a rectangle
		shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

	# if the shape is a pentagon, it will have 5 vertices
	elif len(approx) == 5:
		shape = "pentagon"

	# otherwise, we assume the shape is a circle
	else:
		shape = "circle"

	# return the name of the shape
	return shape





ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to the input image")
args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread(args["image"])
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]


cv2.namedWindow('Image', flags=cv2.WINDOW_NORMAL)

cv2.resizeWindow('Image', 600,600)
# loop over the contours
for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	shape = detect(c)

	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)

	
	# show the output image

	cv2.imshow("Image", image)
	cv2.waitKey(0)