#Based on tutorial by author Jason Dsouza through freecodecamp.org
#Accessed at
#https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images/bluff.jpg')
cv.imshow('Bluff', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)


# Calculate histogram
gray_hist = cv.calcHist([img], [0], mask, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

colors = ('b', 'g', 'r')


plt.figure()
plt.title('Colors Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)