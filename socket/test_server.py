__author__ ='Shakib Limon'
__version__ = '1.0.0'

# import eventlet
# import socketio
#
# sio = socketio.Server()
# app = socketio.WSGIApp(sio,static_files={
#     '/':{'content_type': 'text/html', 'filename':'index.html'}
# })
#
# @sio.on('connect')
# def connect(sid, environ):
#     print('connect', sid)
#
# @sio.on('my message')
# def message(sid, data):
#     print('message', data)
#
# @sio.on('disconnect')
# def disconnet(sid):
#     print('disconnect',sid)
#
# if __name__ == '__main__':
#     eventlet.wsgi.server(eventlet.listen(('',5000)),app)

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# @sio.on('connect', namespace='/chat')
# def connect(sid, environ):
#     print("connect ", sid)
#
# @sio.on('chat message', namespace='/chat')
# async def message(sid, data):
#     print("message ", data)
#     await sio.emit('reply', room=sid)
#
# @sio.on('disconnect', namespace='/chat')
# def disconnect(sid):
#     print('disconnect ', sid)
@sio.on('message')
async def print_message(sid, message):
    # When we receive a new event of type
    # 'message' through a socket.io connection
    # we print the socket ID and the message
    print("Socket ID: " , sid)
    print(message)
    await sio.emit('message', message[::-1])


# app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)