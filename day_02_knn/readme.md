# Day 02 - K-Means Clustering from Scratch

## What I did today
- Implemented K-Means clustering algorithm from scratch in Python (without using sklearn's KMeans for the core logic)
- Built the full pipeline:
  - Random centroid initialization
  - Cluster assignment based on Euclidean distance
  - Centroid update (move centroids to mean of assigned points)
  - Convergence check to stop iterations early
  - Inertia (WCSS) calculation for evaluating cluster quality
- Used the Elbow Method to find the optimal number of clusters (`k`) by plotting `k` vs inertia for k = 1 to 10
- Tested the algorithm on a real dataset (`student_clustering.csv`) and visualized the resulting clusters using `matplotlib`
- Debugged several issues along the way:
  - Module import case-sensitivity (`Kmeans` vs `kmeans`)
  - `self` parameter naming mismatch
  - File path issues when running scripts from different working directories
  - Passing the wrong data type to `fit_predict` (DataFrame vs NumPy array)
  - Missing `inertia_` attribute on the custom class

## Files
- `kmeans.py` - Custom KMeans class implementation
- `app.py` - Script to load data, run KMeans, plot elbow curve, and visualize final clusters
- `student_clustering.csv` - Dataset used for testing

## Key learnings
- Inertia (WCSS) is a single value per `k`, representing the total squared distance of all points from their assigned centroids — not one value per cluster
- K-Means results can vary across runs due to random centroid initialization (can be fixed with a seed for reproducibility)
- Working directory matters a lot when reading files with relative paths in Python