# face detection을 이용하기 위해서 코드를 합쳤으나, 오류.

# 참조 : http://bartoebotics.com/2016/01
# 		https://github.com/BartoeBotics/Projects/tree/master/Christmas_Fun

# Requirements - Raspberry Pi, Raspberry Pi Camera, Python, and OpenCV

# This runs the program
# python beards_on_face_detection.py --face cascades/haarcascade_frontalface_default.xml --beard images/white_beard.jpg

from picamera.array import PiRGBArray
from picamera import PiCamera

import numpy as np
import argparse
import time
import cv2

fix = 0
x = 0

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True,
	help = "Path to the face cascade file")
ap.add_argument("-v", "--video",
	help = "Path to the (optional) video file")
ap.add_argument("--beard", required = True,
	help = "Path to the beard file")
args = vars(ap.parse_args())

# load image of beard and set up templates
beard = cv2.imread(args["beard"])

# initialize the camera and grab a reference to the raw camera
# capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# construct the face detector and allow the camera to warm
# up
fd = FaceDetector(args["face"])
time.sleep(0.1)

# capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image
	frame = f.array
	# resize the frame and convert it to grayscale
	# frame = imutils.resize(frame, width = 300)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# detect faces in the image and then clone the frame
	# so tbeard we can draw on it
	faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 5,
		minSize = (30, 30))
	frameClone = frame.copy()
	new_beard = frameClone.copy()
	cv2.rectangle(new_beard, (0,0), (new_beard.shape[1],new_beard.shape[0]),		(255, 255, 255), -1)
	# loop over the face bounding boxes and draw them
	for (x, y, w, h) in faceRects:
		# cv2.rectangle(frameClone, (x, y), (x + w, y + h), (0, 255, 0), 2)
		resized_beard = imutils.resize(beard, width = w)
		if (resized_beard.shape[0] + y + (3/5 * h)) < frameClone.shape[0]:
			fix = 1
			x_offset = x
			y_offset = y + (3/5 * h)
			new_beard[y_offset:y_offset + resized_beard.shape[0],
				x_offset:x_offset + resized_beard.shape[1]] = resized_beard
			gray_beard = cv2.cvtColor(new_beard, cv2.COLOR_BGR2GRAY)
			# blurred_beard = cv2.GaussianBlur(gray_beard, (5,5), 0)
			# edged_beard = cv2.Canny(gray_beard, 169, 255)
			edged_beard = auto_canny.auto_canny(gray_beard)
			(_, cnts, _) = cv2.findContours(edged_beard.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)
			# print("I count {} beard(s)".format(len(cnts)))
			# create negative mask
			cv2.drawContours(frameClone, cnts, -1, (0, 0, 0), cv2.FILLED)
	# create positive mask and combine
	if fix == 1:
		mask = np.zeros(frameClone.shape[:2], dtype = "uint8")
		cv2.drawContours(mask, cnts, -1, (255, 255, 255), cv2.FILLED)
		final = cv2.bitwise_and(new_beard, new_beard, mask = mask)
	# show our detected faces, then clear the frame in
	# preparation for the next frame
	if fix == 1:
		resized_frameClone = imutils.resize(frameClone, width = 1065)
		resized_final = imutils.resize(final, width = 1065)
		cv2.imshow("Face", cv2.bitwise_or(resized_frameClone, resized_final))
	else:
		resized_frameClone = imutils.resize(frameClone, width = 1065)
		cv2.imshow("Face", resized_frameClone)
	rawCapture.truncate(0)
	# take a picture it will last longer
	if cv2.waitKey(1) & 0xFF == ord("c"):
		if fix == 1:
			x = x + 1
			cv2.imwrite("Momento_{}.jpg".format(x), cv2.bitwise_or(resized_frameClone, resized_final))
			print("Photo Taken!!!")
			time.sleep(2)
		else:
			x = x + 1
			cv2.imwrite("Momento_{}.jpg".format(x), resized_frameClone)
			print("Photo Taken!!!")
			time.sleep(2)
	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
	fix = 0

class FaceDetector:
	def __init__(self, faceCascadePath):
		# load the face detector
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
	def detect(self, image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30)):

		# detect faces in the image
		rects = self.faceCascade.detectMultiScale(image,
			scaleFactor = scaleFactor, minNeighbors = minNeighbors,
			minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)

		# return the rectangles representing bounding
		# boxes around the faces
		return rects

def auto_canny(image, sigma=0.33):

	# compute the median of the single channel pixel intensities
	v = np.median(image)

	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)

	# print("Lower", lower)
	# print("Upper", upper)
	# return the edged image
	return edged
def translate(image, x, y):

	# Define the translation matrix and perform the translation
	M = np.float32([[1, 0, x], [0, 1, y]])
	shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
	# Return the translated image
	return shifted
def rotate(image, angle, center = None, scale = 1.0):
	# Grab the dimensions of the image
	(h, w) = image.shape[:2]
	# If the center is None, initialize it as the center of
	# the image
	if center is None:
		center = (w / 2, h / 2)

	# Perform the rotation
	M = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, M, (w, h))
	# Return the rotated image
	return rotated
def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
	# initialize the dimensions of the image to be resized and
	# grab the image size
	dim = None
	(h, w) = image.shape[:2]
	# if both the width and height are None, then return the
	# original image
	if width is None and height is None:
		return image
	# check to see if the width is None
	if width is None:
		# calculate the ratio of the height and construct the
		# dimensions
		r = height / float(h)
		dim = (int(w * r), height)
	# otherwise, the height is None
	else:
		# calculate the ratio of the width and construct the
		# dimensions
		r = width / float(w)
		dim = (width, int(h * r))
	# resize the image
	resized = cv2.resize(image, dim, interpolation = inter)
	# return the resized image
	return resized
