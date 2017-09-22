import numpy as np
import cv2

img = cv2.imread("Images/book_page.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#There are basically 3 types of thresholding.
#1.Simple thresholding
#2.Adaptive thresholding
#3.Otsu thresholding

#Thresholding is used for simplying the image

#1. Simple Thresholding : If a pixel is greater than a threshold, convert it one value say white and if its less
#the convert it to say black

retval, image_with_threshold = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
retval, image_with_threshold_gray = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)

#Function used is cv2.threshold(image,threshold_value,max_threshold,type of binary threshold)
#retval is used for otsu, for simple it is your threshold_value value

cv2.imwrite("Images/Coloured Image Simple Threshold.jpg",image_with_threshold)
cv2.imwrite("Images/GrayScale Image Simple Threshold.jpg",image_with_threshold_gray)
#cv2.imshow("Image with Threshold Coloured",image_with_threshold)
#cv2.imshow("Image with Threshold Gray",image_with_threshold_gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#2. Adaptive Thresholding : Sometimes applying same threshold over all the image parts is not the right solution
#because the brightness of the image varies from part to part and we thus need threshold that can be Adaptive
#so we will be using Adaptive Threshold for that which will yeild better resuts than simple threshold

#There are 2 types of adaptiveThreshold:
#cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.

image_with_adaptive_threshold_gray_mean =  cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)
image_with_adaptive_threshold_gray_gaussian =  cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,2)

#Function used is cv2.adaptiveThreshold(image,max_threshold,type of adaptiveThreshold,neighbourhood block size, constant to be subtracted)

cv2.imwrite("Images/GrayScale Image Adaptive Threshold Mean.jpg",image_with_adaptive_threshold_gray_mean)
cv2.imwrite("Images/GrayScale Image Adaptive Threshold Gaussian.jpg",image_with_adaptive_threshold_gray_gaussian)
#cv2.imshow("Image with adaptiveThreshold Gray",image_with_adaptive_threshold_gray_mean)
##cv2.waitKey(0)
#cv2.destroyAllWindows()

#3.Otsu thresholding : Otsu thresholding is used in case the image processed is bi-modol image, we pass threshold
# as zero here and retval is the threshold that the algorithem deteremines for us

retval,image_with_otsu_threshold = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Function used is cv2.threshold(image,threshold_value,max_threshold,type of binary threshold)

cv2.imwrite("Images/GrayScale Image Otsu Threshold.jpg",image_with_otsu_threshold)
cv2.imshow("Image with Otsu Threshold Gray",image_with_otsu_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

#It should be noted that for our image otsu is not the best way to go,its for bi-modol images only
