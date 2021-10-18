# that code for the most beautiful kitties 💗💗💗
# Выгрузка данных по погоде
# сохранение их
# работа с аналитикой по данным
# программа строит исторчиеские даныне виде графика изменения осадков
# I am using api openweathermap.org
import requests
import json
import datetime
import time

from requests import api

# DEFAULT_PATH_SAVE_FILE = r'../{name_doc}.{form}'
# DEFAULT_CITY = r'London'
# DEFAULT_API_WEATHER = r'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude={part}&appid={api_key}'
# DEFAULT_API_CITY = r'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'
# DEFAULT_API_WEATHER_HISTORY = r'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&lang=ru&dt={time}&appid={api_key}'
DEFAULT_API_KEY = r'8864601f4ae98b4994aa53941f6bc733'

class City:
    """
    Этот класс для преоброзования города и работы с данными по городу в основном парсере
    """
    DEFAULT_API_CITY_DIRECT = 'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'
    DEFAULT_API_CITY_REVERSE = 'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&appid={api_key}'
    def __init__(self, api_key=None, lat_lon=None, name=None) -> None:
        """
        ...description...
        """
        if api_key is None:
            raise ValueError
        if (name is None) and (not (lat_lon is None)):
            city_inf = City.reverse_geocoding(lat_lon=lat_lon, api_key=api_key)
            name = city_inf['name']
            country = city_inf['country']
        elif (lat_lon is None) and (not (name is None)):
            city_inf = City.direct_geocoding(name=name, api_key=api_key)
            lat_lon = city_inf['lat'], city_inf['lon']
            country = city_inf['country']
        self.api_key = api_key
        self.lat_lon=lat_lon
        self.name = name
        self.country = country

    @classmethod
    def direct_geocoding(cls, name:str,  api_key:str) -> dict:
        """
        :return: :
        """
        answer = requests.get(url=City.DEFAULT_API_CITY_DIRECT.format(city_name=name, api_key=api_key))
        if answer.status_code == 200:
            return answer.json()[0]
        else:
            print('STATUS CODE: {a1}'.format(a1=answer.status_code))

    @classmethod
    def reverse_geocoding(cls, lat_lon:tuple,  api_key:str) -> dict:
        """
        :return: :
        """
        answer = requests.get(url=City.DEFAULT_API_CITY_REVERSE.format(lat=lat_lon[0], lon=lat_lon[1], api_key=api_key))
        if answer.status_code == 200:
            return answer.json()[0]
        else:
            print('STATUS CODE: {a1}'.format(a1=answer.status_code))


class DateTime:
    """
    This is a class for working with date and time when preparing api requests
    It has a default parameter that is called from the class if the user does not pass the time when requesting historical data : DEFAULT_HISTORICAL_DATETIME
    """
    DEFAULT_TIMEDELTA = 4.9
    DEFAULT_HISTORICAL_DATETIME = int(time.mktime((datetime.date.today() - datetime.timedelta(DEFAULT_TIMEDELTA)).timetuple()))
    DEFAULT_TODAY_DATETIME = int(time.mktime(datetime.date.today().timetuple()))
    
    @classmethod
    def create_unix(cls, utctime:str):
        """
            The function converts utc date to unix
        """
        return int(time.mktime(datetime.datetime.strptime(utctime, r'%d.%m.%Y').timetuple()))

    @classmethod
    def create_utc(cls, unixdatetime):
        """
            Converts unix date to utc and returns as a string
        """
        utcdatetime = time.localtime(unixdatetime)
        # There are different time formats: UTC, unix, GMT
        return '{d}.{m}.{Y}'.format(d=utcdatetime.tm_mday, m=utcdatetime.tm_mon, Y=utcdatetime.tm_year)

    @classmethod
    def create_time_unix_from_datetime(cls, datetime:datetime.datetime):
        """
            Creating unix time from datetime
        """
        return time.mktime(datetime.utcnow().timetuple())
    
    
