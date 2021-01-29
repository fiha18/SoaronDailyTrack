import numpy as np 
import cv2 as cv 

img = np.zeros((512,512,3), np.uint8)

cv.line(img, (0,0), (511,511), (0,0,255),7)

cv.rectangle(img,(300,300),(399,399),(0,255,0),5)

cv.circle(img, (150,150), 50, (255,0,0), -1)

cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()