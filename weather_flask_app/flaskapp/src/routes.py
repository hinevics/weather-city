from flask import render_template

from src import server
from src.weather_core import get_graph_weather_changes_day

@server.route('/')
def start():
    return render_template('index.html')


@server.route('/weather_api', methods=['GET'])
def render_api():
    bar = get_graph_weather_changes_day()
    return render_template('weather_api.html', plot=bar)


@server.route('/parser', methods=['GET'])
def render_parser():
    # return render_template('parser.html', plot=bar)
    return render_template('weather_parser.html')

@server.route('/weather_database', methods=['GET'])
def render_database():
    return 'Hello'
