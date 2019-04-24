import numpy as np
import cv2 as cv
import argparse
import matplotlib.pyplot as pt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

img = cv.imread(args["image"])
cv.imshow("org", img)


blurrr=np.hstack([cv.blur(img,(3,3)),cv.blur(img,(5,5)),cv.blur(img,(9,9))])
cv.imshow("Blurr", blurrr)
cv.waitKey(0)