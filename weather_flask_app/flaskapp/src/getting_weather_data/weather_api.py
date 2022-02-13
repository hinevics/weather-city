from typing import List, Dict, Union
import json

import pandas as pd
import plotly
import plotly.express as px


class City:
    """[summary]

    Returns:
        [type]: [description]
    """
    pass


class DailyHistoricalWeatherAPI:
    
    @classmethod
    def get_weather_this_day_test(cls):
        df = pd.DataFrame({
            'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
                      'Bananas'], 'Amount': [4, 1, 2, 2, 4, 5],
            'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})
        fig = px.bar(df, x='Fruit', y='Amount', color='City',
                     barmode='group')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    @classmethod
    def get_weather_this_day(cls, today: str) -> Dict[str, Union[str, float]]:
        """Weather on this day in the past years

        Args:
            today ([type]): [description]
        """
        pass
