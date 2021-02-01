import imutils 
import cv2

#loading the input image

image = cv2.imread("jp.png")
 
# images are read as a numpy multi-dimensional array 
# image height, width and depth are equivalent to shape of rows, number of columns and number of channels respectively

(h, w, d) = image.shape

print("width = {}, height = {}, depth = {} ".format(w, h, d))

# Display the image on Screen
cv2.imshow("Image", image)
#Wait for Keypress
cv2.waitKey(0) 

#Access the BGR pixel value of any pixel

(B,G,R) = image[200,50]
print("B = {},	G = {},	R = {}".format(B, G, R))

# Extracting 100*100 pixel square ROIs 

roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

resized = cv2.resize(image, (200,200))
cv2.imshow("Resized Image.", resized)
cv2.waitKey(0)

#Maintaining Aspect Ratio of the image 
r = 300.0 / w # Aspect Ratio 
dim = (300, int(h*r)) # new height is h*r(aspect ratio)
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resized", resized)
cv2.waitKey(0)

#imutils library function for resize with maintaining the aspect ratio 
#This will reduce the size of codes   
resized = imutils.resize(image, width = 300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

#Rotaion of Image around center 
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated",rotated)
cv2.waitKey(0)

#Rotaion using imutils 

rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

#Rotation without clipping 

rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)
(h_r, w_r, d_r) = rotated.shape
print("width = {}, height = {}, depth = {} ".format(w_r, h_r, d_r))


#Blur by using Guassian Blur 

blurred = cv2.GaussianBlur(image, (21,21), 0)
cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)


#Drawing on the images 
#Rectangle
img1 = image.copy()
cv2.rectangle(img1, (320,15), (420,170), (0,255,0), 2)


#Circle 
cv2.circle(img1, (290,150), 20, (255,0,0),5) # if thickness is -1 then circle will be solid and filled in

out = image.copy()
cv2.line(out, (60,20), (400,200), (0,0,255), 5)

out = image.copy()
cv2.putText(out, "Writing Text Here", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1)
cv2.imshow("Text",out)
cv2.waitKey(0)
