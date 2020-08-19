# Image Processing basic techniques with OpenCV
# Tutorial from PyImageSearch
import cv2
import imutils

img = cv2.imread("jp.png")

# Images are numpy objects, depth is the number of channels
(h, w, d) = img.shape 
print("width={}, height={}, depth={}".format(w,h,d))
cv2.imshow("Image", img)
cv2.waitKey(0)

# Access BGR pixel x=50,y=100
# BGR rather than RGB, pixels [y,x]
(B,G,R) = img[100,50]
print("R={}, G={}, B={}".format(R,G,B))

# ROI (Region of Interest)
# Rectangle from x,y = 320,60 to x,y = 420,160
roi = img[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# Resize to 200x200px
resized = cv2.resize(img, (200,200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# Resize keeping aspect ratio
# resize width to be 300px and calculating the new height
r = 300.0/w
dim = (300, int(h*r))
resized = cv2.resize(img, dim)
cv2.imshow("Proportional Resizing", resized)
cv2.waitKey(0)

# imutils auto compute proportional resize
resized = imutils.resize(img, width=200)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

# Rotation with rotation matrix and affine warp
center = (w//2, h//2)
mat = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(img, mat, (w,h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

# Rotation with imutils
rotated = imutils.rotate(img, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# Rotation with bounds
rotated = imutils.rotate_bound(img, 45)
cv2.imshow("Rotate with bounds", rotated)
cv2.waitKey(0)

# Gaussian Blur
blurred = cv2.GaussianBlur(img, (11,11), 0)
cv2.imshow("Gaussian Blur", blurred)
cv2.waitKey(0)

# Median Blur
blurred = cv2.medianBlur(img, 7)
cv2.imshow("Median Blur", blurred)
cv2.waitKey(0)


