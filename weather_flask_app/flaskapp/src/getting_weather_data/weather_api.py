import pandas as pd
import json
import plotly
import plotly.express as px


class WeatherAPI:
    @classmethod
    def get_weather_this_day(cls):
        df = pd.DataFrame({
            'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
                      'Bananas'], 'Amount': [4, 1, 2, 2, 4, 5],
            'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})
        fig = px.bar(df, x='Fruit', y='Amount', color='City',
                     barmode='group')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
