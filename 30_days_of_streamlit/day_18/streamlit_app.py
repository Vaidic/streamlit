import streamlit as st
import pandas as pd


st.title("st.file_uploader")
st.divider()
st.header("st.file_uploader")
st.divider()
st.subheader("st.file_uploader")



uploaded_file = st.file_uploader("Upload a file")

if uploaded_file is not None:
    st.write("File name:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", uploaded_file.size)
    df= pd.read_csv(uploaded_file)
    st.subheader("Dataframe")
    st.write(df)
    st.subheader("Descriptive statistics")
    st.write(df.describe())

else: 
    st.info("Please upload a file")