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

def scrapeFighterStats():
    #parse site using alphabet
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(alphabet)):
        url=f'http://ufcstats.com/statistics/fighters?char={alphabet[i]}&page=all'
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

        #site request
        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        #scrape fighters from each page
        fighterLinks = []
        fighter_links = soup.find_all('a', class_=re.compile("b-link b-link_style_black"))

        #find hrefs
        for link in fighter_links:
            href = link['href']
            if href:
                fighterLinks.append(href)
        
        

        

        





        