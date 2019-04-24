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
    cv.medianBlur(img,3),
    cv.medianBlur(img,5),
    cv.medianBlur(img,7)
])
cv.imshow("Blurrm", blurrr)
cv.waitKey(0)