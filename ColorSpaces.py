import numpy as np
import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

img = cv.imread(args["image"])
cv.imshow("org", img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("gray", gray)
cv.imshow("hsv", hsv)
cv.imshow("lab", lab)
cv.waitKey(0)