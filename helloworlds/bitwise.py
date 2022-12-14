#Based on tutorial by author Jason Dsouza through freecodecamp.org
#Accessed at
#https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise AND', bitwise_and)

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise OR', bitwise_or)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise XOR', bitwise_xor)

# Bitwise NOT
bitwise_not_rect = cv.bitwise_not(rectangle)
cv.imshow('bitwise NOT rect', bitwise_not_rect)

cv.waitKey(0)