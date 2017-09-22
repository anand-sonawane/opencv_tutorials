import cv2
import numpy as np

# 1 here tells you the number of your webcam
cap = cv2.VideoCapture(1)
# to load an recorded VideoCapture
# cap = cv2.VideoCapture('video.mp4')
# to download the video that is being captured
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    if(ret == False):
        print("Breaking because no frame was found")
        break
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)#show gray frame
        cv2.imshow('frame_original',frame)#show original frame
        out.write(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
