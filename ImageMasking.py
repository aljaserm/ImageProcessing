import numpy as np
import cv2 as cv
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to img")
args=vars(ap.parse_args())

img= cv.imread(args["image"])
cv.imshow("org",img)

mask=np.zeros(img.shape[:2],dtype="uint8")
(cx,cy)=(img.shape[1]//2,img.shape[0]//2)
cv.rectangle(mask,(cx-90,cy-90),(cx+90,cy+90),(255.255,255),-1)
cv.imshow("mask",mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)
cv.waitKey(0)