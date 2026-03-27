import streamlit as st

st.title(' my first app')
st.header('hello, i am nilesh')

name=st.text_input('enter a name')
if name:
    st.write(f'welcome {name}')

age= st.slider('select you age', 1,100,25)
st.write(f'your age is {age}')

if st.button('click me'):
    st.success('you clicked the button')
    