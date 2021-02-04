Day 5 - 4 Feb 2021

Contours :
Features of Contour:
	Area
	Perimeter
	Bounding Box

Image moments(M) are a weighted average of image oixel intensities. The pixel intensity at location (x,y) is given by I(x,y). Note for a binary image I(x,y) can take a value of 0 or 1.

Centroid :-
	Cx = int(M['m10']/M['m00'])
	Cy = int(M['m01']/M['m00'])

Perimeter :-
	cv2.arcLength(cnt, True) - second argument whether shape is closed shape(True) or just curve.

Area :-
	cv2.contourArea(cnt)

Cntour Approximation:-
	Approximates a contour shape to another shape with less number of vertices depending on the precision specified.
	cv2.approxPolyDP(cnt, epsilon, True)
		epsilon - Maximum distance from contour to approximated contours,for just our convinience - epsilon = 0.1*Perimeter
		3rd argument - if it is closed shape(True) or curve(False)

Bounding Rectangle of Contour:
	Straight Rectangle:
		x,y,w,h = cv2.boundingRect(cnt)
		img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
	Rotated Rectangle:
	Bounding Rectangle is made with minimum area, so it is rotated also.
		rect = cv2.minAreaRect(cnt)
		box  = cv2.boxPoints(rect)
		box  = np.int0(box)
		im 	 = cv2.drawContour(img, [box], 0, (0,0,255), 2)

Enclosing Circle around Contour:
	(x,y), radius = cv2.minEnclosingCircle(cnt)
	center = (int(x), int(y))
	radius = int(radius)
	img = cv2.circle(img, center, radius, (0,255,0), 2)


Morphological Transformation:
	Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. Two basic morphological operators are Erosion and Dilation.

	Erosion - The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object. The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).

	Dilation - It is just opposite of erosion. Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases. It is also useful in joining broken parts of an object.

	Opening - Opening is just another name of erosion followed by dilation.It is useful in removing noise.

	Closing - Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the forebround  
	
	
