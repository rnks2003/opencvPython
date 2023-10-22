# Author : rnks//AI043
# Illustrate basic image operations using openCV-python

import cv2

# --- LOADING AN IMAGE --- #

#to read image into a variable
img = cv2.imread('path',1)
#-1 for color
#0 for grayscale
#1 for transparent

# --- WHAT IS AN IMAGE --- #

print(type(img))
#prints datastructure/type used to store img

print(img.shape)
#displays height,width, channels

print(img)
#prints contents of numpy array

# --- RESIZING AN IMAGE --- #

#to resize by giving px value
img = cv2.resize(img,(400,400))

#to resize by fraction
img = cv2.resize(img,(0,0),fx=0.05,fy=0.05)
#fx is fraction (factor) by which the width is changed
#fy is fraction (factor) by which the height is changed

# --- ROTATING AN IMAGE --- #

#to rotate 
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
#rotates clockwise 90 degree

img = cv2.rotate(img,cv2.ROTATE_180)
#rotates by 180 degree

img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
#rotates anticlockwise 90 degrees

# --- SAVING AN IMAGE --- #

#to write/ save image
cv2.imwrite('path',img)

# --- DISPLAYING AN IMAGE --- #

#to display image
cv2.imshow('Image',img)
#takes window name and sorce variable as parameters

#to set waitTime
cv2.waitKey(5)

#to close display panel
cv2.destroyAllWindows()