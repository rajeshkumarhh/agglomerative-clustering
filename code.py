Import pandas as pd import matplotlib.pyplot as plt
data = pd.read_excel('filename.x/sx')
data.head)
print(data.columns)
from sklearn.preprocessing import normalize
data_scaled = normalize(data)data_scaled = pd.DataFrame(data_scaled, columns = data.columns)
data_scaled.head)
import scipy.cluster.hierarchy as shc plt. figure figsize=(10, 7))
plt. title("Dendrograms")
dend = shc.dendrogram(shc.linkage(data_scaled, method=ward'))
plt. axhline(y=n, color='r, linestyle=-)
from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=2, linkage= ward')
cluster. fit_predict(data_scaled)
cluster_labels = cluster fit_predict (data_scaled)
plt. figure(figsize=(10, 7))
plt.scatter(data_scaled['column1], data_scaled|'column2'], c=cluster_labels,
cmap= viridis )
pit. title(Agglomerative Clustering of column1 and column2') plt.xlabel('column1')
plt.ylabel('column2")
plt.colorbar(label='Cluster Label')
pit.show()
