from skimage.exposure import is_low_contrast
import numpy as np 
import skimage.filters
import imutils 
import cv2
import math

img = cv2.imread("Board.jpg")


finalContours = []

frame = imutils.resize(img, width=600)
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(blurred, 5, 180)
cnts, hie = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt_sw = sorted(cnts, key = cv2.contourArea, reverse = True)
cp = frame.copy()
cnt_sw = np.delete(cnt_sw, 0)
cnt_sw = np.delete(cnt_sw, 0)

peri = cv2.arcLength(cnt_sw[0], True)
cnt_approx = cv2.approxPolyDP(cnt_sw[0], 0.02*peri, True)
(x_swi,y_swi,w_swi,h_swi) = cv2.boundingRect(cnt_approx)
cv2.rectangle(cp, (x_swi,y_swi), (x_swi+w_swi, y_swi+h_swi), (0,255,0), 2)


cnt = sorted(cnts, key = cv2.contourArea, reverse = True)
cv2.drawContours(cp, cnt[0], -1, (0,0,255), 1)
hull = cv2.convexHull(cnt[0])
hull1 = hull.tolist()
hull1 = sorted(hull1, key = lambda x: x[0][0]+x[0][1])
x_min,y_min = hull1[0][0][0],hull1[0][0][1]
cv2.drawContours(cp,[hull], -1, (0,0,255), 2)
# Now after applying Contours we get the swtich board contour as the first element of 

cnts_Bo, hie_boa = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts_Bo = sorted(cnts_Bo, key = cv2.contourArea, reverse = True)
cnt_s = cnts_Bo[0]
M = cv2.moments(cnt_s)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

copy = frame.copy()

width_switch = int(w_swi + 0.1*w_swi)
hieght_switch = int(h_swi + 0.1*h_swi)
width_board = (cx - x_min)*2
hieght_board = (cy - y_min)*2 
w_ratio = width_board/width_switch
h_ratio = hieght_board/hieght_switch
swtich_width = 22 # In CM
swtich_height = 15 # In CM 
board_width = int(swtich_width*w_ratio)
board_height = int(swtich_height*h_ratio)

cv2.rectangle(copy, (x_min,y_min), (x_min+width_board,y_min+hieght_board),(0,0,0),2)
cv2.putText(copy, '{}cm'.format(board_width), (x_min + 30, y_min - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (0, 0, 255), 2)
cv2.putText(copy, '{}cm'.format(board_height), (x_min - 70, y_min + board_height), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,(0, 0, 255), 2)

Area  = board_width * board_height
Diagonal = int(math.sqrt(board_width**2 + board_height**2))


print("Dimensions of White Board - Width : {} CM, Height : {} CM".format(board_width,board_height))
print(" Diagonal : {} CM, Area : {} SQUARE CM".format(Diagonal,Area))
cv2.imshow("Rects", copy)

cv2.waitKey(0)
cv2.destroyAllWindows()