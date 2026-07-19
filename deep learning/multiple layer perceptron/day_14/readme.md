# Day 14 - ANN Practice | Binary Classification + Image Classification

## What I did today

### 1. Customer Churn Prediction (Binary Classification)
- Predicted whether a bank customer will churn (leave) or not
- Full pipeline:
  - Dropped irrelevant columns (RowNumber, CustomerId, Surname)
  - Label Encoding for Gender
  - One Hot Encoding for Geography
  - Train/Test split
  - Feature Scaling using StandardScaler
  - Built ANN using Keras (TensorFlow)
  - Tracked training with accuracy and val_accuracy plots

### 2. MNIST Digit Classification (Multiclass Image Classification)
- Classified handwritten digits (0-9) using ANN
- Full pipeline:
  - Loaded MNIST dataset directly from Keras
  - Normalized pixel values (0-255 → 0-1)
  - Used Flatten layer to convert 28×28 images to 1D vectors
  - Built ANN with Dense layers
  - Predicted digit class using `argmax`

## Datasets
- [Credit Card Customer Churn - Kaggle](https://www.kaggle.com/datasets/rjmanoj/credit-card-customer-churn-prediction)
- MNIST — built-in Keras dataset (`keras.datasets.mnist`)

## Notebooks
- [Customer Churn - Kaggle](https://www.kaggle.com/code/superviseddeep/customer-churn-self-prac)
- [MNIST Classification - Google Colab](https://colab.research.google.com/drive/1q0C6U9VrICygWElbHwiU1bcablvPxeDp?usp=drive_link)

## Tech Stack
- Python, Pandas, NumPy
- Scikit-learn (preprocessing, encoding, train/test split)
- TensorFlow / Keras (ANN)
- Matplotlib (visualizations)

## Key Learnings
- ANN for tabular data (churn) vs image data (MNIST) — same architecture, different preprocessing
- `Flatten` layer converts 2D image (28×28) to 1D vector (784) for Dense layers
- `argmax` use karte hain multiclass output se predicted class nikalne ke liye
- MNIST ek classic benchmark dataset hai — almost every DL framework pe test kiya jaata hai
- StandardScaler tabular data ke liye, normalization (÷255) image data ke liye

## Part of
[100 Days of ML Challenge](https://github.com/abhishekagrawal14/100-days-of-ml-challenge)