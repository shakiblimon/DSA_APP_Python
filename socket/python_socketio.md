### Getting Started
#### What is Socket.IO?
Socket.IO is a transport protocol that enables real-time bidirectional event-based communication between clients
(typically, though not always, web browsers) and a server. The official implementations of the client and server 
components are written in JavaScript. This package provides Python implementations of both,
each with standard and asyncio variants.

#### Installation
To install the standard Python client along with its dependencies, use the following command:
```python
pip install "python-socketio[client]"
```
If instead you plan on using the asyncio client, then use this:
```python
pip install "python-socketio[asyncio_client]"
```
#### Creating a Client Instance

To instantiate an Socket.IO client, simply create an instance of the appropriate client class:
```python
import socketio

# standard Python
sio = socketio.Client()

# asyncio
sio = socketio.AsyncClient()
```