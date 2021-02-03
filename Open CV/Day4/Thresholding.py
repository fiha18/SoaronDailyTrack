import cv2
import numpy as numpy

img = cv2.imread("bookpage.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
guassian  = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Image", img)
cv2.imshow("Threshold", threshold)
cv2.imshow("Guassian", guassian)
cv2.waitKey(0)
