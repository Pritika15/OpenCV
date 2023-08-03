import cv2 as cv
import numpy as np
img=cv.imread('Photos/cats.jpg')
cv.imshow('original image',img)
down_width=300
down_height=200
down_points=(down_width,down_height)
resized_down=cv.resize(img,down_points,interpolation=cv.INTER_LINEAR)
cv.imshow('resized img',resized_down)
cv.waitKey()
cv.destroyAllWindows()