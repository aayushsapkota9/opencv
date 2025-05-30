import numpy as np
import cv2 as cv

# Create a black image
img = np.full((511,511,3),[0,0,0],np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(0,0),(510,510),(0,0,255),3)
cv.circle(img,(447,63), 63, (0,0,255), 1)
cv.ellipse(img,(256,170),(80,80),120,0,300,(0,0,255),-1)
cv.ellipse(img,(256,170),(40,40),0,0,360,(0,0,0),-1)
cv.ellipse(img,(170,340),(80,80),-20,0,315,(0,255,0),-1)
cv.ellipse(img,(170,340),(40,40),0,0,360,(0,0,0),-1)

cv.ellipse(img,(340,340),(80,80),300,0,300,(255,0,0),-1)
cv.ellipse(img,(340,340),(40,40),0,0,360,(0,0,0),-1)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
cv.imshow("Display window", img)
k = cv.waitKey(0)
