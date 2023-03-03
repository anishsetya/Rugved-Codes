import cv2 as cv
# why does gray scale not work
img= cv.imread('boston.jpg')
cv.imshow('Image',img)

#gray=cv.cvtColor(img, cv.COLOR_BAYER_BG2BGR)
#cv.imshow('Gray Image',gray)

blur= cv.GaussianBlur(img,(5,5), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)

dilate= cv.dilate(canny,(3,3), iterations=1)
cv.imshow('dilate', dilate)

erode= cv.erode(dilate,(3,3), iterations=1)
cv.imshow('eroded', erode)

resize= cv.resize(img,(500,500))
cv.imshow('Resized', resize)

cropped=img[0:img.shape[0]//2, 0:img.shape[1]//2]
cv.imshow('cropped',cropped)
cv.waitKey(0)