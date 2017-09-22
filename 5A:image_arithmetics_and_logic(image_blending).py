import cv2
import numpy as np

# 500 x 250 : both the images must be of same size exactly
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

#superimposes one image over the other image
#add = img1+img2

#you can also use
#this will be pixel wise addition, addition pixel by pixel
# for eg pixel from first image is (255,0,0) and second is (0,255,255), the output will be (255,255,255)
#add = cv2.add(img1,img2)

#addWeighted is used for image blending , you can change the weights and it will give you
#a nice blending effect
add = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
#1:image 1
#2: image 1 weight
#3: image 2
#4: image 2 weight
#5: brightness of the total image

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
