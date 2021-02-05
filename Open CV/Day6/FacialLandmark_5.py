# Important Packages 

from imutils.video import VideoStream
from imutils import face_utils

import argparse
import imutils 
import time
import dlib 
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape_predictior", required = True, help= "Path to Facial Landmark Predictions")

args = vars(ap.parse_args())

#Initializing dlib's face detector (HOG-based) and creating predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictior"])

# Initialize the video stream and sleep for a bit
vs = VideoStream(src=0).start()

time.sleep(2.0)


while True:
	frame = vs.read()
	frame = imutils.resize(frame, width = 400)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	rects = detector(gray,0)

	if len(rects)>0:
		text = "{} face(s) found".format(len(rects))
		cv2.putText(frame, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)


	for rect in rects:
		(bX, bY, bW, bH) = face_utils.rect_to_bb(rect)
		cv2.rectangle(frame, (bX,bY), (bX + bW, bY + bH), (0,255,0), 1)

		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		for (i,(x,y)) in enumerate(shape):
			cv2.circle(frame, (x,y), 1, (0,0,255), -1)
			cv2.putText(frame, str(i+1), (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,255),1)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()