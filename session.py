import time

class Session:
    def __init__(self, minutes=0):
        if (minutes == 0):
            self.__start_time = time.localtime() #get the time
            self.__end_time=0
        else:
            self.__end_time = time.localtime()
            seconds = minutes * 60
            start_seconds = time.mktime(self.__end_time) - seconds
            self.__start_time = time.localtime(start_seconds)

    def __str__(self):
        if (self.__end_time == 0):
            return "session start: {}".format(self.__start_time)
        else:
            return "session start: {} session end: {} session duration: {}".format(
            self.__start_time, self.__end_time, get_duration())

    def get_duration(self):
        return time.mktime(self.__end_time) - time.mktime(self.__start_time)

    def end_session(self):
        self.__end_time = time.localtime() #get the time
