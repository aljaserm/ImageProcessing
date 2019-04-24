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
hist=cv.calcHist([img],[0],None,[256],[0,256])
pt.figure()
pt.title("grayScale")
pt.xlabel("Bins")
pt.ylabel("pixels")
pt.plot(hist)
pt.show()

cv.waitKey(0)