import pandas as pd
import streamlit as st
from prediction import predictor
from prediction import probability
import time 


st.title("🚢 RMS TITANIC")
st.subheader("Can You Beat History?")
st.markdown("═══════════════════════════════")
st.image("assets/titanic.gif" , width=1000)
st.markdown("═══════════════════════════════")

# st.image('https://wallpapercat.com/w/full/d/1/a/303670-3840x2160-desktop-4k-titanic-background-photo.jpg' ,use_container_width=True)

st.subheader("Let us know you")

st.markdown("--------------------------------")


# --- Inputs ---
pclass = st.selectbox("Which class are you travelling in?", [1, 2, 3])
sex = st.selectbox("how do you define yourself", ["male", "female"])
age = st.number_input("How old are you?", min_value=0, max_value=100, value=25)
sibsp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)
fare = st.number_input("How much did your ticket cost?", min_value=0.0, value=30.0 , max_value = 513.00)
embarked = st.selectbox("from where you joined ? ", ["S", "C", "Q"])
title = st.selectbox("what would you like yourself to be called", ["Mr", "Mrs", "Miss", "Master", "Rare"])
has_cabin = st.selectbox("do you have a cabin ?", ["Yes", "No"])

# --- Build raw-format single row dict ---
input_dict = {
    "PassengerId": [0],                                  # dummy, sirf drop hoga
    "Pclass": [pclass],
    "Name": [f"Passenger, {title}."],                    # regex se Title yahi se nikalega
    "Sex": [sex],
    "Age": [age],
    "SibSp": [sibsp],
    "Parch": [parch],
    "Ticket": ["0"],                                     # dummy, sirf drop hoga
    "Fare": [fare],
    "Cabin": ["C1" if has_cabin == "Yes" else None],      # sirf notna() check hota hai
    "Embarked": [embarked],
}

input_df = pd.DataFrame(input_dict)

if st.button("🚢 Predict Survival"):

    with st.spinner("🚢 Analyzing historical passenger records..."):
        time.sleep(2)
        result = predictor(input_df)
        prob = float(probability(input_df))

    st.metric("🎯 Survival Probability", f"{prob:.2f}%")
    st.progress(prob/100)

    if result[0] == 1:
        st.success("🎉 Congratulations! You would most likely have survived.")
        st.snow()
    else:
        st.error("💔 Unfortunately, You would most likely not have survived.")


    st.markdown("═══════════════════════════════")

    st.info(
        f"""
    📊 **Historical Comparison**

    Average Titanic survival rate: **32%**

    Predicted survival probability: **{prob:.2f}%**
    """
    )

    if prob > 32:
        st.success("⬆️ You had a better chance of survival than the average Titanic passenger.")

    else :
        st.warning("⬇️ Your survival chances were below the average Titanic passenger.")