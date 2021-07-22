from flask import render_template
from .globals import flask_app
from .socketio import socketio


@flask_app.route('/')
def index():
    return render_template('index.html')


class ChatApp:

    def start(self) -> None:
        """Run the flask app
        """
        socketio.run(
            app=flask_app,
            host='0.0.0.0',
            debug=False,
            port=5000
        )
