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
import csv
import datetime

DEFAULT_PATH_SAVE_FILE = r'..'
DEFAULT_CITY = r'London'
DEFAULT_API_WEATHER = r'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude={part}&appid={api_key}'
DEFAULT_API_CITY = r'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'
DEFAULT_API_KEY = input('Enter the access key: ')
DEFAULT_API_WEATHER_HISTORY = r'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&lang=ru&dt={time}&appid={api_key}'


# DEFAULT_PARAMETER_DESCRIPTION = {
#     'current': {
#         'dt': 'Current time: {value}',
#         'sunrise': 'Sunrise time: {value}',
#         'sunset': 'Sunset time: {value}',
#         'temp': 'Temperature: {value}, ℃',
#         'feels_like': 'Temperature. This temperature parameter accounts for the human perception of weather: {value}, ℃',
#         'pressure': ' Atmospheric pressure on the sea level: {value}, hPa',
#         'humidity': 'Humidity: {value}, %',
#         'dew_point': 'Atmospheric temperature: {value}, Celsius',
#         'clouds': 'Cloudiness: {value}, %',
#         'uvi': 'Current UV index {value}',
#         'visibility': 'Average visibility: {value}, metres',
#         'wind_speed': 'Wind speed: {value}, metre/sec',
#         'wind_gust': 'Wind gust: {value}, metre/sec',
#         'wind_deg': 'Wind direction: {value}, degrees',
#         ''
#     }
# }


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


def encode_time(time: str):
    return int(datetime.datetime.strptime(time, r'%Y-%m-%d').timestamp())


def currentoutput(city: str, country: str, query_result: dict):
    # weather = query_result['current']['weather'][0]['main']
    print('{city}, {country}\nweather: {weather}\ntemp: {temp}\nrain, mm: {rain}'.format(
        city=city, country=country, weather=query_result['current']['weather'][0]['main'],
        temp=query_result['current'].setdefault('temp', '0'),
        rain=query_result['current'].setdefault('rain', '0')))


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
        print('Rain volume for last hour: {rain}, mm'.format(
            rain=hourly['rain'].setdefault('1h', 0) if 'rain' in hourly else 0))
        print('Snow volume for last hour: {snow}, mm'.format(
            snow=hourly['snow'].setdefault('1h', 0) if 'snow' in hourly else 0))
        print('Group of weather parameters: {main}'.format(main=hourly['weather']['main']))
        print('----------------------------------------------------------------------------------------------------')


def dailyoutput(query_result: dict, city: str, country: str):
    print('\n{city}, {country}\n'.format(city=city, country=country))
    for daily in query_result['daily']:
        print('Time of the forecasted data: {dt}'.format(dt=recoding_time(daily['dt'])))
        print('Sunrise time: {sunrise}'.format(sunrise=recoding_time(daily['sunrise'])))
        print('The time of when the moon rises for this day: {moonrise}'.format(
            moonrise=recoding_time(daily['moonrise'])))
        print('The time of when the moon sets for this day: {moonset}'.format(
            moonset=recoding_time(daily['moonset']) if daily['moonset'] != 0 else 0))
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
        print('----------------------------------------------------------------------------------------------------')


