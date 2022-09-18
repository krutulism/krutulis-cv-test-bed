#Based on tutorial by author Jason Dsouza through freecodecamp.org
#Accessed at
#https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv

img = cv.imread('images/flower.jpg')
cv.imshow('Flower', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresh Inv', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                        11, 5)
cv.imshow('Adaptive Thresholding', adaptive_thresh)



cv.waitKey(0)
