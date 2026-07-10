# Day 04 - Agglomerative Clustering on Countries of the World Dataset

## What I did today
- Applied Agglomerative Hierarchical Clustering on real-world countries dataset
- Full pipeline:
  - EDA and feature engineering
  - Handled object columns with comma as decimal separator
  - Missing value imputation using SimpleImputer (mean strategy)
  - Outlier analysis — kept genuine outliers (China, India are naturally extreme)
  - Feature scaling using RobustScaler (chosen over StandardScaler due to outliers)
  - Dendrogram to find optimal number of clusters
  - Agglomerative Clustering with Ward linkage
  - PCA for 2D visualization
  - Found closest countries to India

## Key Findings
- India and China formed their own cluster — both are extreme outliers in Population and Area
- Ward linkage gave the best results for this dataset
- RobustScaler is better than StandardScaler when genuine outliers are present

## Kaggle Notebook
https://www.kaggle.com/code/superviseddeep/notebook905be790d5

## Dataset
[Countries of the World - Kaggle](https://www.kaggle.com/datasets/fernandol/countries-of-the-world)

## Key Learnings
- Genuine outliers should not be removed — they carry real information
- RobustScaler uses median and IQR instead of mean and std — outlier resistant
- PCA visualization in 2D is just an approximation — actual clustering happens in higher dimensions
- Sometimes a country like India is so unique that it forms its own cluster — that itself is an    insight