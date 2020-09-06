from threading import Thread
import cv2

class WebcamStream:
    def __init__(self, src=0, apiPreference=cv2.CAP_DSHOW):
        # initialize video stream and read the first frame
        self.stream = cv2.VideoCapture(src, apiPreference)
        (self.grabbed, self.frame) = self.stream.read()

        # indicate if the thread should be stopped
        self.stopped = False
    
    def start(self):
        # this starts an actual thread
        Thread(target=self.update, args=()).start()
        return self
    
    def update(self):
        # keep looking infinitely until the thread is stopped
        while True:
            if self.stopped == True: return
            (self.grabbed, self.frame) = self.stream.read()
    
    def read(self):
        # most recently frame read
        return self.frame
    
    def stop(self):
        self.stopped = True