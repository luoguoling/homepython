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

#参数的一般使用
#/usr/bin/python
import optparse
from optparse import OptionParser
def parse_args():
	usage = """ more arguments must be given"""
#	parser = optparse.OptionParser(usage)
	parser = OptionParser(usage)
	help = "the port to listen"
	parser.add_option('--port',dest='address',type='int',help=help)
	help = "the ip address"
	parser.add_option('--ip',dest='ip',default='localhost',help=help)
	(options,args) = parser.parse_args()
#	ip = args[0]
#	port = args[1]
	return options
	#if len(args) != 1:
#		parser.error('you must offer 1 argument')
def ta():
	options = parse_args()
	print options.ip,options.address
ta()
