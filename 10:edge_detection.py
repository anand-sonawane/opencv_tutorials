import cv2
import numpy as np

img = cv2.imread("Images/edge_detection.jpg")

#first we will convert the image to Grayscale

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#now removing noise from the image

img_gaussian = cv2.GaussianBlur(img,(15,15),0)

#Now lets find the edgdes in the image

#Laplacian the Laplacian edge detector uses one kernel.
#It calculates second order derivatives in a single pass.
laplacian = cv2.Laplacian(img_gaussian,cv2.CV_64F)

#Sobel edge detector is a gradient based method based on the first order derivatives.
#It calculates the first derivatives of the image separately for the X and Y axes.
#It is more sensitive to noise than laplacian
sobelx = cv2.Sobel(img_gaussian,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img_gaussian,cv2.CV_64F,0,1,ksize=5)  # y

#Canny
#We will use the original image for canny because the algorithm in itself also applies blur
#Function parameters are image , min Value, max Value
canny = cv2.Canny(img_gaussian,100,250)

cv2.imshow("laplacian",laplacian)
cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
