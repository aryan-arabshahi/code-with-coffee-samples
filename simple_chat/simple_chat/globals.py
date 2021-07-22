from flask import Flask
from flask_cors import CORS


flask_app = Flask(__name__, static_folder='react_app/build/static', template_folder='react_app/build')
CORS(flask_app)
