from flask import Flask
from flask_cors import CORS
from aiml import Kernel 
from aiml_bot import __path__ as module_base_path
from os.path import join

flask_app = Flask(__name__, static_folder='react_app/build/static', template_folder='react_app/build')
CORS(flask_app)

aiml_kernel = Kernel()
aiml_kernel.learn(join(module_base_path[0], './database.xml'))
