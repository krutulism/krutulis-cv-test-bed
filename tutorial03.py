#Based on tutorial by author is Jason Dsouza through freecodecamp.org
#Accessed at
#https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

# 1. Dump a color
blank[:] = 0,255,0
#cv.imshow('Green', blank)

# 2. Range of pixels
blank[200:300, 300:400] = 0,0,255
#cv.imshow('Red square', blank)

# 3. Draw a rectangle
cv.rectangle(blank, (blank.shape[1]//4,blank.shape[0]//4), (3*blank.shape[1]//4,3*blank.shape[0]//4), (255,0,0), thickness=-1)
#cv.imshow('Rectangle',blank)

# 4. Draw circle
cv.circle(blank, (blank.shape[1]//4,blank.shape[0]//4), 40, (120,50,100),thickness=3)
#cv.imshow('Circle',blank)

# 5. Draw line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=4)
#cv.imshow('Line',blank)

# 6. Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),thickness=2)
cv.imshow('Text',blank)


cv.waitKey(0)