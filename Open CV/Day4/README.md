Day 4 - 3 Feb 2021


Thresholding is used to simplify video/image data analysis.
	Grayscale - ranges from 0 to 255
	Threshold  Image - ranges from 0 to 1. 
Thresholding is a technique in Open CV, which is the assignment of Pixel values in relation to the threshold value provided. In thresholding, each pixels are compared with threshold value provided and if >= the threshold value it is set to 0(min) or 255(max) vice versa.

Simple Thresholding - Threshold value is global i.e. same for all the pixels in the image.
	cv2.threshold(source, threshold value, maximumValue, threshold technique)
		BINARY THRESHOLD mainly.
		Threshold technique - 
			1.	cv2.THRESH_BINARY - >= threshold set to 255 and < set to 0.
			2.	cv2.THRESH_BINARY_INV - inverted of cv2.THRESH_BINARY.

Adaptive Thresholding - THreshold value is calculated for small regions and should be different for different region of the same image. A real time image has different lighting conditions in different areas.
	cv2.adaptiveThreshold(<source Image>, 255, Adaptive method, Threshold technique,block size, C)
cv2.imshow("Image", img)
	Adaptive methods - 
		1.) ADAPTIVE_THRESH_MEAN_c
		2.) ADAPTIVE_THESH_GUASSIAN_c


Both thresholding technique can be used depending on the condition.

Erosion and Dilation 

Used to reduce noise in Binary Image, these are a side effect of Thresholding.
Erosion - Reduce the size of foreground objects we can erode the pixels given no. of Iteration.
To Enlarge Region , use of Dilation.


Color Filtering 

RGB AND HSV 
RGB - is a additive color model Red,Green and Blue which makes whole range of colours.

HSV - Hue, Saturation and Value and it is designed in a way such that it is closely align with the human vision percieves color-making attributes.
Hue: [0, 179]
Saturation: [0, 255]
Value: [0, 255]

HSV seperates image intensity from chorma/color information.



Contours :

Contours is a curve joining all the continuous points(along the boundary), having same color or intensity.
Useful in Shape Analysis and Object Detection and recognition.
	1.) Use Binary Image before applying Contours.
	2.) Source image is modified so use a copy of image.
	3.) Object to be contoured should be in White and background should be in black.

cv2.findContours(sourceImage, contourRetrivalMode, contourApproximation) :
	1st argument is Source Image.
	2nd argument is Contour Retrival Mode.
	3rd argument is Contour Approximation Method.
the return is 3 output : 1st is Image, 2nd is Contour and 3rd is Hierarchy.

Contour is a Python List of all the contours in the image and each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.

Most used Contour Retrival Mode - cv2.RETR_TREE.
Most used Contour Approximation Method - cv2.CHAIN_APPROX_SIMPLE


cv2.drawContours(sourceImage, contours, index of contours, color, thickness)
	1st argument - Source Image 
	2nd argument - Contours which should be passed as a Python list
	3rd argument - Index of Contours( To draw all contours -1 )
	4th argument - Color 
	5th argument - Thickness 


Contour Approximation Method - Contours are the boundaries of a shape with same intensity.It stores the (x,y) coordinates of the boundary. Two most common methods - 
	1.) cv2.CHAIN_APPROX_NONE - All the boundary points are stored 
	2.) cv2.CHAIN_APPROX_SIMPLE - It removes all the redundaant points in Contour and compress it.
	
