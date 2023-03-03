import cv2 as cv
import numpy as np

img=cv.imread('boston.jpg')


gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh=cv.threshold(gray,160,225,cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C
,11,3)

cv.imshow('adaptive', adaptive_thresh)

cv.waitKey(0)