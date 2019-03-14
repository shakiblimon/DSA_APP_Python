__version__ ="1.0.0"
__author__ ="Shakib Limon"

import socket
#Decalre a socket variable
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind('localhost',80000)
# s.listen(1)
# conn = addr = s.accept()
# while 1:
#     data = conn.recv(1024)
#     if not  data:
#         break
#     conn.sendall(data)
# conn.close()
#ip = socket.gethostbyaddr(host='wwww.python.org')
host = socket.getfqdn('www.google.com')
#print(ip)
print(host)