Day3 - 2 Feb 2021

Argparse - a command line arguments parsing package.
Helps us to provide additional information at runtime.

Converting image to grayscale 
	cv2.cvtColor(<image-path>, cv2.COLOR_BGR2GRAY)

EDGE DETECTION
Edges are significant local change in the intensity of an image, can be defined as set of connected pixels that forms a boundary between two disjoint region. Edges are of 3 types - Horizontal, Vertical, and Diagonal Edge.

Edge detection is a method of segmenting an image into regions of discontinuity. It allows users to observe the features of an image for a significant change in the gray level.

Edge Detection Operators are of 2 types :
Gradient – based operator which computes first-order derivations in a digital image like, Sobel operator, Prewitt operator, Robert operator
Gaussian – based operator which computes second-order derivations in a digital image like, Canny edge detector, Laplacian of Gaussian 

Canny Edge Detection is an algorithm used to extract edges from images.This algorithm is based on the Grayscale images only.
Convert image to grayscale first.

This algorithms has following stages:
	Noise reduction
	Gradient calculation
	Non-maximum suppression
	Double threshold
	Edge Tracking by Hysteresis

1) Noise Reduction - 
By applying Guassian blur to smooth image.Image Convolution technique is applied with Guassian Kernel(3 X 3, 5 X 5, odd order). Kernel Order depends on Blurring effect.

2) Gradient Calculation - 
The Gradient calculation step detects the edge intensity and direction by calculating the gradient of the image using detection operators.Edges correspond to a change of pixels’ intensity. To detect it, the easiest way is to apply filters that highlight this intensity change in both directions: horizontal and vertical.
After smoothing image, by using Sobel Kernel we get Gradient Approximation and Edge Detection.


3) Non-Maximum Suppresion - 
Getting the perfect edges from images.

4) Thresholding -
Double Thresholding 

5) Edge Tracking

6) Final Cleansing 

Thresholding is a technique in Open CV, which is the assignment of Pixel values in relation to the threshold value provided. In thresholding, each pixels are compared with threshold value provided and if >= the threshold value it is set to 0(min) or 255(max) vice versa.

		cv2.threshold(source, threshold value, maximumValue, threshold technique)
		BINARY THRESHOLD mainly.
		Threshold technique - 
			1.	cv2.THRESH_BINARY - >= threshold set to 255 and < set to 0.
			2.	cv2.THRESH_BINARY_INV - inverted of cv2.THRESH_BINARY.
