from os import name
from pandas.core import api
import streamlit as st
import pandas as pd
import numpy as np
import random
import WeatherAPI as wa
DEFAULT_CITY_NAME = 'London'

# если api_key не введен, то выводится тект о том что api не доступно
api_key = st.sidebar.text_input(label='Enter the api key:', value='')

def current(state:str, city:str, api_key:str):
    data_request = wa.get_current(city=city, api_key=api_key)
    st.write('You selected:', state)
    # st.line_chart(data=dict_test[state](city=option))
    col1, col2 = st.columns(2)
    col1.metric(label='temp', value='{}'.format(np.mean(data_request['temp'])))
    col2.metric(label='pressure', value='{}'.format(np.max(data_request['pressure'])))
    st.image(image=data_request['weather_icon'])

def historycal(city:str, api_key:str):
    return wa.get_current(city=city, api_key=api_key)


def forecast(city:str, api_key:str):
    return wa.get_current(city=city, api_key=api_key)


if api_key == '':
    # Добавить описание того что это за app'ка
    st.text('Enter api key')
else:
    input_city = st.sidebar.text_input(label='Write the city whose data you want to see:', value=DEFAULT_CITY_NAME)

    st.title('Weather data')
    'You selected:', input_city

    state = st.selectbox('What kind of data do you want to see??',
                        ('Current', 'Historycal', 'Forecast'))
    if state == "Current":
        current(state=state, city=input_city, api_key=api_key)
    elif state == 'historycal':
        historycal(city=input_city, api_key=api_key)
    elif state == "Forecast":
        forecast(city=input_city, api_key=api_key)
    
   
