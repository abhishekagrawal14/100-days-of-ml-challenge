# Day 07 - Classification Metrics | Binary & Multiclass

## What I did today
- Practiced all major classification evaluation metrics on two real-world datasets
- Binary classification on Heart Disease dataset
- Multiclass classification on Wine Quality dataset
- Compared Logistic Regression vs Random Forest on multiclass problem
- Discovered and fixed a data leakage issue

## Metrics Practiced
- **Accuracy** - overall correct predictions
- **Confusion Matrix** - TP, TN, FP, FN breakdown
- **Precision** - out of predicted positives, how many were actually positive
- **Recall** - out of actual positives, how many were correctly predicted
- **F1 Score** - harmonic mean of Precision and Recall
- **Classification Report** - per class breakdown of all metrics

## Key Findings
- Random Forest (69%) >> Logistic Regression (54%) on wine quality
- `type` column (red/white) was highly correlated with quality — caused fake 99% accuracy (data leakage)
- After removing `type`, realistic scores came — 54% LR, 69% RF
- Rare classes (quality 3, 9) get 0 precision/recall — model never predicts them due to class imbalance
- `weighted` average is better than `macro` for imbalanced datasets

## Kaggle Notebooks
- [Binary Classification - Heart Disease] 
https://www.kaggle.com/code/superviseddeep/notebook3a6b9c1724

- [Multiclass Classification - Wine Quality]
https://www.kaggle.com/code/superviseddeep/notebook71ea229ca3

## Key Learnings
- Data leakage can give fake high accuracy — always check feature correlations with target
- Accuracy alone is misleading — always check classification report
- `zero_division=0` parameter zaroori hai jab rare classes predict nahi hoti
- StandardScaler aur SimpleImputer sirf X_train pe fit karo, X_test pe sirf transform
- Random Forest handles non-linear relationships better than Logistic Regression