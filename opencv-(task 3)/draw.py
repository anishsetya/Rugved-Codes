import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
#img=cv.imread('ducky.png')

#cv.imshow('image',blank)
#blank[250:350 , 250:350]=0,0,255

#cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,0,255), thickness=cv.FILLED)
#cv.imshow('rectangle image',blank)

#cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),100,(255,0,255),thickness=4)
#cv.imshow('cirlce image',blank)

#cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=4)
#cv.imshow('line image',blank)
cv.putText(blank,'lmao',(190,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)
cv.imshow('Text',blank)
cv.waitKey(0)