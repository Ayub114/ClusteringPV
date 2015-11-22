# clustering.py
#
# Reads normalized power data from csv
# Transforms data into histogram format
# Uses histogram as input to k-means algorithm
#
# Input  - _cleanData.csv
# Output - _normData.csv, histPlot001.png, histPlot002.png, ...

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os.path
from matplotlib import style


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
histogram = []
for i in range(len(matrix_data)):
    temp = np.histogram(matrix_data[i, :], bins=20)
    histogram.append(temp[0])

# Run k-means algorithm for each value of k
for k in range(1, 9):
    print k
    k_means = KMeans(n_clusters=k)
    k_means.fit(histogram)
    k_means_labels = k_means.labels_
    k_means_cluster_centers = k_means.cluster_centers_

    # Set up file paths and number of sample bins
    filePath = os.path.normpath("./images/histPlot_k") + str(k) + os.sep
    numBin = 20
    x = np.linspace(0, 1, num=numBin)
    plt.style.use('ggplot')

    # Plot characteristic plots for centroid histogram values
    for i in range(len(k_means_cluster_centers)):
        plotTitle = 'Highbanks #1 Cluster profile ' + str(i)
        plt.title(plotTitle)
        plt.xlabel('Power')
        plt.ylabel('Frequency')
        axes = plt.gca()
        axes.set_xlim([0, 1])
        axes.set_ylim([0, 50])
        y = k_means_cluster_centers[i]
        plt.plot(x, y, 'r--', linewidth=2)
        fileName = filePath + "cluster%02i.png"
        plotName = (fileName % i)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')
        plt.close()

    # Plot histogram for each day using numBin bins
    for i, c in enumerate(normal_data.columns):
        clusterNum = k_means_labels[i]
        plotTitle = 'Highbanks #1 histogram ' + str(c) + ' [Cluster ' + str(clusterNum) + ']'
        plt.title(plotTitle)
        plt.xlabel('Power')
        plt.ylabel('Frequency')
        axes = plt.gca()
        axes.set_xlim([0, 1])
        axes.set_ylim([0, 50])
        y = k_means_cluster_centers[clusterNum]
        normal_data[c].hist(bins=numBin)
        plt.plot(x, y, 'r--', linewidth=2)
        fileName = filePath + str(clusterNum)+"_histPlot%03i.png"
        plotName = (fileName % i)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')
        plt.close()

