import argparse
import imutils 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# Using Canny method for Edge Detection 

edged = cv2.Canny(gray,30,150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

# Thresholding 

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("threshold", thresh)
cv2.waitKey(0)

