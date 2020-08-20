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
cntrs = cv2.findContours(thresh.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
cntrs = imutils.grab_contours(cntrs)
output = img.copy()

for c in cntrs:
    cv2.drawContours(output, contours=[c], contourIdx=-1, color=(240,0,159), thickness=3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)

msg = "{} objects found!".format(len(cntrs))
cv2.putText(output, msg, (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (240,0,159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

# Erosion
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Erode", mask)
cv2.waitKey(0)

# Dilate
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilate", mask)
cv2.waitKey(0)

# Bitwise AND
mask = cv2.cvtColor(thresh.copy(), cv2.COLOR_GRAY2BGR)
output = cv2.bitwise_and(img, mask)
cv2.imshow("Bitwise AND", output)
cv2.waitKey(0)
