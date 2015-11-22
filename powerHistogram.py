# powerHistogram.py
#
# Group data by day
# Plot frequency of power values
# Histogram bin sizes are 0-20, 21-40, ... , 981-1000; this can be adjusted
# Save histogram plot as a PNG image
#
# Input  - dayData.csv
# Output - histogram of power PNG image


from array import *
import matplotlib.pyplot as plt
import csv

# Create arrays to plot power against time
p = array('i')
bins = range(0, 20)

# Current date is blank
current_date = ''
i = 1

with open('X:\My Documents\DABI\PycharmProjects\pvoutput\dayData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if current_date == row['date']:
            p.append(int(row['power']))
        elif current_date == '':
            current_date = row['date']
            p = array('i')
            p.append(int(row['power']))
        else:
            # Reverse the arrays, earliest time and power values first
            p = p[::-1]
            plt.hist(p, bins, histtype='bar', rwidth=0.8)
            title = 'Histogram for ' + str(current_date)
            plt.title(title)
            plt.xlabel('Power')
            plt.ylabel('Frequency')
            filename = (".\images\histogram2\hist_%03i.png" % i)
            plt.savefig(filename)
            plt.close()
            i += 1
            current_date = row['date']
            p = array('i')
            p.append(int(row['power']))
