import json
import re

import pandas as pd

from config import PATH_DATASET
from WeatherAPI import Weather


def parser_weather_data(data: dict):
    res_data = {i: data['days'][0][i] for i in data['days'][0].keys()
                if not (type(data['days'][0][i]) in (dict, list))}
    return pd.DataFrame(data=[[i for i in res_data.values()]], columns=[i for i in res_data.keys()])


def main():
    data = pd.read_csv(PATH_DATASET, encoding='utf-8', sep=';', usecols=[2])
    get_weather_for_date = Weather.get_historical_weather_data(date2='2012-12-10')
    # print(data.Date.map())
    print(parser_weather_data(data))


if __name__ == "__main__":
    main()
