import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Images/watch.jpg',cv2.IMREAD_GRAYSCALE)
#gray scale : so we convert to grey scale to make it easy and fast, also it removes alpha channels
#options for second parameter are IMREAD_GRAYSCALE,IMREAD_COLOR,IMREAD_UNCHANGED
#opencv : BGR
#matplotlib RGB
#using opencv
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#you can use matplotlib to plot things on the image
'''plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()'''

#you can use the following to write the image on a file
#cv2.imwrite("watch_one.jpg",img)
