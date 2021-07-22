from flask import request
from flask_socketio import SocketIO
from .globals import flask_app
from .enums import Sender


socketio = SocketIO(flask_app, cors_allowed_origins='*')


@socketio.on('send_message')
def send_message_handler(message: str):
    """Receive the sent messages

    Arguments:
        message {str}
    """
    socketio.emit('receive_message', {
        'sender': Sender.OTHERS.value,
        'message': f'Server: {message}',
    }, to=request.sid)
