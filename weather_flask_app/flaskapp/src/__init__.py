from flask import Flask

server = Flask(__name__)

from src import routes, config

server.run()
