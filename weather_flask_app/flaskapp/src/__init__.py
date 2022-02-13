from flask import Flask

server = Flask(__name__)

from src import routes, weather_core, getting_weather_data

server.run()
