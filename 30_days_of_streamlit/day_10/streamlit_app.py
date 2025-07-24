import streamlit as st


st.header("Select Box")


color = st.selectbox(
    "What is your favorite color?",
    ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet")
)
st.write("Your favorite color is ", color)
