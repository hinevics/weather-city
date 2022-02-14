from flask import render_template, request, url_for, redirect, flash

from src import server
from src.weather_core import get_graph_weather_changes_city
from src.config import SECRET_KEY

server.secret_key = SECRET_KEY


@server.route('/')
def start():
    return render_template('index.html')


@server.route('/weather_api', methods=['GET', "POST"])
def render_api():
    if request.method == "GET":
        return render_template('weather_api.html')
    if request.method == "POST":
        city = request.form['city']
        sdate = request.form['start_date']
        edate = request.form['end_date']
        print('\n\n')
        if not (city and sdate and edate):
            flash('You were successfully logged in')
            return redirect('/weather_api')
        else:
            graphJSON = get_graph_weather_changes_city(city=city, sdata=sdate, edata=edate)
            return render_template('weather_api.html', graphJSON=graphJSON)


@server.route('/parser', methods=['GET'])
def render_parser():
    # return render_template('parser.html', plot=bar)
    return render_template('weather_parser.html')


@server.route('/weather_database', methods=['GET'])
def render_database():
    return 'Hello'
