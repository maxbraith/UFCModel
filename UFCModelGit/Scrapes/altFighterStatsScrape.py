import requests
import bs4
from bs4 import BeautifulSoup
import re
import math
import csv
from csv import writer

#site request
url = "https://www.ufc.com/athletes/all"

querystring = {"page":"0"}

payload = ""
headers = {
    "cookie": "STYXKEY_region=USA.US.en.Default",
    "User-Agent": "insomnia/8.5.0"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)


#create soup
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('div', class_=re.compile('althelete-total'))

#get num athletes
athleteTotal = div.text.strip().split(' ')[0]
print(f"Athletes found: {athleteTotal}")

#calc number of pages to loop through - 11 fighters shown per
numPages = math.floor(int(athleteTotal)/11)
print(numPages)

linkParts = []
for i in range(numPages):
    #site request
    url = "https://www.ufc.com/athletes/all"
    querystring = {"page":f"{i}"}

    payload = ""
    headers = {
        "cookie": "STYXKEY_region=USA.US.en.Default",
        "User-Agent": "insomnia/8.5.0"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    soup = BeautifulSoup(response.content, 'html.parser')
    urlParts = soup.find_all('a', class_=re.compile("e-button--black"))



    for part in urlParts:
        href = part['href']
        if href:
            linkParts.append(href)

print(f"Fighter links found: {len(linkParts)}")
    

fighterStats = []
for part in linkParts:
    try:
        #scrape statistics
        url = f"https://www.ufc.com{part}"
        site = requests.get(url, headers=headers)

        #initalize attributes
        name = None
        nickname = None
        wins = None
        losses = None
        draws = None
        sig_str_accuracy = None
        sig_str_totals = None
        takedown_accuracy = None
        takedown_totals = None
        sig_str_per_minute = None
        takedown_avg_per_fifteen = None
        sig_str_defense = None
        knockdown_avg = None
        sig_str_absorbed_per_min = None
        submission_avg_per_fifteen = None
        takedown_defense = None
        avg_fight_time = None
        nation = None
        age = None
        height = None
        reach = None

        #soup
        soup = BeautifulSoup(site.content, 'html.parser')

        #scrape + clean name
        try:
            name = soup.find('h1', class_=re.compile('hero-profile__name')).text.strip()
        except:
            pass
        

        #scrape + clean nickname
        try:
            nick = soup.find('p', class_=re.compile('hero-profile__nickname'))
            nickname = nick.text.strip()
        except:
            pass
        #scrape + clean wins, losses, draws
        try:
            record = soup.find('p', class_=re.compile('hero-profile__division-body')).text.strip().split(' ')
            record = record[0].split('-')
            wins = record[0]
            losses = record[1]
            draws = record[2]
        except:
            pass

        #scrape + clean sig_str_accuracy + sig_str_totals + takedown_accuracy + takedown_totals
        try:
            div = soup.find_all('div', class_=re.compile("overlap-athlete-content overlap-athlete-content--horizontal"))
            stripped = div[0].text.strip().split('\n')
            clean_stripped = [item for item in stripped if item != '']
        except:
            pass
        try:
            if(clean_stripped[2].lower() == 'striking accuracy'):
                sig_str_accuracy = clean_stripped[1]
        except:
            pass
        try:
            if(clean_stripped[3].lower() == "sig. strikes landed" and clean_stripped[5].lower() == "sig. strikes attempted"):
                sig_str_totals = f"{clean_stripped[4]} of {clean_stripped[6]}"
        except:
            pass
        try:
            stripped = div[1].text.strip().split('\n')
            clean_stripped = [item for item in stripped if item != '']
        except:
            pass
        try:
            if clean_stripped[2].lower() == 'takedown accuracy':
                takedown_accuracy = clean_stripped[1]
        except:
            pass
        try:
            if clean_stripped[3].lower() == 'takedowns landed' and clean_stripped[5].lower() == "takedowns attempted":
                takedown_totals = f"{clean_stripped[4]} of {clean_stripped[6]}"
        except:
            pass



        #scrape + clean sig_str_per_minute + takedown_avg_per_fifteen + sig_str_defense + knockdown_avg

        divs = soup.find_all('div', class_=re.compile('c-stat-compare__group c-stat-compare__group-1'))

        for div in divs:
            try:
                if(div.find('div', class_=re.compile('c-stat-compare__label')).text.strip().lower() == "sig. str. landed"):
                    sig_str_per_minute = div.find('div', class_=re.compile("c-stat-compare__number")).text.strip()
            except:
                pass
            try:
                if(div.find('div', class_=re.compile('c-stat-compare__label')).text.strip().lower() == "takedown avg"):
                    takedown_avg_per_fifteen = div.find('div', class_=re.compile("c-stat-compare__number")).text.strip()
            except:
                pass
            try:
                if(div.find('div', class_=re.compile('c-stat-compare__label')).text.strip().lower() == "sig. str. defense"):
                    sig_str_defense = str(div.find('div', class_=re.compile("c-stat-compare__number")).text.strip().split("\n")[0]) +"%"
            except:
                pass
            try:
                if(div.find('div', class_=re.compile('c-stat-compare__label')).text.strip().lower() == "knockdown avg"):
                    knockdown_avg = div.find('div', class_=re.compile("c-stat-compare__number")).text.strip()
            except:
                pass


        # scrape + clean sig_str_absorbed_per_min + submission_avg_per_fifteen + takedown_defense + avg_fight_time
        divs = soup.find_all('div', re.compile('c-stat-compare__group c-stat-compare__group-2'))
        for div in divs:
            try:
                if(div.find('div', class_=re.compile('c-stat-compare__label')).text.strip().lower() == "sig. str. absorbed"):
                    sig_str_absorbed_per_min = div.find('div', class_=re.compile("c-stat-compare__number")).text.strip()
            except:
                pass
            try:
                if(div.find('div', class_=re.compile('c-stat-compare__label')).text.strip().lower() == "submission avg"):
                    submission_avg_per_fifteen = div.find('div', class_=re.compile("c-stat-compare__number")).text.strip()
            except:
                pass
            try:
                if(div.find('div', class_=re.compile('c-stat-compare__label')).text.strip().lower() == "takedown defense"):
                    takedown_defense = str(div.find('div', class_=re.compile("c-stat-compare__number")).text.strip().split('\n')[0]) +"%"
            except:
                pass
            try:
                if(div.find('div', class_=re.compile('c-stat-compare__label')).text.strip().lower() == "average fight time"):
                    avg_fight_time = div.find('div', class_=re.compile("c-stat-compare__number")).text.strip()
            except:
                pass
                


        #scrape + clean nation + age + height + reach
        divs = soup.find_all('div', class_=re.compile('c-bio__field'))

        for div in divs:
            try:
                if(div.find('div', class_=re.compile('c-bio__label')).text.strip().lower() == 'place of birth'):
                    nation = div.find('div', class_=re.compile('c-bio__text')).text.strip()
            except:
                pass
            try:
                if(div.find('div', class_=re.compile('c-bio__label')).text.strip().lower() == 'age'):
                    age = div.find('div', class_=re.compile('field field--name-age field--type-integer field--label-hidden field__item')).text.strip()
            except:
                pass
            try:
                if(div.find('div', class_=re.compile('c-bio__label')).text.strip().lower() == 'height'):
                    height = div.find('div', class_=re.compile('c-bio__text')).text.strip()
            except:
                pass
            try:
                if(div.find('div', class_=re.compile('c-bio__label')).text.strip().lower() == 'reach'):
                    reach = div.find('div', class_=re.compile('c-bio__text')).text.strip()
            except:
                pass


        print(f'Scraping {name}...')
        print(url)
        fighterStats.append([name, nickname, wins, losses, draws, height, reach, age, nation, sig_str_accuracy, sig_str_totals, takedown_accuracy, takedown_totals, sig_str_per_minute, takedown_avg_per_fifteen, sig_str_defense, knockdown_avg, sig_str_absorbed_per_min, submission_avg_per_fifteen, takedown_defense, avg_fight_time])
    except:
        pass


#create csv file

head = ['name', 'nickname' 'wins', 'losses', 'draws', 'height', 'reach', 'age', 'nation', 'sig_str_accuracy', 'sig_str_totals', 'takedown_accuracy', 'takedown_totals', 'sig_str_per_minute', 'takedown_avg_per_fifteen', 'sig_str_defense', 'knockdown_avg', 'sig_str_absorbed_per_min', 'submission_avg_per_fifteen', 'takedown_defense', 'avg_fight_time']

with open('alt_fighter_stats.csv', 'w', encoding='UTF8', newline='') as scrapedFighters:
    writer = csv.writer(scrapedFighters)
    writer.writerow(head)
    writer.writerows(fighterStats)
