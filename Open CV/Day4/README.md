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

Adaptive Thresholding - THreshold value is calculated for regions and should be different for different region.
	cv2.adaptiveThreshold(<source Image>, 255, Adaptive method, Threshold technique,block size, C)
cv2.imshow("Image", img)
	Adaptive mwthods - 
		1.) ADAPTIVE_THRESH_MEAN_c
		2.) ADAPTIVE_THESH_GUASSIAN_c

Both thresholding technique can be used depending on the condition.
