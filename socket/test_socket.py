import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('conneted')

@sio.on('my message')
def on_message(data):
    print('message received with ', data)
    sio.emit('my resonse',{'response': 'my reseponse'})

@sio.on('disconnect')
def on_disconnect():
    print()