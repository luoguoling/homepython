#!/usr/bin/python
import time
import thread
def t1(name,x,l):
	for i in range(x):
		print i,name
		time.sleep(1)
	l.release()
lock = thread.allocate_lock()
lock.acquire()
print lock.locked()
thread.start_new_thread(t1,('grap',3,lock))
thread.start_new_thread(t1,('voice',3,lock))
while lock.locked():
	pass
#time.sleep(1)

#t1('voice',3)
#t1('grap',3)

