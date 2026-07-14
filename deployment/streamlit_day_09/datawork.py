import streamlit as st
import pandas as pd

st.title("chai sales dashboard")

file =st.file_uploader("Upload your csv files" , type = ['csv'])

if file :
     df = pd.read_csv(file)
     st.subheader("Data previews")
     st.dataframe(df)

if file :
     st.subheader("summary stats")
     st.write(df.describe())

if file:
    cities =  df['City'].unique()
    selected_cities = st.selectbox("filter by cities" , cities)
    filtered_data = df[df['City']==selected_cities]
    st.dataframe(filtered_data)
