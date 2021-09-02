
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
    DEFAULT_API_CITY = 'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'
    def __init__(self, lon=None, lat=None, name=None) -> None:
        self.lon = lon
        self.lat = lat

    def geocoding(self):
        """
        :return: :class:`Response <Response>` object
        """
        answer = requests.get(url=self.DEFAULT_API_CITY.format(city_name=self.city, api_key=self.api_key))
        if answer.status_code == 200:
            print(answer.json())


class Weather:
    def __init__(self, api_key, city='London', time=None, date=None) -> None:
        self.api_key = api_key
        self.city = city
        self.time = time
        self.date = date
    
    
# добавть форматы сохарения в json или csv 
# не нужно много парсеров для сохра, тип данный запрашиваем через два флага и параметры
def main():
    a = Weather(api_key='', city=City(name='Minsk'))
    a.geocoding()
if __name__ == '__main__':
    main()