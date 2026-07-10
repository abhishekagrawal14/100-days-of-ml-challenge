import pandas as pd 
from unsupervised_learning.day_02_knn.day_03_agglomerative.agg import AgglomerativeClustering
import matplotlib.pyplot as plt

data = pd.read_csv('shopping_data.csv')

X = data.iloc[:,3:5].values

model = AgglomerativeClustering(n_clusters = 5 , linkage = 'ward')

labels = model.fit_predict(X)



# visualize
for cluster in range(6):
    plt.scatter(X[labels == cluster, 0], X[labels == cluster, 1], label=f'Cluster {cluster}')

plt.legend()
plt.title('Agglomerative Clustering')
plt.show()

