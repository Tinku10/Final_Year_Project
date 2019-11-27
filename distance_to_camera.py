from imutils import paths
import numpy as np
import imutils
import cv2
#import ultrasonic library

#distance = ultrasonic()

def find_marker(image):
    	# convert the image to grayscale, blur it, and detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 30, 125)
	cv2.imshow('img', edged)
	#edged = imutils.auto_canny(gray) # Bad edge detection
	cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
	cv2.imshow('win', edged)
	
	
	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	c = max(cnts, key=cv2.contourArea)
 
	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)



#def distance_to_camera(knownWidth, focalLength, perWidth):
#	# compute and return the distance from the maker to the camera
#
#	return (knownWidth * focalLength) / perWidth


def xdimension(distance_to_camera, focalLength, perWidth):
    	return distance_to_camera()*perWidth/focalLength


#Find distance from camera to object using Python and OpenCVPython
# initialize the known distance from the camera to the object, which
# in cms
KNOWN_DISTANCE = # ultrasonic distance

# initialize the known object width, which in this case, the piece of
# paper in cms
KNOWN_WIDTH = xdimension()

path = 'd:\Personal Files\Project_Final\images\\img1.jpg'
image = cv2.imread(path)
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)


cv2.imshow('img', image)
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH


#loop over the images
for imagePath in sorted(paths.list_images("d:\Personal Files\Project_Final\\images")):
	# load the image, find the marker in the image, then compute the
	# distance to the marker from the camera
	image = cv2.imread(imagePath)
	marker = find_marker(image)
	cms = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
 
	# draw a bounding box around the image and display it
	box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
	box = np.int0(box)
	cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
	cv2.putText(image, "%.2fcm" % (cms),
		(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
		1.0, (0, 255, 0), 3)
	cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
	
	cv2.imshow("image", image)
	cv2.waitKey(0)
