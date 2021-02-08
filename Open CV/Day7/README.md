
Histogram :
It is a graph or Plot, which gives us an overall idea about intensity distribution of an image. It is a plot with Pixel value (0 - 255) on X-axis and Corresponding no. of Pixel Value in the image on Y-axis.
By looking at histogram we get intutions about contrast, brightness , intensity distribution of an image.  


cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

	images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".

	channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.

	mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)

	histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
	
	ranges : this is our RANGE. Normally, it is [0,256].

Affine Transformation: 
	Combines Linear Transformations, and Translations 

	Propertities:
		1-Origin does not necessary map to origin
		2-Lines map to lines 
		3-Parallel lines remains parallel
		4-Ratios are preserved