def historioutput(query_result: dict, city: str, country: str):
    print('\n{city}, {country}\n'.format(city=city, country=country))
    print('---Weather at the requested time---')
    print('Requested time: {dt}'.format(dt=recoding_time(query_result['current']['dt'])))
    print('Sunrise time: {sunrise}'.format(sunrise=recoding_time(query_result['current']['sunrise'])))
    print('Sunset time: {sunset}'.format(sunset=recoding_time(query_result['current']['sunset'])))
    print('Temperature: {temp}'.format(temp=query_result['current']['temp']))
    print('Temperature.' +
          '\nThis accounts for the human perception of weather.: {feels_like}'.format(
              feels_like=query_result['current']['feels_like']))
    print('Atmospheric pressure on the sea level: {pressure}, hPa'.format(pressure=query_result['current']['pressure']))
    print('Humidity: {humidity}, %'.format(humidity=query_result['current']['humidity']))
    print('Atmospheric temperature' +
          'below which water droplets begin to condense and dew can form. : {dew_point}, %'.format(
              dew_point=query_result['current']['dew_point']))
    print('Cloudiness: {clouds}, %'.format(clouds=query_result['current']['clouds']))
    print('Midday UV index: {uvi}, %'.format(uvi=query_result['current']['uvi']))
    print('Average visibility: {visibility}, metres'.format(visibility=query_result['current']['visibility']))
    print('Wind speed: {wind_speed}, metres'.format(wind_speed=query_result['current']['wind_speed']))
    print('Wind gust: {wind_gust}, metre/sec'.format(wind_gust=query_result['current']['wind_gust']
                                                     if 'wind_gust' in query_result['current'] else 0))
    print('Wind direction: {wind_deg}, degrees: '.format(wind_deg=query_result['current']['wind_deg']))
    print('Precipitation volume: {rain}, mm: '.format(rain=query_result['current']['rain']
                                                      if 'rain' in query_result['current'] else 0))
    print('Snow volume: {snow}, mm: '.format(snow=query_result['current']['snow']
                                             if 'snow' in query_result['current'] else 0))
    print('\nWeather')
    for weather in query_result['current']['weather']:
        print('Group of weather parameters: {main}'.format(main=weather['main']))
        print('Weather condition within the group: {description}'.format(description=weather['description']))
    print('\n')
    print(
        '---Data block contains hourly historical data startingat 00:00\
        on the requested day and continues until 23:59 on the same day (UTC time)---')
    print('\n')
    for hourly in query_result['hourly']:
        print('{dt}'.format(dt=recoding_time(hourly['dt'])))
        print()
        print('Temperature: {temp}'.format(temp=hourly['temp']))
        print('Temperature.' +
              '\nThis accounts for the human perception of weather.: {feels_like}'.format(
                feels_like=hourly['feels_like']))
        print('Atmospheric pressure on the sea level: {pressure}, hPa'.format(pressure=hourly['pressure']))
        print('Humidity: {humidity}, %'.format(humidity=hourly['humidity']))
        print('Atmospheric temperature' +
              'below which water droplets begin to condense and dew can form. : {dew_point}, %'.format(
                dew_point=hourly['dew_point']))
        print('Cloudiness: {clouds}, %'.format(clouds=hourly['clouds']))
        print('Average visibility: {visibility}, metres'.format(visibility=hourly['visibility']))
        print('Wind speed: {wind_speed}, metres'.format(wind_speed=hourly['wind_speed']))
        print('Wind gust: {wind_gust}, metre/sec'.format(wind_gust=hourly['wind_gust']
                                                         if 'wind_gust' in hourly else 0))
        print('Wind direction: {wind_deg}, degrees: '.format(wind_deg=hourly['wind_deg']))
        print('Precipitation volume: {rain}, mm: '.format(rain=hourly['rain']
                                                          if 'rain' in hourly else 0))
        print('Snow volume: {snow}, mm: '.format(snow=hourly['snow']
                                                 if 'snow' in hourly else 0))
        print('---Weather---')
        for weather in hourly['weather']:
            print('Group of weather parameters: {main}'.format(main=weather['main']))
            print('Weather condition within the group: {description}'.format(description=weather['description']))
        print('----------------------------------------------------------------------------------------------------')


def processing_current_output(arguments):
    city = arguments.city
    api_key = arguments.apikey
    lat, lon, country = geocoding_api(city=city, api_key=api_key)
    part = ','.join([i for i in ['minutely', 'hourly', 'daily', 'current'] if not (i in (
            lambda x: x.split(',') if ',' in x else x)('current'))])
    query_result = weather_api(lat=lat, lon=lon, part=part, api_key=api_key)
    currentoutput(city=city, country=country, query_result=query_result)


def processing_forecast_output(arguments):
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


def processing_history_output(arguments):
    # time
    time = arguments.time
    api_key = arguments.apikey
    city = arguments.city
    # geocoding
    lat, lon, country = geocoding_api(city=city, api_key=api_key)

    # unix
    unix_time = encode_time(time=time)
    query_result = history_api(lat=lat, lon=lon, time=unix_time, api_key=api_key)
    historioutput(query_result, city=city, country=country)


def history_save(query_result: dict, path: str):
    print('start...')
    write_data = []
    for hourly in query_result['hourly']:
        new_dict = dict(
            dt=recoding_time(float(hourly.get('dt', 0))),
            temp=hourly.get('dt', 0),
            feels_like=hourly.get('feels_like', 0),
            pressure=hourly.get('hourly', 0),
            humidity=hourly.get('humidity', 0),
            dew_point=hourly.get('dew_point', 0),
            clouds=hourly.get('clouds', 0),
            visibility=hourly['visibility'],
            wind_speed=hourly['wind_speed'],
            wind_gust=hourly.get('wind_gust', 0),
            wind_deg=hourly['wind_deg'],
            rain_1h=hourly.get('rain', 0)['1h'],
            snow=hourly.get('snow', 0),
            weather_main=hourly['weather'][0]['main'],
            weather_description=hourly['weather'][0]['description'])
        write_data.append(new_dict)
    with open(file=path, mode='w', encoding='utf-8') as file:
        cin = csv.DictWriter(file, [
            'dt', 'temp', 'feels_like', 'pressure', 'humidity', 'dew_point', 'clouds', 'visibility',
            'wind_speed', 'wind_gust', 'wind_deg', 'rain_1h', 'snow', 'weather_main', 'weather_description'])
        cin.writeheader()
        cin.writerows(write_data)
    print('Completed...')
    # I get the keys
    hourly_keys = set()
    for i in range(len(query_result['hourly'])):
        hourly_keys.update(query_result['hourly'][i].keys())
    history_data = [{j: i.get(j, 0) for j in hourly_keys} for i in query_result['hourly']]
    print('1: ', history_data[0])
    print('2: ', query_result['hourly'][0])


def processing_current_save(arguments):
    pass


def processing_forecast_save(arguments):
    pass


