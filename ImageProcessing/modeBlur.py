import argparse
import numpy as np
import cv2
from scipy import stats

def modeBlur(img, pad):
    (h,w) = img.shape[:2]
    ch = 1 if img.ndim == 2 else img.shape[2]
    img = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((h,w,ch), dtype="uint8")

    for k in np.arange(ch):
        for j in np.arange(pad, h+pad):
            for i in np.arange(pad, w+pad):
                roi = image[j-pad:j+pad+1, i-pad:i+pad+1, k]
                val = stats.mode(roi, axis=None)
                output[j-pad, i-pad, k] = val[0][0]
    return output

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to the input image")
args = vars(ap.parse_args())

# load the input image
image = cv2.imread(args["image"])

out = modeBlur(image, 5)
print(out.shape)
cv2.imwrite("output.png", out)
cv2.imshow("Mode Blur", out)
cv2.waitKey(0)