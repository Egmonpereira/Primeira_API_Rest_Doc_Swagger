from flask import Flask
from src.server.instance import server
from src.controllers.books import *

import os
'''
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello " + "está " + "funcionando"
'''
#os.system('clear')
server.run() 