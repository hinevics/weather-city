import pandas as pd

from config import PATH_DATASET
from WeatherAPI import Weather


def parser_weather_data(data: dict):
    res_data = {i: data['days'][0][i] for i in data['days'][0].keys()
                if not (type(data['days'][0][i]) in (dict, list))}
    return pd.DataFrame(
        data=[[i for i in res_data.values()]],
        columns=[i for i in res_data.keys()])


def main():
    data = pd.read_csv(PATH_DATASET, encoding='utf-8', usecols=[3])
    data_weather = []
    for date in data.Date.unique():
        get_weather = Weather.get_historical_weather_data(date2=date)
        data_weather.append(parser_weather_data(get_weather))
    all_data_weather = pd.concat(data_weather)
    print(all_data_weather)


if __name__ == "__main__":
    main()
