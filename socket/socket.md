## Socket programming using Python
Socket programming is a way of connecting two nodes on a network to communicate with each other.
Socket programming is started by importing the socket library and making a simple socket.
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
*_AF_INET_* refers to the address family ipv4.<br>
*_SOCK_STREAM_* means connection oriented TCP protocol. 

