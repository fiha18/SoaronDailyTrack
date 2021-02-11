Sobel Edge Detection:
	sobel_x = cv2.sobel(img, cv2.CV_64F, 1,0,ksize=3)
	sobel_y = cv2.sobel(img, cv2.CV_64F, 0,1,ksize=3)

	1.) Change in color intensity to detect edges by taking first derivative.
	2.) It is a differentiator operator and compute an approximation of the gradient of an image.It combines Guassian smoothing and Differentiation.
	3.) Horozontal Changes : Convolving I with a kernel Gx.
			Gx = [[-1,0,1],[-2,0,2],[-1,0,1]]*I
	4.) Vertical Changes   : Convolving I with a kernel Gy.
			Gy = [[-1,-2,-1],[0,0,0],[1,2,1]]*I

	G = sqrt(Gx**2 + Gy**2)
	5.) If kernel size is 3, then Sobel not used Scharr is used.
		In Scharr Gx,Gy all 1 replaced with 3 and all 2 replaced with 10.
