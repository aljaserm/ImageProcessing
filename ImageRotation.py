import numpy as np
import cv2 as cv
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to img")
args=vars(ap.parse_args())

img= cv.imread(args["image"])
cv.imshow("org",img)

# (h,w)=img.shape[:2]
# center=(w//2, h//2)
# m=cv.getRotationMatrix2D(center,45,1.0)
# rot=cv.warpAffine(img,m,(img.shape[1],img.shape[0]))
# cv.imshow("shift",rot)
# cv.waitKey(0)

def rotateImg(img,angle,center=None, scale=1.0):
    (h, w) = img.shape[:2]
    if center is None:
        center = (w // 2, h // 2)
    m = cv.getRotationMatrix2D(center, angle, scale)
    rot = cv.warpAffine(img, m, (img.shape[1], img.shape[0]))
    return rot

rotate=rotateImg(img,-80)
cv.imshow("shift",rotate)
cv.waitKey(0)