def processing_history_save(arguments):
    # time
    time = arguments.time
    api_key = arguments.apikey
    city = arguments.city
    path = '{path}/{name}-{data}.csv'.format(path=arguments.path_file, name='history', data=time)
    # geocoding
    lat, lon, country = geocoding_api(city=city, api_key=api_key)
    # unix
    unix_time = encode_time(time=time)
    query_result = history_api(lat=lat, lon=lon, time=unix_time, api_key=api_key)
    history_save(query_result, path=path)


def set_parser(parser: argparse.ArgumentParser):
    subparser = parser.add_subparsers(
        help="The One Call API provides the following weather data for any geographical coordinates:" +
        "Current weather" +
        "Forecast: Minute forecast for 1 hour, Hourly forecast for 48 hours, Daily forecast for 7 days" +
        "Historical weather data for the previous 5 days")
    # CLI parser
    output = subparser.add_parser('output', help='outputting information to the console')
    save = subparser.add_parser('save', help='save to file')
    # app = subparser.add_parser('app', help='application launch')
    # output
    suboutput = output.add_subparsers(help='output in CLI')
    # suboutput
    output_current = suboutput.add_parser('current', help='Current weather')
    output_forecast = suboutput.add_parser(
        'forecast',
        help='Forecast weather: minute forecast for 1 hour, hourly forecast for 48 hours, daily forecast for 7 days')
    output_history = suboutput.add_parser('history', help='Historical weather data for the previous 5 days')

    # current
    output_current.add_argument(
        '-c', '--city', help='City for which weather information is collected', type=str, default=DEFAULT_CITY)
    output_current.add_argument('-k', '--apikey', help='API key', default=DEFAULT_API_KEY)
    output_current.set_defaults(callback=processing_current_output)

    # forecast
    output_forecast.add_argument('-p', '--parameter', help='Parameter specifying the type of information returned.' +
                                 'Available values: minutely, hourly, daily', default='minutely')
    output_forecast.add_argument(
        '-c', '--city', help='City for which weather information is collected', type=str, default=DEFAULT_CITY)
    output_forecast.add_argument('-k', '--apikey', help='API key', default=DEFAULT_API_KEY)
    output_forecast.set_defaults(callback=processing_forecast_output)

    # history
    output_history.add_argument(
        '-t',
        '--time',
        help='Date from the previous five days (Unix time, UTC time zone), e.g. dt=2021-06-10',
        default='...')
    output_history.add_argument(
        '-c', '--city', help='City for which weather information is collected', type=str, default=DEFAULT_CITY)
    output_history.add_argument('-k', '--apikey', help='API key', default=DEFAULT_API_KEY)
    output_history.set_defaults(callback=processing_history_output)

    # save
    subsave = save.add_subparsers(help='Save in doc')

    # subsave
    save_current = subsave.add_parser('current', help='Save the current weather')
    save_forecast = subsave.add_parser(
        'forecast',
        help='Saving Weather Forecast: 1 hour forecast 1 hour, 48 hour hourly forecast, 7 days daily forecast')
    save_history = subsave.add_parser('history', help='Storing historical weather data for the previous 5 days')

    # current
    save_current.add_argument(
        '-c', '--city', help='City for which weather information is collected', type=str, default=DEFAULT_CITY)
    save_current.add_argument('-k', '--apikey', help='API key', default=DEFAULT_API_KEY)
    save_current.add_argument('-path', '--path-to-file', help='File save path', default=DEFAULT_PATH_SAVE_FILE)
    save_current.set_defaults(callback=processing_current_save)

    # forecast
    save_forecast.add_argument(
        '-p', '--parameter', help='Parameter specifying the type of information returned.' +
        'Available values: minutely, hourly, daily', default='minutely')
    save_forecast.add_argument(
        '-c', '--city', help='City for which weather information is collected', type=str, default=DEFAULT_CITY)
    save_forecast.add_argument('-k', '--apikey', help='API key', default=DEFAULT_API_KEY)
    save_forecast.add_argument('-path', '--path-to-file', help='File save path', default=DEFAULT_PATH_SAVE_FILE)
    save_forecast.set_defaults(callback=processing_forecast_save)

    # history
    save_history.add_argument(
        '-t',
        '--time',
        help='Date from the previous five days (Unix time, UTC time zone), e.g. dt=2021-06-10',
        default='...')
    save_history.add_argument(
        '-c', '--city', help='City for which weather information is collected', type=str, default=DEFAULT_CITY)
    save_history.add_argument('-k', '--apikey', help='API key', default=DEFAULT_API_KEY)
    save_history.add_argument('-path', '--path_file', help='File save path', default=DEFAULT_PATH_SAVE_FILE)
    save_history.set_defaults(callback=processing_history_save)

# добавть форматы сохарения в json или csv
# не нужно много парсеров для сохра, тип данный запрашиваем через два флага и параметры


def main():
    parser = argparse.ArgumentParser(
        description='This is a CLI application for getting weather data through\
            the api of the climate data storage service',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    set_parser(parser)
    args = parser.parse_args()
    args.callback(args)  # callback for branches


if __name__ == '__main__':
    main()
