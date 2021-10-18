import streamlit as st
import pandas as pd
import numpy as np
import random
st.title('Hello word')

data1 = [random.random() for i in range(10)]
data2 = [random.random() for i in range(10)]

option = st.sidebar.selectbox(
    'Which number do you like best?',
     ['City1', 'City2'])

dict_test = {
    'City1': data1,
    'City2': data2
}

'You selected:', option

st.line_chart(data=dict_test[option])
col1, col2 = st.columns(2)
col1.metric('Mode', '{}'.format(np.mean(dict_test[option])))
col2.metric('Max','{}'.format(np.max(dict_test[option])))