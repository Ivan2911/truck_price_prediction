from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests
import time

def find_jobs(page_num):
    for page in range(1,page_num+1):
        url = 'https://www.soarr.com/for-sale/trucks/search/results?page='+str(page)
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text,'lxml')
        jobs = soup.find_all('div', class_ = 'unit-body')

        for job in jobs:
            #Make
            make_and_year = job.find('span', class_ = 'ymm').text.split()
            make=''
            for i in range(len(make_and_year)):
                if i+1 < len(make_and_year):
                    make += make_and_year[i+1]+" "

            #Year            
            year = make_and_year[0]
            #Category
            category = job.find('span', class_ = 'type-name').text
            #Odometer
            odometer = job.find('div', class_ = 'item odom').text
            #Price
            price = NULL
            if job.find('div', class_='item price') is not None:
                price = job.find('div', class_='item price').text
            
            #Location
            location = job.find('span', class_ = 'dealer-loc').text.split(', ')
            city = location[0]
            state = location[1]
            #link
            sub_link = job.find('a', {'class': 'spec-link'})['href']
            link = 'https://www.soarr.com'+sub_link
            print(make,year,category,odometer, price, city, state, link)
        print('#'*50)
        print('THE END OF PAGE '+ str(page))

"""
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 0.2
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)

"""
find_jobs(3)