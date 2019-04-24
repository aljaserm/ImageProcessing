import numpy as np
import cv2 as cv
import argparse
import matplotlib.pyplot as pt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

img = cv.imread(args["image"])
cv.imshow("org", img)

blurrr=np.hstack([
    cv.bilateralFilter(img,5,25,35),
    cv.bilateralFilter(img,7,34,40),
    cv.bilateralFilter(img,9,40,50)
])
cv.imshow("BlurrB", blurrr)
cv.waitKey(0)