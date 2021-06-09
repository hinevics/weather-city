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


def recoding_time(time: float):
    return datetime.datetime.fromtimestamp(time)

def weathernow_request(city: str, lat: str, lon: str, country: str, exclude: str, api_key: str, part:str):
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


def forecast_request(lat:str, lon:str, country:str, exclude:str, api_key:str, city:str, part:str):
    str_request = DEFAULT_API_WEATHER.format(lat=lat, lon=lon, part=part, api_key=api_key)
    requests_result = requests.get(url=str_request).json()
    if exclude == 'minutely':
        for minutely in requests_result['minutely']:
            print('\tdatetim: {dt}\nprecipitation:{precipitation}, mm'.format(dt=recoding_time(float(minutely['dt'])),
            precipitation=minutely['precipitation']))
    elif exclude == 'hourly':
        for hourly in requests_result['hourly']:
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
    elif exclude == 'daily':
        for daily in requests_result['daily']:
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


def histori_request():
    pass


def processing_output(arguments):
    city = arguments.city
    api_key = arguments.apikey
    lat, lon, country = geocoding_api(city=city, api_key=api_key)
    exclude = arguments.exclude  # Сюда передают же занчения которые удлаить, те унжно конвертировать аргумент. 
                                 # У меня exclude является тем, что останется в выводе
    part = ','.join([i for i in ['minutely', 'hourly', 'daily', 'current'] if not (i in (
        lambda x: x.split(',') if ',' in x else x)(exclude))])
    if exclude == 'current':
        weathernow_request(city=city, lat=lat, lon=lon, country=country, exclude=exclude, part=part, api_key=api_key)
    elif exclude == 'minutely':
        forecast_request(lat=lat, lon=lon, country=country, exclude=exclude, api_key=api_key, city=city, part=part)


def set_parser(parser: argparse.ArgumentParser):
    subparser = parser.add_subparsers(help='choose command to run')
    
    # CLI parser
    output = subparser.add_parser('output', help='Outputting information to the console')
# create subparser
    # субпарсеры использовать для режимов работы: 1 вывод информации в консоль, 2 выгрузка данных в приложение 3. выгрузка данных в файл
    # Сами аргументы можно сгрупировать 



    # create arguments for weathernow
    output.add_argument(
        '-c', '--city',
        help='City for which weather information is collected',
        type=str,
        default=DEFAULT_CITY)
    output.add_argument(
        '-e', '--exclude',
        help="By using this parameter you can exclude some parts of the weather data from the API response."
        "It should be a comma-delimited list (without spaces). Available values:current,minutely,hourly,daily,alerts.",
        default='minutely,hourly,daily'
    )
    output.add_argument(
        '-k', '--apikey',
        help='This is the access key to the web resource api',
        type=str,
        default=DEFAULT_API_KEY)
    output.set_defaults(callback=processing_output)


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