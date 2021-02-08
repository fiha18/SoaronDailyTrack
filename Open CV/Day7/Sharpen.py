import cv2 
import numpy as np 
from matplotlib import pyplot as plt 


img1 = cv2.imread('input.jpg')

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize = (15, 10))

axs[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
axs[0].set_title('MAIN IMAGE')

kernel_sharp = np.array([[-1,-1,-1],[-1,11,-1],[-1,-1,-1]])

sharpen = cv2.filter2D(img1, -1, kernel_sharp)

axs[1].imshow(cv2.cvtColor(sharpen, cv2.COLOR_BGR2RGB))
axs[1].set_title('SHARPEN IMAGE')
cv2.imwrite('sharpen_img.jpg', sharpen)
plt.show()