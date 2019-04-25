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

lap=cv.Laplacian(img,cv.CV_64F)
lap=np.uint8(np.absolute(lap))

cv.imshow("lap", lap)

cv.waitKey(0)