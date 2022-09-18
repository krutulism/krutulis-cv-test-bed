import cv2 as cv

img = cv.imread('images/tower.jpg')
cv.imshow('Tower', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Median
median = cv.medianBlur(img, 3)
cv.imshow('Median',median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)