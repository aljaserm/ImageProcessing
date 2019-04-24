import numpy as np
import cv2 as cv
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to img")
args=vars(ap.parse_args())

img= cv.imread(args["image"])
cv.imshow("org",img)
# m=np.float32([[1,0,50],[0,1,60]])
# shift=cv.warpAffine(img,m,(img.shape[1],img.shape[0]))
# cv.imshow("shift",shift)
def translate(img,x,y):
    m = np.float32([[1, 0, x], [0, 1, y]])
    shift = cv.warpAffine(img, m, (img.shape[1], img.shape[0]))
    return shift

shiftCall=translate(img,70,-45)
cv.imshow("shift",shiftCall)
cv.waitKey(0)