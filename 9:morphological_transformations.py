import cv2
import numpy as np


img = cv2.imread("Images/morphological_transformations.png")
img_opening = cv2.imread("Images/opening_input.png")
img_closing = cv2.imread("Images/closing_input.png")
img_tophat = cv2.imread("Images/top_hat.png")
#We are using a binary image as Morphological Transformations are usually done on binary images,
#if you have a grayscale image you can convert it into a binary image by using Thresholding

#First we need to create a kernel that will slide through the image for Morphological Transformations

kernel = np.ones((5,5))

#Types of Morphological transformations

#1.Erosion
#2.Dilation

#3.Opening
#4.Closing

#5.Morphological Gradient

#6.Top-Hat
#7.Black-Hat



#1.Erosion : Erosion in simple language cuts or erodes away the boundaries of an object, In Erosion all
# if there is a say a zero in between a group of ones in the kernel matrix then it converts the zero into a ones
# It is useful to remove white noise from images

erosion = cv2.erode(img,kernel,iterations = 1)

#2.Dialation :  Dilation is completely opposite of erosion, it will increase the boundaries of an object, In Dilation
# if all value is say one and remaining zero then it will change all the values to one. Dilation is usually
# used after Erosion as Erosion will remove white noise and slim the objects while then Dilation will get the
# size of the objects back

dilation = cv2.dilate(img,kernel,iterations = 1)

#3.Opening : Opening is just another name of erosion followed by dilation. It is useful in removing noise.

opening = cv2.morphologyEx(img_opening, cv2.MORPH_OPEN, kernel)
opening_result = np.concatenate((img_opening, opening), axis=1)

#4.Closing : Closing is reverse of Opening, Dilation followed by Erosion.
#It is useful in closing small holes inside the foreground objects, or small black points on the object.

closing = cv2.morphologyEx(img_closing, cv2.MORPH_CLOSE, kernel)
closing_result = np.concatenate((img_closing, closing), axis=1)

#5.Morphological Gradient : It is the difference between dilation and erosion of an image.
# The result will look like the outline of the object.

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

#6.Top-Hat : The top-hat filter (a.k.a. white top-hat filter) is used to enhance bright
#objects of interest in a dark background

#convert to grayscale
img_tophat =  cv2.cvtColor(img_tophat,cv2.COLOR_BGR2GRAY)
#convert to binary
_,img_tophat = cv2.threshold(img_tophat, 75, 255, cv2.THRESH_BINARY)
tophat = cv2.morphologyEx(img_tophat, cv2.MORPH_TOPHAT, kernel)

#6.Botton-Hat : The bottom hat is exactly opposite of top hat to enhance dark
#objects of interest in a bright background

cv2.imshow("Image",img)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Gradient",gradient)
cv2.imshow("Opening Comparsion",opening_result)
cv2.imshow("Closing Comparsion",closing_result)
cv2.imshow("Top Hat",tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Different types of Kernel
'''# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)'''
