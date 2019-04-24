import numpy as np
import cv2 as cv

rectangle = np.zeros((300, 300), dtype="uint8")
cv.rectangle(rectangle, (25, 25), (275, 275), (255, 0, 0), -1)
cv.imshow('rectangle', rectangle)
circle = np.zeros((300, 300), dtype="uint8")
cv.circle(circle, (150, 150), 150, (255, 0, 0), -1)
cv.imshow('circle', circle)
cv.waitKey(0)

bitwiseAnd = cv.bitwise_and(rectangle, circle)
cv.imshow('and', bitwiseAnd)

bitwiseOr = cv.bitwise_or(rectangle, circle)
cv.imshow('or', bitwiseOr)

bitwiseXor = cv.bitwise_xor(rectangle, circle)
cv.imshow('xor', bitwiseXor)

bitwiseNotR = cv.bitwise_not(rectangle)
cv.imshow('notr', bitwiseNotR)

bitwiseNotc = cv.bitwise_not(circle)
cv.imshow('notc', bitwiseNotc)

cv.waitKey(0)
