"""
to-do
1. нужно сделать функцию выгруски для histori
2. нужно сделать вывод полных данных (гялнуть какие есть ключи в json)
3. придумать как все это сделать черех классы в мерии !!!!!
"""
# I am using api openweathermap.org
import argparse
import requests
import json
from re import sub
import datetime


DEFAULT_CITY = r'London'
DEFAULT_API_WEATHER = r'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude={part}&appid={api_key}'
DEFAULT_API_CITY = r'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'
DEFAULT_API_KEY = r'8cd65e1b7f292a69366f2a526046a32c'

def open_file(filepath: str):
    with open(file=filepath, mode='r', encoding='utf-8') as file:
        return file.read()

def mean(town: str, strng: str):
    # функции для подсчета срежней велечины осадков и температуры
    pass


def variance(town: str, strng: str):
    pass


def weathernow_request_min(city: str, lat: str, lon: str, country: str, exclude: str, api_key: str, part:str):
    print('...start search city...')
    str_request = DEFAULT_API_WEATHER.format(lat=lat, lon=lon, part=part, api_key=api_key)
    print('...loading weather in {city}...'.format(city=city))
    requests_result = requests.get(url=str_request).json()
    weather = requests_result[exclude]['weather'][0]['main']
    print('\n')
    print('{city}, {country}\nweather: {weather}\ntemp: {temp}\nrain, mm: {rain}'.format(
        city=city, country=country, weather=requests_result[exclude]['weather'][0]['main'],
        temp=requests_result[exclude].setdefault('temp', '0'),
        rain=requests_result[exclude].setdefault('rain','0')
                        )
        )


def weathernow_request_full(city: str, lat: str, lon: str, country: str, exclude: str, api_key: str):
    # тут нужно расписать аждый отдеьный признак, который доступен в json
    pass


def forecast_request_full():
    pass


def recoding_time(time: float):
    return datetime.datetime.fromtimestamp(time)


def forecast_request_min(lat:str, lon:str, country:str, exclude:str, api_key:str, city:str, part:str):
    str_request = DEFAULT_API_WEATHER.format(lat=lat, lon=lon, part=part, api_key=api_key)
    requests_result = requests.get(url=str_request).json()
    if exclude == 'minutely':
        for minutely in requests_result['minutely']:
            print('datetim:\t{datetime}\nprecipitation:\t{precipitation}, mm'.format(datetime=recoding_time(float(minutely['dt'])),
            precipitation=minutely['precipitation']))
            


def histori_request():
    pass


def geocoding_api(city: str, api_key: str):
    """
    return lat, lon, country
    """
    str_request = DEFAULT_API_CITY.format(city_name=city, api_key=api_key)
    requests_result = requests.get(url=str_request)
    return requests_result.json()[0]['lat'], requests_result.json()[0]['lon'], requests_result.json()[0]['country']


def processing_weathernow(arguments):
    city = arguments.city
    api_key = arguments.apikey
    lat, lon, country = geocoding_api(city=city, api_key=api_key)
    weather_request = weathernow_request_full if arguments.full else weathernow_request_min
    weather_request(lat=lat, lon=lon, country=country, exclude='current', api_key=api_key, city=city, part='minutely,hourly,daily')


def processing_forecast(arguments):
    city = arguments.city
    api_key = arguments.apikey
    lat, lon, country = geocoding_api(city=city, api_key=api_key)
    exclude = arguments.exclude  # Сюда передают же занчения которые удлаить, те унжно конвертировать аргумент. 
                                 # У меня exclude является тем, что останется в выводе
    part = ','.join([i for i in ['minutely', 'hourly', 'daily', 'current'] if not (i in (
        lambda x: x.split(',') if ',' in x else x)(exclude))])
    weather_request = forecast_request_full if arguments.full else forecast_request_min
    weather_request(lat=lat, lon=lon, country=country, exclude=exclude, api_key=api_key, city=city, part=part)


def processing_histori(arguments):
    pass


def set_parser(parser: argparse.ArgumentParser):
    subparser = parser.add_subparsers(help='choose command ro run')
    # create subparser 
    weathernow_parser = subparser.add_parser(
        'weathernow', help='The weather is now')
    forecast_parser = subparser.add_parser(
        'forecast', help='This real weather forecast and day weather forecast for a minute, hour')
    histori_parser = subparser.add_parser(
        'histori', help='Historical weather data. Prediction weather from my ML algorithms')

    # create arguments for weathernow
    weathernow_parser.add_argument(
        '-c', '--city',
        help='City for which weather information is collected',
        type=str,
        default=DEFAULT_CITY)
    weathernow_parser.add_argument(
        '-f', '--full',
        help='Flag for displaying complete data',
        default=False,
    )
    weathernow_parser.add_argument(
        '-k', '--apikey',
        help='This is the access key to the web resource api',
        type=str,
        default=DEFAULT_API_KEY)
    weathernow_parser.set_defaults(callback=processing_weathernow)

    # create arguments for forecast
    forecast_parser.add_argument('-c', '--city',
        help='City for which weather information is collected',
        type=str,
        default=DEFAULT_CITY)
    forecast_parser.add_argument(
        '-f', '--full',
        help='Flag for displaying complete data',
        default=None,)
    forecast_parser.add_argument(
        '-e', '--exclude',
        help="By using this parameter you can exclude some parts of the weather data from the API response."
        "It should be a comma-delimited list (without spaces). Available values:current,minutely,hourly,daily,alerts.",
        default='minutely,hourly,daily'
    )
    forecast_parser.add_argument(
        '-k', '--apikey',
        help='This is the access key to the web resource api',
        type=str,
        default=DEFAULT_API_KEY)
    forecast_parser.set_defaults(callback=processing_forecast)

    # create arguments for histori
    histori_parser.add_argument(
        '-c', '--city',
        help='City for which weather information is collected',
        type=str,
        default=DEFAULT_CITY)
    histori_parser.add_argument(
        '-k', '--apikey',
        help='This is the access key to the web resource api',
        type=str,
        default=DEFAULT_API_KEY)
    histori_parser.set_defaults(callback=processing_histori)


def main():
    parser = argparse.ArgumentParser(
        description='This is a CLI application for getting weather data through the api of the climate data storage service',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    set_parser(parser)
    args = parser.parse_args()
    args.callback(args)  # callback for branches


if __name__ == '__main__':
    main()