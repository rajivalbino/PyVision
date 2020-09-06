import datetime as dt

class Fps:
    def __init__(self):
        self._start = None
        self._end = None
        self._numFrames = 0
    
    def start(self):
        self._start = dt.datetime.now()
        return self
    
    def stop(self):
        self._end = dt.datetime.now()
    
    def update(self):
        self._numFrames += 1
    
    def elapsed(self):
        return (self._start - self._end).total_seconds()
    
    # as simple as this
    def fps(self):
        return self._numFrames / self.elapsed()