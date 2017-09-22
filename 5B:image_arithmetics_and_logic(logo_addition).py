import cv2
import numpy as np

# 500 x 250 : both the images must be of same size exactly
img1 = cv2.imread('Images/3D-Matplotlib.png')
img2 = cv2.imread('Images/mainlogo.png')

#ROI the top left corner
rows,cols,channel = img2.shape
roi = img1[0:rows,0:cols]

#mask of the logo
img_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#print(img_gray[2,2])
#now we are creating a mask of the above image as follows:
#We have a threshold value of 220 , anything below 220 is converted to 255 meaning white and other
#all are converted into black, after this we take an inverse of it.
ret , mask = cv2.threshold(img_gray,220,255,cv2.THRESH_BINARY_INV)
#print(mask[2,2])
#1.image
#2.threshold value
#3.threshold max
#4.type
#different binary types
'''cv2.THRESH_BINARY
cv2.THRESH_BINARY_INV
cv2.THRESH_TRUNC
cv2.THRESH_TOZERO
cv2.THRESH_TOZERO_INV'''


#This gives you the complete inverse of the image, black becomes white and white becomes black
mask_inv = cv2.bitwise_not(mask)

# Now we will take the image background from image 1
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# and we will take the image foreground from image 2
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('Mask',mask)
cv2.imshow('Inverse Mask',mask_inv)
cv2.imshow('Image 1 background',img1_bg)
cv2.imshow('Image 2 foreground',img2_fg)
cv2.imshow('Resulted ROI',dst)
cv2.imshow('Final Image',img1)
cv2.imwrite('Images/Logo Addition Final Image.jpg',img1)
#Mask is Black background
#Inv Mask is White background
#Image 1 background is Inverse Mask plus the chart image area of the image in the background
#Image 2 foreground is Logo image with Mask in the background
#So then we just add the above two to get dst
#replace image 1 region with dst to get the final image
cv2.waitKey(0)
cv2.destroyAllWindows()
