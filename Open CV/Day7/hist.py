import cv2 
import numpy as np 
from matplotlib import pyplot as plt 


img1 = cv2.imread('input.jpg')

histogram = cv2.calcHist( [img1], [0], None, [256],	[0,256])

plt.hist(img1.ravel(), 256, [0,256]); plt.show()

color = ('b', 'g', 'r')

for i, col in enumerate(color):
	hist2 = cv2.calcHist( [img1], [i], None, [256], [0,256])
	plt.plot(hist2, color = col)
	plt.xlim([0,256])

plt.show()


row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize = (15, 10))
fig .tight_layout()

axs[0].imshow(img1)
axs[0].set_title('Matplotlib color')


axs[1].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
axs[1].set_title('Original RGB Color')

plt.show()


img2 = cv2.imread('tobago.jpg')

hist3 = cv2.calcHist([img2], [0], None, [256], [0,256])
plt.hist(img2.ravel(), 256, [0,256]); plt.show()


color = ('b', 'g', 'r')

for i, col in enumerate(color):
	hist4 = cv2.calcHist( [img2], [i], None, [256], [0,256])
	plt.plot(hist4, color = col)
	plt.xlim([0,256])

plt.show()


row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize = (15, 10))
fig .tight_layout()

axs[0].imshow(img2)
axs[0].set_title('Matplotlib color')


axs[1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
axs[1].set_title('Original RGB Color')

plt.show()