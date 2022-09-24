#Author is Jason Dsouza through freecodecamp.org
#Accessed at
#https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv

#Reading images

img = cv.imread('images/bluff.jpg')

cv.imshow('Bluff',img)

cv.waitKey(0)

#Reading videos
capture = cv.VideoCapture('videos/seacave.ogv')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()