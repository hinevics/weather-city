import streamlit as st
import pandas as pd
import numpy as np
import random
import WeatherAPI as wa
DEFAULT_CITY_NAME = 'London'

dataCurrent1 = [1, 2, 3, 4]
dataHistorycal1 = [4, 3, 2, 1]

dict_test = {
    'Current':lambda city, api_key: wa.get_current(city=city, api_key=api_key), 
    'Historycal': lambda city, api_key: wa.get_historycal(city=city, api_key=api_key),
    'Forecast': lambda city, api_key: wa.get_forecast(city=city, api_key=api_key),
    }

# dict_test = {
#     'Current':WeatherAPI.get_current(city=option), 
#     'Historycal': WeatherAPI.get_historycal(city=option),
#     'Forecast': WeatherAPI.get_forecast(city=option),
#     }

option = st.sidebar.text_input(label='Write the city whose data you want to see:', value=DEFAULT_CITY_NAME)
api_key = st.sidebar.text_input(label='Enter the api key:')

st.title('Weather data')
'You selected:', option

state = st.selectbox('What kind of data do you want to see??',
                      ('Current', 'Historycal', 'Forecast'))

st.write('You selected:', state)
dt = dict_test[state](city=option, api_key=api_key)
# st.line_chart(data=dict_test[state](city=option))
col1, col2 = st.columns(2)
col1.metric(label='temp', value='{}'.format(np.mean(dt['temp'])))
col2.metric(label='pressure', value='{}'.format(np.max(dt['pressure'])))
st.image(image=dt['weather_icon'])
