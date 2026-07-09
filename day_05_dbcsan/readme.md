# Day 05 - DBSCAN from Scratch

## What I did today
- Implemented DBSCAN (Density-Based Spatial Clustering of Applications with Noise) from scratch
- Built the full pipeline:
  - `get_neighbors` - finds all points within epsilon radius of a given point
  - `expand_cluster` - expands cluster by recursively adding density-connected points
  - `fit_predict` - main function that identifies core, border and noise points and assigns labels
- Tested on `make_moons` dataset to showcase DBSCAN's ability to find arbitrary shaped clusters

## Key Concepts
- **Core point** - has at least `min_samples` points within epsilon radius
- **Border point** - within epsilon radius of a core point but not a core point itself
- **Noise point** - neither core nor border, gets label `-1`
- **Epsilon** - radius of neighborhood
- **min_samples** - minimum points needed to form a core point

## Key Learnings
- DBSCAN does not require number of clusters beforehand (unlike KMeans)
- Noise points automatically get `-1` label — no need to handle separately
- `expand_cluster` magic — loop dynamically grows as new core point neighbors get added
- Epsilon too large → one giant cluster, too small → everything becomes noise
- DBSCAN >> KMeans for arbitrary shaped clusters (moons, circles etc.)

## Files
- `db.py` - Custom DBSCAN implementation
- `app.py` - Testing on make_moons dataset