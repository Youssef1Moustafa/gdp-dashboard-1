import streamlit as st
import pandas as pd
import math
from pathlib import Path
import pickle 

st.title('car co2 out')

f1 = st.number_input('feature_1',  min_value = 1, max_value = 10)
f2 = st.number_input('feature_2',  min_value = 1, max_value = 10)
f3 = st.number_input('feature_3',  min_value = 1, max_value = 10)

