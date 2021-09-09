from re import A
import pytest
import weather


def test_import_modul_weater_1():
    """
    ...description...
    """
    assert weather


def test_can_work_with_class_city_2():
    """
    ...description...
    """
    assert weather.City


def test_how_init_class_city_3():
    """
    ...description...
    """
    # creat test obj
    a = weather.City(api_key='8cd65e1b7f292a69366f2a526046a32c', name="Minsk")
    assert a.name == "Minsk"
    assert a.country == 'BY'
    assert a.lon_lat == (27.5667, 53.9)


def test_how_working_class_when_dont_get_api_key():
    """
    description
    """
    a = weather.City(api_key='8cd65e1b7f292a69366f2a526046a32c', name="Minsk")
    with pytest.raises(ValueError):
        a = weather.City(name='Minsk')