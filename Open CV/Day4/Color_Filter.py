import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while(True):

	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([77, 21, 0])
	upper_blue = np.array([230, 248, 176])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	res = cv2.bitwise_and(frame, frame, mask= mask)

	cv2.imshow("Original", frame)
	cv2.imshow("Masked", mask)
	cv2.imshow("Result", res)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()