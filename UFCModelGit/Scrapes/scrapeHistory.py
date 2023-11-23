import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy
import math
import csv
import unidecode
from unidecode import unidecode
from csv import writer

def scrapeHistory():
    #define url and header
    url='http://ufcstats.com/statistics/events/completed?page=all'
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    
    #site request
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
   
    #scraping event dates
    eventDates = []
    event_dates = soup.find_all('span', class_=re.compile("b-statistics__date"))

    #clean dates
    for i in range(len(event_dates)):
        for j in event_dates[i]:
            eventDates.append(j.text.strip())


    eventDates = list(dict.fromkeys(eventDates))
    eventDates.pop(0)


    #scraping event names
    eventNames = []
    event_names = soup.find_all('a', class_=re.compile("b-link b-link_style_black"))

    #clean event names
    for i in range(len(event_names)):
        for j in event_names[i]:
            eventNames.append(j.text.strip())

    eventNames = list(dict.fromkeys(eventNames))

    #scrape locations
    eventLocations = []
    event_locations = soup.find_all('td', class_=re.compile("b-statistics__table-col b-statistics__table-col_style_big-top-padding"))

    #clean locations
    for i in range(len(event_locations)):
        for j in event_locations[i]:
            eventLocations.append(j.text.strip())

    eventLocations = list(dict.fromkeys(eventLocations))







    

scrapeHistory()