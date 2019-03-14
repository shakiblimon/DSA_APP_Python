__version__ ="1.0.0"
__author__ ="Shakib Limon"

import socket
import sys
#Decalre a socket variable

'''
|           Conneting to server
'''
# ip = socket.gethostbyname('www.google.com')
# print('ip address is :', ip)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket successfully created')

except socket.error as err:
    print('socket creation failed with error %s'%(err))

port=56
try:
    host_ip= socket.gethostbyname('www.google.com')
    #host_ip = socket.gethostbyaddr('172.217.194.104')
except socket.gaierror:
    print('there is en error resolving the host')

s.connect(host_ip,port)
print('the socket has successfully connected to google \ on port == %s'% (host_ip))