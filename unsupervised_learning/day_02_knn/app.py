from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt 
from unsupervised_learning.day_02_knn.kmeans import KMeans 
import pandas as pd

# centroids = [(-5,-5),(5,5),(-2.5,2.5),(2.5,-2.5)]
# cluster_std = [1,1,1,1]

# X ,y = make_blobs(n_samples = 100 , cluster_std = cluster_std , centers = centroids , n_features = 2 , random_state = 2)

import os
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'student_clustering.csv'))
X = df.iloc[:,:].values


wcss =[]
for i in range(1,11):
    km = KMeans(n_clusters = i )
    km.fit_predict(X)
    wcss.append(km.inertia_)

# plt.plot(range(1,11),wcss)
# plt.grid()
# plt.show()


km = KMeans(n_clusters = 4 , max_iter = 300 )

y_means = km.fit_predict(X)



plt.scatter(X[y_means == 0 ,0] , X[y_means ==0 ,1],color = 'blue')
plt.scatter(X[y_means == 1 ,0] , X[y_means ==1 ,1],color = 'red')
plt.scatter(X[y_means == 2 ,0] , X[y_means ==2 ,1],color = 'green')
plt.scatter(X[y_means == 3 ,0] , X[y_means ==3 ,1],color = 'yellow')


plt.show()