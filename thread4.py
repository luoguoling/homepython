__author__ = 'Administrator'
#coding:utf-8
import Queue
import threading
import urllib2
import time
queue = Queue.Queue()
hosts = ["http://www.baidu.com","http://www.google.com.hk","http://www.sina.com","http://www.517na.com"]
class ThreadUrl(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
#            host = self.queue.get()
            graburl(self,queue)
start = time.time()
def main():
    for i in range(2):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
    for host in hosts:
        queue.put(host)
    queue.join()
def graburl(self,queue):
    host = self.queue.get()
#    print host
    url = urllib2.urlopen(host)
    print url.read(1024)
    self.queue.task_done()
main()
print "Elapsed Time:%s" % (time.time() - start)


