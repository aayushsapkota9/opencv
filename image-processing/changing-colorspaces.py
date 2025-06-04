import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

while(1):

    # Take each frame
    _, frame = cap.read()
    frame=cv.flip(frame,1)

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([0,0,0])
    upper_blue = np.array([[180, 255, 75]])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',cv.bitwise_not(mask))
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()