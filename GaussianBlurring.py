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
    cv.GaussianBlur(img,(3,3),0),
    cv.GaussianBlur(img,(5,5),0),
    cv.GaussianBlur(img,(7,7),0)
])
cv.imshow("BlurrG", blurrr)
cv.waitKey(0)