import joblib
from feature_engineering import add_features
from config import ALGO_PATH

algorithym = joblib.load(ALGO_PATH)

def predictor(input_df):
    y_pred = algorithym.predict(input_df)
    return y_pred

def probability(input_df):
    prob = algorithym.predict_proba(input_df)
    survival_probability =  float(prob[0][1] * 100)
    return survival_probability


