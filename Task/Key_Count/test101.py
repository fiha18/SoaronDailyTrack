import cv2
import numpy as np 
# Apply this to real time video of Macbook keypad and cover each contour with colors(apply transparent) with count on the contour 
def reorder(points):
	#print(points.shape)
	pointsNew= np.zeros_like(points)
	points = points.reshape((4,2))
	add = points.sum(1)
	diff = np.diff(points, axis=1)
	pointsNew[0] = points[np.argmin(add)]
	pointsNew[3] = points[np.argmax(add)]
	pointsNew[1] = points[np.argmin(diff)]
	pointsNew[2] = points[np.argmax(diff)]
	return pointsNew
def mid(y1,y2):
	mid_y = (y2 - y1)/2
	mid_y += y1
	return mid_y
img = cv2.imread("keypad.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurr = cv2.GaussianBlur(gray,(11,11),0)
edged = cv2.Canny(blurr,0, 255)
cnts, hie = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cnts:
	cv2.drawContours(blurr,[c], -1,(0,0,255),1)
cnt = sorted(cnts, key = cv2.contourArea, reverse = True)
cp = img.copy()
box_point = []
for c in cnt:
	rect = cv2.minAreaRect(c)
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	box = reorder(box)
	box_point.append(box)
box_point = sorted(box_point, key = lambda x: x[0][0]+ x[0][1])
box_point = box_point[1:]
box_point = sorted(box_point, key = lambda x: mid(x[0][1],x[2][1]))
#box_point = sorted(box_point, key = lambda x: x[0][0])
for i in range(len(box_point)):
	x_t,y_t = box_point[i][0][0], box_point[i][0][1]
	x_b,y_b = box_point[i][3][0], box_point[i][3][1]
	mid_x,mid_y = int((x_t+x_b)/2) , int((y_t+y_b)/2)
	cv2.rectangle(cp, (x_t,y_t), (x_b,y_b), (0,0,0),-1)
	cv2.putText(cp,"{}".format(i+1) ,(mid_x - 6,mid_y + 2), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, cv2.LINE_AA)
print(box_point[:20])
cv2.imshow("Copy", cp)
cv2.waitKey(0)
cv2.destroyAllWindows()

