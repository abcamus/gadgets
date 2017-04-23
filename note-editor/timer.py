#--coding:utf-8 --

import threading
import time

def timer_handler():
    print "hello, timer"
    global timer
    #timer.start()

timer = threading.Timer(0.1, timer_handler)
timer.start()
