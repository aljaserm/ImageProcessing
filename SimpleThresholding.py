import numpy as np
import cv2 as cv
import argparse
import matplotlib.pyplot as pt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

img = cv.imread(args["image"])
cv.imshow("org", img)

img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blurrr=cv.GaussianBlur(img,(5,5),0)
cv.imshow("blured", blurrr)

(t,thresholded)=cv.threshold(img,140,255,cv.THRESH_BINARY)

cv.imshow("thresholded", thresholded)

(t,thresholdedInv)=cv.threshold(img,140,255,cv.THRESH_BINARY_INV)
cv.imshow("thresholdedInv", thresholdedInv)

cv.waitKey(0)

