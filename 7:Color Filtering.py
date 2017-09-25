import cv2
import numpy as np

img = cv2.imread("Images/color_filtering.jpeg")

#convert to your HSV colors : (Hue Saturation Value)
#This can help you actually pinpoint a more specific color,
#based on hue and saturation ranges, with a variance of value.

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#the ordering here is hue sat value
lower_red = np.array([50,150,100])
upper_red = np.array([180,255,255])

mask = cv2.inRange(hsv,lower_red,upper_red)#everything that is within the above ranges

result = cv2.bitwise_and(img,img,mask = mask)

#the result here we have tried to get the cap (red coloured object) to be filtered and everything else becomes dark
cv2.imshow("result",result)
cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
