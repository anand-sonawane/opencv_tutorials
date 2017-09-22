import numpy as np
import cv2

img = cv2.imread('Images/watch.jpg',cv2.IMREAD_COLOR)

#to draw an line on the image
#cv2.line(img,(0,0),(150,150),(255,0,0),5)#here colors are BGR
#arguments are :
#1.image
#2.start co-ordinates
#3.end co-ordinates
#4.linewidth
#if -1 for linewidth gives fill effect
#cv2.rectangle(img,(15,25),(100,100),(0,255,0),5)
#2: Top Left corner
#3: Bottom Right corner
#cv2.circle(img,(50,50),3,(0,0,255),5)
#2: center of the circle
#3: radius of the circle
#drawing a polygon

#points_poly = np.array([[10,5],[20,30],[70,25],[50,20],[100,10]], np.int32)
points_poly = np.array([(0, 0), (1998, 120), (1998, 2300), (0, 2600)],np.int32)
points_poly = points_poly.reshape((-1,1,2))
cv2.polylines(img,[points_poly],True,(255,255,255),3)
#3: whether to connect first point ot the last point or not

font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(img,"Anand",(0,130),font,1,(200,50,0),2,cv2.LINE_AA)
#2: Text you want to write
#3: Starting point of the Text
#4: Font of the Text
#5: Size of the Text
#6: color of the Text
#7: Spacing or width of the Text
#white is (255,255,255))
#black is (0,0,0)

#to draw an rectange on the image


cv2.imshow('image',img)
cv2.imwrite('Images/Drawing and Writing Result.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
