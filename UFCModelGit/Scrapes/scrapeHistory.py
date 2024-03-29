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
    print(i)
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

    #initialize attributes
    redCorner = None
    blueCorner = None
    winner = None
    event = None
    referee = None
    method_of_victory = None
    round = None
    time = None
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
    redCorner_height = None
    blueCorner_height = None
    redCorner_reach = None
    blueCorner_reach = None
    redCorner_stance = None
    blueCorner_stance = None

    #site request
    try:
        site = requests.get(i, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
    except:
        pass
    
    #scrape corners
    try:
        red_corner = soup.find_all('i', class_=re.compile('b-fight-details__charts-name b-fight-details__charts-name_pos_left js-chart-name'))
    except:
        pass
    try:
        blue_corner = soup.find_all('i', class_=re.compile('b-fight-details__charts-name b-fight-details__charts-name_pos_right js-chart-name'))
    except:
        pass

    #clean corners
    try:
        redCorner = red_corner[0].text.strip()
    except:
        pass
    try:
        blueCorner = blue_corner[0].text.strip()
    except:
        pass

    #scrape + clean winner
    try:
        divs = soup.find_all('div', class_=re.compile('b-fight-details__person'))
    except:
        pass
    try:
        if(divs[1].find('i', class_='b-fight-details__person-status b-fight-details__person-status_style_green') != None):
            winner = divs[1].find('a', class_=re.compile('b-link b-fight-details__person-link')).text.strip()
        if(divs[3].find('i', class_='b-fight-details__person-status b-fight-details__person-status_style_green') != None):
            winner = divs[3].find('a', class_=re.compile('b-link b-fight-details__person-link')).text.strip()
    except:
        pass
    
    #scrape +clean event
    try:
        event = soup.find('a', class_=re.compile('b-link')).text.strip()
    except:
        pass

    #scrape + clean method of vitory
    try:
        method_of_victory = soup.find('i', style='font-style: normal').text.strip()
    except:
        pass

    #scrape + clean referee
    try:
        referee = soup.find('span').text.strip()
    except:
        pass

    iz = soup.find_all('i', class_=re.compile('b-fight-details__text-item'))
    for j in range(len(iz)):
        details = iz[j].find('i', class_=re.compile('b-fight-details__label'))
        try:
            test = details.text.strip()
            if "Round:" in test:
                round = iz[j].text.strip().replace(' ', '').replace('R', '').replace('o', '').replace('u', '').replace('n', '').replace('d', '').replace(':', '').replace("\n", '')
            if "Time:" in test:
                unFormattedTime = iz[j].text.strip().replace(' ', '').replace('T', '').replace('i', '').replace('m', '').replace('e', '').replace(':', '').replace("\n", '')
                time = unFormattedTime[0] + ":" + unFormattedTime[1:]
        except:
            pass

    #scrape red blue stats
    try:
        ps = soup.find_all('p', class_='b-fight-details__table-text')
    except:
        pass
    
    try:
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
    except:
        pass


    try:
        #scrape redCorner/blueCorner links 
        indstatLinks = soup.find_all('a', class_=re.compile('b-link b-link_style_black'))
        redCornerLink = indstatLinks[0]
        blueCornerLink = indstatLinks[1]
        
        #clean for href
        redCornerLink = redCornerLink['href']
        blueCornerLink = blueCornerLink['href']

        response = requests.get(redCornerLink, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        #clean soup for rest of stats
        i_tags = soup.find_all('i')
        for itags in i_tags:
            itags.decompose()
        tempRest = soup.find_all('li', class_=re.compile('b-list__box-list-item b-list__box-list-item_type_block'))
        redCorner_height = tempRest[0].text.strip()
        redCorner_reach = tempRest[2].text.strip()
        redCorner_stance = tempRest[3].text.strip()

        #height, reach, stance blue
        response = requests.get(blueCornerLink, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        #clean soup for rest of stats
        i_tags = soup.find_all('i')
        for itags in i_tags:
            itags.decompose()
        tempRest = soup.find_all('li', class_=re.compile('b-list__box-list-item b-list__box-list-item_type_block'))
        blueCorner_height = tempRest[0].text.strip()
        blueCorner_reach = tempRest[2].text.strip()
        blueCorner_stance = tempRest[3].text.strip()
    except:
        pass


    fightStats.append([redCorner, blueCorner, winner, event, referee, method_of_victory, red_Knockdowns, blue_Knockdowns, red_sig_str, blue_sig_str, red_sig_str_percentage, blue_sig_str_percentage, red_total_strikes, blue_total_strikes, red_takedowns, blue_takedowns, red_takedown_percentage, blue_takedown_percentage, red_subs_attempted, blue_subs_attempted, round, time, redCorner_height, blueCorner_height, redCorner_reach, blueCorner_reach, redCorner_stance, blueCorner_stance])


    print(f'Sraping {redCorner} vs {blueCorner}...{f"{count/len(statLinks):.0%}"}')
    print(i)
    count+=1  


#create csv file

head = ['redCorner', 'blueCorner', 'winner', 'event', 'referee', 'method_of_victory', 'red_Knockdowns', 'blue_Knockdowns', 'red_sig_str', 'blue_sig_str', 'red_sig_str_percentage', 'blue_sig_str_percentage', 'red_total_strikes', 'blue_total_strikes', 'red_takedowns', 'blue_takedowns', 'red_takedown_percentage', 'blue_takedown_percentage', 'red_subs_attempted', 'blue_subs_attempted', 'round', 'time', 'red_height', 'blue_height', 'red_reach', 'blue_reach', 'red_stance', 'blue_stance']

with open('ufc_history_fight_statistics.csv', 'w', encoding='UTF8', newline='') as scrapedHistory:
    writer = csv.writer(scrapedHistory)
    writer.writerow(head)
    writer.writerows(fightStats)


    




  

