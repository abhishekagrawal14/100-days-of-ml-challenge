import streamlit as st
import requests

st.title("Live currency converter")
amount =st.number_input("enter the amount in INR"  , min_value=1)

target_currency = st.selectbox("convert to : " , ['USD','EUR' ,'GBP' , "JPY"])

if st.button("convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    responce = requests.get(url)

    if responce.status_code == 200:
        data = responce.json()
        rate = data['rates'][target_currency]
        converted = rate * amount
        st.success(f"{amount} INR = {converted:.2f}  {target_currency}")

    else :
        st.error('failed to featch conversion rate')

