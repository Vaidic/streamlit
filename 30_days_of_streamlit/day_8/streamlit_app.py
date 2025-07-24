from datetime import datetime, time
import streamlit as st

st.header("st.slider")

# Example 1
st.header("Slider")
age = st.slider("How old are you?", 0, 130, 25)
st.write("You are ", age, "years old")

# Example 2 
st.header("Range Slider")
values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0)
)
st.write("Values:", values)

# Example 3
st.header("Rage Time Slider")
start_time = st.slider(
    "When do you start?",
    value=(time(9, 30), time(11, 45))
)
st.write("Start time:", start_time)

# Example 3
st.header("Range Date Slider")

appointment = st.slider(
    "Schedule your appointment:",
    value=(datetime(2022, 4, 7, 12), datetime(2022, 4, 7, 13))
)

st.write("You selected:", appointment)

