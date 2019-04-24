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


tres=cv.adaptiveThreshold(blurrr,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,15,3)
cv.imshow("tres", tres)



cv.waitKey(0)



