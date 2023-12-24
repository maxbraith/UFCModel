import requests
from bs4 import BeautifulSoup
import re
import math
import csv
from csv import writer

#define url and header
url='http://ufcstats.com/statistics/events/completed?page=all'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

#site request
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

#scraping event dates
event_dates = []
eventDates = []
event_dates.append(soup.find_all('span', class_=re.compile("b-statistics__date")))

#clean dates
for i in range(len(event_dates)):
    for j in event_dates[i]:
        eventDates.append(j.text.strip())


eventDates = list(dict.fromkeys(eventDates))

#scrape event links
start = 1
eventLinks = []
for start in range(len(eventDates)):
    event_links = soup.find_all('a', class_=re.compile('b-link b-link_style_black'))

#clean links
for link in event_links:
    href = link['href']
    if href:
        eventLinks.append(href)
eventLinks = list(dict.fromkeys(eventLinks))
print(f'Event links found: {len(eventLinks)}')

#scrape links for satistics
statLinks = []
for i in eventLinks:
    site = requests.get(i, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    
    #scrape stat links
    stat_links = []
    stat_links = soup.find_all('a', class_=['b-flag b-flag_style_green', 'b-flag b-flag_style_bordered'])

    #clean stat links
    for link in stat_links:
        href = link['href']
        if href:
            statLinks.append(href)
statLinks = list(dict.fromkeys(statLinks)) 
print(f'Fights found: {len(statLinks)}')

#scrape stats
fightStats = []
count = 0
for i in statLinks:
    try:
        #initialize attributes
        redCorner = None
        blueCorner = None
        winner = None
        event = None
        referee = None
        method_of_victory = None
        red_Knockdowns = None
        blue_Knockdowns = None
        red_sig_str = None
        blue_sig_str = None
        red_sig_str_percentage = None
        blue_sig_str_percentage = None
        red_total_strikes = None
        blue_total_strikes = None
        red_takedowns = None
        blue_takedowns = None
        red_takedown_percentage = None
        blue_takedown_percentage = None
        red_subs_attempted = None
        blue_subs_attempted = None

        #site request
        site = requests.get(i, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        
        #scrape corners
        red_corner = soup.find_all('i', class_=re.compile('b-fight-details__charts-name b-fight-details__charts-name_pos_left js-chart-name'))
        blue_corner = soup.find_all('i', class_=re.compile('b-fight-details__charts-name b-fight-details__charts-name_pos_right js-chart-name'))
        
        #clean corners
        redCorner = red_corner[0].text.strip()
        blueCorner = blue_corner[0].text.strip()

        #scrape + clean winner
        divs = soup.find_all('div', class_=re.compile('b-fight-details__person'))
        if(divs[1].find('i', class_='b-fight-details__person-status b-fight-details__person-status_style_green') != None):
            winner = divs[1].find('a', class_=re.compile('b-link b-fight-details__person-link')).text.strip()
        if(divs[3].find('i', class_='b-fight-details__person-status b-fight-details__person-status_style_green') != None):
            winner = divs[3].find('a', class_=re.compile('b-link b-fight-details__person-link')).text.strip()

        
        #scrape +clean event
        event = soup.find('a', class_=re.compile('b-link')).text.strip()

        #scrape + clean method of vitory
        method_of_victory = soup.find('i', style='font-style: normal').text.strip()

        #scrape + clean referee
        referee = soup.find('span').text.strip()

        #scrape red blue stats
        ps = soup.find_all('p', class_='b-fight-details__table-text')

        #scrape + clean knockdowns
        red_Knockdowns = ps[2].text.strip()
        blue_Knockdowns = ps[3].text.strip()

        #scrape + clean sig strikes
        red_sig_str = ps[4].text.strip()
        blue_sig_str = ps[5].text.strip()

        #scrape + clean sig strike percentage
        red_sig_str_percentage = ps[6].text.strip()
        blue_sig_str_percentage = ps[7].text.strip()

        #scrape + clean total strikes
        red_total_strikes = ps[8].text.strip()
        blue_total_strikes = ps[9].text.strip()

        #scrape + clean takedowns
        red_takedowns = ps[10].text.strip()
        blue_takedowns = ps[11].text.strip()

        #scrape + clean takedown percentage
        red_takedown_percentage = ps[12].text.strip()
        blue_takedown_percentage = ps[13].text.strip()

        #scrape + clean
        red_subs_attempted = ps[14].text.strip()
        blue_subs_attempted = ps[15].text.strip()

        fightStats.append([redCorner, blueCorner, winner, event, referee, method_of_victory, red_Knockdowns, blue_Knockdowns, red_sig_str, blue_sig_str, red_sig_str_percentage, blue_sig_str_percentage, red_total_strikes, blue_total_strikes, red_takedowns, blue_takedowns, red_takedown_percentage, blue_takedown_percentage, red_subs_attempted, blue_subs_attempted])


        print(f'Sraping {redCorner} vs {blueCorner}...{f"{count/len(statLinks):.0%}"}')
        print(i)
        count+=1  
    except:
        pass

#create csv file

head = ['redCorner', 'blueCorner', 'winner', 'event', 'referee', 'method_of_victory', 'red_Knockdowns', 'blue_Knockdowns', 'red_sig_str', 'blue_sig_str', 'red_sig_str_percentage', 'blue_sig_str_percentage', 'red_total_strikes', 'blue_total_strikes', 'red_takedowns', 'blue_takedowns', 'red_takedown_percentage', 'blue_takedown_percentage', 'red_subs_attempted', 'blue_subs_attempted']

with open('ufc_history_fight_statistics.csv', 'w', encoding='UTF8', newline='') as scrapedHistory:
    writer = csv.writer(scrapedHistory)
    writer.writerow(head)
    writer.writerows(fightStats)



    




  

