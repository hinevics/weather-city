import WeatherWebAPI
import re
import os



def get_current(city:str, api_key:str):
    city = WeatherWebAPI.City(name=city, api_key=api_key)
    current_weather = WeatherWebAPI.Current.get_weather(city=city, api_key=api_key)
    return {
        'dt': {'values':WeatherWebAPI.DateTime.create_utc(current_weather['current']['dt']),
                'description':''},
        'temp':current_weather['current']['temp'],
        'pressure':current_weather['current']['pressure'],
        'humidity': current_weather['current']['humidity'],
        'dew_point': current_weather['current']['dew_point'],
        'uvi': current_weather['current']['uvi'],
        'clouds': current_weather['current']['clouds'],
        'visibility': current_weather['current']['visibility'],
        'wind_speed': current_weather['current']['wind_speed'], 
        'wind_deg': current_weather['current']['wind_deg'],
        'wind_gust': current_weather['current']['wind_gust'], 
        'weather_icon': r'http://openweathermap.org/img/wn/{icon}.png'.format(icon=current_weather['current']['weather'][0]['icon'])
        }

# def get_his

def main():
    get_current(city='Minsk', api_key=WeatherWebAPI.DEFAULT_API_KEY)
    print('Ok!')


if __name__ == '__main__':
    main()