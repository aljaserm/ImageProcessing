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

eq=cv.equalizeHist(img)
cv.imshow("eq", np.hstack([img,eq]))
cv.waitKey(0)