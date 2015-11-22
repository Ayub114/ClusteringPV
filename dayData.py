# dayData.py
#
# Only considers data between the hours of 8am to 6pm
# Output file dayData.csv holds date, time and power values
#
# Input  - convertData.csv
# Output - dayData.csv


import csv

start_time =  800
end_time   = 1800

f = open('X:\My Documents\DABI\PycharmProjects\pvoutput\dayData.csv', 'w')
f.write('date,time,power\n')

with open('X:\My Documents\DABI\PycharmProjects\pvoutput\convertData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (int(row['time']) >= start_time) and (int(row['time']) <= end_time):
            f.write(row['date'] + ',' + row['time'] + ',' + row['power'] + '\n')

f.close()
