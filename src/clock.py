import threading
import time

class Clock(threading.Thread):

    def __init__(self, aTimer):
        threading.Thread.__init__(self)
        self.timer = aTimer

    def run(self):
        """Sleeps one second, and then clocks the timer."""
        while(True):
            time.sleep(1)
            self.timer.clock()

