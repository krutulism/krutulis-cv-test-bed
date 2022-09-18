#Based on tutorial by author is Jason Dsouza through freecodecamp.org
#Accessed at
#https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv
import numpy as np

img = cv.imread('images/tower.jpg')
cv.imshow('Tower', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

translated = translate(img, -100, 150)
cv.imshow('Translated',translated)

rotated = rotate(img, 45)
cv.imshow('Rotated',rotated)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

flip = cv.flip(img, 1)
cv.imshow('Flipped',flip)

cv.waitKey(0)