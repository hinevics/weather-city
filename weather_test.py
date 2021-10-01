from re import A

from requests import api
import pytest
import WeatherWebAPI
 
DEFAULT_API_KEY = r'8cd65e1b7f292a69366f2a526046a32c'
DEFAULT_CITU = r'Minsk'
DEFAULT_LON_LAT = (27.5667, 53.9)

class TestWeatherWebAPI:
    def test_import_modul_weater_1(self):
        """
        ...description...
        """
        assert WeatherWebAPI


    def test_can_work_with_class_city_2(self):
        """
        ...description...
        """
        assert WeatherWebAPI.City


    def test_how_init_class_city_3(self):
        """
        ...description...
        """
        # creat test obj
        a = WeatherWebAPI.City(api_key=DEFAULT_API_KEY, name="Minsk")
        assert a.name == "Minsk"
        assert a.country == 'BY'
        assert a.lon_lat == (27.5667, 53.9)


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
        a = WeatherWebAPI.City(lon_lat=(27.5667, 53.9), api_key=DEFAULT_API_KEY)
        print(a.name)
        assert a.name == 'Horad Minsk'
    
    
    def test_how_working_class_city_classmethod_reverse_geocoding_5(self):
        """
        description
        """
        result = WeatherWebAPI.City.reverse_geocoding(lon_lat=(27.5667, 53.9), api_key=DEFAULT_API_KEY)
        assert result['name'] == 'Horad Minsk'
        
    def test_how_working_class_city_classmethod_direct_geocoding_6(self):
        """
        description
        """
        result = WeatherWebAPI.City.direct_geocoding(name='Minsk', api_key=DEFAULT_API_KEY)
        assert result['lon'] == 27.5667
        assert result['lat'] == 53.9
        
        
    
    def test_datetime_class_testing_default_date(self)


class TestWeatherDB:
    pass

class TestWeatherAPP:
    pass

class TestWeatherGUI:
    pass