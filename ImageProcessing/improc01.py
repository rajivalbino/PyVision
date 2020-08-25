# Image Processing basic techniques with OpenCV
# Tutorial from PyImageSearch
import argparse
import cv2
import imutils

# Argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

# Load
img = cv2.imread(args["image"])

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
rx,ry,rw,rh = cv2.selectROI("Image", img)
#roi = img[220:420, 160:360]
roi = img[ry:ry+rh, rx:rx+rw]
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

# Rectangle
imgcpy = img.copy()
cv2.rectangle(img=imgcpy, pt1=(160,220), pt2=(360,420), color=(0,255,0), thickness=2, lineType=4)
cv2.imshow("Output", imgcpy)
cv2.waitKey(0)

# Circle
# imgcpy = img.copy()
cv2.circle(img=imgcpy, center=(220,265), radius=10, color=(255,0,0), thickness=-1)
cv2.imshow("Output", imgcpy)
cv2.waitKey(0)

# Line
# imgcpy = img.copy()
b = 40
cv2.line(img=imgcpy, pt1=(b,b), pt2=(w-b,h-b), color=(0,0,255), thickness=5)
cv2.imshow("Output", imgcpy)
cv2.waitKey(0)

# Text
# imgcpy = img.copy()
cv2.putText(img=imgcpy, text="OpenCV", org=(10,25), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.7, color=(0,255,0), thickness=2)
cv2.imshow("Output", imgcpy)
cv2.waitKey(0)
