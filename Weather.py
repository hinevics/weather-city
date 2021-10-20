import WeatherWebAPI
import re
import os



def get_current(city:str, api_key:str):
    city = WeatherWebAPI.City(name=city, api_key=api_key)
    current_weather = WeatherWebAPI.Current.get_weather(city=city, api_key=api_key)
    return {
        'dt': {'values':WeatherWebAPI.DateTime.create_utc(current_weather['current']['dt']),
                '':'',
                'description':'Current time'},
        'temp': {
            'values':current_weather['current']['temp'],
            'units':'°C',
            'description': 'Temperature'},
        'temp_feels_like':{
            'values': current_weather['current']['feels_like'],
            'units':'°C',
            'description':'Celsius'},
        'pressure':{
            'values':current_weather['current']['pressure'],
            'units':'hPa',
            'description': 'Atmospheric pressure on the sea level'},
        'humidity': {
            'values':current_weather['current']['humidity'],
            'units':'%',
            'description':'Humidity'},
        'dew_point':{
            'values': current_weather['current']['dew_point'],
            'description':''},
        'uvi': {
            'values':current_weather['current']['uvi'],
            'description':''},
        'clouds': {
            'values':current_weather['current']['clouds'],
            "description":""},
        'visibility': {
            'values':current_weather['current']['visibility'],
            'description':''},
        'wind_speed': {
            'values':current_weather['current']['wind_speed'],
            'description':''},
        'wind_deg': {
            'values':current_weather['current']['wind_deg'],
            'description':''},
        'wind_gust': {
            'values':current_weather['current']['wind_gust'],
            "description":""},
        'weather_icon': {
                        'values':r'http://openweathermap.org/img/wn/{icon}.png'.format(icon=current_weather['current']['weather'][0]['icon']),
            'description':"{}".format(current_weather['current']['weather'][0]['description'])}}

# def get_his

def main():
    a = get_current(city='Minsk', api_key=WeatherWebAPI.DEFAULT_API_KEY)
    for i in a.keys():
        print(a[i].values())


if __name__ == '__main__':
    main()