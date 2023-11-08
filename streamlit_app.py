# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:57:34 2023

@author: Jesus
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title('Mi primera app')
n = st.slider('n', 5, 100, step = 1)
char_data = pd.DataFrame(np.random.rand(n), columns = ['data'])
st.line_chart(char_data)
