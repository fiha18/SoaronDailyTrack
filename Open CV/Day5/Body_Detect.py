import cv2
import numpy as np

#Take the trackbar to H_low, S_low, V_low value 0 and H_high and S_high value 255 and V_high = 150
import util as extractor

extractor.create('HSV')
cap = cv2.VideoCapture(0)

while True:

	_, frame = cap.read()
	hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

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