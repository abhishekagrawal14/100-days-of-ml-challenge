# Day 14 - Customer Churn Prediction using ANN

## What I did today
- Built a complete ANN (Artificial Neural Network) pipeline for binary classification
- Predicted whether a bank customer will churn (leave) or not
- Full pipeline:
  - Dropped irrelevant columns (RowNumber, CustomerId, Surname)
  - Label Encoding for Gender
  - One Hot Encoding for Geography
  - Train/Test split
  - Feature Scaling using StandardScaler
  - Built ANN using Keras (TensorFlow)
  - Tracked training with accuracy and val_accuracy plots

## Dataset
[Credit Card Customer Churn Prediction - Kaggle](https://www.kaggle.com/datasets/rjmanoj/credit-card-customer-churn-prediction)

10,000 bank customers with features like CreditScore, Age, Balance, NumOfProducts etc.
Target: `Exited` (1 = churned, 0 = stayed)

## Kaggle Notebook
[Customer Churn - Kaggle Notebook](https://www.kaggle.com/code/superviseddeep/customer-churn-self-prac)

## Tech Stack
- Python, Pandas, NumPy
- Scikit-learn (preprocessing, train/test split)
- TensorFlow / Keras (ANN)
- Matplotlib (training curves)

## Key Learnings
- First end-to-end ANN project — from raw data to trained neural network
- Label Encoding for binary categorical (Gender), OHE for multi-class categorical (Geography)
- StandardScaler zaroori hai ANN ke liye — neural networks scaling pe sensitive hote hain
- `val_accuracy` plot se pata chalta hai model overfit ho raha hai ya nahi
- ANN classical ML models se zyada powerful hai complex patterns ke liye