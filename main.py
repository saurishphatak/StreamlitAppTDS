import streamlit as st

st.write('Enter Three Numbers')

a=st.number_input('Enter first number : ')
b=st.number_input('Enter second number : ')
c=st.number_input('Enter third number : ')

st.write('Maximum of the above 3 numbers is:',max(a,b,c))
