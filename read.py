import cv2 as cv

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)
cv.waitKey(0)
# capture=cv.VideoCapture('Videos/dog.mp4')
# while True:
#     isTrue,frame=capture.read()
#     cv.imshow('video',frame)
#     if cv.waitKey(20) &OXFF==('d'):
#         break
# capture.release()
# cv.destroyAllWindows()    