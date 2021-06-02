# I am using api openweathermap.org
import argparse
import requests
import json
from re import sub

DEFAULT_CITY = r'London'
DEFAULT_API_WEATHER = r'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude={part}&appid={api_key}'
DEFAULT_API_CITY = r'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'


def open_file(filepath: str):
    with open(file=filepath, mode='r', encoding='utf-8') as file:
        return file.read()

def mean(town: str, strng: str):
    pass


def variance(town: str, strng: str):
    pass


def weather_request(city: str, lat: str, lon: str, country: str, exclude: str, api_key: str):
    # minutely,hourly,daily,alerts
    str_request = DEFAULT_API_WEATHER.format(lat=lat, lon=lon, part=exclude, api_key=api_key)
    requests_result = requests.get(url=str_request).json()
    # with open(file='r.json', mode='w', encoding='utf-8') as file:
    #     json.dump(requests_result, file)

    weather = requests_result['current']['weather'][0]['main']
    print('{city}, {country}\nweather: {weather}\ntemp: {temp}\nrain, mm: {rain}'.format(
        city=city, country=country, weather=requests_result['current']['weather'][0]['main'],
        temp=requests_result['current'].setdefault('temp', '0'),
        rain=requests_result['current'].setdefault('rain','0')
                        )
        )


def geocoding_api(city: str, api_key: str):
    """
    return lat, lon, country
    """
    str_request = DEFAULT_API_CITY.format(city_name=city, api_key=api_key)
    requests_result = requests.get(url=str_request)
    return requests_result.json()[0]['lat'], requests_result.json()[0]['lon'], requests_result.json()[0]['country']


def processing(arguments):
    city = arguments.city
    api_key = arguments.apikey
    exclude = arguments.exclude
    lat, lon, country = geocoding_api(city=city, api_key=api_key)
    weather_request(lat=lat, lon=lon, country=country, exclude=exclude, api_key=api_key, city=city)

def set_parser(parser: argparse.ArgumentParser):
    # api key
    parser.add_argument(
        '-k', '--apikey',
        help='This is the access key to the web resource api',
        type=str)

    parser.add_argument(
        '-c', '--city',
        help='City for which weather information is collected',
        type=str,
        default=DEFAULT_CITY)

    parser.add_argument(
        '-e', '--exclude',
        help="By using this parameter you can exclude some parts of the weather data from the API response."
        "It should be a comma-delimited list (without spaces). Available values:current,minutely,hourly,daily,alerts.",
        default='minutely,hourly,daily,alerts'
    )

    parser.set_defaults(callback=processing)


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