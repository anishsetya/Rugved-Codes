import cv2 as cv
import numpy as np

capture=cv.VideoCapture('ball_tracking_example.mp4')

while True:
    isTrue, frame= capture.read()
    cv.imshow('Video',frame)
    
    blur=cv.GaussianBlur(frame,(11,11), cv.BORDER_DEFAULT)

    hsv=cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    lowerValues = np.array([42, 30, 30])
    upperValues = np.array([65, 220, 220])
    ball=cv.inRange(hsv, lowerValues, upperValues)
    
    contours,hierarchies=cv.findContours(ball, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    cv.drawContours(frame, contours, -1,(0,0,255),5)
    cv.imshow('tracking ball',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
