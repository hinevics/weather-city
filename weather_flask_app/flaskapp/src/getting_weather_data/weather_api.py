from typing import List, Dict, Union
import json
import requests

import pandas as pd
import plotly
import plotly.express as px

from config import REQUEST_HISTORICAL_DAILY, API_KEY


class City:
    """[summary]

    Returns:
        [type]: [description]
    """
    pass


class DailyHistoricalWeatherAPI:
    REQUEST_HISTORICAL_DAILY = REQUEST_HISTORICAL_DAILY
    API_KEY = API_KEY

    @classmethod
    def get_weather_this_day_test(cls, city):
        print(city)
        df = pd.DataFrame({
            'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
                      'Bananas'], 'Amount': [4, 1, 2, 2, 4, 5],
            'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})
        fig = px.bar(df, x='Fruit', y='Amount', color='City',
                     barmode='group')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    @classmethod
    def get_hisorical_daily(cls, city: str, sdata: str, e_data: str) -> Dict[str, Union[str, float]]:
        """Weather on this day in the past years

        Args:
            today ([type]): [description]
        """
        aswer = requests.get(url=cls.REQUEST_HISTORICAL_DAILY)
        print(aswer)


def main():
    DailyHistoricalWeatherAPI.get_hisorical_daily()


if __name__ == "__main__":
    main()
