import numpy as np
import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

img = cv.imread(args["image"])
cv.imshow("org", img)

(b, g, r) = cv.split(img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

cv.waitKey(0)

merged = cv.merge([b, g, r])
cv.imshow("merged", merged)
cv.waitKey(0)

zeros = np.zeros(img.shape[:2],dtype="uint8")
blue = cv.merge([b, zeros, zeros])
green = cv.merge([zeros, g, zeros])
red = cv.merge([zeros, zeros, r])

cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)


cv.waitKey(0)
