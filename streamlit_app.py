import streamlit as st
import pandas as pd
import math
from pathlib import Path

st.title('car co2 out')
st.number_input('feature_1',  min_value = 1, max_value = 10)
st.number_input('feature_2',  min_value = 1, max_value = 10)
st.number_input('feature_3',  min_value = 1, max_value = 10)
