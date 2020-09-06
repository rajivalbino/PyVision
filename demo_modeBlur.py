import argparse
import cv2
from image import modeBlur

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to the input image")
args = vars(ap.parse_args())

# load the input image
image = cv2.imread(args["image"])

out = modeBlur(image, 3)
cv2.imwrite("Source", image)
cv2.imshow("Mode Blur", out)
cv2.waitKey(0)