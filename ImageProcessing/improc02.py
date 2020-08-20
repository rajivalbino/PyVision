# Image Processing basic techniques with OpenCV
# Tutorial from PyImageSearch
import imutils
import cv2

# Load
img = cv2.imread("tetris_blocks.png")
cv2.imshow("img", img)
cv2.waitKey(0)

# Grayscale convert
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)

# Canny edge detection
edge = cv2.Canny(gray, threshold1=30, threshold2=150)
cv2.imshow("Canny", edge)
cv2.waitKey(0)

# Tresholding
thresh = cv2.threshold(gray, thresh=225, maxval=255, type=cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

# Find Contours
#cntrs = cv2.findContours(thresh.copy(), )