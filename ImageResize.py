import numpy as np
import cv2 as cv
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to img")
args=vars(ap.parse_args())

img= cv.imread(args["image"])
cv.imshow("org",img)

# r=200.0/img.shape[1]
# dim=(200,int(img.shape[0]*r))
# newSize= cv.resize(img,dim,cv.INTER_AREA)
# cv.imshow("new",newSize)
# cv.waitKey(0)

def resizeIt(img,width=None,height=None,inter=cv.INTER_AREA):
    dim=None
    (h,w)=img.shape[:2]
    if width is None and height is None:
        return img
    if width is None:
        r=height/float(h)
        dim=(int(w*r),height)
    else:
        r=width/float(w)
        dim=(width,int(h*r))
    resized=cv.resize(img,dim,inter)
    return resized

resize=resizeIt(img,height=1000)
cv.imshow("new",resize)
cv.waitKey(0)
