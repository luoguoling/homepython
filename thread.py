__author__ = 'Administrator'
#from multiprocessing import pool
from multiprocessing.dummy import Pool as ThreadPool
import urllib2,time
pool = ThreadPool(7)
urls = [
    'http://www.google.com.hk',
    'http://www.python.org',
    'http://www.baidu.com',
    'http://www.jd.com'
]
a1 = time.time()
results = pool.map(urllib2.urlopen,urls)
a2 = time.time() -a1
print a2
pool.close()
pool.join()



