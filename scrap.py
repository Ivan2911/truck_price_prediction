from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests
import time

def find_jobs(page_num):
    list_output= []
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
            odometer = odometer.split()[0]
            
            #Price
            price = NULL
            if job.find('div', class_='item price') is not None:
                price = job.find('div', class_='item price').text
                price = price[1:]
            #Location
            location = job.find('span', class_ = 'dealer-loc').text.split(', ')
            city = location[0]
            state = location[1]
            #link
            sub_link = job.find('a', {'class': 'spec-link'})['href']
            link = 'https://www.soarr.com'+sub_link
            #imageLink
            #To be included
            tmp = [make,year,category,odometer, city, state, price, link]
            list_output.append(tmp)
    return list_output   

#Storing file
import csv

header = ['make','year','category','odometer', 'city', 'state', 'price', 'link']
data = find_jobs(2)

with open('truck_dataset.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
