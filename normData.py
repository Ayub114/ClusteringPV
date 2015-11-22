# normData.py
#
# Normalizes the power values to between 0 and 1
#
# Input  - _cleanData.csv
# Output - _normData.csv


import pandas as pd


# Read data
clean_data = pd.read_csv('X:\My Documents\DABI\PycharmProjects\pvoutput\_cleanData.csv', index_col=0)

# Normalize the data
maxValue = max(clean_data.max(numeric_only=True))
normal_data = clean_data.div(maxValue)

# Write output to _normData.csv
normal_data.to_csv('X:\My Documents\DABI\PycharmProjects\pvoutput\_normData.csv')


