import cv2 as cv
import numpy as np
cap=cv.VideoCapture('Videos/kitten.mp4')
if(cap.isOpened()==False):
    print("Error openeing the file")
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow('frame',frame)
    if cv.waitKey(10000000) & 0xFF == ord('q'):
        break
    else:
        break

cap.release()
cv.destroyAllWindows()            