import numpy as np
import cv2 as cv
import argparse
import matplotlib.pyplot as pt

img = cv.imread("ce3.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
pt.imshow(img)
