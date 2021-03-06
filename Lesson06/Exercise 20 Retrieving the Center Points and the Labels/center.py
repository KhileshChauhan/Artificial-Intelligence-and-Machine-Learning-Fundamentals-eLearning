import numpy as np
from sklearn.cluster import KMeans
k_means_model = KMeans(n_clusters=3)
k_means_model.fit(data_points)
data_points = np.array([
 [1, 1],
 [1, 1.5],
 [2, 2],
 [8, 1],
 [8, 0],
 [8.5, 1],
 [6, 1],
 [1, 10],
 [1.5, 10],
 [1.5, 9.5],
 [10, 10],
 [1.5, 8.5]
])

k_means_model.cluster_centers_

k_means_model.labels_