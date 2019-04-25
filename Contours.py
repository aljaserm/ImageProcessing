import numpy as np
import cv2 as cv
import argparse
import matplotlib.pyplot as pt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

img = cv.imread(args["image"])
cv.imshow("org", img)

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", img)

blurrr = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow("blured", blurrr)

canny = cv.Canny(blurrr, 30, 150)
cv.imshow("canny", canny)

conto,hierachy = cv.findContours(canny.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# cv.imshow("conto", conto)
print("imgs Contours {}".format(len(conto)))

coin = img.copy()
cv.drawContours(coin, conto, -1, (0, 0, 0), 2)
cv.imshow("coin", coin)

cv.waitKey(0)
