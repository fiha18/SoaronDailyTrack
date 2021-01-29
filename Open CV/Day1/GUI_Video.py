import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID') # OR ('X','V,'I','D')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

print(cap.isOpened())
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
while (cap.isOpened()):
	#ret will return bool value if frame is presennt or not
	#frame will save each frame
	ret, frame = cap.read()
	if not ret:
		break
	out.write(frame)
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	cv.imshow('frame', gray)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
out.release()
cv.destroyAllWindows()
