# createURL.py
#
# Generates a list of valid calendar dates between dateStart and dateEnd inclusive
#
# Input  - none
# Output - urls.txt


import datetime

text_file = open("urls4.txt", "w")
# Highbanks #1, Weymouth, UK PV site
# url = 'http://pvoutput.org/intraday.jsp?id=4602&sid=3642&dt='

# TC's Power Solar, Milton Keynes, UK PV site
# url = 'http://pvoutput.org/intraday.jsp?id=8138&sid=6594&dt='

# Fly Solar, Brisbane, Australia PV site
# url = 'http://pvoutput.org/intraday.jsp?id=1791&sid=31379&dt='

# Kirstyrat, Edinburgh, UK PV site
# url = 'http://pvoutput.org/intraday.jsp?id=13329&sid=11240&dt='

# WoodsideUK, Loughborough, UK PV site
url = 'http://www.pvoutput.org/intraday.jsp?id=2868&sid=2191&dt='

dateStart = '2014-12-31'
dateEnd   = '2014-10-01'
start     = datetime.datetime.strptime(dateStart, '%Y-%m-%d')
end       = datetime.datetime.strptime(dateEnd, '%Y-%m-%d')
step      = datetime.timedelta(days=1)

# Loop through all dates, append url with the date to generate web URLs
while start >= end:
    full_url = url+'{:%Y%m%d}'.format(start.date())
    text_file.write("%s\n" % full_url)
    print full_url
    start -= step

text_file.close()


