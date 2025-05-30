import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)

size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*"MP4V")
out = cv.VideoWriter('output.mp4', fourcc, 15, size)

# # Create a named window and set it to fullscreen
# cv.namedWindow('frame', cv.WINDOW_NORMAL)
# cv.setWindowProperty('frame', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # write the frame
    
    out.write(frame)
    frame = cv.flip(frame, 1)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
