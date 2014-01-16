__author__ = 'Administrator'
import time2
import thread
def print_time(threadname,delay):

    count = 0
    while count < 6:
        time2.sleep(delay)
        count += 1
        print '%s is %s' % (threadname,time2.ctime(time2.time2()))
try:
    thread.start_new(print_time,('thread1',3))
    thread.start_new(print_time,('thread2',4))
except:
    print "error"
while True:
    pass