import pickle 
import streamlit as st

st.title('model')

engine_size = st.number_input('engine_size',min_value =0, max_value = 10, value = 1)
cylinder = st.number_input('CYLINDERS',min_value =0, max_value = 10, value = 1)
fuelconsumption = st.number_input('FUELCONSUMPTION_CITY',min_value =0, max_value = 10, value = 1)

with open('model.pkl', 'rb' ) as file:
  model = pickle.load(file)
output = model.predict([[engine_size, cylinder, fuelconsumption]])
st.write('co2 of car is :', output[0][0]) 
