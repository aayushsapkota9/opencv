import cv2 as cv

img = cv.imread(cv.samples.findFile("../test1.png"), cv.IMREAD_COLOR)

if img is None:
    sys.exit("Could not read the image.")

# b,g,r = cv.split(img)
# cv.imshow("Rgb original",img)
# img[:,:,2] = 255


# cv.imshow("Red Channel in Color", r)
# cv.imshow("blue Channel in Color", b)
# cv.imshow("green Channel in Color", g)
print(img.shape)
ball = img[0:300, 000:300]
cv.imshow("ball",ball)
img[150:450, 450:750] = ball
cv.imshow("Rgb",img)


k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)
