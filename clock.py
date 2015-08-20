#!/usr/bin/python

from datetime import datetime


class Clock:

    def __get_time__(self):
        current_time = datetime.now().time()
        hh = str("%02d" % current_time.hour)
        mm = str("%02d" % current_time.minute)
        ss = str("%02d" % current_time.second)

        return (hh + ":" + mm + ":" + ss)



