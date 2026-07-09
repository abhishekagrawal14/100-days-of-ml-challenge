
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import numpy as np
from db import dbscan

X, y = make_moons(n_samples=300, noise=0.1, random_state=42)

model = dbscan(epsilon=0.2, min_sample=5)
labels = model.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')
plt.title('DBSCAN on Make Moons')
plt.show()
