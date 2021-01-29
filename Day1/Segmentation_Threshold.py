
#Imporing Necessary Libraries of Python Programming Language
from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage


# Loading Image and Adjusting its size for Image Show
img = cv2.imread('building.jpg')
img = cv2.resize(img, (960, 540))    


# Converting RGB image into Binary Image i.e. Grayscale
gray = rgb2gray(img)
cv2.imwrite('gray_img.jpg', gray)
print(gray.shape)



# Detecting Colouring Region and Non-Colouring Region
gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
mean = gray_r.mean()
n = gray_r.shape[0]
for i in range(n):
	if (gray_r[i] > mean):
		gray_r[i] = 1
	else:
		gray_r[i] = 0
gray = gray_r.reshape(gray.shape[0],gray.shape[1])


cv2.imwrite('Non-Colouring.jpg', gray)
cv2.imshow('image-2', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

