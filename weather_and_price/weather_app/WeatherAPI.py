import requests

from config import API_KEY

# format date 2020-10-19
# YYYY - MM - DD


class Weather:
    DEFULT_API_FORM_REGUEST = \
        r'https://weather.visualcrossing.com/VisualCrossingWebServices'
    DEFULT_API_FORM_REGUEST_TIMELINE = \
        r'rest/services/timeline/{location}/{date1}/{date2}?key={api_key}'
    DEFULT_API_FORM_REGUEST_DATA2 = \
        r'rest/services/timeline/{location}/{date2}?key={api_key}'

    @classmethod
    def get_historical_weather_data(cls, date2, date1=False,
                                    location='Bengaluru'):
        if date1:
            api_form_reguest = '{request}/{timeline}'.format(
                request=cls.DEFULT_API_FORM_REGUEST,
                timeline=cls.DEFULT_API_FORM_REGUEST_TIMELINE.format(
                    date1=date1,
                    date2=date2,
                    api_key=API_KEY,
                    location=location))
        else:
            api_form_reguest = '{request}/{timeline}'.format(
                request=cls.DEFULT_API_FORM_REGUEST,
                timeline=cls.DEFULT_API_FORM_REGUEST_DATA2.format(
                    location=location,
                    date2=date2,
                    api_key=API_KEY))
        get = requests.get(api_form_reguest)
        if get.status_code == 200:
            weather_data = get.json()
            return weather_data
        else:
            print(get.status_code)
            return None


def main():
    a = Weather.get_historical_weather_data(date2='2020-10-19')
    print(type(a))


if __name__ == '__main__':
    main()
