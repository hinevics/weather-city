import datetime
import time

import pytest

from config import DEFAULT_API_HISTORY, DEFAULT_API_FORECAST_MINUTE,\
    DEFAULT_API_FORECAST_HOURLY, DEFAULT_API_FORECAST_DAILY, DEFAULT_API_CURRENT, DEFAULT_API_KEY

import WeatherWebAPI
import Weather

DEFAULT_CITU = r'Minsk'
DEFAULT_LON_LAT = (53.9, 27.5667)


class TestWeatherWebAPI:
    # Testing the module
    def test_import_module_weather_1(self):
        """
            description...
        """
        assert WeatherWebAPI

    # class City
    def test_can_work_with_class_city_2(self):
        """
            description...
        """
        assert WeatherWebAPI.City

    def test_how_init_class_city_3(self):
        """
            description...
        """
        # creat test obj
        a = WeatherWebAPI.City(api_key=DEFAULT_API_KEY, name="Minsk")
        assert a.name == "Minsk"
        assert a.country == 'BY'
        assert a.lat_lon == DEFAULT_LON_LAT

    # def test_how_working_class_when_dont_get_api_key_4(self):
    #     """
    #         description
    #     """
    #     a = WeatherWebAPI.City(api_key=DEFAULT_API_KEY, name="Minsk")
    #     with pytest.raises(ValueError):
    #         a = WeatherWebAPI.City(name='Minsk')

    def test_how_work_class_when_get_lat_lon_5(self):
        """
            description
        """
        a = WeatherWebAPI.City(lat_lon=DEFAULT_LON_LAT, api_key=DEFAULT_API_KEY)
        print(a.name)
        assert a.name == 'Horad Minsk'

    def test_how_working_class_city_classmethod_reverse_geocoding_5(self):
        """
            description
        """
        result = WeatherWebAPI.City.reverse_geocoding(lat_lon=DEFAULT_LON_LAT, api_key=DEFAULT_API_KEY)
        assert result['name'] == 'Horad Minsk'

    def test_how_working_class_city_classmethod_direct_geocoding_6(self):
        """
            description
        """
        result = WeatherWebAPI.City.direct_geocoding(name='Minsk', api_key=DEFAULT_API_KEY)
        print(result)
        assert result['lon'] == DEFAULT_LON_LAT[1]
        assert result['lat'] == DEFAULT_LON_LAT[0]

    # class DateTime
    def test_datetime_class_testing_default_date_7(self):
        """
            Test of the default time operation
        """
        deltatime = datetime.date.today() - datetime.timedelta(WeatherWebAPI.DateTime.DEFAULT_TIMEDELTA)
        unixdelta = time.mktime(deltatime.timetuple())
        assert unixdelta == WeatherWebAPI.DateTime.DEFAULT_HISTORICAL_DATETIME

    def test_datetime_class_testing_default_date_8(self):
        """
            Check the operation of the default parameter: today date
        """
        nowtime = datetime.date.today()
        nowunix = time.mktime(nowtime.timetuple())
        assert nowunix == WeatherWebAPI.DateTime.DEFAULT_TODAY_DATETIME

    def test_datetime_class_testing_create_dattime_unix_format_9(self):
        """
            Create datetime data in unix format.
            The function takes parameters as a string, and returns as an unix time format
        """
        test_query = '20.9.2021'  # test date
        # test time value in unix
        test_query_unix = time.mktime(datetime.datetime.strptime(test_query, r'%d.%m.%Y').timetuple())
        assert WeatherWebAPI.DateTime.create_unix(test_query) == test_query_unix

    def test_datetime_class_testing_recoding_dattime_utc_format_10(self):
        """
            Convert date and time to utc format.
            The function takes the date in unix and returns it in utc
        """
        test_time = '20.9.2021'  # expected answer
        # transferred value
        test_unix_time = time.mktime(datetime.datetime.strptime(test_time, r'%d.%m.%Y').timetuple())
        assert WeatherWebAPI.DateTime.create_utc(test_unix_time) == test_time

    def test_datetime_class_testing_recoding_dattime_utc_format_11(self):
        """
            Checking the conversion process
        """
        unix_time = time.mktime(datetime.datetime.utcnow().timetuple())
        assert WeatherWebAPI.DateTime.create_time_unix_from_datetime(datetime=datetime.datetime.utcnow()) == unix_time

    # class Historical
    def test_historical_class_can_use_default_var_12(self):
        """
            Calling the default variable
        """
        assert WeatherWebAPI.Historical.DEFAULT_API_HISTORY == DEFAULT_API_HISTORY

    def test_historical_class_can_fill_default_parameter_with_new_values_13(self):
        """
            Check the default parameter. Substituting new values there
        """
        name_city = 'London'
        test_city = WeatherWebAPI.City(api_key=DEFAULT_API_KEY, name=name_city)
        test_lat, test_lon = test_city.lat_lon
        test_time = WeatherWebAPI.DateTime.create_time_unix_from_datetime(datetime=datetime.datetime.utcnow())
        test_res = DEFAULT_API_HISTORY.format(lat=test_lat, lon=test_lon, time=test_time, api_key=DEFAULT_API_KEY)
        assert WeatherWebAPI.Historical.DEFAULT_API_HISTORY.format(
            lat=test_lat, lon=test_lon, time=test_time, api_key=DEFAULT_API_KEY) == test_res

    def test_historical_class_can_use_classmethod_get_weather_when_used_default_dt_14(self):
        """
            Can I use the get_weather class method.
            Method operation at default time.
        """
        test_city = WeatherWebAPI.City(api_key=DEFAULT_API_KEY, name='Minsk')
        test_lat, test_lon = test_city.lat_lon
        assert WeatherWebAPI.Historical.get_weather(city=test_city, api_key=DEFAULT_API_KEY)['lat'] == test_lat
        assert WeatherWebAPI.Historical.get_weather(city=test_city, api_key=DEFAULT_API_KEY)['lon'] == test_lon

    def test_historical_class_can_use_classmethod_get_weather_when_used_dt_15(self):
        """
            How the Historical get_weather class method works when the time is passed to it.
        """
        test_time = '17.10.2021'
        test_unix_time = WeatherWebAPI.DateTime.create_unix(utctime=test_time)
        test_city = WeatherWebAPI.City(name='London', api_key=DEFAULT_API_KEY)
        date_query_unix = WeatherWebAPI.Historical.get_weather(
            city=test_city, api_key=DEFAULT_API_KEY, dt=test_unix_time)['current']['dt']
        date_query = WeatherWebAPI.DateTime.create_utc(unixdatetime=date_query_unix)
        assert date_query == test_time

    # class Current
    def test_can_use_class_current_16(self):
        """
            I can import the class Current
        """
        assert WeatherWebAPI.Current

    def test_checking_default_api_class_current_17(self):
        """
            Checking the default api
        """
        assert DEFAULT_API_CURRENT == WeatherWebAPI.Current.DEFAULT_API_CURRENT

    def test_can_use_method_get_weather_api_18(self):
        """
            Is there a method for executing the query
        """
        assert WeatherWebAPI.Current.get_weather

    def test_can_query_current_weather_19(self):
        """
            Checking the work of the method get_weather_api class Current
        """
        name_city = 'Minsk'
        test_city = WeatherWebAPI.City(name=name_city, api_key=DEFAULT_API_KEY)
        current_dt = WeatherWebAPI.Current.get_weather(city=test_city, api_key=DEFAULT_API_KEY)['current']['dt']
        now_dt = int(time.mktime(datetime.date.today().timetuple()))
        assert WeatherWebAPI.DateTime.create_utc(
            unixdatetime=now_dt) == WeatherWebAPI.DateTime.create_utc(unixdatetime=current_dt)

    # class Forecast
    def test_can_used_class_forecast_20(self):
        """
            Могу ли я использовать этот класс
        """
        assert WeatherWebAPI.Forecast

    def test_can_use_default_api_weather_forecast_21(self):
        """
            Могу я использовать параметры по умолчанию из этого класса
        """
        assert WeatherWebAPI.Forecast.DEFAULT_API_FORECAST_MINUTE == DEFAULT_API_FORECAST_MINUTE
        assert WeatherWebAPI.Forecast.DEFAULT_API_FORECAST_HOURLY == DEFAULT_API_FORECAST_HOURLY
        assert WeatherWebAPI.Forecast.DEFAULT_API_FORECAST_DAILY == DEFAULT_API_FORECAST_DAILY

    def test_can_use_method_get_minute_weather_22(self):
        """
            Я могу использовать метод get_minute_weather
        """
        assert WeatherWebAPI.Forecast.get_minute_weather

    def test_can_use_method_get_hourly_weather_23(self):
        """
            Я могу использовать метод get_hourly_weather
        """
        assert WeatherWebAPI.Forecast.get_hourly_weather

    def test_can_use_method_get_daily_weather_24(self):
        """
            Я могу использовать метод get_daily_weather
        """
        assert WeatherWebAPI.Forecast.get_daily_weather

    def test_how_work_method_get_minute_weather_25(self):
        """
            Как работает метод get_minute_weather
        """
        name = 'Minsk'
        city = WeatherWebAPI.City(name=name, api_key=DEFAULT_API_KEY)
        result = WeatherWebAPI.Forecast.get_minute_weather(city=city, api_key=DEFAULT_API_KEY)
        assert 'minutely' in result.keys()
        assert result['lat'], result['lon'] == city.lat_lon

    def test_how_work_method_get_hourly_weather_26(self):
        """
            Как рабоатет метод get_hourly_weather
        """
        name = 'Minsk'
        city = WeatherWebAPI.City(name=name, api_key=DEFAULT_API_KEY)
        result = WeatherWebAPI.Forecast.get_hourly_weather(city=city, api_key=DEFAULT_API_KEY)
        assert 'hourly' in result.keys()
        assert result['lat'], result['lon'] == city.lat_lon

    def test_how_work_method_get_daily_weather_27(self):
        """
            Как рабоатет метод get_daily_weather
        """
        name = 'Minsk'
        city = WeatherWebAPI.City(name=name, api_key=DEFAULT_API_KEY)
        result = WeatherWebAPI.Forecast.get_daily_weather(city=city, api_key=DEFAULT_API_KEY)
        assert 'daily' in result.keys()
        assert result['lat'], result['lon'] == city.lat_lon


