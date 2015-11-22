# createTable.py
#
# Creates a table written to CSV file
# This is used for efficient distance metric calculation
#
# Rows    = dates
# Columns = times (in 5 minute intervals)
#
# Input  - dayData.csv
# Output - _tableData.csv

import csv
import datetime

# Set up table column headings (times)
# We want time to start from 6pm down to 8am in 5 minute intervals
# Note that this generates numbers such as 1795 which are invalid times
times = range(1800, 755, -5)

# Open file to write table data
validtimes = []
f = open('X:\My Documents\DABI\PycharmProjects\pvoutput\_tableData.csv', 'w')
f.write('date')
# Only writes valid minutes (ignores > 60)
for t in times:
    minutes = t % 100
    if minutes < 60:
        f.write(",%s" % t)
        validtimes.append(t)
f.write('\n')

# Set up table rows (dates)
dateStart = '2014-12-31'
dateEnd   = '2014-01-01'
start     = datetime.datetime.strptime(dateStart, '%Y-%m-%d')
end       = datetime.datetime.strptime(dateEnd, '%Y-%m-%d')
step      = datetime.timedelta(days=1)

# Create all valid dates between dateStart and dateEnd and save in list 'days'
days = []
while start >= end:
    date = '{:%d/%m/%y}'.format(start.date())
    days.append(date)
    start -= step

# Copy power values to table
power = []
dIndex = 0
tIndex = 0
with open('X:\My Documents\DABI\PycharmProjects\pvoutput\dayData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if days[dIndex] == row['date']:
            if (str(validtimes[tIndex]) == row['time']):
                # print row['date'] + ' ' + str(validtimes[tIndex]) + ' ' + row['time']
                power.append(row['power'])
            else:
                while str(validtimes[tIndex]) != row['time']:
                    power.append("")
                    tIndex += 1
                power.append(row['power'])
            tIndex += 1
        else:
            f.write(days[dIndex])
            for p in power:
                f.write(",%s" % p)
            f.write('\n')
            dIndex += 1
            tIndex = 1
            power = []
            power.append(row['power'])

f.close()

