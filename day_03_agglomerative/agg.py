import numpy as np 

class AgglomerativeClustering :
    def __init__ (self , n_clusters = 2 , linkage = 'single'):
        self.n_clusters = n_clusters 
        self.linkage = linkage
        self.labels_ = None

    def fit_predict(self,X):
        # step 01 ----
        n = X.shape[0]

        self.proximity_matrix = np.zeros((n,n))

        for i in range(n):
            for j in range (n):
                self.proximity_matrix[i][j] = np.sqrt(np.dot( X[i]-X[j] , X[i]-X[j]))


       
        # step 02 ---
        clusters = [[i] for i in range(n)]

        
        # step 03 ---
        for i in range(n - self.n_clusters):
            # step a : find 2 closest clusters 
            idx1, idx2 = self.find_closest_clusters()
            
            # step b : merge them 
            clusters = self.merge_clusters(clusters, idx1, idx2)
            
            #step c : update proximity matrix
            self.update_proximity_matrix(idx1, idx2,clusters)

        # step 4 ---
        self.labels_ = np.zeros(n, dtype=int)
        for cluster_idx, cluster in enumerate(clusters):
                for point in cluster:
                    self.labels_[point] = cluster_idx
    
        return self.labels_

    def find_closest_clusters(self ):

        np.fill_diagonal(self.proximity_matrix, np.inf)
        index = np.argmin(self.proximity_matrix)  
        return np.unravel_index(index,self.proximity_matrix.shape)
    

   
    def merge_clusters(self, clusters, idx1, idx2):
        new_cluster = clusters[idx1] + clusters[idx2]  
        
        # bade index pehle remove karo (warna index shift ho jaayega)
        clusters.pop(max(idx1, idx2))
        clusters.pop(min(idx1, idx2))
        
        clusters.append(new_cluster)  
        return clusters
        

    def update_proximity_matrix(self, idx1, idx2, clusters):
        n = len(clusters)
        new_matrix = np.zeros((n, n))

        # purani matrix se idx1 aur idx2 ko chhodkar baaki indices
        old_indices = [i for i in range(len(self.proximity_matrix)) if i != idx1 and i != idx2]

        # existing distances copy karo
        for i, oi in enumerate(old_indices):
            for j, oj in enumerate(old_indices):
                new_matrix[i][j] = self.proximity_matrix[oi][oj]

        # naye merged cluster ki distances calculate karo (last row/col mein)
        for i, oi in enumerate(old_indices):
            if self.linkage == 'single':
                dist = min(self.proximity_matrix[idx1][oi],
                        self.proximity_matrix[idx2][oi])
            elif self.linkage == 'complete':
                dist = max(self.proximity_matrix[idx1][oi],
                        self.proximity_matrix[idx2][oi])
            elif self.linkage == 'average':
                dist = (self.proximity_matrix[idx1][oi] +
                    self.proximity_matrix[idx2][oi]) / 2
            elif self.linkage == 'ward':
                dist = np.sqrt((self.proximity_matrix[idx1][oi]**2 +
                            self.proximity_matrix[idx2][oi]**2) / 2)

            new_matrix[n-1][i] = dist  # last row
            new_matrix[i][n-1] = dist  # last col (symmetric)

        self.proximity_matrix = new_matrix


