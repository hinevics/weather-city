import WeatherWebAPI
import re
import os



def get_current(city:str, api_key:str) -> dict:
    city = WeatherWebAPI.City(name=city, api_key=api_key)
    current_weather = WeatherWebAPI.Current.get_weather(city=city, api_key=api_key)
    return {
        
        'dt': {'values':WeatherWebAPI.DateTime.create_utc(current_weather['current']['dt']),
                'units':'',
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
            'units':'°C',
            'description':''},
        
        'clouds':
            {
            'values': current_weather['current']['clouds'],
            'units':'%',
            'description':'Cloudiness'},
        
        'uvi': {
            'values':current_weather['current']['uvi'],
            'units':'',
            'description':'Current UV index'},
        
        'visibility': {
            'values':current_weather['current']['visibility'],
            'units':'metre',
            'description':'Average visibility'},
        
        'wind_speed': {
            'values':current_weather['current']['wind_speed'],
            'units':'metre/sec',
            'description':'Wind speed'},
        
        'wind_gust': {
            'values':current_weather['current']['wind_gust'],
            'units':'metre/sec',
            'description':'Wind gust'} if 'wind_gust' in current_weather['current'] else None,
        
        'wind_deg': {
            'values':current_weather['current']['wind_deg'],
            'units':'°',
            'description':'Wind direction'} if 'wind_deg' in current_weather['current'] else None,
        
        'rain': {
            'values':current_weather['current']['rain']['1h'],
            'units':'mm',
            'description':'Rain volume for last hour'}
                if (
                    'rain' in current_weather['current'] and
                    '1h' in current_weather['current']['rain'] and
                    'description' in current_weather['current']['rain'])
                else None,
        
        'snow': {
            'values':current_weather['current']['snow']['1h'],
            'units':'mm',
            'description':'Snow volume for last hour'} if (
                'snow' in current_weather['current'] and '1h' in current_weather['current']['snow']) else None,
        
        'weather': {
            'icon':r'http://openweathermap.org/img/wn/{icon}.png'.format(icon=current_weather['current']['weather'][0]['icon'])
                if 'icon' in current_weather['current']['weather'][0] else None,
            'group': current_weather['current']['weather'][0]['main'] if 'main' in current_weather['current']['weather'][0] else None, 
            'description':"{}".format(current_weather['current']['weather'][0]['description'])
                if 'description' in current_weather['current']['weather'][0] else None}
            if 'weather' in current_weather['current'] else None
        }

# def get_his

def main():
    a = get_current(city='Minsk', api_key=WeatherWebAPI.DEFAULT_API_KEY)
    for i in a.keys():
        print(a[i].values())


if __name__ == '__main__':
    main()