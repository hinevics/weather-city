from src.getting_weather_data.weather_api import WeatherAPI


def get_graph_weather_changes_day():
    graphJSON = WeatherAPI.get_weather_this_day()
    return graphJSON


def main():
    print(WeatherAPI)


if __name__ == "__main__":
    main()
