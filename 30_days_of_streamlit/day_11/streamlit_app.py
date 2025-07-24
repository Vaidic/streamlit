import streamlit as st


st.header("Multi-Select Box")


colors = st.multiselect(
    "What is your favorite color?",
    ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet")
)
st.write("Your favorite color is ", colors)
