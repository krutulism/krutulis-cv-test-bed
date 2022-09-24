import cv2 as cv

#OpenCV DNN
net = cv.dnn.readNet()


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv.imshow('Frame', frame)
    cv.waitKey(1)