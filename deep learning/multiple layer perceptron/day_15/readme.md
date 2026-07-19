# Day 15 - Graduate Admission Prediction using ANN (Regression)

## What I did today
- Built an ANN for regression problem — predicting chance of admission for graduate students
- First time using ANN for regression (previous day was classification)
- Full pipeline:
  - Dropped irrelevant column (Serial No.)
  - No missing values, no duplicates — clean dataset
  - Train/Test split
  - Feature Scaling using StandardScaler
  - Built ANN using Keras with linear output activation (regression)
  - Tracked training with loss and val_loss plots

## Dataset
[Graduate Admissions Dataset - Kaggle](https://www.kaggle.com/datasets/mohansacharya/graduate-admissions)

500 students with features like GRE Score, TOEFL Score, CGPA, Research etc.
Target: `Chance of Admit` (continuous value between 0 and 1)

## Kaggle Notebook
[Graduate Admission Prediction using ANN](https://www.kaggle.com/code/superviseddeep/gra-prac-using-ann)

## Tech Stack
- Python, Pandas, NumPy
- Scikit-learn (preprocessing, train/test split)
- TensorFlow / Keras (ANN)
- Matplotlib (training curves)

## Key Learnings
- ANN regression vs classification — output layer activation changes (`linear` for regression, `sigmoid` for binary classification)
- Loss function changes too — `mse` for regression, `binary_crossentropy` for classification
- Clean dataset mein bhi scaling zaroori hai — ANN always needs it
- `val_loss` plot se overfitting track karte hain regression mein bhi

## Part of
[100 Days of ML Challenge](https://github.com/abhishekagrawal14/100-days-of-ml-challenge)