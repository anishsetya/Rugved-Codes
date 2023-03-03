import cv2 as cv
import numpy as np

img= cv.imread('boston.jpg')
cv.imshow('image', img)

blank=np.zeros(img.shape, dtype='uint8')
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('grayscale',gray_image)

blur= cv.GaussianBlur(gray_image,(3,3), cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)

canny=cv.Canny(gray_image, 150,175)
cv.imshow('Canny edges', canny) 

ret,thresh= cv.threshold(blur, 150, 255, cv.THRESH_BINARY) #converting  to binary
cv.imshow('Threshold', thresh)
contours,hierarchies=cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1,(0,0,255),1)
cv.imshow('Contours',blank)
cv.waitKey(0)
