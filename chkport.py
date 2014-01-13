#!/usr/bin/python
#_*_ coding: utf-8 _*_
import socket
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-a","--address",dest='address',default='127.0.0.1',help='address')
parser.add_option("-p","--port",dest='port',type=int,default=22,help='port')
(options,args) = parser.parse_args()
#print options.address,options.port
def chkport(address,port):
        sock = socket.socket()
        try:
                sock.connect((address,port))
                print "connected"
        except socket.error,e:
                print "can not conect"
chkport(options.address,options.port)
