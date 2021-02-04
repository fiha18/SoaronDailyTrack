import cv2
import numpy as np

import util as extractor

extractor.create('HSV')
cap = cv2.VideoCapture(0)

while True:

	_, frame = cap.read()
	hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)

	low, high = extractor.extract('HSV')
	low = np.array(list(low))
	high = np.array(list(high))

	mask = cv2.inRange(hsv_img, low, high)
	res = cv2.bitwise_and(frame, frame, mask =  mask)

	cv2.imshow("res", res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()