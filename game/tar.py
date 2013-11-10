__author__ = 'Administrator'
import os
import tarfile
import socket
import sys
tar_dir = ''
dis_dir = ''
#def get_workspace_files():
TAR_PATH = 'c:\\test\\hongten.tar'
tarfile.open(TAR_PATH,'w')
path = os.path.split(TAR_PATH)[0]
print path
result = socket.getaddrinfo('www.baidu.com',None,0,socket.SOCK_STREAM)
counter = 0
for item in result:
    print "% -3d: %s" % (counter,item[4])
    counter += 1
os.mkdir(os.path.join('E://','a.txt'))
path =
print os.listdir('E://')






