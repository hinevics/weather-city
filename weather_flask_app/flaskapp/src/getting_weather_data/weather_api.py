import time
import datetime
from typing import List, Dict, Union
import requests

import pandas as pd
import plotly
import plotly.express as px

from src.getting_weather_data.config import REQUEST_HISTORICAL_DAILY, API_KEY

# class Date    

class City:
    """This class is for quickly determining lat and lon
    Returns:
        [type]: [description]
    """
    pass


class DailyHistorical:
    REQUEST_HISTORICAL_DAILY = REQUEST_HISTORICAL_DAILY
    API_KEY = API_KEY

    @classmethod
    def get_data(cls, city: str, sdata: str, edata: str) -> List[Dict[str, Union[str, float, int]]]:
        """Weather on this day in the past years.
        start_date=[YYYY-MM-DD] (REQUIRED)
        end_date=[YYYY-MM-DD] (REQUIRED)
        Args:
            today ([type]): [description]
        """
        aswer = requests.get(url=cls.REQUEST_HISTORICAL_DAILY.format(
            city=city, start_date=sdata, end_date=edata, api_key=cls.API_KEY))
        result = aswer.json()['data']
        return result



def main():
    DailyHistorical.get_data(city='London, UK', sdata='2022-02-01', edata='2022-02-13')


if __name__ == "__main__":
    main()
