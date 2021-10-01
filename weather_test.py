from re import A

from requests import api
import pytest
import WeatherWebAPI
import datetime
import time
 
DEFAULT_API_KEY = r'8864601f4ae98b4994aa53941f6bc733'
DEFAULT_CITU = r'Minsk'
DEFAULT_LON_LAT = (53.9, 27.5667)

class TestWeatherWebAPI:
    def test_import_modul_weater_1(self):
        """
            description...
        """
        assert WeatherWebAPI


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


    def test_how_working_class_when_dont_get_api_key_4(self):
        """
            description
        """
        a = WeatherWebAPI.City(api_key=DEFAULT_API_KEY, name="Minsk")
        with pytest.raises(ValueError):
            a = WeatherWebAPI.City(name='Minsk')
    
    
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
        
        
    
    def test_datetime_class_testing_default_date_7(self):
        """
            Test of the default time operation
        """
        deltatime = datetime.date.today() - datetime.timedelta(5)
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
        test_query = '20.09.2021' # test date
        test_query_unix = time.mktime(datetime.datetime.strptime(test_query, r'%d.%m.%Y').timetuple())  # test time value in unix
        assert WeatherWebAPI.DateTime.create_datetime(test_query) == test_query_unix
    
    # def test
    
class TestWeatherDB:
    pass

class TestWeatherAPP:
    pass

class TestWeatherGUI:
    pass