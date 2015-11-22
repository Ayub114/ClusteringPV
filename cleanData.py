# cleanData.py
#
# Transposes the data so that columns contain the days and rows contain the time
# Reverse sorts the columns so first row is earliest time and last row is latest time
# Makes it easier for histogram plots
# Converts NaN values to 0.0
# Deletes date columns that have too many zero values due to pv panel malfunction
# Fills in missing values by using previous values
#
# Input  - _tableData.csv
# Output - _cleanData.csv


import pandas as pd
import numpy as np


# Create Pandas dataframe object by reading csv file and set 'Date' (column) as the index
data = pd.read_csv('X:\My Documents\DABI\PycharmProjects\pvoutput\_tableData.csv', index_col=0)

# Convert all objects, including strings in to numbers
data.convert_objects(convert_numeric=True)

# Transpose data frame; rows are now times and columns are dates
data = data.transpose()
data.index.names = ['Time']

# Reverse column order; earliest times first row
data = data.iloc[::-1]

# Replace all NaN with 0.0
clean_data = data.fillna(0.0)

# Drop columns that have more than 'numZeros' zeros
numZeros = 20
x = clean_data.apply(pd.value_counts).fillna(0)
x = x.iloc[:1]
for c in x:
    if float(x[c]) > numZeros:
        clean_data = clean_data.drop(c, 1)

# Replace all 0.0 with NaN to use .fillna, use .isclose since floating point representation
col = 0
last_column = len(clean_data.columns)
while col < last_column:
    colData = clean_data.ix[:, col]
    colName = colData.name
    mask = np.isclose(clean_data[colName], 0.0)
    clean_data.loc[mask, colName] = np.nan
    col += 1

# Fill in missing values. ffill - fill forwards, bfill - fill backwards
clean_data = clean_data.fillna(method='ffill')
clean_data = clean_data.fillna(method='bfill')

# Write output to _cleanData.csv
clean_data.to_csv('X:\My Documents\DABI\PycharmProjects\pvoutput\_cleanData.csv')

