# convertData.py
#
# Converts the data:
# Scrapes the data and discards units text (kW, kW/hr, C etc)
# Converts data values from kW to W
# Converts time format to 24 hour format
#
# Input  - Data.csv
# Output - convertData.csv


import csv


# Function to convert to 24 hour format
def convert_time(str):
    "Converts a time string in to 24 format"
    t = str.split(':')
    hour = t[0]
    minute = t[1][:-2]
    meridian = t[1][-2:]
    if (meridian == 'PM') and (int(hour) < 12):
        hour24 = int(hour) + 12
        new_time = "{:d}{:s}".format(hour24, minute)
    elif (meridian == 'PM') and (int(hour) == 12):
        new_time = "{:s}{:s}".format(hour, minute)
    elif (meridian == 'AM') and (int(hour) < 12):
        new_time = "{:s}{:s}".format(hour, minute)
    elif (meridian == 'AM') and (int(hour) == 12):
        new_time = "{:s}".format(minute)
    else:
        print 'Error'
    return new_time


# Function to convert from kW to W
def convert_kw(kw):
    "Converts kW to W values"
    kw_value = float(kw)
    w_value  = 1000 * kw_value
    return str(w_value)


# Start of main program
f = open('X:\My Documents\DABI\PycharmProjects\pvoutput\convertData.csv', 'w')
f.write('date,time,energy,efficiency,power,average,normalised,temperature\n')

with open('X:\My Documents\DABI\PycharmProjects\pvoutput\Data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tb_date        = row['date']
        tb_time        = convert_time(row['time'])
        tb_energy      = convert_kw(row['energy'][:-3])
        tb_efficiency  = row['efficiency'][:-6]
        tb_power       = row['power'][:-1]
        tb_average     = row['average'][:-1]
        tb_normalised  = row['normalised'][:-5]
        tb_temperature = row['temperature'][:-1]
        f.write(tb_date + ',' + tb_time + ',' + tb_energy + ',' + tb_efficiency + ',' + tb_power + ',')
        f.write(tb_average + ',' + tb_normalised + ',' + tb_temperature + '\n')

f.close()
