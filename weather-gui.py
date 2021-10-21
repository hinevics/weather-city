from os import name
from pandas.core import api
import streamlit as st
import pandas as pd
import numpy as np
import random
import Weather
DEFAULT_CITY_NAME = 'London'

# если api_key не введен, то выводится тект о том что api не доступно
api_key = st.sidebar.text_input(label='Enter the api key:', value='')

def current(state:str, city:str, api_key:str):
    st.write('You selected:', state)
    data_request = Weather.get_current(city=city, api_key=api_key)
    # line 1
    cols = st.columns(3)
    # # Придумать как сделать это автоматически !!!
    cols[0].image(
        image=data_request['weather']['icon'],
        caption='{}'.format(data_request['weather']['description']))
    cols[1].metric(
        label=data_request['temp']['description'],
        value='{values}, {units}'.format(
            values=data_request['temp']['values'],
            units=data_request['temp']['units']),
            delta='{delta}{values}, {units}'.format(
                delta='-' if data_request['temp_feels_like']['values']<data_request['temp']['values'] else '+',
                values=data_request['temp_feels_like']['values'],
                units=data_request['temp_feels_like']['units']))

    cols[2].metric(
        label=data_request['pressure']['description'],
        value='{values}, {units}'.format(
            values=data_request['pressure']['values'],
            units=data_request['pressure']['units']))
    k = [i for i in data_request.keys() if not (i in ['pressure', 'temp', 'weather'])]
    for col in cols:
        for i in range(len(k)//len(cols)):
            if data_request[k[i]] != None:
                col.metric(
                    label=data_request[k[i]]['description'],
                    value='{value}, {units}'.format(
                        value=data_request[k[i]]['values'],
                        units=data_request[k[i]]['units']))
            

            
def historycal(state:str, city:str, api_key:str):
    st.write('You selected:', state)

    data_test1 = [random.random() for i in range(50)]
    st.line_chart(data=data_test1)
    # columns1
    
    col1, col2 = st.columns(2)
    col1.metric(label='temp', value='{}'.format(np.mean(data_test1)))
    col2.metric(label='pressure', value='{}'.format(np.max(data_test1)))
    # 2
    data_test2 = [random.random() for i in range(50)]
    st.line_chart(data=data_test2)
    # columns1
    col1, col2 = st.columns(2)
    col1.metric(label='temp', value='{}'.format(np.mean(data_test2)))
    col2.metric(label='pressure', value='{}'.format(np.max(data_test2)))

def forecast(city:str, api_key:str):
    return Weather.get_current(city=city, api_key=api_key)


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
    elif state == 'Historycal':
        historycal(state=state, city=input_city, api_key=api_key)
    elif state == "Forecast":
        forecast(city=input_city, api_key=api_key)
    
   
