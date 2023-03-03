import cv2 as cv
def rescaleFrame(frame, scale=0.50):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] *scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
img= cv.imread('ducky.png')
cv.imshow('image',img)
newimg=rescaleFrame(img)
cv.imshow('imagenew',newimg)
cv.waitKey(0)
capture=cv.VideoCapture('testt.mkv')

#while True:
    #isTrue,frame=capture.read()
    #cv.imshow('video',frame)
    
    #if cv.waitKey(20) & 0xFF==ord('d'):
      #  break
while True:
    isTrue,frame=capture.read()
    cv.imshow('video',frame)

    framenew=rescaleFrame(frame)
    cv.imshow('smaller video', framenew)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()