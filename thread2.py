__author__ = 'Administrator'
import time
import threading
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):

        print "starting" + self.name
        #Get lock to synchronize threads
        threadLock.acquire()
        a = time.time()
        print_time(self.name,self.counter,5)
        threadLock.release()
        print time.time() - a
def print_time(threadname,delay,counter):
    a = time.time()

#    counter = 0
    while counter:
#        if exitFlag:
#            threading.thread.exit()
        time.sleep(delay)
        print '%s is %s' % (threadname,time.ctime(time.time()))
#        print time.time() - a
        counter -= 1
#create new threads
threadLock = threading.Lock()
threads = []
thread1 = myThread(1,"thread1",6)
thread2 = myThread(1,"thread2",6)
thread3 = myThread(1,"thread3",6)
#start new threads
thread1.start()
thread2.start()
thread3.start()
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
print threads
for t in threads:
    t.join()
print "exit main thread"



