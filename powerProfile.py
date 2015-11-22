# powerProfile.py
#
# Plots the power profile for each day
#
# Sums the absolute differences in power values per 5 minute interval
#
# Input  - dayData.csv
# Output - powerProfile.csv


import csv

# Initialize variables
current_date = ''
current_power = 0.0
previous_power = 0.0
sum_power = 0.0

f = open('X:\My Documents\DABI\PycharmProjects\pvoutput\powerProfile.csv', 'w')
f.write('date,power profile\n')

with open('X:\My Documents\DABI\PycharmProjects\pvoutput\dayData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if current_date == '':
            current_date = row['date']
            current_power = float(row['power'])
        elif current_date == row['date']:
            previous_power = current_power
            current_power = float(row['power'])
            sum_power += abs(current_power - previous_power)
        else:
            f.write(row['date'] + ',' + str(sum_power) + '\n')
            sum_power = 0.0
            current_date = row['date']
            current_power = float(row['power'])

f.close()