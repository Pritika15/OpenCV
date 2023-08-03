import cv2 as cv
import numpy as np
img=cv.imread('Photos/lady.jpg')
cv.imshow('original',img)
#cv.waitKey(0)
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
translated_img=translate(img,-60,50)
cv.imshow('translated',translated_img)
cv.waitKey(0)
cv.destroyAllWindows()

