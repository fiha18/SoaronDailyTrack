Day2 - 1 Feb 2021

Imutils are a series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, and displaying Matplotlib images easier with OpenCV and both Python 2.7 and Python 3.
Installing imutils 
	pip install imutils 

Images are read as a numpy multi-dimensional array, image height, width and depth are equivalent to shape of rows, number of columns and number of channels respectively.
Depth is the number of channels — I am working with 3 color channels: Blue, Green, and Red.
In OpenCV color images in the RGB (Red, Green, Blue) color space have a 3-tuple associated with each pixel: (B, G, R).
Each value in BGR tuple can range from [0-255] that means colors possible is 256*256*256 = 16777216.

Extracting Region of Interest (ROIs) with array slicing:
	image[startY:endY, startX:endX]	

Image interpolation occurs when you resize or distort image from pixel grid to another. 

Image resizing is necessary to increase or decrease the total number of pixels.

Image zooming refers to increase the quantity of pixels.

Interpolation works by using known data to estimate values at unknown points.

Image interpolation works in two directions, and tries to achieve a best approximation of a pixel's intensity based on the values at surrounding pixels. 

Common interpolation algorithms can be grouped into two categories: adaptive and non-adaptive. Adaptive methods change depending on what they are interpolating, whereas non-adaptive methods treat all pixels equally. 

Rotation in Open CV :
	1 - First calculate the Center of the pixel grid.
		center = (width // 2, height // 2)
	2 - Rotaion matrix using getRotationMatrix2D(center, angle , scaling)
		for angle - positive angles are counterclockwise and negative angles are clockwise.

By using imutils rotate_bound function , No clipping happens but the pixel grid width and height increases.
	imutils.rotate_bound(image, 45) - positive angles are clockwise and negative angles are counterclockwise.

Smoothing an image
Bluring an image to reduce high-frequency noise, making it easier for algorithms to detect and understand the actual contents of the image instead of noise that will confuse the algorithms. Blurring is. applying a low-pass filter to an image. In computer vision, the term “low-pass filter” applies to removing noise from an image while leaving the majority of the image intact. A blur is a very common operation we need to perform before other tasks such as edge detection.
Blurring can be achieved by many ways. The common type of filters that are used to perform blurring are.
	Mean filter
	Weighted average filter
	Gaussian filter

Mean Filter/Box Filter:
	1 - Odd Ordered.
	2 - The sum of element should be 1.
	3 - All elements should be same. 

Weighted Average Filter:
	1 - Odd Ordered.
	2 - The sum of element should be 1.
	3 - Weight of Center element should be more than the other elements.

Gaussian Blur operation, the image is convolved with a Gaussian filter instead of the box filter. The Gaussian filter is a low-pass filter that removes the high-frequency components are reduced.
 
As the order of kernel increases the intensity of blur also increase.

Convolution is simply an element-wise multiplication of two matrices followed by a sum.
An image as a big matrix and kernel or convolutional matrix as a tiny matrix that is used for blurring, sharpening, edge detection, and other image processing functions.It’s normal to hand-define kernels to obtain various image processing functions.Blurring (average smoothing, Gaussian smoothing, median smoothing, etc.), edge detection (Laplacian, Sobel, Scharr, Prewitt, etc.), and sharpening — all of these operations are forms of hand-defined kernels that are specifically designed to perform a particular function.

Big Matrix - Image and Tiny Matrix - Kernel.
Kernels are mainly of size N x N matrices where N is always Odd(because Odd matrices gives an integer center)
