# bestK.py
#
# Reads normalized power data from csv
# Plots jjj graphs to determine best value of k to use
# in k-means algorithm
# Fix axes so graphs can be compared
#
# Input  - _normData.csv
# Output - elbow1.png, elbow2.png

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
from scipy.spatial.distance import cdist, pdist
from sklearn.cluster import KMeans


# Start of main program

# Read normalized data (CSV created by histPlot.py)
normal_data = pd.read_csv('X:\My Documents\DABI\PycharmProjects\pvoutput\_normData.csv', index_col=0)

# Store list of dates to identify cluster points
dates = normal_data.columns

# Transpose data frame; rows are now dates and columns are times
# Required for K-Means clustering analysis where each row (date) is an instance to be classified
# and each column (time in 5 min intervals) are the attributes of each day
transpose_data = normal_data.transpose()

# Convert to matrix form
matrix_data = transpose_data.as_matrix()

# Transform power values in to histogram form for KMeans algorithm
histo = []
for i in range(len(matrix_data)):
    temp = np.histogram(matrix_data[i, :], bins=20)
    histo.append(temp[0])

histogram = np.array(histo)

# k-means algorithm
K = range(1, 30)
KM = [KMeans(n_clusters=k).fit(histogram) for k in K]
centroids = [k.cluster_centers_ for k in KM]

D_k = [cdist(histogram, cent, 'euclidean') for cent in centroids]
cIdx = [np.argmin(D,axis=1) for D in D_k]
dist = [np.min(D,axis=1) for D in D_k]
avgWithinSS = [sum(d)/histogram.shape[0] for d in dist]

# Total with-in sum of square
wcss = [sum(d**2) for d in dist]
tss = sum(pdist(histogram)**2)/histogram.shape[0]
bss = tss-wcss
kIdx = 6-1  # visually determined at 'elbow' of curve

# Plot histogram for each day using numBin bins
filePath = os.path.normpath("./images/histPlot") + os.sep
# plt.style.use('ggplot')

# Elbow curve - average within-cluster sum of squares
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, avgWithinSS, 'm*-')
# ax.plot(K[kIdx], avgWithinSS[kIdx], marker='o', markersize=12, markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Average within-cluster sum of squares')
plt.title('Elbow for KMeans clustering')
plotName = filePath + "elbow1.png"
plt.savefig(plotName, dpi=300, bbox_inches='tight')
plt.close()

# Elbow curve - percentage of variance explained
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, bss/tss*100, 'm*-')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Percentage of variance explained')
plt.title('Elbow for KMeans clustering')
plotName = filePath + "elbow2.png"
plt.savefig(plotName, dpi=300, bbox_inches='tight')
plt.close()