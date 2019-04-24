import numpy as np
import cv2 as cv
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to img")
args=vars(ap.parse_args())

img= cv.imread(args["image"])
cv.imshow("org",img)

flippedH=cv.flip(img,1)
flippedV=cv.flip(img,0)
flippedHV=cv.flip(img,-1)

cv.imshow("h",flippedH)
cv.imshow("v",flippedV)
cv.imshow("hv",flippedHV)
cv.waitKey(0)