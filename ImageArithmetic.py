import numpy as np
import cv2 as cv
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to img")
args=vars(ap.parse_args())

img= cv.imread(args["image"])
cv.imshow("org",img)

M=np.ones(img.shape,dtype="uint8")*100

added=cv.add(img,M)
cv.imshow("add",added)

subs=cv.subtract(img,M)
cv.imshow("sub",subs)

cv.waitKey(0)