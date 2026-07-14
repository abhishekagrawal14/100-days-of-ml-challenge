import streamlit as st

# the very basic layout 

st.title("Hii this is reccomendation app")
st.subheader("made with streamlit")
st.text(" welcome to the movie world")
st.write("get your next fav watch ")

# selectbox is used for dropdown

movie = st.selectbox("Your fav movie : " , ['Avatar' , 'Avengers' , 'Toy story' , 'nahi dekhta main to'])

# conditional statements . 
if (movie == 'nahi dekhta main to'):
    st.write("please choose one sir .")

else :
    st.write(f"you choosed {movie} . good choice")

st.success("ready for reccomendation ? ")

