#!usr/bin/python

import sys

import BaseHTTPServer

from SimpleHTTPServer import SimpleHTTPRequestHandler

srvr = BaseHTTPServer.HTTPServer
hnd = SimpleHTTPRequestHandler

Protocol = 'HTTP/1.0'

try:
    port = int (sys.argv[1])
except IndexError :
    port = 8000

srvradrs=('127.0.0.1',port)
hnd.protocol_version = Protocol
h = srvr(srvradrs,hnd)
try:
    print('Server started') 
    h.serve_forever()
except KeyboardInterrupt:
    print('server socket closed')
    h.socket.close()
