import cv2
import numpy as np

img = cv2.imread("Images/color_filtering.jpeg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#the ordering here is hue sat value

lower_red = np.array([50,150,100])
upper_red = np.array([180,255,255])

mask = cv2.inRange(hsv,lower_red,upper_red)#everything that is within the above ranges
res = cv2.bitwise_and(img,img,mask = mask)

#now we will apply different types of blur to remove noise and smoothen the result

#1.Average Blurring
kernel = np.ones((15,15),np.float32)/225
smoothed = cv2.filter2D(res,-1,kernel)
#this is simple but the clarity is reduced a lot

#2.Gaussian Blurring
blur = cv2.GaussianBlur(res,(15,15),0)
#this contains a bit of noise

#3. Median Blurring
median = cv2.medianBlur(res,15)

#4. Bilateral Blurring
bilateral = cv2.bilateralFilter(res,15,75,75)

cv2.imshow("result",res)
cv2.imshow('Average Blurring',smoothed)
cv2.imshow('Gaussian Blurring',blur)
cv2.imshow('Median Blur',median)
cv2.imshow('bilateral Blur',bilateral)

#Depending on your use case you may have to use the blur which you feel is right for your case

cv2.waitKey(0)
cv2.destroyAllWindows()
