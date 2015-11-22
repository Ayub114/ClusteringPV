# powerPlot.py
#
# Plots power against time
# Fix axes so graphs can be compared
#
# Input  - _cleanData.csv
# Output - powerPlot001.png, powerPlot002.png, ...


import pandas as pd
import matplotlib.pyplot as plt


# Read data
clean_data = pd.read_csv('X:\My Documents\DABI\PycharmProjects\pvoutput\_cleanData.csv', index_col=0)

# Plot power data against time for each day
plt.style.use('ggplot')
for i, c in enumerate(clean_data.columns):
    plotTitle = 'Highbanks #1 power profile ' + c
    plt.ylabel('Power')
    axes = plt.gca()
    axes.set_ylim([0, 3000])
    clean_data[c].plot(title=plotTitle, color='green')
    filename = (".\images\powerPlot\powerPlot%03i.png" % i)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()