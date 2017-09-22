import cv2
import numpy as np

img = cv2.imread('Images/watch.jpg',cv2.IMREAD_COLOR)

#referencing a specific pixel
px = img[55,55]

#modify the pixel with BGR values
px = (255,255,255)
print(px)

#ROI : Region of Image
region_image =  img[100:150,100:150]
print(region_image)

#modify the region
#img[100:150,100:150] = [255,255,255]

#more with ROI
watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
