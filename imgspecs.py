import cv2 as cv
from cv2 import imread
img=imread('Photos/cats 2.jpg')
cv.imshow('original img',img)
#cv.waitKey(0)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
cv.waitKey(0)
# blur=cv.GaussianBlur(img,(3,3),0)
# cv.imshow('blur',blur)
# cv.waitKey(0)
# canny=cv.Canny(img,125,175)
# cv.imshow('canny',canny)
# cv.waitKey(0)