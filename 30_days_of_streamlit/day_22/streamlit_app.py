import streamlit as st

st.title("st.forms")

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('order'):
    st.write('What would you like to order?')
    icecream = st.checkbox('Ice cream')
    coffee = st.checkbox('Coffee')
    cola = st.checkbox('Cola')
    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.markdown(f'''Great! Here is your order:
        Ice cream: {icecream}
        Coffee: {coffee}
        Cola: {cola}
        Coffee bean: {coffee_bean_val}
        Coffee roast: {coffee_roast_val}
        Brewing method: {brewing_val}
        Serving format: {serving_type_val}
        Milk intensity: {milk_val}
        Bring own cup: {owncup_val}
        ''')
    else:
        st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')
st.subheader('Coffee machine')

form = st.form('my_form_2')
form.write('What would you like to order?')
icecream = form.checkbox('Ice cream')
coffee = form.checkbox('Coffee')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write(f'''Selected value: {selected_val}
Ice cream: {icecream}
Coffee: {coffee}
''')    