class TestWeather:
    def test_can_import_module_28(self):
        assert Weather

    def test_can_use_fuction_get_current_29(self):
        assert Weather.get_current

    def test_can_work_with_fuction_30(self):
        result = Weather.get_current(city='Minsk', api_key=DEFAULT_API_KEY)
        assert result.values()

    def test_utc_time_in_return_31(self):
        result = Weather.get_current(city='Minsk', api_key=DEFAULT_API_KEY)
        assert 'dt' in result.keys()

    def test_utc_time_in_return_32(self):
        result = Weather.get_current(city='Minsk', api_key=DEFAULT_API_KEY)
        assert not(result['dt'].values() == {}.values())

    def test_utc_time_in_return_33(self):
        result = Weather.get_current(city='Minsk', api_key=DEFAULT_API_KEY)
        utcdatetime = time.localtime(time.mktime(datetime.date.today().timetuple()))
        time_now = '{d}.{m}.{Y}'.format(d=utcdatetime.tm_mday, m=utcdatetime.tm_mon, Y=utcdatetime.tm_year)
        assert result['dt']['values'] == time_now

    def test_get_current_dt_descrition_34(self):
        result = Weather.get_current(city='Minsk', api_key=DEFAULT_API_KEY)
        assert result['dt']['description'] != ''

    def test_get_current_temp_values_35(self):
        result = Weather.get_current(city='Minsk', api_key=DEFAULT_API_KEY)
        assert result['temp'].values() != {}.values()

    def test_get_current_temp_description_36(self):
        result = Weather.get_current(city='Minsk', api_key=DEFAULT_API_KEY)
        assert result['temp']['description'] != ''

    def test_get_current_values_37(self):
        result = Weather.get_current(city='Minsk', api_key=DEFAULT_API_KEY)
        for k in result.keys():
            assert result[k].values() != {}.values()


class TestWeatherDB:
    pass


class TestWeatherGUI:
    pass
