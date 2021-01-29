import cv2 as cv
# Read the image 
img = cv.imread("arrow.jpg", 0)
#Display the image 
cv.imshow("Image", img)
# k equals Key Pressed
k = cv.waitKey(0)
# if Esc is pressed then image displayed image will disappear
if k == 27:
	cv.destroyAllWindows()
# if s key is pressed then img will be save in as png file
elif k == ord('s'):
	cv.imwrite('arrow1.png',img)
	cv.destroyAllWindows()
