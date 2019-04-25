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
cv.imshow("gray", img)

blurrr=cv.GaussianBlur(img,(5,5),0)
cv.imshow("blured", blurrr)

canny=cv.Canny(blurrr,30,150)
cv.imshow("canny", canny)
cv.waitKey(0)

