import streamlit as st
## widgets
 
 # botton
if st.button("find movie"): 
    st.write("finding the best choice for you ..... ")

# checkbox
add_ref = st.checkbox("find small length only")

if add_ref:
    st.success("your wish is our command sir ")

# radio
movie_genre = st.radio("pick your genre sir :" , ['adventure' , 'romance' , 'comedy'])
st.write(f" your selected movie genre is {movie_genre} ")

# selectbox
Actor = st.selectbox("Your fav Actor : ", ['RDJ' , 'Leonardo' , 'tom cruise'])
st.write(f"you love {Actor}")

# slider 
number1 = st.slider("number" , 0,10,5)
st.write(f"you selcted {number1}")

# taking number input
number2 = st.number_input("how many movies" , min_value = 1, max_value= 10 , step=1 )

st.write(f"selcted {number2} eh")

# taking text input . 
name = st.text_input("your name sir ? ")
if name :
    st.write(f"welcome Mr {name} .")

dob = st.date_input("select your date of birth")
st.write(f" your dob is {dob}")
