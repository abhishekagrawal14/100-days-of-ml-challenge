import streamlit as st

st.title("Movie choice poll")

col1 , col2 = st.columns(2)

with col1 :
    st.header("the life of pie")
    vote1 = st.button("vote for life of pie")
    st.image("https://m.media-amazon.com/images/I/A1EdVPpeGCL.jpg" , width = 200 )

with col2 :
    st.header("masaan")
    vote2 = st.button("vote for banaras")
    st.image("https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/07/22/Incoming/Pictures/masaan_963a9233-3053-11e5-a8da-005056b4648e.jpg" , width = 200)

if vote1:
    st.success("thanks for voting for imran khan")
elif vote2 :
    st.success("thanks for voting for masaan")

name = st.sidebar.text_input("your name sir .")
movie = st.sidebar.selectbox("choose your movie sir :" , ['masaan' , 'bahubali' , 'inception' , 'life of pie'])

st.write(f"hello Mr {name} your selected movie is {movie}")
