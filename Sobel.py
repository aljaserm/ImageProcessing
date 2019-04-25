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

Xsobel=cv.Sobel(img,cv.CV_64F,1,0)
Ysobel=cv.Sobel(img,cv.CV_64F,0,1)

Xsobel=np.uint8(np.absolute(Xsobel))
Ysobel=np.uint8(np.absolute(Ysobel))

mixed=cv.bitwise_or(Xsobel,Ysobel)
cv.imshow("Xsobel", Xsobel)
cv.imshow("Ysobel", Ysobel)
cv.imshow("mixed", mixed)

cv.waitKey(0)

