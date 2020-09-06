from __future__ import print_function
import cv2
import imutils
import argparse
from pyvision.video import WebcamStream
from pyvision.video import Fps

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=200, help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=1, help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

# grab pointers to the streams
#stream = cv2.VideoCapture(0, cv2.CAP_DSHOW)
stream = WebcamStream(src=0).start()
fps = Fps().start()

while fps._numFrames < args["num_frames"]:
    #_,frame = stream.read()
    frame = stream.read()
    frame = imutils.resize(frame, width=600)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
    
    fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
#stream.release()
stream.stop()
cv2.destroyAllWindows()