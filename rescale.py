import cv2 as cv
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_LINEAR)

#capture=cv.VideoCapture('Videos/dog.mp4')
img=cv.imread('Photos/cat.jpg')
while True:
    #isTrue,frame=capture.read()
   # frame_resized=rescaleFrame(frame,scale=0.2)
    image_resized=rescaleFrame(img)
    #cv.imshow('Video',frame)
    #cv.imshow('Resized Video',frame_resized)
    cv.imshow('image',img)
    cv.imshow('Resized_img',image_resized)
#capture.release()
#cv.destroyAllWindows()    
