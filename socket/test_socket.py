__author__ ='Shakib Limon'
__version__ = '1.0.0'

import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connection established')

@sio.on('my message')
def on_message(data):
    print('message received with ', data)
    sio.emit('my message', {'foo': 'bar'})

@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')
sio.wait()