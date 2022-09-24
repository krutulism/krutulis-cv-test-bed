#Based on tutorial by author Jason Dsouza through freecodecamp.org
#Accessed at
#https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv
import numpy as np

img = cv.imread('images/flower.jpg')
cv.imshow('Flower', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

cv.imshow('Mask', mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)