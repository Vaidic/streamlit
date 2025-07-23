import streamlit as st


st.header("st.button")

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")
