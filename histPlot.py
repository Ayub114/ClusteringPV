# histPlot.py
#
# Reads normalized data
# Plots histogram of frequency count for each binned value of power between 0 and 1
# 20 bins are selected by default
# Fix axes so graphs can be compared
#
# Input  - _normData.csv
# Output - histPlot001.png, histPlot002.png, ...


import pandas as pd
import matplotlib.pyplot as plt


# Read data
normal_data = pd.read_csv('X:\My Documents\DABI\PycharmProjects\pvoutput\_normData.csv', index_col=0)

# Plot histogram for each day using 20 bins
plt.style.use('ggplot')
for i, c in enumerate(normal_data.columns):
    plotTitle = 'Highbanks #1 power profile ' + c
    plt.title(plotTitle)
    plt.xlabel('Power')
    plt.ylabel('Frequency')
    axes = plt.gca()
    axes.set_xlim([0, 1])
    axes.set_ylim([0, 50])
    normal_data[c].hist(bins=20)
    filename = (".\images\histPlot\histPlot%03i.png" % i)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
