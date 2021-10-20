import WeatherWebAPI
import re
import os



def get_current(city:str, api_key:str):
    city = WeatherWebAPI.City(name=city, api_key=api_key)
    current_weather = WeatherWebAPI.Current.get_weather(city=city, api_key=api_key)
    return {
        'dt':current_weather['current']['dt'],
        'temp':current_weather['current']['temp'],
        'pressure':current_weather['current']['pressure'],
        'humidity': 80,
        'dew_point': -1.94,
        'uvi': 1.25,
        'clouds': 6,
        'visibility': 10000,
        'wind_speed': 3.77, 
        'wind_deg': 290,
        'wind_gust': 9.76, 
        'weather_icon': r'http://openweathermap.org/img/wn/{icon}.png'.format(icon=current_weather['current']['weather'][0]['icon'])
        }

def get_his

def main():
    get_current(city='Minsk', api_key=WeatherWebAPI.DEFAULT_API_KEY)
    print('Ok!')


if __name__ == '__main__':
    main()