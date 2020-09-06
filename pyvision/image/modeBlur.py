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
                roi = img[j-pad:j+pad+1, i-pad:i+pad+1, k]
                val = stats.mode(roi, axis=None)
                output[j-pad, i-pad, k] = val[0][0]
    return output
