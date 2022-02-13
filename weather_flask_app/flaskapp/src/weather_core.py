import json

import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

from src.getting_weather_data.weather_api import DailyHistorical


def get_graph_weather_changes_day(city: str, sdata: str, edata: str):
    """The function collects a JSON object for
    plotting temperature and precipitation changes

    Args:
        city (str): _description_
        sdata (str): _description_
        edata (str): _description_

    Returns:
        _type_: _description_
    """
    datetimes = []
    max_temps = []
    min_temps = []
    data = DailyHistorical.get_data(city=city, sdata=sdata, edata=edata)
    data = sorted(data, key=lambda x: x['datetime'])
    for obj in data:
        datetimes.append(obj['datetime'])
        max_temps.append(obj['max_temp'])
        min_temps.append(obj['min_temp'])
    # return graphJSON
    # df = pd.DataFrame({
    #     'date': datetimes,
    #     'max_temp': max_temps,
    #     'min_temp': min_temps})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=datetimes, y=max_temps,
                             mode='lines',
                             name='lines'))
    # fig.add_trace(go.Scatter())
    # fig = px.line(df, x="date", y="lifeExp", color="continent",
    #               line_group="country", hover_name="country",
    #               line_shape="spline", render_mode="svg")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print('--Ok--')
    return graphJSON


def main():
    get_graph_weather_changes_day(city='London, UK', sdata='2022-02-01', edata='2022-02-13')


if __name__ == "__main__":
    main()
