import streamlit as st
import pandas as pd
import numpy as np
import random
st.title('Hello word')

data1 = [random.random() for i in range(10)]
data2 = [random.random() for i in range(10)]

# st.write(pd.DataFrame({'first column': data1, 'second column': data2}))
# data1
# st.line_chart(pd.DataFrame({'first column': data1, 'second column': data2}))

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
df = pd.DataFrame({'first column': data1, 'second column': data2})
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option


left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")