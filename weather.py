
# программа строит исторчиеские даныне виде графика изменения осадков
# I am using api openweathermap.org
import argparse
import requests
import json
from re import sub
import datetime

from requests import api

# DEFAULT_PATH_SAVE_FILE = r'../{name_doc}.{form}'
# DEFAULT_CITY = r'London'
# DEFAULT_API_WEATHER = r'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude={part}&appid={api_key}'
# DEFAULT_API_CITY = r'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'
# DEFAULT_API_WEATHER_HISTORY = r'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&lang=ru&dt={time}&appid={api_key}'


class City:
    DEFAULT_API_CITY_DIRECT = 'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'
    DEFAULT_API_CITY_REVERSE = 'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&appid={api_key}'
    def __init__(self, api_key, lon=None, lat=None, name=None) -> None:
        if name is None:
            pass
        # elif pass
        self.name=name
        self.api_key = api_key
        self.lon = lon if not (lon is None) else City.direct_geocoding(name=self.name, api_key=self.api_key)['lon']
        self.lat = lat if not (lat is None) else City.direct_geocoding(name=self.name, api_key=self.api_key)['lat']
        
        
    @classmethod
    def direct_geocoding(cls, name,  api_key):
        """
        :return: :
        """
        answer = requests.get(url=City.DEFAULT_API_CITY_DIRECT.format(city_name=name, api_key=api_key))
        if answer.status_code == 200:
            return answer.json()[0]
        else:
            print('STATUS CODE: {a1}'.format(a1=answer.status_code))
    @classmethod
    def reverse_geocoding(cls, lon, lat,  api_key):
        """
        :return: :
        """
        answer = requests.get(url=City.DEFAULT_API_CITY_REVERSE.format(lat=lat, lon=lon, api_key=api_key))
        if answer.status_code == 200:
            return (answer.json())
        else:
            print('STATUS CODE: {a1}'.format(a1=answer.status_code))


# class Weather:
#     def __init__(self, api_key, city='London', time=None, date=None) -> None:
#         self.api_key = api_key
#         self.city = city
#         self.time = time
#         self.date = date
    
    

def main():
    # 'lat': 53.9, 'lon': 27.5667
    a = City(name='Minsk', api_key='8cd65e1b7f292a69366f2a526046a32c')
    # print(a.lat)
    
if __name__ == '__main__':
    main()