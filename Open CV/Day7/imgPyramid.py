import cv2 
import numpy as np 
from matplotlib import pyplot as plt 


img1 = cv2.imread('input.jpg')

smaller = cv2.pyrDown(img1)
larger = cv2.pyrUp(smaller)

row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize = (15, 10))

axs[0].imshow(img1)
axs[0].set_title('Matplotlib color')

axs[1].imshow(smaller)
axs[1].set_title('Smaller Image')

axs[2].imshow(larger)
axs[2].set_title('Larger Image')

plt.show()