class Historical:
    """
    Historical weather data
    
    Historical weather data for the previous 5 days
    """
    DEFAULT_API_HISTORY = r'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={api_key}'
    @classmethod
    def get_weather(cls, city:City, api_key:str, dt:int=DateTime.DEFAULT_HISTORICAL_DATETIME):
        """
            When this method is called, the City object and the int number corresponding to the time are passed to it 
        """
        # Incoming weather data must be converted to the City class
        str_request = Historical.DEFAULT_API_HISTORY.format(api_key=api_key, lat=city.lat_lon[0], lon=city.lat_lon[1], time=dt)
        answer = requests.get(url=str_request)
        if answer.status_code == 200:
            print('I love you! ❤️❤️❤️')
            return answer.json()
        else:
            print(answer.status_code)
            for key in answer.headers.keys():
                print('{a1}: {a2}'.format(a1=key, a2=answer.headers[key]))


class Current:
    """
        ...description...
    """
    DEFAULT_API_CURRENT = r'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={api_key}'
    @classmethod
    def get_weather(cls, city:City, api_key:str):
        """
            ...description...
        """
        lat, lon = city.lat_lon
        str_request = Current.DEFAULT_API_CURRENT.format(lat=lat, lon=lon, api_key=api_key)
        answer = requests.get(url=str_request)
        if answer.status_code == 200:
            print('I love you! ❤️❤️❤️')
            return answer.json()
        else:
            print(answer.status_code)
            for key in answer.headers.keys():
                print('{a1}: {a2}'.format(a1=key, a2=answer.headers[key]))



class Forecast:
    """
        Это нужно переделать. добавить возможность принимать параметр который поределяет какие именно нужны данные а не делать запросы с разных методов.
    """
    DEFAULT_API_FORECAST_MINUTE = r'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,hourly,daily,alerts&appid={api_key}'
    DEFAULT_API_FORECAST_HOURLY = r'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,daily,alerts&appid={api_key}'
    DEFAULT_API_FORECAST_DAILY = r'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={api_key}'

    @classmethod
    def get_minute_weather(cls, city:City, api_key:str):
        """
            ...description...
        """
        lat, lon = city.lat_lon
        str_request = Forecast.DEFAULT_API_FORECAST_MINUTE.format(lat=lat, lon=lon, api_key=api_key)
        answer = requests.get(url=str_request)
        if answer.status_code == 200:
            print('I love you! ❤️❤️❤️')
            return answer.json()
        else:
            print(answer.status_code)
            for key in answer.headers.keys():
                print('{a1}: {a2}'.format(a1=key, a2=answer.headers[key]))

    @classmethod
    def get_hourly_weather(cls, city:City, api_key:str):
        """
            ...description...
        """
        lat, lon = city.lat_lon
        str_request = Forecast.DEFAULT_API_FORECAST_HOURLY.format(lat=lat, lon=lon, api_key=api_key)
        answer = requests.get(url=str_request)
        if answer.status_code == 200:
            print('I love you! ❤️❤️❤️')
            return answer.json()
        else:
            print(answer.status_code)
            for key in answer.headers.keys():
                print('{a1}: {a2}'.format(a1=key, a2=answer.headers[key]))

    @classmethod
    def get_daily_weather(cls, city:City, api_key:str):
        """
            ...description...
        """
        lat, lon = city.lat_lon
        str_request = Forecast.DEFAULT_API_FORECAST_DAILY.format(lat=lat, lon=lon, api_key=api_key)
        answer = requests.get(url=str_request)
        if answer.status_code == 200:
            print('I love you! ❤️❤️❤️')
            return answer.json()
        else:
            print(answer.status_code)
            for key in answer.headers.keys():
                print('{a1}: {a2}'.format(a1=key, a2=answer.headers[key]))
    

def main():
    # dt = DateTime.create_unix('9.10.2021')
    # a = Historical.get_weather_api(city=City(name='Minsk', api_key=DEFAULT_API_KEY), api_key=DEFAULT_API_KEY, dt=dt)['current']['dt']
    # print(DateTime.create_utc(unixdatetime=a))
    print(DateTime.create_utc(DateTime.DEFAULT_TODAY_DATETIME))
    print(DateTime.create_utc(1633987116))
if __name__ == '__main__':
    main()
