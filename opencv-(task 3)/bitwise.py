import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
#histogram not working
img=cv.imread('boston.jpg')
blank=np.zeros(img.shape[:2], dtype='uint8')

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#rectangle= cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)

mask=circle= cv.circle(blank.copy(),(img.shape[1]//2, img.shape[0]//2),200,255,-1)
gray_hist= cv.calcHist([gray],[0], None,[256],[0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('no of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])

cv.imshow('Mask', mask)
#cv.imshow('circle', circle)

masked= cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked image', masked)
cv.waitKey(0)