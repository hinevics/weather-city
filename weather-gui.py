import streamlit as st
import pandas as pd
import numpy as np
import random

DEFAULT_CITY_NAME = 'London'

dataCurrent1 = [1, 2, 3, 4]
dataHistorycal1 = [4, 3, 2, 1]

class WeatherAPI:
    @classmethod
    def get_current(cls, city:str):
        if city == 'London':
            return [(0.8**i)**i for i in dataCurrent1]
        elif city == 'Minsk':
            return [10**(-i) for i in dataCurrent1]
    
    @classmethod
    def get_historycal(cls, city:str):
        if city == 'London':
            return [2**i for i in dataCurrent1]
        elif city == 'Minsk':
            return [i**10 for i in dataCurrent1]
    
    @classmethod
    def get_forecast(cls, city:str):
        if city == 'London':
            return [(-1022)**i for i in dataCurrent1]
        elif city == 'Minsk':
            return [10**i for i in dataCurrent1]

dict_test = {
    'Current':lambda city: WeatherAPI.get_current(city=city), 
    'Historycal': lambda city: WeatherAPI.get_historycal(city=city),
    'Forecast': lambda city: WeatherAPI.get_forecast(city=city),
    }

# dict_test = {
#     'Current':WeatherAPI.get_current(city=option), 
#     'Historycal': WeatherAPI.get_historycal(city=option),
#     'Forecast': WeatherAPI.get_forecast(city=option),
#     }

option = st.sidebar.text_input(label='Write the city whose data you want to see:', value=DEFAULT_CITY_NAME)

st.title('Weather data')
'You selected:', option

state = st.selectbox('How would you like to be contacted?',
                      ('Current', 'Historycal', 'Forecast'))

st.write('You selected:', state)

st.line_chart(data=dict_test[state](city=option))
col1, col2 = st.columns(2)
col1.metric(label='Mode', value='{}'.format(np.mean(dict_test[state](city=option))))
col2.metric(label='Max', value='{}'.format(np.max(dict_test[state](city=option))))

