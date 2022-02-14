import json

import plotly
import plotly.graph_objects as go
# import plotly.express as px
from plotly.subplots import make_subplots

from src.getting_weather_data.weather_api import DailyHistorical


def get_graph_weather_changes_city(city: str, sdata: str, edata: str) -> str:
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
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # max_temps
    fig.add_trace(
        go.Scatter(x=datetimes, y=max_temps, name="max_temp"),
        secondary_y=False,)
    # min_temps
    fig.add_trace(
        go.Scatter(x=datetimes, y=min_temps, name="min_temp"),
        secondary_y=False,)
    # snows
    fig.add_trace(
        go.Scatter(x=datetimes, y=snows, name="snow"),
        secondary_y=True,)

    # Add figure title
    fig.update_layout(
        title_text="Changes in snow thickness and changes in max/min temperature")

    # Set x-axis title
    fig.update_xaxes(title_text="date")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Temperature</b>, Celcius", secondary_y=False)
    fig.update_yaxes(title_text="<b>Accumulated snowfall</b>, mm", secondary_y=True)
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print('--Ok--')
    
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=datetimes, y=max_temps,
    #                          mode='lines',
    #                          name='max_temps'))
    # fig.add_trace(go.Scatter(x=datetimes, y=min_temps,
    #                          mode='lines',
    #                          name='min_temps'))
    # fig.add_trace(go.Scatter(x=datetimes, y=snows,
    #                          mode='lines',
    #                          name='snows'))
    # fig.add_trace(go.Scatter())
    # fig = px.line(df, x="date", y="lifeExp", color="continent",
    #               line_group="country", hover_name="country",
    #               line_shape="spline", render_mode="svg")
    return graphJSON


def main():
    get_graph_weather_changes_city(city='London, UK', sdata='2022-02-01', edata='2022-02-13')


if __name__ == "__main__":
    main()
