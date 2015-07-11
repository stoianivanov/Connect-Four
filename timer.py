import datetime
import time


class Timer:
    def __init__(self):
        self.current_time = 0
        self.start_time = 0

    def start(self):
        self.start_time = datetime.datetime.now()
        self.start_time = time.mktime(self.start_time.timetuple())

    def sleep(self):
        _time = datetime.datetime.now()
        _time = time.mktime(_time.timetuple())
        self.current_time = self.current_time + _time - self.start_time

    def stop(self):
        return self.current_time
