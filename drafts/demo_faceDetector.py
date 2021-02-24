# Face detector with dlib's HOG detector
import numpy as np
import argparse
import imutils
import dlib
import cv2
from pyvision.video import WebcamStream
from pyvision.image import rect2xywh
from pyvision.image import shape2np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True, help="path to facial landmark predictor")
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# start a threaded video stream
stream = WebcamStream(src=0).start()

while True:
    frame = stream.read()
    frame = imutils.resize(frame, width=800)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # face detector
    rects = detector(gray,0)

    # for each face found
    #for (i, rect) in enumerate(rects):
    for rect in rects:
        # bounding box of the face
        x,y,w,h = rect2xywh(rect)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        # facial landmarks
        shape = predictor(gray, rect)
        shape = shape2np(shape)

        # draw coordinates
        for (x,y) in shape:
            cv2.circle(frame, (x,y), 2, (0,0,255), -1)
        
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

stream.stop()
cv2.destroyAllWindows()
