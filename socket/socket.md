## Socket programming using Python
Socket programming is a way of connecting two nodes on a network to communicate with each other.
Socket programming is started by importing the socket library and making a simple socket.
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
*_AF_INET_* refers to the address family ipv4.<br>
*_SOCK_STREAM_* means connection oriented TCP protocol.

#### Conneting to server
**Using Ip Address**

Let's check ip address first
```shell
$ping www.google.com
```
Also can find the ip using python:
```python
ip = socket.gethostbyname('www.=google.com')
print('ip address is :', ip)
```
> ip address is : 74.125.24.105

**Now connecting to google server**
```python

```




