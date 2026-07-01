# Day 03 - Agglomerative Hierarchical Clustering from Scratch

## What I did today
- Implemented Agglomerative Hierarchical Clustering algorithm from scratch in Python
- Built the full pipeline:
  - Proximity matrix construction (pairwise Euclidean distances between all points)
  - Iterative merging of closest clusters
  - Proximity matrix update after each merge
  - Label assignment to each point based on final clusters
- Implemented all 4 linkage methods:
  - **Single** - minimum distance between clusters
  - **Complete** - maximum distance between clusters
  - **Average** - mean distance between clusters
  - **Ward** - minimizes increase in total inertia after merge
- Observed the **chaining effect** of single linkage and why complete/ward gives better results
- Tested on `shopping_data.csv` with 5 clusters using ward linkage

## Files
- `agg.py` - Custom AgglomerativeClustering class implementation
- `app.py` - Script to load data, run clustering and visualize results
- `shopping_data.csv` - Dataset used for testing

## Key Learnings
- Agglomerative clustering is **bottom-up** — every point starts as its own cluster and merges happen iteratively
- Single linkage causes **chaining effect** — one giant cluster forms, not useful for real data
- Ward linkage generally gives the best results for real-world datasets
- Proximity matrix shrinks after every merge (n×n → (n-1)×(n-1))
- `update_proximity_matrix` needs revision — ward implementation is simplified, not exact