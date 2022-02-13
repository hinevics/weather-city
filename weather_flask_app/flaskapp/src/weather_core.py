from src.getting_weather_data.weather_api import DailyHistoricalWeatherAPI


def get_graph_weather_changes_day():
    graphJSON = DailyHistoricalWeatherAPI.get_weather_this_day_test()
    return graphJSON


def main():
    pass


if __name__ == "__main__":
    main()
