"""
to-do
1. добавить console output
1. нужно сделать функцию выгруски файл для histori
2. нужно сделать вывод полных данных (гялнуть какие есть ключи в json)
3. придумать как все это сделать черех классы в мерии !!!!!
    3.1 Если это будет класс, то будет реализована возможность получить доступк к каждому отдельному признаку query
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
DEFAULT_API_KEY = input('Enter the access key: ')
DEFAULT_API_WEATHER_HISTORY = r'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={api_key}'

class WeatherJSON:
    pass


class ParameterErrors(BaseException):
    # How does it work?
    pass


def open_file(filepath: str):
    with open(file=filepath, mode='r', encoding='utf-8') as file:
        return file.read()

def mean(town: str, strng: str):
    # функции для подсчета срежней велечины осадков и температуры
    pass


def variance(town: str, strng: str):
    pass


def geocoding_api(city: str, api_key: str):
    """
    return lat, lon, country
    """
    str_request = DEFAULT_API_CITY.format(city_name=city, api_key=api_key)
    requests_result = requests.get(url=str_request)
    return requests_result.json()[0]['lat'], requests_result.json()[0]['lon'], requests_result.json()[0]['country']


def weather_api(lat: str, lon: str, part: str, api_key: str):
    str_request = DEFAULT_API_WEATHER.format(lat=lat, lon=lon, part=part, api_key=api_key)
    return requests.get(url=str_request).json()


def history_api(lat: str, lon: str, time: str, api_key: str):
    str_request = DEFAULT_API_WEATHER_HISTORY.format(lat=lat, lon=lon, api_key=api_key, time=time)
    return requests.get(url=str_request).json()


def recoding_time(time: float):
    return datetime.datetime.fromtimestamp(time)


def encode_time(city_name, api_key):
    # posix = datetime.datetime.fromisoformat(time)
    # print(posix)
    # res = datetime.datetime.fromtimestamp(posix)
    # print(res)
    # # return datetime.datetime.utcoffset(posix)
    str_request = DEFAULT_API_CITY.format(city_name=city_name, api_key=api_key)
    requests_result = requests.get(url=str_request)
    print(requests_result)
    
def currentoutput(city: str, country: str, query_result: dict):
    weather = query_result['current']['weather'][0]['main']
    print('{city}, {country}\nweather: {weather}\ntemp: {temp}\nrain, mm: {rain}'.format(
        city=city, country=country, weather=query_result['current']['weather'][0]['main'],
        temp=query_result['current'].setdefault('temp', '0'),
        rain=query_result['current'].setdefault('rain','0')
                        )
        )


def minutelyoutput(query_result: dict, city: str, country: str):
    print('\n{city}, {country}\n'.format(city=city, country=country))
    for minutely in query_result['minutely']:
        print('\tdatetim: {dt}\nprecipitation:{precipitation}, mm'.format(dt=recoding_time(float(minutely['dt'])),
        precipitation=minutely['precipitation']))


def hourlyoutput(query_result: dict, city: str, country: str):
    print('\n{city}, {country}\n'.format(city=city, country=country))
    for hourly in query_result['hourly']:
        print('datetime: {dt}'.format(dt=recoding_time(float(hourly['dt']))))
        print('Temperature: {temperature}, Celsius'.format(temperature=hourly['temp']))
        print(
            'Temperature. This accounts for the human perception of weather: {feels_like}, Celsius'.format(
                feels_like=hourly['feels_like'])
                )
        print('Atmospheric pressure on the sea level: {pressure}, hPa'.format(pressure=hourly['pressure']))
        print('Atmospheric temperature: {dew_point}'.format(dew_point=hourly['dew_point']))
        print('Humidity: {humidity}, %'.format(humidity=hourly['humidity']))
        print('clouds: {clouds}'.format(clouds=hourly['clouds']))
        print('wind_speed: {wind_speed}'.format(wind_speed=hourly['wind_speed']))
        print('probability of precipitation: {pop}'.format(pop=hourly['pop']))
        print('Group of weather parameters: {weather}'.format(weather=hourly['weather']))
        print('Rain volume for last hour: {rain}, mm'.format(rain=hourly['rain'].setdefault('1h', 0) if 'rain' in hourly else 0))
        print('Snow volume for last hour: {snow}, mm'.format(snow=hourly['snow'].setdefault('1h', 0) if 'snow' in hourly else 0))
        print('Group of weather parameters: {main}'.format(main=hourly['weather']['main']))
        print('------------------------------------------------------------------------------------------------------------')


def dailyoutput(query_result: dict, city: str, country: str):
    print('\n{city}, {country}\n'.format(city=city, country=country))
    for daily in query_result['daily']:
        print('Time of the forecasted data: {dt}'.format(dt=recoding_time(daily['dt'])))
        print('Sunrise time: {sunrise}'.format(sunrise=recoding_time(daily['sunrise'])))
        print('The time of when the moon rises for this day: {moonrise}'.format(moonrise=recoding_time(daily['moonrise'])))
        print('The time of when the moon sets for this day: {moonset}'.format(moonset=recoding_time(daily['moonset']) if daily['moonset'] != 0 else 0))
        print('moon_phase: {moon_phase}'.format(moon_phase=daily['moon_phase']))
        print('Temperature:')
        print('\tMorning temperature: {morn}'.format(morn=daily['temp']['morn']))
        print('\tDay temperature: {day}'.format(day=daily['temp']['day']))
        print('\t Evening temperature: {eve}'.format(eve=daily['temp']['eve']))
        print('\tNight temperature: {night}'.format(night=daily['temp']['night']))
        print('\tMin daily temperature: {min}'.format(min=daily['temp']['min']))
        print('\tMax daily temperature: {max}'.format(max=daily['temp']['max']))
        print('Atmospheric pressure on the sea level: {pressure}, hPa'.format(pressure=daily['pressure']))
        print('Humidity: {humidity}, %'.format(humidity=daily['humidity']))
        print('Wind speed: {wind_speed}'.format(wind_speed=daily['wind_speed']))
        print('Wind gust: {wind_gust}'.format(wind_gust=daily['wind_gust'] if 'wind_gust' in daily else 0))
        print('Wind direction, degrees: {wind_deg}'.format(wind_deg=daily['wind_deg']))
        print('Cloudiness: {clouds} %'.format(clouds=daily['clouds']))
        print('Probability of precipitation: {pop}'.format(pop=daily['pop']))
        print('Precipitation volume: {rain} mm'.format(rain=daily['rain'] if 'rain' in daily else 0))
        print('Snow volume: {snow} mm'.format(snow=daily['snow'] if 'snow' in daily else 0))
        print('Weather:')
        print('\tGroup of weather parameters: {main}'.format(main=daily['weather'][0]['main']))
        print('------------------------------------------------------------------------------------------------------------')


def historioutput():
    pass


def processing_current(arguments):
    city = arguments.city
    api_key = arguments.apikey
    
    lat, lon, country = geocoding_api(city=city, api_key=api_key)
    
    part = ','.join([i for i in ['minutely', 'hourly', 'daily', 'current'] if not (i in (
            lambda x: x.split(',') if ',' in x else x)('current'))])
    
    query_result = weather_api(lat=lat, lon=lon, part=part, api_key=api_key)
    currentoutput(city=city, country=country, query_result=query_result)


def processing_forecast(arguments):
    city = arguments.city
    api_key = arguments.apikey
    parameter = arguments.parameter

    lat, lon, country = geocoding_api(city=city, api_key=api_key)
    part = ','.join([i for i in ['minutely', 'hourly', 'daily', 'current'] if not (i in (
        lambda x: x.split(',') if ',' in x else x)(parameter))])
    
    query_result = weather_api(lat=lat, lon=lon, part=part, api_key=api_key)  # return dict from api query
    if parameter == 'minutely':
        minutelyoutput(query_result=query_result, city=city, country=country)
    elif parameter == 'hourly':
        hourlyoutput(query_result=query_result, city=city, country=country)
    elif parameter == 'daily':
        dailyoutput(query_result=query_result, city=city, country=country)
    else:
        raise ParameterErrors


def processing_history(arguments):
    time = arguments.time
    encode_time(city_name=DEFAULT_CITY, api_key=DEFAULT_API_KEY)


def set_parser(parser: argparse.ArgumentParser):
    subparser = parser.add_subparsers(help="The One Call API provides the following weather data for any geographical coordinates:" +
                         "Current weather" +
                         "Forecast: Minute forecast for 1 hour, Hourly forecast for 48 hours, Daily forecast for 7 days" +
                         "Historical weather data for the previous 5 days"
                         )
    
    # CLI parser
    output = subparser.add_parser('output', help='outputting information to the console')
    save = subparser.add_parser('save', help='save to file')
    app = subparser.add_parser('app', help='application launch')

    # output
    suboutput = output.add_subparsers(help='!!!!')
    
    # suboutput
    current = suboutput.add_parser('current', help='Current weather')
    forecast = suboutput.add_parser(
        'forecast',
        help='Forecast weather: minute forecast for 1 hour, hourly forecast for 48 hours, daily forecast for 7 days')
    history = suboutput.add_parser('history', help='Historical weather data for the previous 5 days')
    
    # current
    current.add_argument('-c', '--city', help='City for which weather information is collected', type=str, default=DEFAULT_CITY)
    current.add_argument('-k', '--apikey', help='API key', default=DEFAULT_API_KEY)
    current.set_defaults(callback=processing_current)
    
    # forecast
    forecast.add_argument('-p', '--parameter', help='Parameter specifying the type of information returned.'
                        + 'Available values: minutely, hourly, daily', default='minutely')
    forecast.add_argument('-c', '--city', help='City for which weather information is collected', type=str, default=DEFAULT_CITY)
    forecast.add_argument('-k', '--apikey', help='API key', default=DEFAULT_API_KEY)
    forecast.set_defaults(callback=processing_forecast)
    
    # history
    history.add_argument(
        '-t',
        '--time',
        help='Date from the previous five days (Unix time, UTC time zone), e.g. dt=2021-06-10',
        default='...')
    history.set_defaults(callback=processing_history)
    # output.add_argument('-p', '--parameter', help='Parameter specifying the type of information returned.'
                        # + 'Available values: current, minutely, hourly, daily', default='current')
    # output.add_argument('-h', '--history', help='Data for the past 5 days')
    # output.add_argument('-c', '--city', help='City for which weather information is collected', type=str, default=DEFAULT_CITY)
    # output.add_argument('-k', '--apikey', help='API key', default=DEFAULT_API_KEY)

    # output.set_defaults(callback=processing_output)

    # current.add_argument('-o', '--output', help='outputting information to the console', action='store_true', default=False)
    # current.add_argument('-s', '--save', help='Save to file', action='store_true')
    # current.add_argument('-a', '--app', help='Application launch', action='store_true')
    # current.add_argument(
    #     '-c', '--city',
    #     help='City for which weather information is collected',
    #     type=str,
    #     default=DEFAULT_CITY
    #     )
    # current.set_defaults(callback=processing_current)
# current.add_argument(
    #     '-e', '--exclude',
    #     help="By using this parameter you can exclude some parts of the weather data from the API response."
    #     "It should be a comma-delimited list (without spaces). Available values:current,minutely,hourly,daily,alerts.",
    #     default='current'
    # )
    

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