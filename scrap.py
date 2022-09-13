from bs4 import BeautifulSoup
import requests

url = 'https://www.soarr.com/for-sale/trucks/search/results?'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('div', class_ = 'unit-body')

for job in jobs:
    make_and_year = job.find('span', class_ = 'ymm').text.split()
    make=''
    for i in range(len(make_and_year)):
        if i+1 < len(make_and_year):
            make += make_and_year[i+1]+" "
                
    year = make_and_year[0]
    category = job.find('span', class_ = 'type-name').text
    odometer = job.find('div', class_ = 'item odom').text
    print(make,year,category,odometer)

print('DATA COMPLETE')