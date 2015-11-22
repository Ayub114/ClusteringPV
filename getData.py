# getData.py
#
# Automatic web scraper:
# Uses external Python libraries Beautiful Soup (http://www.crummy.com/software/BeautifulSoup/)
# and Selenium (http://www.seleniumhq.org/download/)
#
# Logs on to the http://www.pvoutput.org/ website (registration needed)
# Reads each line from urls.txt and opens the corresponding web page (daily PV output table data)
# Identifies table data using XPath
#
# Captures raw data only
# Cleaning and data conversion takes place later
# Only concession is removal of commas from values in the thousands as this adversely affects
# the comma-separated data output
#
# Input  - urls.txt
# Output - Data.csv, Errors.txt


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Function to log on to PVoutput.org website
def website_logon():
    "Automatically logs on to the website"
    chromedriver = "X:\My Documents\DABI\PycharmProjects\chromedriver"
    driver       = webdriver.Chrome(chromedriver)
    driver.get("http://pvoutput.org")

    loginID     = driver.find_element_by_xpath('//*[@id="login"]')
    passwordID  = driver.find_element_by_xpath('//*[@id="password"]')
    loginButton = driver.find_element_by_xpath('/html/body/form/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/input[2]')

    loginID.send_keys('XXX')         # replace with actual username
    passwordID.send_keys('XXX')        # replace with actual password
    loginButton.send_keys(Keys.ENTER)
    return driver


# Removes thousands separator from number values
def remove_comma(thousands):
    "Removes thousands separator from number values"
    s = thousands.replace(',', '')
    return s


# Start of main program
driver = website_logon()
f = open('X:\My Documents\DABI\PycharmProjects\pvoutput\DataLE1.csv', 'w')
errorFile = open('X:\My Documents\DABI\PycharmProjects\pvoutput\Errors.txt', 'w')
f.write('date,time,energy,efficiency,power,average,normalised,temperature\n')


with open('X:\My Documents\DABI\PycharmProjects\pvoutput\urls.txt') as g:
    urls = g.readlines()

for url in urls:
    # print url
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page)
    tableStats = soup.find("table", {"id": "tb"})
    # print soup.find("table")
    for row in tableStats.findAll('tr')[2:]:
        col = row.findAll('td')

        try:
            tb_date        = col[0].string
            tb_time        = col[1].string
            tb_energy      = col[2].string
            tb_efficiency  = col[3].string
            tb_power       = remove_comma(col[4].string)
            tb_average     = remove_comma(col[5].string)
            tb_normalised  = col[6].string
            tb_temperature = col[7].string
            # ignore lines with - entries
            if col[5].string != '-':
                f.write(tb_date + ',' + tb_time + ',' + tb_energy + ',' + tb_efficiency + ',' + tb_power + ',')
                f.write(tb_average + ',' + tb_normalised + ',' + tb_temperature + '\n')

        except Exception as e:
            errorFile.write('{0} --- {1} --- {2}\n'.format(tb_date, str(e), str(col)))
            pass

f.close()
errorFile.close()
driver.close()
