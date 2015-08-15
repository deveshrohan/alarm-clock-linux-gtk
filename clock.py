#!/usr/bin/python

from datetime import datetime

class clock:

    def __get_time__(self):
        current_time = datetime.now().time()
        hh = str(current_time.hour)
        mm = str(current_time.minute)
        ss = str(current_time.second)

        return (hh+ ":" + mm +":" + ss)



