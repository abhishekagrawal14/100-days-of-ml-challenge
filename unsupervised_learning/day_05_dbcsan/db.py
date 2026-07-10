import numpy as np 
import pandas as pd 

class dbscan :
    def __init__(self,epsilon = 3 , min_sample = 4 ):
        self.epsilon = epsilon
        self.min_sample = min_sample

    def fit_predict(self , X):
        labels = [-1] * X.shape[0]
        visited = [False] * X.shape[0]
        cluster_id = 0 
        for i in range(X.shape[0]):
            if visited[i] == True:
                continue 
            neighbors = self.get_neighbors(X, i)
            if len(neighbors) >= self.min_sample:
                ## anything that followed this criteria is in epsilon neighborhood of a core point so 
                ## it can either be core or border .
                labels[i] = cluster_id
                visited[i] = True
                self.expand_cluster(X, labels, visited, neighbors, cluster_id) ## expansion of a cluster .
                cluster_id+=1 ## making new clusters 

        return labels 


    def expand_cluster(self , X , labels, visited, neighbors, cluster_id):
        for neighbor in neighbors :
            if visited[neighbor] == False :
                visited[neighbor] = True
                new_neighbors = self.get_neighbors(X, neighbor)
                if len(new_neighbors)>= self.min_sample:
                    neighbors += new_neighbors ## if its a core point add its neighbors with neighbor too.
                labels[neighbor] = cluster_id 

            elif labels[neighbor] == -1:  # visited but noise tha
                labels[neighbor] = cluster_id
                    
                


    def get_neighbors(self , X , point_idx):
        neighbors = []
        for i in range (X.shape[0]):
            distance = np.sqrt(np.dot(X[i]-X[point_idx] , X[i]-X[point_idx]))
            if distance <= self.epsilon:
                neighbors.append(i)

        return neighbors 

        
