import streamlit as st


st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
""")

number = st.sidebar.slider('Pick a number', 0, 10)

st.write('Selected number from slider widget is:', number)
