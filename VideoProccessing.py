import numpy as np
import cv2 as cv

film=cv.VideoCapture('Film.mp4')

while True:
    ret,frame=film  .read()
    if ret==True:
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow("Frame",gray)

        if cv.waitKey(0==ord('q')):
            break
    else:
        break

film.release()
cv.destroyAllWindows()