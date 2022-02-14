import json

from src.getting_weather_data.weather_api import DailyHistorical
import graph_generator as gg


def get_graph_weather_changes_day(city: str, sdata: str, edata: str) -> str:
    """Changes in snow thickness and changes in maximum / minimum temperature

    Args:
        city (str): _description_
        sdata (str): _description_
        edata (str): _description_

    Returns:
        str: _description_
    """
    datetimes = []
    max_temps = []
    min_temps = []
    snows = []
    data = DailyHistorical.get_data(city=city, sdata=sdata, edata=edata)
    data = sorted(data, key=lambda x: x['datetime'])
    for obj in data:
        datetimes.append(obj['datetime'])
        max_temps.append(obj['max_temp'])
        min_temps.append(obj['min_temp'])
        snows.append(obj['snow'])
    fig = gg.multiple_axes(x=datetimes, y1=[max_temps, min_temps], y2=snows)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print('--Ok--')
    return graphJSON


def main():
    get_graph_weather_changes_day(city='London, UK', sdata='2022-02-01', edata='2022-02-13')


if __name__ == "__main__":
    main()
