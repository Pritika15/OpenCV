import cv2 as cv



def rescale_frame(frame, scale=75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] *scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation =cv.INTER_AREA)

cap = cv.VideoCapture('Video/kitten.mp4')
while True:
    rect, frame = cap.read()
    frame75 = rescale_frame(frame, scale=75)
    cv.imshow('frame75', frame75)
    frame150 = rescale_frame(frame, scale=150)
    cv.imshow('frame150', frame150)

cap.release()
cv.destroyAllWindows()