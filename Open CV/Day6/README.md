
Histogram :
It is a graph or Plot, which gives us an overall idea about intensity distribution of an image. It is a plot with Pixel value (0 - 255) on X-axis and Corresponding no. of Pixel Value in the image on Y-axis.
By looking at histogram we get intutions about contrast, brightness , intensity distribution of an image.  

matplotlib subplot :
	import matplotlib.pyplot as plt 
	plt.subplot(221), plt.imshow("Image name", image_variable) -  no of rows = 2, no of column = 2 and this plot is at 1st position , display plot at sub plot location
	plt.subplot(222), plt.imshow("Image name", image_variable) -  no of rows = 2, no of column = 2 and this plot is at 2nd position , display plot at sub plot location
	plt.subplot(223), plt.imshow("Image name", image_variable) -  no of rows = 2, no of column = 2 and this plot is at 3rd position, display plot at sub plot location
	plt.subplot(224), plt.imshow("Image name", image_variable) -  no of rows = 2, no of column = 2 and this plot is at 4th position, display plot at sub plot location



Face Detection Models :
	1.) Haar cascades: Fast, but less accurate. Can be a pain to tune parameters.
	2.) HOG + Linear SVM: Typically (significantly) more accurate than Haar cascades with less false positives. Normally less parameters to tune at test time. Can be slow compared to Haar cascades.
	3.)Deep learning-based detectors: Significantly more accurate and robust than Haar cascades and HOG + Linear SVM when trained correctly. Can be very slow depending on depth and complexity of model. Can be sped up by performing inference on GPU .


Facial Land Mark Detection using HOG + Linear SVM Technique :

