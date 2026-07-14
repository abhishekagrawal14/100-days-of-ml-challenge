import streamlit as st
from recommender import recommend
from config import MOVIE_LIST_PATH
import pickle

movies = pickle.load(open(MOVIE_LIST_PATH, 'rb'))

st.title("🎬 Movie Recommender System")

user_name = st.text_input("What's your name?")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    if user_name.strip() == "":
        st.warning("Please enter your name first!")
    else:
        names, posters = recommend(selected_movie)
        st.subheader(f"Hii {user_name}! 👋 Here are your suggested movies:")
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])