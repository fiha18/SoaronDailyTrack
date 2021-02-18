import numpy as np 
import cv2

img = cv2.imread("keyboard.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
minArea = 4
blurred = cv2.GaussianBlur(gray,(3,3),0)
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
thres = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
thres = cv2.adaptiveThreshold(thres, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
thres = cv2.adaptiveThreshold(thres, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
thres = cv2.adaptiveThreshold(thres, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)

edged = cv2.Canny(thres,0,255)
kernel = np.ones((3,3),np.uint8)
#edged = cv2.dilate(edged, kernel, iterations =1)
cnts, hie = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
Contours = []

for c in cnts:
	area = cv2.contourArea(c)
	if area > minArea:
		'''peri = cv2.arcLength(c, True)
								approx = cv2.approxPolyDP(c, 0.02*peri, True)
								bbox = cv2.boundingRect(approx)
								Contours.append([len(approx), area, approx, bbox, c])'''
		Contours.append([c])
for c in Contours:
	cv2.drawContours(img,c, -1,(0,0,255),1)
print(len(Contours))
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Image", thres)
cv2.imshow("Blurr", img)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()