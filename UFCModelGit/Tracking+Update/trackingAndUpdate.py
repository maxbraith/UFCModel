import requests
from bs4 import BeautifulSoup
import re
import csv
from csv import writer
import random
import time
import pandas as pd
import csv
import numpy as np
import math
import itertools
import concurrent.futures
import datetime
from datetime import date
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping

#get name of most recent database
mostRecentDatabase = input("Enter date of most recent update YYYY-MM-DD: ")

#get number of events to update the database with
numberOfEventsForUpdate = input("Enter number of events for update: ")


#scrape from freeproxy.world
url = "https://www.freeproxy.world/"
proxylist =[]
#filter through all pages
for i in range(1,75):
    print(i)
    try:
        #filter to http proxy
        querystring = {"type":"http","anonymity":"","country":"","speed":"","port":"","page":f"{i}"}

        payload = ""
        headers = {"User-Agent": "insomnia/8.4.5"}

        #site request
        site = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        soup = BeautifulSoup(site.content, 'html.parser')
        trs = soup.find_all('tr')
        for tr in trs:
            try:
                ip = tr.find('td',class_=re.compile('show-ip-div')).text.strip()
                port = tr.find('a').text.strip()
                proxylist.append(f'{ip}:{port}')
            except:
                pass
    except:
        pass
print(len(proxylist))




#scrape free proxies from proxyscrape.com
headers = {"User-Agent": "insomnia/8.4.5"}
#site request
url = 'https://proxyscrape.com/free-proxy-list'
site = requests.get(url,headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
#scrape http proxy download link
divs = soup.find_all('div', class_=re.compile('itemcard downloadcard'))
for div in divs:
    h2 = div.find('h2')
    try:
        if(h2.text.strip()=='HTTP Proxies'):
            a = div.find('a')
            download = a['download_url']
    except:
        pass

#get content of download link
try:
    site = requests.get(download,headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    #add proxies to testlist
    tempproxylist = soup.text.strip().split('\r')
    for proxy in tempproxylist:
        proxylist.append(proxy)

    print(len(proxylist))
except:
    pass    
#scrape proxies from free-proxy-list.net
url = 'https://free-proxy-list.net/'
#site + soup
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
#scrape table
try:
    table = soup.find('div', class_=re.compile('table-responsive'))
    trlabels = table.find_all('tr')
except:
    pass
#scrape proxies and add to test list
try:
    for i in trlabels:
            tdlabels = i.find_all('td')
            if(tdlabels[6].text.strip()=='yes'):
                proxylist.append(tdlabels[0].text.strip())
except:
    pass
print(len(proxylist))
#scrape proxies from hidemy.io
url = 'https://hidemy.io/en/proxy-list/'
#site request + soup
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
table = soup.find('div',class_=re.compile('table_block'))
#scrape table
trlabels = table.find_all('tr')
#scrape proxies and add to test list
for i in trlabels:
    tdlabels = i.find_all('td')
    try:

        if(tdlabels[4].text.strip()=='HTTP'):
            proxylist.append(tdlabels[0].text.strip())
    except:
        pass
print(len(proxylist))





#test proxies
workingProxies = []
def extract(proxy):
    works = False
    try:
        r = requests.get('https://www.whatismybrowser.com/detect/what-is-my-ip-address', proxies={'http':proxy, 'https':proxy}, timeout=2)
        soup = BeautifulSoup(r.content, 'html.parser')
        div = soup.find('div', class_='detected_result')
        ip = div.find('div').text.strip()
        print(f'{r}, {ip}')
        works = True
        workingProxies.append(proxy)
        with open('working_proxies.csv', 'w', encoding='UTF8', newline='') as workingProx:
            writer = csv.writer(workingProx)
            for k in workingProxies:
                writer.writerow([k])

    except:
        print(proxy)
    return works

#excecute test faster
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, list(set(proxylist)))


proxylist =[]
with open('working_proxies.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])
print(f'Proxies: {len(proxylist)}')


#ensure site is accessible
def getProxyUserAgent():
    for i in proxylist:
        #test to see if website is accessible
        userAgents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0','Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188','insomnia/8.4.5','Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36v','Mozilla/5.0 (Linux; Android 13; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15','Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1']
        userAgent = userAgents[random.randint(0,len(userAgents)-1)]
        try:
            payload = ''
            headers = {
                "cookie": "_tapology_mma_session=zo%252F9cU1na2qfRAvGf4E%252FBdxyMqNEgZbmqUYGnDxTYw%252BkgkuquO4qPimSMq%252FNc4fAxpLoIGwkl%252Fvw%252FhO04rqrL1PuS7516fTWktFyWhkz6YUy7MvWUVyjNQ7R26QYA8TeQruG5w%252B6RAj71bMME5MxoLjpSOs%252FyinaA6qsprmBZ2LnagrpzZ7bxaPvk7o%252FohTgZgxpo0FGWGaDdHERD%252B3Bt3C3ucykGOC7WB65EM8xB6C8gMNzGsvEu8FbvGnbMaoqzGzx%252FjRprzFrLN4mE5vdrJ1fsjoDV9cn5NEE2zI%253D--IkSvjCRiM5qMGaKi--o55iUwoIEhI6T8jM4UW6tA%253D%253D",
                "User-Agent": f'{userAgent}'
            }

            url = "https://www.tapology.com"
        
            #site request
            response = requests.request("GET", url, data=payload, headers=headers, proxies={'http': f"http://{i}"})
            soup = BeautifulSoup(response.content, 'html.parser')
            boutInfo = soup.find('div', class_=re.compile('right'))
            labels = boutInfo.find_all('li')
            proxyheader = [i,userAgent]
            return proxyheader
        except:
            pass
        #check to see if user agent was the issue
        try:
            userAgents.remove(userAgent)
            userAgent = userAgents[random.randint(0,len(userAgents)-1)]
            payload = ''
            headers = {'User-Agent':f'{userAgent}',
            "cookie": "_tapology_mma_session=TCLB17ieOPnBLmCBTuxpX8s3uBODZMN3jL3jBbFhwPoywfbzG7gyvp%252BAzbOk4gOZ%252FOCykOUwcpEoJBwoj2rJyiMxdHWSaiLFkBYjfuUDpZ2VY6ECFn6rpTPmUBY1Zr2anIqiklY6fz9yQlBkPAhcx%252BWSzVgsc%252B%252F8UCqkb6WnM6xr8GUikb8U2UkMVYZ3Nj1dIA0vbXpDhKykqgW%252BCnlyglp8rtdlQ37m0SaYWjLDthG7Tik3idUvGlSXFAU55zAnxz6UNncMNhTbo5ltINfso54j60i7hOq0utNOz9w%253D--ChZexYwNpevIJ%252BV8--HhKStLELFfNWYOTZIAKM6Q%253D%253D"}
            url = "https://www.tapology.com/fightcenter/bouts/2974-ufc-64-clay-the-carpenter-guida-vs-justin-pretty-boy-james"
        
            #site request
            response = requests.request("GET", url, data=payload, headers=headers, proxies={'http': f"http://{i}"})
            soup = BeautifulSoup(response.content, 'html.parser')
            boutInfo = soup.find('div', class_=re.compile('right'))
            labels = boutInfo.find_all('li')
            proxyheader = [i,userAgent]
            return proxyheader
        #if user agent is not new issue, wait for next IP
        except:
            pass
        try:
            print("Waiting for new IP...")
            ipurl = "https://ipecho.net/plain"
            ipHeader = {"User-Agent": "insomnia/8.4.5"}
            ipr = requests.request("GET", url=ipurl, headers=ipHeader)
            soup = BeautifulSoup(ipr.content, 'html.parser')
            currentIp = soup.text.strip()
            newIP = soup.text.strip()
            while(currentIp == newIP):
                ipurl = "https://ipecho.net/plain"
                ipHeader = {"User-Agent": "insomnia/8.4.5"}
                ipr = requests.request("GET", url=ipurl, headers=ipHeader)
                soup = BeautifulSoup(ipr.content, 'html.parser')
                newIP = soup.text.strip()
                time.sleep(15)
            userAgents.remove(userAgent)
            userAgent = userAgents[random.randint(0,len(userAgents)-1)]
            payload = ''
            headers = {'User-Agent':f'{userAgent}',
            "cookie": "_tapology_mma_session=TCLB17ieOPnBLmCBTuxpX8s3uBODZMN3jL3jBbFhwPoywfbzG7gyvp%252BAzbOk4gOZ%252FOCykOUwcpEoJBwoj2rJyiMxdHWSaiLFkBYjfuUDpZ2VY6ECFn6rpTPmUBY1Zr2anIqiklY6fz9yQlBkPAhcx%252BWSzVgsc%252B%252F8UCqkb6WnM6xr8GUikb8U2UkMVYZ3Nj1dIA0vbXpDhKykqgW%252BCnlyglp8rtdlQ37m0SaYWjLDthG7Tik3idUvGlSXFAU55zAnxz6UNncMNhTbo5ltINfso54j60i7hOq0utNOz9w%253D--ChZexYwNpevIJ%252BV8--HhKStLELFfNWYOTZIAKM6Q%253D%253D"}
            url = "https://www.tapology.com/fightcenter/bouts/2974-ufc-64-clay-the-carpenter-guida-vs-justin-pretty-boy-james"
        
            #site request
            response = requests.request("GET", url, data=payload, headers=headers, proxies={'http': f"http://{i}"})
            soup = BeautifulSoup(response.content, 'html.parser')
            boutInfo = soup.find('div', class_=re.compile('right'))
            labels = boutInfo.find_all('li')
            proxyheader = [i,userAgent]
            return proxyheader
        except:
            print("Maintenence required...")
            input("Press enter to continue")
            userAgents.remove(userAgent)
            userAgent = userAgents[random.randint(0,len(userAgents)-1)]
            payload = ''
            headers = {'User-Agent':f'{userAgent}',
            "cookie": "_tapology_mma_session=TCLB17ieOPnBLmCBTuxpX8s3uBODZMN3jL3jBbFhwPoywfbzG7gyvp%252BAzbOk4gOZ%252FOCykOUwcpEoJBwoj2rJyiMxdHWSaiLFkBYjfuUDpZ2VY6ECFn6rpTPmUBY1Zr2anIqiklY6fz9yQlBkPAhcx%252BWSzVgsc%252B%252F8UCqkb6WnM6xr8GUikb8U2UkMVYZ3Nj1dIA0vbXpDhKykqgW%252BCnlyglp8rtdlQ37m0SaYWjLDthG7Tik3idUvGlSXFAU55zAnxz6UNncMNhTbo5ltINfso54j60i7hOq0utNOz9w%253D--ChZexYwNpevIJ%252BV8--HhKStLELFfNWYOTZIAKM6Q%253D%253D"}
            url = "https://www.tapology.com/fightcenter/bouts/2974-ufc-64-clay-the-carpenter-guida-vs-justin-pretty-boy-james"
        
            #site request
            response = requests.request("GET", url, data=payload, headers=headers, proxies={'http': f"http://{i}"})
            soup = BeautifulSoup(response.content, 'html.parser')
            boutInfo = soup.find('div', class_=re.compile('right'))
            labels = boutInfo.find_all('li')
            proxyheader = [i,userAgent]
            return proxyheader
        

#site request
proxyheader = getProxyUserAgent()
proxy = proxyheader[0]
userAgent = proxyheader[1]
querystring = {"group":"ufc","page":1,"region":"","schedule":"results","sport":"all"}
url = 'https://www.tapology.com/fightcenter'

payload = ""
headers = {
    "cookie": "_tapology_mma_session=%252BnGrxOO8u60FBkwjnPf5U9cMUlW%252B%252F76dZtFNqnrNzBiOvQybvXmEnNM%252Fu1%252BEvOx0w4zOYLO6aIlNCfl8UnsrtSYiMl2eRJHAyiBcnd2iP0A0MCwFxGErsRcK9jbT%252BixWWetj2aX%252FvsQSBYea%252Fe73CRDIdSn95lPxaMgzhrkIGIY2KzurUSeLm0hoWxHQyq01nb7UJfYbF53mL1vhZO1yAYpprixBeuhXy70HLYlQemANkpVvl7tT0Z5DTe68LgVyn8qXKLn1hOvclfkBIfaVwBd1HyV5eIRqOMicbIQ%253D--%252BzoeexZ3ARMoGYGy--kqTFUNtOGR74GqxibycT1g%253D%253D",
    "User-Agent": f"{userAgent}"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
print(response)


#get part for url of event, range defines number of events to scrape
parts0 = []
for i in range(0, int(numberOfEventsForUpdate)):
    soup = BeautifulSoup(response.content, 'html.parser')
    az = soup.find_all('a', class_=re.compile('border-b border-tap_3 border-dotted hover:border-solid'))
    parts0.append(az[i]['href'])

parts = []
for part in parts0:
    #site request
    proxyheader = getProxyUserAgent()
    proxy = proxyheader[0]
    userAgent = proxyheader[1]
    headers = {
        "cookie": "_tapology_mma_session=SalX0GSlJmX83Xr61Esyd2IpHEnEaKZ8EYxG%252FzqzxFw61SFd5cUeTP0bI6faVXCwYrNZI%252FCI%252F8k3ulCobIDgFsfjQS0mH2Cmyrjw8uRPRid1zHpuRUdB38T9zitk9HAt06s%252BJfGPJHcaekBUI5HjpDKqJqiMNg7codsNhLvZcnHeW1FlGhcz%252BGEtmlLZDuRBcl2UPylh%252B4x97JplnC7%252FxEOXfQg51XgXLvIBL4dbuO90Cwblj7LJe3XnNpqLWcefA4r6d9gVHHKBiRN10S1K9ntnmMjzz%252FLTgDxPUBI%253D--cIDn0iKYjggibUZ3--CAvjxd4oiPcvmYyMijxPGA%253D%253D",
        "User-Agent": f'{userAgent}'
    }

    url = f'https://www.tapology.com{part}'
    print(url)
    site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
    #get url parts from all fights on the card
    soup = BeautifulSoup(site.content, 'html.parser')
    spans = soup.find_all('span', class_=re.compile('text-xs11 md:text-xs10 uppercase font-bold'))
    for span in spans:
        href = span.find('a')
        part = href['href']
        if part not in parts:
            parts.append(part)
print(parts) 


fightStats = []

for i in parts:
    proxyheader = getProxyUserAgent()
    proxy = proxyheader[0]
    userAgent = proxyheader[1]
    payload = ""
    headers = {
        "cookie": "_tapology_mma_session=6FGp%252FJUSTWYMfoxo8TfW%252BIXzLpUq7U9PMAJo5rHJA0IW5nmUvBfyvSfM1xK04kt35b9X7qEKQCxCoWu2ufxYHMbwDH88yla0%252FpzMP71n6pbfW%252FroMtWAh2n5sk9oxYFnmpfxohRaQMysmv%252B9f5fj0Omemblq8KM9NEDFiR5UPFyFXXYiM0Ee%252FWLYZ5JqObzpWnulDsrgvVtdtWFthH9vY6xz9HAvSb4KOm1HA6TvXXxYOO2Vuk6MeJwKYdwj3yqz8dV%252FHRgPknI5PsGEx3z3mxBNOJaFkRBT6iB%252B5Zo%253D--pNnhVuV4ORLaBVOE--yUSbtIv6C91epo3hOY0i5w%253D%253D",
        "User-Agent": f'{userAgent}'
    }


    url = f"https://www.tapology.com{i}"
        
    #site request
    response = requests.request("GET", url, data=payload, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
    soup = BeautifulSoup(response.content, 'html.parser')

    
    try:
        #scrape event details
        lilabels = soup.find_all('li', class_=re.compile('even:bg-tap_f2 leading-normal py-1.5 md:py-2 px-1 md:text-xs'))
    except:
        proxyheader = getProxyUserAgent()
        proxy = proxyheader[0]
        userAgent = proxyheader[1]
        payload = ""
        headers = {
            "cookie": "_tapology_mma_session=6FGp%252FJUSTWYMfoxo8TfW%252BIXzLpUq7U9PMAJo5rHJA0IW5nmUvBfyvSfM1xK04kt35b9X7qEKQCxCoWu2ufxYHMbwDH88yla0%252FpzMP71n6pbfW%252FroMtWAh2n5sk9oxYFnmpfxohRaQMysmv%252B9f5fj0Omemblq8KM9NEDFiR5UPFyFXXYiM0Ee%252FWLYZ5JqObzpWnulDsrgvVtdtWFthH9vY6xz9HAvSb4KOm1HA6TvXXxYOO2Vuk6MeJwKYdwj3yqz8dV%252FHRgPknI5PsGEx3z3mxBNOJaFkRBT6iB%252B5Zo%253D--pNnhVuV4ORLaBVOE--yUSbtIv6C91epo3hOY0i5w%253D%253D",
            "User-Agent": f'{userAgent}'
        }
        response = requests.request("GET", url, data=payload, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
        soup = BeautifulSoup(response.content, 'html.parser')
        #scrape event details
        lilabels = soup.find_all('li', class_=re.compile('even:bg-tap_f2 leading-normal py-1.5 md:py-2 px-1 md:text-xs'))

        
    print(url)
    #initialize attributes
    event = None
    date = None
    venue = None
    title_fight = 'no'
    billing = None
    winner = None
    loser = None
    winner_wins = None
    loser_wins = None
    winner_losses = None
    loser_losses = None
    winner_draws = None
    loser_draws = None
    winner_age = None
    loser_age = None
    belt_status = None
    winner_nationality = None
    loser_nationality = None
    winner_fan = None
    loser_fan = None
    fight_name = None


    for num in range(0, len(lilabels)+1):
        #scrape + clean event name
        try:
            if(lilabels[num].find('span', class_=re.compile('font-bold text-neutral-900')).text.strip() == 'Event:'):
                event = lilabels[num].find('a', class_=re.compile('link-primary-red')).text.strip()
        except:
            pass
        #scrape + clean date
        try:
            if(lilabels[num].find('span', class_=re.compile('font-bold text-neutral-900')).text.strip() == 'Date:'):
                nCleanDate = lilabels[num].find('span', class_=re.compile('text-neutral-700')).text.strip()
                dateList = nCleanDate.split(' ')
                date = dateList[1]
        except:
            pass
        #scrape + clean venue
        try:
            if(lilabels[num].find('span', class_=re.compile('font-bold text-neutral-900')).text.strip() == 'Venue:'):
                venue = lilabels[num].find('span', class_=re.compile('text-neutral-700')).text.strip()
        except:
            pass
        #scrape whether it is a title fight
        try:
            if(lilabels[num].find('span', class_=re.compile('font-bold text-neutral-90')).text.strip() == 'Title on Line:'):
                title_fight = 'yes'
        except:
            pass
        #scrape + clean billing
        try:
            if(lilabels[num].find('span', class_=re.compile('font-bold text-neutral-900')).text.strip() == 'Bout Billing:'):
                billing = lilabels[num].find('span', class_=re.compile('text-neutral-700')).text.strip()
        except:
            pass
    
    #scrape +clean winner
    try:
        winnerCheck = soup.find('span', class_=re.compile('text-lg leading-tight text-tap_3 font-bold')).text.strip()
        if('defeats' in winnerCheck):
            fighters = soup.find_all('a', class_=re.compile('link-primary-red hidden md:inline'))
            winner = fighters[0].text.strip()
            loser = fighters[1].text.strip()
    except:
        pass

    #scrape + parse table
    table = soup.find('table', class_=re.compile('md:mt-5 w-full text-center'))
    tdLabels = table.find_all('td')

    #scrape + clean winner record
    try:
        winnerRecordTempList = tdLabels[0].text.strip().split('\n')
        winnerRecord = winnerRecordTempList[0]
        winnerRecordList = winnerRecord.split('-')
        winner_wins = winnerRecordList[0]
        winner_losses = winnerRecordList[1]
        winner_draws = winnerRecordList[2]
    except:
        pass
    
    #scrape + clean loser record
    try:
        loserRecordTempList = tdLabels[5].text.strip().split('\n')
        loserRecord = loserRecordTempList[0]
        loserRecordList = loserRecord.split('-')
        loser_wins = loserRecordList[0]
        loser_losses = loserRecordList[1]
        loser_draws = loserRecordList[2]
    except:
        pass
    
    #scrape and parse table
    trLabels = table.find_all('tr')
    for tr in trLabels:
        #scrape + clean winner and loser age
        try:
            if('Age at Fight' in tr.text.strip()):
                td = tr.find_all('td')
                winner_ageTemp = td[0].text.strip().split(' ')
                winner_age = winner_ageTemp[0]
                loser_ageTemp = td[5].text.strip().split(' ')
                loser_age = loser_ageTemp[0]
        except:
            pass
        #scrape + clean nationality
        try:
            if('Nation' in tr.text.strip()):
                td = tr.find_all('td')
                winner_nationTemp = td[0].text.strip().split('\n')
                winner_nationality = winner_nationTemp[0]
                loser_nationTemp = td[4].text.strip().split('\n')
                loser_nationality = loser_nationTemp[0]
        except:
            pass
            

    #scrape + clean fight name
    try:
        fight_name = soup.find('h2', class_=re.compile('text-2xl md:text-2xl text-center font-bold text-tap_3')).text.strip()
    except:
        fight_name = soup.find('h2', class_=re.compile('text-xl md:text-2xl text-center font-bold text-tap_3')).text.strip()

    print(f'Scraping {fight_name}...')
    fightStats.append([fight_name,winner, loser, event,date,venue,title_fight,billing,winner_wins ,loser_wins ,winner_losses ,loser_losses ,winner_draws,loser_draws,winner_age ,loser_age ,belt_status ,winner_nationality ,loser_nationality ,winner_fan ,loser_fan])

     
head = ['fight','winner', 'loser', 'event','date','venue','title_fight','billing','winner_wins' ,'loser_wins' ,'winner_losses' ,'loser_losses' ,'winner_draws','loser_draws','winner_age' ,'loser_age' ,'belt_status' ,'winner_nationality' ,'loser_nationality' ,'winner_fan ','loser_fan']


with open('updateTapology.csv', 'w', encoding='UTF8', newline='') as updateTapology:
    writer = csv.writer(updateTapology)
    writer.writerow(head)
    writer.writerows(fightStats)


#define url and header
url = 'http://ufcstats.com/statistics/events/completed?page=all'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

#site request
site = requests.get(url, headers=headers)
print(site)


#soup and get hrefs
soup = BeautifulSoup(site.content, 'html.parser')
hrefs = soup.find_all('a', class_=re.compile('b-link b-link_style_black'))

#get link for most recent event
link = hrefs[0]['href']

#get part for url of event, range defines number of events to scrape
links = []
for i in range(0, int(numberOfEventsForUpdate)):
    link = hrefs[i]['href']
    links.append(link)

print(links)


stat_links = []
for link in links:
    #site request
    site = requests.get(link, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    #scrape stat links
    stat_linksTemp = soup.find_all('a', class_=['b-flag b-flag_style_green', 'b-flag b-flag_style_bordered'])
    for statLink in stat_linksTemp:
        stat_links.append(statLink)

#clean stat links
statLinks = []
for link in stat_links:
    href = link['href']
    if href:
        statLinks.append(href)


#remove dups
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
    round = None
    time = None
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
    
    #scrape + clean round and time
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
head = ['redCorner', 'blueCorner', 'winner', 'event', 'referee', 'method_of_victory', 'red_Knockdowns', 'blue_Knockdowns', 'red_sig_str', 'blue_sig_str', 'red_sig_str_percentage', 'blue_sig_str_percentage', 'red_total_strikes', 'blue_total_strikes', 'red_takedowns', 'blue_takedowns', 'red_takedown_percentage', 'blue_takedown_percentage', 'red_subs_attempted', 'blue_subs_attempted', 'round', 'time', 'redCorner_height', 'blueCorner_height', 'redCorner_reach', 'blueCorner_reach', 'redCorner_stance', 'blueCorner_stance']

with open('updateUfc_history_fight_statistics.csv', 'w', encoding='UTF8', newline='') as updateHistory:
    writer = csv.writer(updateHistory)
    writer.writerow(head)
    writer.writerows(fightStats)


#create dataframes
df = pd.read_csv('updateTapology.csv')
df2 = pd.read_csv('updateUfc_history_fight_statistics.csv')
df.head()

#match event names
for (index, row), (index2, row2) in zip(df.iterrows(), df2.iterrows()):
        if(row['event'] != row2['event']):
            df.at[index, 'event'] = row2['event']


#find special characters in df
winners = (df['winner'].values)
losers = (df['loser'].values)
fights = (df['fight'].values)
chars2rep = []
for winner in winners:
    if(isinstance(winner, str)):
        for char in winner:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
for loser in losers:
    if(isinstance(loser, str)):
        for char in loser:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
for fight in fights:
    if(isinstance(fight, str)):
        for char in fight:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
chars2rep = list(set(chars2rep))
for char in chars2rep:
    print(char)


#clean winners, losers, fights
for i in range(5):
    for index, row in df.iterrows():
        winner = row['winner']
        loser = row['loser']
        fight = row['fight']
        if(isinstance(winner, str)):
            if('ć' in winner):
                df.loc[index, 'winner'] = winner.replace('ć', 'c')
            if('ê' in winner):
                df.loc[index, 'winner'] = winner.replace('ê', 'e')
            if('Á' in winner):
                df.loc[index, 'winner'] = winner.replace('Á', 'A')
            if('Ł' in winner):
                df.loc[index, 'winner'] = winner.replace('Ł', 'L')
            if('č' in winner):
                df.loc[index, 'winner'] = winner.replace('č', 'c')
            if('ă' in winner):
                df.loc[index, 'winner'] = winner.replace('ă', 'a')
            if('á' in winner):
                df.loc[index, 'winner'] = winner.replace('á', 'a')
            if('ä' in winner):
                df.loc[index, 'winner'] = winner.replace('ä', 'a')
            if('ú' in winner):
                df.loc[index, 'winner'] = winner.replace('ú', 'u')
            if('ę' in winner):
                df.loc[index, 'winner'] = winner.replace('ę', 'e')
            if('ã' in winner):
                df.loc[index, 'winner'] = winner.replace('ã', 'a')
            if('.' in winner):
                df.loc[index, 'winner'] = winner.replace('.', '')
            if('é' in winner): 
                df.loc[index, 'winner'] = winner.replace('é', 'e')
            if('ô' in winner):
                df.loc[index, 'winner'] = winner.replace('ô', 'o')
            if("'" in winner):
                df.loc[index, 'winner'] = winner.replace("'", '')
            if('ö' in winner):
                df.loc[index, 'winner'] = winner.replace('ö', 'o')
            if('í' in winner):
                df.loc[index, 'winner'] = winner.replace('í', 'i')
            if('ř' in winner):
                df.loc[index, 'winner'] = winner.replace('ř', 'r')
            if('-' in winner):
                df.loc[index, 'winner'] = winner.replace('-', ' ')
            if('â' in winner):
                df.loc[index, 'winner'] = winner.replace('â', 'a')
            if('Ľ' in winner):
                df.loc[index, 'winner'] = winner.replace('Ľ', 'L')
            if('ţ' in winner):
                df.loc[index, 'winner'] = winner.replace('ţ', 't')
            if('ł' in winner):
                df.loc[index, 'winner'] = winner.replace('ł', 'l')
            if('õ' in winner):
                df.loc[index, 'winner'] = winner.replace('õ', 'o')
            if('š' in winner):
                df.loc[index, 'winner'] = winner.replace('š', 's')
            if('ó' in winner):
                df.loc[index, 'winner'] = winner.replace('ó', 'o')
            if('ç' in winner):
                df.loc[index, 'winner'] = winner.replace('ç', 'c')
            if('ń' in winner):
                df.loc[index, 'winner'] = winner.replace('ń', 'n')
            if('ñ' in winner):
                df.loc[index, 'winner'] = winner.replace('ñ', 'n')
            if('ž' in winner):
                df.loc[index, 'winner'] = winner.replace('ž', 'z')
        if(isinstance(loser, str)):
            if('ć' in loser):
                df.loc[index, 'loser'] = loser.replace('ć', 'c')
            if('ê' in loser):
                df.loc[index, 'loser'] = loser.replace('ê', 'e')
            if('Á' in loser):
                df.loc[index, 'loser'] = loser.replace('Á', 'A')
            if('Ł' in loser):
                df.loc[index, 'loser'] = loser.replace('Ł', 'L')
            if('č' in loser):
                df.loc[index, 'loser'] = loser.replace('č', 'c')
            if('ă' in loser):
                df.loc[index, 'loser'] = loser.replace('ă', 'a')
            if('á' in loser):
                df.loc[index, 'loser'] = loser.replace('á', 'a')
            if('ä' in loser):
                df.loc[index, 'loser'] = loser.replace('ä', 'a')
            if('ú' in loser):
                df.loc[index, 'loser'] = loser.replace('ú', 'u')
            if('ę' in loser):
                df.loc[index, 'loser'] = loser.replace('ę', 'e')
            if('ã' in loser):
                df.loc[index, 'loser'] = loser.replace('ã', 'a')
            if('.' in loser):
                df.loc[index, 'loser'] = loser.replace('.', '')
            if('é' in loser): 
                df.loc[index, 'loser'] = loser.replace('é', 'e')
            if('ô' in loser):
                df.loc[index, 'loser'] = loser.replace('ô', 'o')
            if("'" in loser):
                df.loc[index, 'loser'] = loser.replace("'", '')
            if('ö' in loser):
                df.loc[index, 'loser'] = loser.replace('ö', 'o')
            if('í' in loser):
                df.loc[index, 'loser'] = loser.replace('í', 'i')
            if('ř' in loser):
                df.loc[index, 'loser'] = loser.replace('ř', 'r')
            if('-' in loser):
                df.loc[index, 'loser'] = loser.replace('-', ' ')
            if('â' in loser):
                df.loc[index, 'loser'] = loser.replace('â', 'a')
            if('Ľ' in loser):
                df.loc[index, 'loser'] = loser.replace('Ľ', 'L')
            if('ţ' in loser):
                df.loc[index, 'loser'] = loser.replace('ţ', 't')
            if('ł' in loser):
                df.loc[index, 'loser'] = loser.replace('ł', 'l')
            if('õ' in loser):
                df.loc[index, 'loser'] = loser.replace('õ', 'o')
            if('š' in loser):
                df.loc[index, 'loser'] = loser.replace('š', 's')
            if('ó' in loser):
                df.loc[index, 'loser'] = loser.replace('ó', 'o')
            if('ç' in loser):
                df.loc[index, 'loser'] = loser.replace('ç', 'c')
            if('ń' in loser):
                df.loc[index, 'loser'] = loser.replace('ń', 'n')
            if('ñ' in loser):
                df.loc[index, 'loser'] = loser.replace('ñ', 'n')
            if('ž' in loser):
                df.loc[index, 'loser'] = loser.replace('ž', 'z')
        if(isinstance(fight, str)):
            if('ć' in fight):
                df.loc[index, 'fight'] = fight.replace('ć', 'c')
            if('ê' in fight):
                df.loc[index, 'fight'] = fight.replace('ê', 'e')
            if('Á' in fight):
                df.loc[index, 'fight'] = fight.replace('Á', 'A')
            if('Ł' in fight):
                df.loc[index, 'fight'] = fight.replace('Ł', 'L')
            if('č' in fight):
                df.loc[index, 'fight'] = fight.replace('č', 'c')
            if('ă' in fight):
                df.loc[index, 'fight'] = fight.replace('ă', 'a')
            if('á' in fight):
                df.loc[index, 'fight'] = fight.replace('á', 'a')
            if('ä' in fight):
                df.loc[index, 'fight'] = fight.replace('ä', 'a')
            if('ú' in fight):
                df.loc[index, 'fight'] = fight.replace('ú', 'u')
            if('ę' in fight):
                df.loc[index, 'fight'] = fight.replace('ę', 'e')
            if('ã' in fight):
                df.loc[index, 'fight'] = fight.replace('ã', 'a')
            if('.' in fight):
                df.loc[index, 'fight'] = fight.replace('.', '')
            if('é' in fight): 
                df.loc[index, 'fight'] = fight.replace('é', 'e')
            if('ô' in fight):
                df.loc[index, 'fight'] = fight.replace('ô', 'o')
            if("'" in fight):
                df.loc[index, 'fight'] = fight.replace("'", '')
            if('ö' in fight):
                df.loc[index, 'fight'] = fight.replace('ö', 'o')
            if('í' in fight):
                df.loc[index, 'fight'] = fight.replace('í', 'i')
            if('ř' in fight):
                df.loc[index, 'fight'] = fight.replace('ř', 'r')
            if('-' in fight):
                df.loc[index, 'fight'] = fight.replace('-', ' ')
            if('â' in fight):
                df.loc[index, 'fight'] = fight.replace('â', 'a')
            if('Ľ' in fight):
                df.loc[index, 'fight'] = fight.replace('Ľ', 'L')
            if('ţ' in fight):
                df.loc[index, 'fight'] = fight.replace('ţ', 't')
            if('ł' in fight):
                df.loc[index, 'fight'] = fight.replace('ł', 'l')
            if('õ' in fight):
                df.loc[index, 'fight'] = fight.replace('õ', 'o')
            if('š' in fight):
                df.loc[index, 'fight'] = fight.replace('š', 's')
            if('ó' in fight):
                df.loc[index, 'fight'] = fight.replace('ó', 'o')
            if('ç' in fight):
                df.loc[index, 'fight'] = fight.replace('ç', 'c')
            if('ń' in fight):
                df.loc[index, 'fight'] = fight.replace('ń', 'n')
            if('ñ' in fight):
                df.loc[index, 'fight'] = fight.replace('ñ', 'n')
            if('ž' in fight):
                df.loc[index, 'fight'] = fight.replace('ž', 'z')    
    

#find special characters in df2
redcorners = (df2['redCorner'].values)
bluecorners = (df2['blueCorner'].values)

chars2rep = []
for redCorner in redcorners:
    if(isinstance(redCorner, str)):
        for char in redCorner:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
for blueCorner in bluecorners:
    if(isinstance(blueCorner, str)):
        for char in blueCorner:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)


chars2rep = list(set(chars2rep))
for char in chars2rep:
    print(char)


#clean redCorner, blueCorner, winner
for index, row in df2.iterrows():
    redCorner = row['redCorner']
    blueCorner = row['blueCorner']
    winner = row['winner']
    if(isinstance(redCorner, str)):
        if("'" in redCorner):
            df2.loc[index, 'redCorner'] = redCorner.replace("'", '')
        if('.' in redCorner):
            df2.loc[index, 'redCorner'] = redCorner.replace('.', '')
        if('-' in redCorner):
            df2.loc[index, 'redCorner'] = redCorner.replace('-', ' ')
    if(isinstance(blueCorner, str)):
        if("'" in blueCorner):
            df2.loc[index, 'blueCorner'] = blueCorner.replace("'", '')
        if('.' in blueCorner):
            df2.loc[index, 'blueCorner'] = blueCorner.replace('.', '')
        if('-' in blueCorner):
            df2.loc[index, 'blueCorner'] = blueCorner.replace('-', ' ')
    if(isinstance(winner, str)):
        if("'" in winner):
            df2.loc[index, 'winner'] = winner.replace("'", '')
        if('.' in winner):
            df2.loc[index, 'winner'] = winner.replace('.', '')
        if('-' in winner):
            df2.loc[index, 'winner'] = winner.replace('-', ' ')
    
    
#define headers
column_headers = [
    'fight', 'redCorner', 'blueCorner', 'winner', 'event', 'referee', 'method_of_victory',
    'date', 'venue', 'title_fight', 'billing', 'redCorner_wins', 'blueCorner_wins',
    'redCorner_losses', 'blueCorner_losses', 'redCorner_draws', 'blueCorner_draws',
    'redCorner_age', 'blueCorner_age', 'redCorner_nation', 'blueCorner_nation',
    'redCorner_fan', 'blueCorner_fan', 'redCorner_knockdowns', 'blueCorner_knockdowns',
    'redCorner_sig_str', 'blueCorner_sig_str', 'redCorner_sig_str_percentage',
    'blueCorner_sig_str_percentage', 'redCorner_total_str', 'blueCorner_total_str',
    'redCorner_takedowns', 'blueCorner_takedowns', 'redCorner_takedown_percentage',
    'blueCorner_takedown_percentage', 'redCorner_subs_attempted', 'blueCorner_subs_attempted', 'round', 'time',
    'redCorner_height', 'blueCorner_height', 'redCorner_reach', 'blueCorner_reach', 'redCorner_stance', 'blueCorner_stance'
]

#create dataframe using headers
dfNew = pd.DataFrame(columns=column_headers)

dfNew.head()

#fix some inconsistencies
df2['redCorner'] = df2['redCorner'].replace('Loopy Godinez', 'Lupita Godinez', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Loopy Godinez', 'Lupita Godinez', regex=True)
df2['winner'] = df2['winner'].replace('Loopy Godinez', 'Lupita Godinez', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Viktoriia Dudakova', 'Victoria Dudakova', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Viktoriia Dudakova', 'Victoria Dudakova', regex=True)
df2['winner'] = df2['winner'].replace('Viktoriia Dudakova', 'Victoria Dudakova', regex=True)

#fight overturned - only shown in one df
index = (df['fight'] == 'Miles Johns vs Dan Argueta') & (df['date'] == '09.23.2023')
df.loc[index, 'winner'] = ''
df.loc[index, 'loser'] = ''

df2['redCorner'] = df2['redCorner'].replace('Blood Diamond', 'Mike Mathetha', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Blood Diamond', 'Mike Mathetha', regex=True)
df2['winner'] = df2['winner'].replace('Blood Diamond', 'Mike Mathetha', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Assu Almabayev', 'Asu Almabaev', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Assu Almabayev', 'Asu Almabaev', regex=True)
df2['winner'] = df2['winner'].replace('Assu Almabayev', 'Asu Almabaev', regex=True)

df['fight'] = df['fight'].replace('Carl Deaton III', 'Carl Deaton', regex=True)
df['winner'] = df['winner'].replace('Carl Deaton III', 'Carl Deaton', regex=True)
df['loser'] = df['loser'].replace('Carl Deaton III', 'Carl Deaton', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Alexander Munoz', 'Alex Munoz', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Alexander Munoz', 'Alex Munoz', regex=True)
df2['winner'] = df2['winner'].replace('Alexander Munoz', 'Alex Munoz', regex=True)

df['fight'] = df['fight'].replace('Ovince St Preux', 'Ovince Saint Preux', regex=True)
df['winner'] = df['winner'].replace('Ovince St Preux', 'Ovince Saint Preux', regex=True)
df['loser'] = df['loser'].replace('Ovince St Preux', 'Ovince Saint Preux', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Kazula Vargas', 'Rodrigo Vargas', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Kazula Vargas', 'Rodrigo Vargas', regex=True)
df2['winner'] = df2['winner'].replace('Kazula Vargas', 'Rodrigo Vargas', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Da Woon Jung', 'Da Un Jung', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Da Woon Jung', 'Da Un Jung', regex=True)
df2['winner'] = df2['winner'].replace('Da Woon Jung', 'Da Un Jung', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Lara Procopio', 'Lara Fritzen', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Lara Procopio', 'Lara Fritzen', regex=True)
df2['winner'] = df2['winner'].replace('Lara Procopio', 'Lara Fritzen', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Jacare Souza', 'Ronaldo Souza', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Jacare Souza', 'Ronaldo Souza', regex=True)
df2['winner'] = df2['winner'].replace('Jacare Souza', 'Ronaldo Souza', regex=True)

df['fight'] = df['fight'].replace('Jose Alberto Quinonez', 'Jose Quinonez', regex=True)
df['winner'] = df['winner'].replace('Jose Alberto Quinonez', 'Jose Quinonez', regex=True)
df['loser'] = df['loser'].replace('Jose Alberto Quinonez', 'Jose Quinonez', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Mara Romero Borella', 'Mara Borella', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Mara Romero Borella', 'Mara Borella', regex=True)
df2['winner'] = df2['winner'].replace('Mara Romero Borella', 'Mara Borella', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Grigory Popov', 'Grigorii Popov', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Grigory Popov', 'Grigorii Popov', regex=True)
df2['winner'] = df2['winner'].replace('Grigory Popov', 'Grigorii Popov', regex=True)

df['fight'] = df['fight'].replace('Yanan Wu', 'Wu Yanan', regex=True)
df['winner'] = df['winner'].replace('Yanan Wu', 'Wu Yanan', regex=True)
df['loser'] = df['loser'].replace('Yanan Wu', 'Wu Yanan', regex=True)

df['fight'] = df['fight'].replace('Alexey Kunchenko', 'Aleskei Kunchenko', regex=True)
df['winner'] = df['winner'].replace('Alexey Kunchenko', 'Aleskei Kunchenko', regex=True)
df['loser'] = df['loser'].replace('Alexey Kunchenko', 'Aleskei Kunchenko', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Cristiane Justino', 'Cris Cyborg', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Cristiane Justino', 'Cris Cyborg', regex=True)
df2['winner'] = df2['winner'].replace('Cristiane Justino', 'Cris Cyborg', regex=True)

df['fight'] = df['fight'].replace('Des Green', 'Desmond Green', regex=True)
df['winner'] = df['winner'].replace('Des Green', 'Desmond Green', regex=True)
df['loser'] = df['loser'].replace('Des Green', 'Desmond Green', regex=True)

df['fight'] = df['fight'].replace('Dmitry Smolyakov', 'Dmitrii Smoliakov', regex=True)
df['winner'] = df['winner'].replace('Dmitry Smolyakov', 'Dmitrii Smoliakov', regex=True)
df['loser'] = df['loser'].replace('Dmitry Smolyakov', 'Dmitrii Smoliakov', regex=True)

df['fight'] = df['fight'].replace('Ulka Sasaki', 'Yuta Sasaki', regex=True)
df['winner'] = df['winner'].replace('Ulka Sasaki', 'Yuta Sasaki', regex=True)
df['loser'] = df['loser'].replace('Ulka Sasaki', 'Yuta Sasaki', regex=True)

df['fight'] = df['fight'].replace('Roberto Sanchez', 'Robert Sanchez', regex=True)
df['winner'] = df['winner'].replace('Roberto Sanchez', 'Robert Sanchez', regex=True)
df['loser'] = df['loser'].replace('Roberto Sanchez', 'Robert Sanchez', regex=True)

df['fight'] = df['fight'].replace('Dmitriy Sosnovskiy', 'Dmitry Sosnovskiy', regex=True)
df['winner'] = df['winner'].replace('Dmitriy Sosnovskiy', 'Dmitry Sosnovskiy', regex=True)
df['loser'] = df['loser'].replace('Dmitriy Sosnovskiy', 'Dmitry Sosnovskiy', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Timothy Johnson', 'Tim Johnson', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Timothy Johnson', 'Tim Johnson', regex=True)
df2['winner'] = df2['winner'].replace('Timothy Johnson', 'Tim Johnson', regex=True)

df['fight'] = df['fight'].replace('Maia Kahaunaele', 'Maia Stevenson', regex=True)
df['winner'] = df['winner'].replace('Maia Kahaunaele', 'Maia Stevenson', regex=True)
df['loser'] = df['loser'].replace('Maia Kahaunaele', 'Maia Stevenson', regex=True)

df['fight'] = df['fight'].replace('Bharat Khandare', 'Bharat Kandare', regex=True)
df['winner'] = df['winner'].replace('Bharat Khandare', 'Bharat Kandare', regex=True)
df['loser'] = df['loser'].replace('Bharat Khandare', 'Bharat Kandare', regex=True)

df['fight'] = df['fight'].replace('Nico Musoke', 'Nicholas Musoke', regex=True)
df['winner'] = df['winner'].replace('Nico Musoke', 'Nicholas Musoke', regex=True)
df['loser'] = df['loser'].replace('Nico Musoke', 'Nicholas Musoke', regex=True)

#fight overturned
index = (df['fight'] == 'Alex Morono vs Niko Price') & (df['date'] == '02.04.2017')
df.loc[index, 'winner'] = ''
df.loc[index, 'loser'] = ''

df2['redCorner'] = df2['redCorner'].replace('Joseph Gigliotti', 'Joe Gigliotti', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Joseph Gigliotti', 'Joe Gigliotti', regex=True)
df2['winner'] = df2['winner'].replace('Joseph Gigliotti', 'Joe Gigliotti', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Tiago dos Santos e Silva', 'Tiago Trator', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Tiago dos Santos e Silva', 'Tiago Trator', regex=True)
df2['winner'] = df2['winner'].replace('Tiago dos Santos e Silva', 'Tiago Trator', regex=True)

df['fight'] = df['fight'].replace('Manny Gamburyan', 'Manvel Gamburyan', regex=True)
df['winner'] = df['winner'].replace('Manny Gamburyan', 'Manvel Gamburyan', regex=True)
df['loser'] = df['loser'].replace('Manny Gamburyan', 'Manvel Gamburyan', regex=True)

df['fight'] = df['fight'].replace('Mike Graves', 'Michael Graves', regex=True)
df['winner'] = df['winner'].replace('Mike Graves', 'Michael Graves', regex=True)
df['loser'] = df['loser'].replace('Mike Graves', 'Michael Graves', regex=True)

df['fight'] = df['fight'].replace('Marcio Alexandre Jr', 'Marcio Alexandre Junior', regex=True)
df['winner'] = df['winner'].replace('Marcio Alexandre Jr', 'Marcio Alexandre Junior', regex=True)
df['loser'] = df['loser'].replace('Marcio Alexandre Jr', 'Marcio Alexandre Junior', regex=True)

df['fight'] = df['fight'].replace('Steven Kennedy', 'Steve Kennedy', regex=True)
df['winner'] = df['winner'].replace('Steven Kennedy', 'Steve Kennedy', regex=True)
df['loser'] = df['loser'].replace('Steven Kennedy', 'Steve Kennedy', regex=True)

df['fight'] = df['fight'].replace('Ronald Stallings', 'Ron Stallings', regex=True)
df['winner'] = df['winner'].replace('Ronald Stallings', 'Ron Stallings', regex=True)
df['loser'] = df['loser'].replace('Ronald Stallings', 'Ron Stallings', regex=True)

df['fight'] = df['fight'].replace('Tony Christodoulou', 'Anthony Christodoulou', regex=True)
df['winner'] = df['winner'].replace('Tony Christodoulou', 'Anthony Christodoulou', regex=True)
df['loser'] = df['loser'].replace('Tony Christodoulou', 'Anthony Christodoulou', regex=True)

df['fight'] = df['fight'].replace('Costas Philippou', 'Constantinos Philippou', regex=True)
df['winner'] = df['winner'].replace('Costas Philippou', 'Constantinos Philippou', regex=True)
df['loser'] = df['loser'].replace('Costas Philippou', 'Constantinos Philippou', regex=True)

df['fight'] = df['fight'].replace('Alp Ozkilic', 'Alptekin Ozkilic', regex=True)
df['winner'] = df['winner'].replace('Alp Ozkilic', 'Alptekin Ozkilic', regex=True)
df['loser'] = df['loser'].replace('Alp Ozkilic', 'Alptekin Ozkilic', regex=True)

df['fight'] = df['fight'].replace('Robbie Peralta', 'Robert Peralta', regex=True)
df['winner'] = df['winner'].replace('Robbie Peralta', 'Robert Peralta', regex=True)
df['loser'] = df['loser'].replace('Robbie Peralta', 'Robert Peralta', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Elizeu Zaleski dos Santos', 'Elizeu Zaleski', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Elizeu Zaleski dos Santos', 'Elizeu Zaleski', regex=True)
df2['winner'] = df2['winner'].replace('Elizeu Zaleski dos Santos', 'Elizeu Zaleski', regex=True)

#fight overturned
index = (df['fight'] == 'Norifumi Yamamoto vs Roman Salazar') & (df['date'] == '02.28.2015')
df.loc[index, 'winner'] = ''
df.loc[index, 'loser'] = ''

df['fight'] = df['fight'].replace('Alexander Torres', 'Alex Torres', regex=True)
df['winner'] = df['winner'].replace('Alexander Torres', 'Alex Torres', regex=True)
df['loser'] = df['loser'].replace('Alexander Torres', 'Alex Torres', regex=True)

df['fight'] = df['fight'].replace('Pat Walsh', 'Patrick Walsh', regex=True)
df['winner'] = df['winner'].replace('Pat Walsh', 'Patrick Walsh', regex=True)
df['loser'] = df['loser'].replace('Pat Walsh', 'Patrick Walsh', regex=True)

df['fight'] = df['fight'].replace('Zhumabek Tursyn', 'Jumabieke Tuerxun', regex=True)
df['winner'] = df['winner'].replace('Zhumabek Tursyn', 'Jumabieke Tuerxun', regex=True)
df['loser'] = df['loser'].replace('Zhumabek Tursyn', 'Jumabieke Tuerxun', regex=True)

df['fight'] = df['fight'].replace('Dan Spohn', 'Daniel Spohn', regex=True)
df['winner'] = df['winner'].replace('Dan Spohn', 'Daniel Spohn', regex=True)
df['loser'] = df['loser'].replace('Dan Spohn', 'Daniel Spohn', regex=True)

df['fight'] = df['fight'].replace('Guilherme Bomba', 'Guilherme Vasconcelos', regex=True)
df['winner'] = df['winner'].replace('Guilherme Bomba', 'Guilherme Vasconcelos', regex=True)
df['loser'] = df['loser'].replace('Guilherme Bomba', 'Guilherme Vasconcelos', regex=True)

df['fight'] = df['fight'].replace('Bubba McDaniel', 'Robert McDaniel', regex=True)
df['winner'] = df['winner'].replace('Bubba McDaniel', 'Robert McDaniel', regex=True)
df['loser'] = df['loser'].replace('Bubba McDaniel', 'Robert McDaniel', regex=True)

#fight overturned
index = (df['fight'] == 'Louis Gaudinot vs Phil Harris') & (df['date'] == '03.08.2014')
df.loc[index, 'winner'] = ''
df.loc[index, 'loser'] = ''

df['fight'] = df['fight'].replace('Benny Alloway', 'Ben Alloway', regex=True)
df['winner'] = df['winner'].replace('Benny Alloway', 'Ben Alloway', regex=True)
df['loser'] = df['loser'].replace('Benny Alloway', 'Ben Alloway', regex=True)

df['fight'] = df['fight'].replace('Phil De Fries', 'Philip De Fries', regex=True)
df['winner'] = df['winner'].replace('Phil De Fries', 'Philip De Fries', regex=True)
df['loser'] = df['loser'].replace('Phil De Fries', 'Philip De Fries', regex=True)

df['fight'] = df['fight'].replace('Matt Riddle', 'Matthew Riddle', regex=True)
df['winner'] = df['winner'].replace('Matt Riddle', 'Matthew Riddle', regex=True)
df['loser'] = df['loser'].replace('Matt Riddle', 'Matthew Riddle', regex=True)

df['fight'] = df['fight'].replace('Manny Rodriguez', 'Manuel Rodriguez', regex=True)
df['winner'] = df['winner'].replace('Manny Rodriguez', 'Manuel Rodriguez', regex=True)
df['loser'] = df['loser'].replace('Manny Rodriguez', 'Manuel Rodriguez', regex=True)

df['fight'] = df['fight'].replace('John Olav Einemo', 'Jon Olav Einemo', regex=True)
df['winner'] = df['winner'].replace('John Olav Einemo', 'Jon Olav Einemo', regex=True)
df['loser'] = df['loser'].replace('John Olav Einemo', 'Jon Olav Einemo', regex=True)

df['fight'] = df['fight'].replace('Kimbo Slice', 'Kevin Ferguson', regex=True)
df['winner'] = df['winner'].replace('Kimbo Slice', 'Kevin Ferguson', regex=True)
df['loser'] = df['loser'].replace('Kimbo Slice', 'Kevin Ferguson', regex=True)

df['fight'] = df['fight'].replace('Roli Delgado', 'Rolando Delgado', regex=True)
df['winner'] = df['winner'].replace('Roli Delgado', 'Rolando Delgado', regex=True)
df['loser'] = df['loser'].replace('Roli Delgado', 'Rolando Delgado', regex=True)

df['fight'] = df['fight'].replace('Dave Kaplan', 'David Kaplan', regex=True)
df['winner'] = df['winner'].replace('Dave Kaplan', 'David Kaplan', regex=True)
df['loser'] = df['loser'].replace('Dave Kaplan', 'David Kaplan', regex=True)

df['fight'] = df['fight'].replace('Mike Patt', 'Michael Patt', regex=True)
df['winner'] = df['winner'].replace('Mike Patt', 'Michael Patt', regex=True)
df['loser'] = df['loser'].replace('Mike Patt', 'Michael Patt', regex=True)

df['fight'] = df['fight'].replace('Thomas Speer', 'Tommy Speer', regex=True)
df['winner'] = df['winner'].replace('Thomas Speer', 'Tommy Speer', regex=True)
df['loser'] = df['loser'].replace('Thomas Speer', 'Tommy Speer', regex=True)

df['fight'] = df['fight'].replace('Douglas Evans', 'Doug Evans', regex=True)
df['winner'] = df['winner'].replace('Douglas Evans', 'Doug Evans', regex=True)
df['loser'] = df['loser'].replace('Douglas Evans', 'Doug Evans', regex=True)

df['fight'] = df['fight'].replace('Daniel Barrera', 'Dan Barrera', regex=True)
df['winner'] = df['winner'].replace('Daniel Barrera', 'Dan Barrera', regex=True)
df['loser'] = df['loser'].replace('Daniel Barrera', 'Dan Barrera', regex=True)

df['fight'] = df['fight'].replace('Allen Berubie', 'Allen Berube', regex=True)
df['winner'] = df['winner'].replace('Allen Berubie', 'Allen Berube', regex=True)
df['loser'] = df['loser'].replace('Allen Berubie', 'Allen Berube', regex=True)

df['fight'] = df['fight'].replace('Yoshitomi Mishima', 'Dokonjonosuke Mishima', regex=True)
df['winner'] = df['winner'].replace('Yoshitomi Mashima', 'Dokonjonosuke Mashima', regex=True)
df['loser'] = df['loser'].replace('Yoshitomi Mashima', 'Dokonjonosuke Mashima', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Steve Lynch', 'Steven Lynch', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Steve Lynch', 'Steven Lynch', regex=True)
df2['winner'] = df2['winner'].replace('Steve Lynch', 'Steven Lynch', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Stevie Lynch', 'Steven Lynch', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Stevie Lynch', 'Steven Lynch', regex=True)
df2['winner'] = df2['winner'].replace('Stevie Lynch', 'Steven Lynch', regex=True)

df['fight'] = df['fight'].replace('Josh Schockman', 'Josh Shockman', regex=True)
df['winner'] = df['winner'].replace('Josh Schockman', 'Josh Shockman', regex=True)
df['loser'] = df['loser'].replace('Josh Schockman', 'Josh Shockman', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Sammy Morgan', 'Sam Morgan', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Sammy Morgan', 'Sam Morgan', regex=True)
df2['winner'] = df2['winner'].replace('Sammy Morgan', 'Sam Morgan', regex=True)

df['fight'] = df['fight'].replace('Kris Rotharmel', 'Kristian Rothaermel', regex=True)
df['winner'] = df['winner'].replace('Kris Rotharmel', 'Kristian Rothaermel', regex=True)
df['loser'] = df['loser'].replace('Kris Rotharmel', 'Kristian Rothaermel', regex=True)

df['fight'] = df['fight'].replace('Joao Marcos Pierini', 'Joao Pierini', regex=True)
df['winner'] = df['winner'].replace('Joao Marcos Pierini', 'Joao Pierini', regex=True)
df['loser'] = df['loser'].replace('Joao Marcos Pierini', 'Joao Pierini', regex=True)

df['fight'] = df['fight'].replace('Tsuyoshi Kosaka', 'Tsuyoshi Kohsaka', regex=True)
df['winner'] = df['winner'].replace('Tsuyoshi Kosaka', 'Tsuyoshi Kohsaka', regex=True)
df['loser'] = df['loser'].replace('Tsuyoshi Kosaka', 'Tsuyoshi Kohsaka', regex=True)

df['fight'] = df['fight'].replace('Andrey Semenov', 'Andrei Semenov', regex=True)
df['winner'] = df['winner'].replace('Andrey Semenov', 'Andrei Semenov', regex=True)
df['loser'] = df['loser'].replace('Andrey Semenov', 'Andrei Semenov', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Cesar Marsucci', 'Cesar Marscucci', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Cesar Marsucci', 'Cesar Marscucci', regex=True)
df2['winner'] = df2['winner'].replace('Cesar Marsucci', 'Cesar Marscucci', regex=True)

df['fight'] = df['fight'].replace('Cristophe Leninger', 'Christophe Leninger', regex=True)
df['winner'] = df['winner'].replace('Cristophe Leninger', 'Christophe Leninger', regex=True)
df['loser'] = df['loser'].replace('Cristophe Leninger', 'Christophe Leninger', regex=True)

df['fight'] = df['fight'].replace('Kazuo Takahashi', 'Yoshiki Takahashi', regex=True)
df['winner'] = df['winner'].replace('Kazuo Takahashi', 'Yoshiki Takahashi', regex=True)
df['loser'] = df['loser'].replace('Kazuo Takahashi', 'Yoshiki Takahashi', regex=True)

df2['redCorner'] = df2['redCorner'].replace('Felix Lee Mitchell', 'Felix Mitchell', regex=True)
df2['blueCorner'] = df2['blueCorner'].replace('Felix Lee Mitchell', 'Felix Mitchell', regex=True)
df2['winner'] = df2['winner'].replace('Felix Lee Mitchell', 'Felix Mitchell', regex=True)

df['fight'] = df['fight'].replace('John Campatella', 'John Campetella', regex=True)
df['winner'] = df['winner'].replace('John Campatella', 'John Campetella', regex=True)
df['loser'] = df['loser'].replace('John Campatella', 'John Campetella', regex=True)

df['fight'] = df['fight'].replace('Eldo Dias Xavier', 'Eldo Xavier Diaz', regex=True)
df['winner'] = df['winner'].replace('Eldo Dias Xavier', 'Eldo Xavier Diaz', regex=True)
df['loser'] = df['loser'].replace('Eldo Dias Xavier', 'Eldo Xavier Diaz', regex=True)

df['fight'] = df['fight'].replace('Alberto Cerra Leon', 'Alberta Cerra Leon', regex=True)
df['winner'] = df['winner'].replace('Alberto Cerra Leon', 'Alberta Cerra Leon', regex=True)
df['loser'] = df['loser'].replace('Alberto Cerra Leon', 'Alberta Cerra Leon', regex=True)

#combine dfs updater
for (index, row), (index2, row2) in zip(df.iterrows(), df2.iterrows()):
    if(row['event'] == row2['event']):
        fight = row['fight'].split(' vs ')
        fighter1 = ''.join(sorted(str(fight[0]).replace(" ", "").lower()))
        fighter2 = ''.join(sorted(str(fight[1]).replace(" ", "").lower()))
        redCorner = ''.join(sorted(str(row2['redCorner']).replace(" ", "").lower()))
        blueCorner = ''.join(sorted(str(row2['blueCorner']).replace(" ", "").lower()))
        winner1 = ''.join(sorted(str(row['winner']).replace(" ", "").lower()))
        winner2 = ''.join(sorted(str(row2['winner']).replace(" ", "").lower()))
        if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
            if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                if(winner1 in winner2 or winner2 in winner1):
                    fight = row['fight']
                    redCorner = row2['redCorner']
                    blueCorner = row2['blueCorner']
                    winner = row2['winner']
                    event = row2['event']
                    referee = row2['referee']
                    method_of_vic = row2['method_of_victory']
                    date = row['date']
                    venue = row['venue']
                    title_fight = row['title_fight']
                    billing = row['billing']
                    if(winner1 in redCorner or redCorner in winner1):
                        redCorner_wins = row['winner_wins']
                        redCorner_losses = row['winner_losses']
                        redCorner_draws = row['winner_draws']
                        redCorner_age = row['winner_age']
                        redCorner_nation = row['winner_nationality']
                        redCorner_fan = row['winner_fan ']
                        blueCorner_wins = row['loser_wins']
                        blueCorner_losses = row['loser_losses']
                        blueCorner_draws = row['loser_draws']
                        blueCorner_age = row['loser_age']
                        blueCorner_nation = row['loser_nationality']
                        blueCorner_fan = row['loser_fan']
                    elif(winner1 in blueCorner or blueCorner in winner1):
                        blueCorner_wins = row['winner_wins']
                        blueCorner_losses = row['winner_losses']
                        blueCorner_draws = row['winner_draws']
                        blueCorner_age = row['winner_age']
                        blueCorner_nation = row['winner_nationality']
                        blueCorner_fan = row['winner_fan ']
                        redCorner_wins = row['loser_wins']
                        redCorner_losses = row['loser_losses']
                        redCorner_draws = row['loser_draws']
                        redCorner_age = row['loser_age']
                        redCorner_nation = row['loser_nationality']
                        redCorner_fan = row['loser_fan']
                    else:
                        if(fight[0] in redCorner or redCorner in fight[0]):
                            redCorner_wins = row['winner_wins']
                            redCorner_losses = row['winner_losses']
                            redCorner_draws = row['winner_draws']
                            redCorner_age = row['winner_age']
                            redCorner_nation = row['winner_nationality']
                            redCorner_fan = row['winner_fan ']
                            blueCorner_wins = row['loser_wins']
                            blueCorner_losses = row['loser_losses']
                            blueCorner_draws = row['loser_draws']
                            blueCorner_age = row['loser_age']
                            blueCorner_nation = row['loser_nationality']
                            blueCorner_fan = row['loser_fan']
                        if(fight[0] in blueCorner or blueCorner in fight[0]):
                            blueCorner_wins = row['winner_wins']
                            blueCorner_losses = row['winner_losses']
                            blueCorner_draws = row['winner_draws']
                            blueCorner_age = row['winner_age']
                            blueCorner_nation = row['winner_nationality']
                            blueCorner_fan = row['winner_fan ']
                            redCorner_wins = row['loser_wins']
                            redCorner_losses = row['loser_losses']
                            redCorner_draws = row['loser_draws']
                            redCorner_age = row['loser_age']
                            redCorner_nation = row['loser_nationality']
                            redCorner_fan = row['loser_fan']
                    redCorner_knockdowns = row2['red_Knockdowns']
                    blueCorner_knockdowns = row2['blue_Knockdowns']
                    redCorner_sig_str = row2['red_sig_str']
                    blueCorner_sig_str = row2['blue_sig_str']
                    redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                    blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                    redCorner_total_str = row2['red_total_strikes']
                    blueCorner_total_str = row2['blue_total_strikes']
                    redCorner_takedowns = row2['red_takedowns']
                    blueCorner_takedowns = row2['blue_takedowns']
                    redCorner_takedown_percentage = row2['red_takedown_percentage']
                    blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                    redCorner_subs_attempted = row2['red_subs_attempted']
                    blueCorner_subs_attempted = row2['blue_subs_attempted']
                    roundA = row2['round']      
                    time = row2['time']
                    redCorner_height = row2['redCorner_height']
                    blueCorner_height = row2['blueCorner_height']
                    redCorner_reach = row2['redCorner_reach']
                    blueCorner_reach = row2['blueCorner_reach']
                    redCorner_stance = row2['redCorner_stance']
                    blueCorner_stance = row2['blueCorner_stance']
            else:
                fight = row['fight'].split(' vs ')
                fighter1 = str(fight[0]).replace(" ", "").lower()
                fighter2 = str(fight[1]).replace(" ", "").lower()
                redCorner = str(row2['redCorner']).replace(" ", "").lower()
                blueCorner = str(row2['blueCorner']).replace(" ", "").lower()
                winner1 = str(row['winner']).replace(" ", "").lower()
                winner2 = str(row2['winner']).replace(" ", "").lower()
                if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
                    if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                        if(winner1 in winner2 or winner2 in winner1):
                            fight = row['fight']
                            redCorner = row2['redCorner']
                            blueCorner = row2['blueCorner']
                            winner = row2['winner']
                            event = row2['event']
                            referee = row2['referee']
                            method_of_vic = row2['method_of_victory']
                            date = row['date']
                            venue = row['venue']
                            title_fight = row['title_fight']
                            billing = row['billing']
                            if(winner1 in redCorner or redCorner in winner1):
                                redCorner_wins = row['winner_wins']
                                redCorner_losses = row['winner_losses']
                                redCorner_draws = row['winner_draws']
                                redCorner_age = row['winner_age']
                                redCorner_nation = row['winner_nationality']
                                redCorner_fan = row['winner_fan ']
                                blueCorner_wins = row['loser_wins']
                                blueCorner_losses = row['loser_losses']
                                blueCorner_draws = row['loser_draws']
                                blueCorner_age = row['loser_age']
                                blueCorner_nation = row['loser_nationality']
                                blueCorner_fan = row['loser_fan']
                            elif(winner1 in blueCorner or blueCorner in winner1):
                                blueCorner_wins = row['winner_wins']
                                blueCorner_losses = row['winner_losses']
                                blueCorner_draws = row['winner_draws']
                                blueCorner_age = row['winner_age']
                                blueCorner_nation = row['winner_nationality']
                                blueCorner_fan = row['winner_fan ']
                                redCorner_wins = row['loser_wins']
                                redCorner_losses = row['loser_losses']
                                redCorner_draws = row['loser_draws']
                                redCorner_age = row['loser_age']
                                redCorner_nation = row['loser_nationality']
                                redCorner_fan = row['loser_fan']
                            else:
                                if(fight[0] in redCorner or redCorner in fight[0]):
                                    redCorner_wins = row['winner_wins']
                                    redCorner_losses = row['winner_losses']
                                    redCorner_draws = row['winner_draws']
                                    redCorner_age = row['winner_age']
                                    redCorner_nation = row['winner_nationality']
                                    redCorner_fan = row['winner_fan ']
                                    blueCorner_wins = row['loser_wins']
                                    blueCorner_losses = row['loser_losses']
                                    blueCorner_draws = row['loser_draws']
                                    blueCorner_age = row['loser_age']
                                    blueCorner_nation = row['loser_nationality']
                                    blueCorner_fan = row['loser_fan']
                                if(fight[0] in blueCorner or blueCorner in fight[0]):
                                    blueCorner_wins = row['winner_wins']
                                    blueCorner_losses = row['winner_losses']
                                    blueCorner_draws = row['winner_draws']
                                    blueCorner_age = row['winner_age']
                                    blueCorner_nation = row['winner_nationality']
                                    blueCorner_fan = row['winner_fan ']
                                    redCorner_wins = row['loser_wins']
                                    redCorner_losses = row['loser_losses']
                                    redCorner_draws = row['loser_draws']
                                    redCorner_age = row['loser_age']
                                    redCorner_nation = row['loser_nationality']
                                    redCorner_fan = row['loser_fan']
                            redCorner_knockdowns = row2['red_Knockdowns']
                            blueCorner_knockdowns = row2['blue_Knockdowns']
                            redCorner_sig_str = row2['red_sig_str']
                            blueCorner_sig_str = row2['blue_sig_str']
                            redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                            blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                            redCorner_total_str = row2['red_total_strikes']
                            blueCorner_total_str = row2['blue_total_strikes']
                            redCorner_takedowns = row2['red_takedowns']
                            blueCorner_takedowns = row2['blue_takedowns']
                            redCorner_takedown_percentage = row2['red_takedown_percentage']
                            blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                            redCorner_subs_attempted = row2['red_subs_attempted']
                            blueCorner_subs_attempted = row2['blue_subs_attempted']
                            roundA = row2['round']      
                            time = row2['time']
                            redCorner_height = row2['redCorner_height']
                            blueCorner_height = row2['blueCorner_height']
                            redCorner_reach = row2['redCorner_reach']
                            blueCorner_reach = row2['blueCorner_reach']
                            redCorner_stance = row2['redCorner_stance']
                            blueCorner_stance = row2['blueCorner_stance'] 
                    else:
                        fight = row['fight'].split(' vs ')
                        fighter1 = str(fight[0]).replace(" ", "").lower()
                        fighter2 = str(fight[1]).replace(" ", "").lower()
                        redCorner = str(row2['redCorner']).replace(" ", "").lower()
                        blueCorner = str(row2['blueCorner']).replace(" ", "").lower()
                        winner1 = str(row['winner']).replace(" ", "").lower()
                        winner2 = str(row2['winner']).replace(" ", "").lower()
                        fighter1 = redCorner
                        fighter2 = blueCorner
                        if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
                            if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                                if(winner1 in winner2 or winner2 in winner1):
                                    fight = row['fight']
                                    redCorner = row2['redCorner']
                                    blueCorner = row2['blueCorner']
                                    winner = row2['winner']
                                    event = row2['event']
                                    referee = row2['referee']
                                    method_of_vic = row2['method_of_victory']
                                    date = row['date']
                                    venue = row['venue']
                                    title_fight = row['title_fight']
                                    billing = row['billing']
                                    if(winner1 in redCorner or redCorner in winner1):
                                        redCorner_wins = row['winner_wins']
                                        redCorner_losses = row['winner_losses']
                                        redCorner_draws = row['winner_draws']
                                        redCorner_age = row['winner_age']
                                        redCorner_nation = row['winner_nationality']
                                        redCorner_fan = row['winner_fan ']
                                        blueCorner_wins = row['loser_wins']
                                        blueCorner_losses = row['loser_losses']
                                        blueCorner_draws = row['loser_draws']
                                        blueCorner_age = row['loser_age']
                                        blueCorner_nation = row['loser_nationality']
                                        blueCorner_fan = row['loser_fan']
                                    elif(winner1 in blueCorner or blueCorner in winner1):
                                        blueCorner_wins = row['winner_wins']
                                        blueCorner_losses = row['winner_losses']
                                        blueCorner_draws = row['winner_draws']
                                        blueCorner_age = row['winner_age']
                                        blueCorner_nation = row['winner_nationality']
                                        blueCorner_fan = row['winner_fan ']
                                        redCorner_wins = row['loser_wins']
                                        redCorner_losses = row['loser_losses']
                                        redCorner_draws = row['loser_draws']
                                        redCorner_age = row['loser_age']
                                        redCorner_nation = row['loser_nationality']
                                        redCorner_fan = row['loser_fan']
                                    else:
                                        if(fight[0] in redCorner or redCorner in fight[0]):
                                            redCorner_wins = row['winner_wins']
                                            redCorner_losses = row['winner_losses']
                                            redCorner_draws = row['winner_draws']
                                            redCorner_age = row['winner_age']
                                            redCorner_nation = row['winner_nationality']
                                            redCorner_fan = row['winner_fan ']
                                            blueCorner_wins = row['loser_wins']
                                            blueCorner_losses = row['loser_losses']
                                            blueCorner_draws = row['loser_draws']
                                            blueCorner_age = row['loser_age']
                                            blueCorner_nation = row['loser_nationality']
                                            blueCorner_fan = row['loser_fan']
                                        if(fight[0] in blueCorner or blueCorner in fight[0]):
                                            blueCorner_wins = row['winner_wins']
                                            blueCorner_losses = row['winner_losses']
                                            blueCorner_draws = row['winner_draws']
                                            blueCorner_age = row['winner_age']
                                            blueCorner_nation = row['winner_nationality']
                                            blueCorner_fan = row['winner_fan ']
                                            redCorner_wins = row['loser_wins']
                                            redCorner_losses = row['loser_losses']
                                            redCorner_draws = row['loser_draws']
                                            redCorner_age = row['loser_age']
                                            redCorner_nation = row['loser_nationality']
                                            redCorner_fan = row['loser_fan']
                                    redCorner_knockdowns = row2['red_Knockdowns']
                                    blueCorner_knockdowns = row2['blue_Knockdowns']
                                    redCorner_sig_str = row2['red_sig_str']
                                    blueCorner_sig_str = row2['blue_sig_str']
                                    redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                                    blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                                    redCorner_total_str = row2['red_total_strikes']
                                    blueCorner_total_str = row2['blue_total_strikes']
                                    redCorner_takedowns = row2['red_takedowns']
                                    blueCorner_takedowns = row2['blue_takedowns']
                                    redCorner_takedown_percentage = row2['red_takedown_percentage']
                                    blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                                    redCorner_subs_attempted = row2['red_subs_attempted']
                                    blueCorner_subs_attempted = row2['blue_subs_attempted']
                                    roundA = row2['round']      
                                    time = row2['time'] 
                                    redCorner_height = row2['redCorner_height']
                                    blueCorner_height = row2['blueCorner_height']
                                    redCorner_reach = row2['redCorner_reach']
                                    blueCorner_reach = row2['blueCorner_reach']
                                    redCorner_stance = row2['redCorner_stance']
                                    blueCorner_stance = row2['blueCorner_stance']
                else:
                    fight = row['fight'].split(' vs ')
                    fighter1 = str(fight[0]).replace(" ", "").lower()
                    fighter2 = str(fight[1]).replace(" ", "").lower()
                    redCorner = str(row2['redCorner']).replace(" ", "").lower()
                    blueCorner = str(row2['blueCorner']).replace(" ", "").lower()
                    winner1 = str(row['winner']).replace(" ", "").lower()
                    winner2 = str(row2['winner']).replace(" ", "").lower()
                    fighter1 = redCorner
                    fighter2 = blueCorner
                    if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
                        if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                            if(winner1 in winner2 or winner2 in winner1):
                                fight = row['fight']
                                redCorner = row2['redCorner']
                                blueCorner = row2['blueCorner']
                                winner = row2['winner']
                                event = row2['event']
                                referee = row2['referee']
                                method_of_vic = row2['method_of_victory']
                                date = row['date']
                                venue = row['venue']
                                title_fight = row['title_fight']
                                billing = row['billing']
                                if(winner1 in redCorner or redCorner in winner1):
                                    redCorner_wins = row['winner_wins']
                                    redCorner_losses = row['winner_losses']
                                    redCorner_draws = row['winner_draws']
                                    redCorner_age = row['winner_age']
                                    redCorner_nation = row['winner_nationality']
                                    redCorner_fan = row['winner_fan ']
                                    blueCorner_wins = row['loser_wins']
                                    blueCorner_losses = row['loser_losses']
                                    blueCorner_draws = row['loser_draws']
                                    blueCorner_age = row['loser_age']
                                    blueCorner_nation = row['loser_nationality']
                                    blueCorner_fan = row['loser_fan']
                                elif(winner1 in blueCorner or blueCorner in winner1):
                                    blueCorner_wins = row['winner_wins']
                                    blueCorner_losses = row['winner_losses']
                                    blueCorner_draws = row['winner_draws']
                                    blueCorner_age = row['winner_age']
                                    blueCorner_nation = row['winner_nationality']
                                    blueCorner_fan = row['winner_fan ']
                                    redCorner_wins = row['loser_wins']
                                    redCorner_losses = row['loser_losses']
                                    redCorner_draws = row['loser_draws']
                                    redCorner_age = row['loser_age']
                                    redCorner_nation = row['loser_nationality']
                                    redCorner_fan = row['loser_fan']
                                else:
                                    if(fight[0] in redCorner or redCorner in fight[0]):
                                        redCorner_wins = row['winner_wins']
                                        redCorner_losses = row['winner_losses']
                                        redCorner_draws = row['winner_draws']
                                        redCorner_age = row['winner_age']
                                        redCorner_nation = row['winner_nationality']
                                        redCorner_fan = row['winner_fan ']
                                        blueCorner_wins = row['loser_wins']
                                        blueCorner_losses = row['loser_losses']
                                        blueCorner_draws = row['loser_draws']
                                        blueCorner_age = row['loser_age']
                                        blueCorner_nation = row['loser_nationality']
                                        blueCorner_fan = row['loser_fan']
                                    if(fight[0] in blueCorner or blueCorner in fight[0]):
                                        blueCorner_wins = row['winner_wins']
                                        blueCorner_losses = row['winner_losses']
                                        blueCorner_draws = row['winner_draws']
                                        blueCorner_age = row['winner_age']
                                        blueCorner_nation = row['winner_nationality']
                                        blueCorner_fan = row['winner_fan ']
                                        redCorner_wins = row['loser_wins']
                                        redCorner_losses = row['loser_losses']
                                        redCorner_draws = row['loser_draws']
                                        redCorner_age = row['loser_age']
                                        redCorner_nation = row['loser_nationality']
                                        redCorner_fan = row['loser_fan']
                                redCorner_knockdowns = row2['red_Knockdowns']
                                blueCorner_knockdowns = row2['blue_Knockdowns']
                                redCorner_sig_str = row2['red_sig_str']
                                blueCorner_sig_str = row2['blue_sig_str']
                                redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                                blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                                redCorner_total_str = row2['red_total_strikes']
                                blueCorner_total_str = row2['blue_total_strikes']
                                redCorner_takedowns = row2['red_takedowns']
                                blueCorner_takedowns = row2['blue_takedowns']
                                redCorner_takedown_percentage = row2['red_takedown_percentage']
                                blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                                redCorner_subs_attempted = row2['red_subs_attempted']
                                blueCorner_subs_attempted = row2['blue_subs_attempted']
                                roundA = row2['round']      
                                time = row2['time'] 
                                redCorner_height = row2['redCorner_height']
                                blueCorner_height = row2['blueCorner_height']
                                redCorner_reach = row2['redCorner_reach']
                                blueCorner_reach = row2['blueCorner_reach']
                                redCorner_stance = row2['redCorner_stance']
                                blueCorner_stance = row2['blueCorner_stance']
        else:
            fight = row['fight'].split(' vs ')
            fighter1 = str(fight[0]).replace(" ", "").lower()
            fighter2 = str(fight[1]).replace(" ", "").lower()
            redCorner = str(row2['redCorner']).replace(" ", "").lower()
            blueCorner = str(row2['blueCorner']).replace(" ", "").lower()
            winner1 = str(row['winner']).replace(" ", "").lower()
            winner2 = str(row2['winner']).replace(" ", "").lower()
            if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
                if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                    if(winner1 in winner2 or winner2 in winner1):
                        fight = row['fight']
                        redCorner = row2['redCorner']
                        blueCorner = row2['blueCorner']
                        winner = row2['winner']
                        event = row2['event']
                        referee = row2['referee']
                        method_of_vic = row2['method_of_victory']
                        date = row['date']
                        venue = row['venue']
                        title_fight = row['title_fight']
                        billing = row['billing']
                        if(winner1 in redCorner or redCorner in winner1):
                            redCorner_wins = row['winner_wins']
                            redCorner_losses = row['winner_losses']
                            redCorner_draws = row['winner_draws']
                            redCorner_age = row['winner_age']
                            redCorner_nation = row['winner_nationality']
                            redCorner_fan = row['winner_fan ']
                            blueCorner_wins = row['loser_wins']
                            blueCorner_losses = row['loser_losses']
                            blueCorner_draws = row['loser_draws']
                            blueCorner_age = row['loser_age']
                            blueCorner_nation = row['loser_nationality']
                            blueCorner_fan = row['loser_fan']
                        elif(winner1 in blueCorner or blueCorner in winner1):
                            blueCorner_wins = row['winner_wins']
                            blueCorner_losses = row['winner_losses']
                            blueCorner_draws = row['winner_draws']
                            blueCorner_age = row['winner_age']
                            blueCorner_nation = row['winner_nationality']
                            blueCorner_fan = row['winner_fan ']
                            redCorner_wins = row['loser_wins']
                            redCorner_losses = row['loser_losses']
                            redCorner_draws = row['loser_draws']
                            redCorner_age = row['loser_age']
                            redCorner_nation = row['loser_nationality']
                            redCorner_fan = row['loser_fan']
                        else:
                            if(fight[0] in redCorner or redCorner in fight[0]):
                                redCorner_wins = row['winner_wins']
                                redCorner_losses = row['winner_losses']
                                redCorner_draws = row['winner_draws']
                                redCorner_age = row['winner_age']
                                redCorner_nation = row['winner_nationality']
                                redCorner_fan = row['winner_fan ']
                                blueCorner_wins = row['loser_wins']
                                blueCorner_losses = row['loser_losses']
                                blueCorner_draws = row['loser_draws']
                                blueCorner_age = row['loser_age']
                                blueCorner_nation = row['loser_nationality']
                                blueCorner_fan = row['loser_fan']
                            if(fight[0] in blueCorner or blueCorner in fight[0]):
                                blueCorner_wins = row['winner_wins']
                                blueCorner_losses = row['winner_losses']
                                blueCorner_draws = row['winner_draws']
                                blueCorner_age = row['winner_age']
                                blueCorner_nation = row['winner_nationality']
                                blueCorner_fan = row['winner_fan ']
                                redCorner_wins = row['loser_wins']
                                redCorner_losses = row['loser_losses']
                                redCorner_draws = row['loser_draws']
                                redCorner_age = row['loser_age']
                                redCorner_nation = row['loser_nationality']
                                redCorner_fan = row['loser_fan']
                        redCorner_knockdowns = row2['red_Knockdowns']
                        blueCorner_knockdowns = row2['blue_Knockdowns']
                        redCorner_sig_str = row2['red_sig_str']
                        blueCorner_sig_str = row2['blue_sig_str']
                        redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                        blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                        redCorner_total_str = row2['red_total_strikes']
                        blueCorner_total_str = row2['blue_total_strikes']
                        redCorner_takedowns = row2['red_takedowns']
                        blueCorner_takedowns = row2['blue_takedowns']
                        redCorner_takedown_percentage = row2['red_takedown_percentage']
                        blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                        redCorner_subs_attempted = row2['red_subs_attempted']
                        blueCorner_subs_attempted = row2['blue_subs_attempted']
                        roundA = row2['round']      
                        time = row2['time'] 
                        redCorner_height = row2['redCorner_height']
                        blueCorner_height = row2['blueCorner_height']
                        redCorner_reach = row2['redCorner_reach']
                        blueCorner_reach = row2['blueCorner_reach']
                        redCorner_stance = row2['redCorner_stance']
                        blueCorner_stance = row2['blueCorner_stance'] 
                else:
                    fight = row['fight'].split(' vs ')
                    fighter1 = str(fight[0]).replace(" ", "").lower()
                    fighter2 = str(fight[1]).replace(" ", "").lower()
                    redCorner = str(row2['redCorner']).replace(" ", "").lower()
                    blueCorner = str(row2['blueCorner']).replace(" ", "").lower()
                    winner1 = str(row['winner']).replace(" ", "").lower()
                    winner2 = str(row2['winner']).replace(" ", "").lower()
                    fighter1 = redCorner
                    fighter2 = blueCorner
                    if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
                        if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                            if(winner1 in winner2 or winner2 in winner1):
                                fight = row['fight']
                                redCorner = row2['redCorner']
                                blueCorner = row2['blueCorner']
                                winner = row2['winner']
                                event = row2['event']
                                referee = row2['referee']
                                method_of_vic = row2['method_of_victory']
                                date = row['date']
                                venue = row['venue']
                                title_fight = row['title_fight']
                                billing = row['billing']
                                if(winner1 in redCorner or redCorner in winner1):
                                    redCorner_wins = row['winner_wins']
                                    redCorner_losses = row['winner_losses']
                                    redCorner_draws = row['winner_draws']
                                    redCorner_age = row['winner_age']
                                    redCorner_nation = row['winner_nationality']
                                    redCorner_fan = row['winner_fan ']
                                    blueCorner_wins = row['loser_wins']
                                    blueCorner_losses = row['loser_losses']
                                    blueCorner_draws = row['loser_draws']
                                    blueCorner_age = row['loser_age']
                                    blueCorner_nation = row['loser_nationality']
                                    blueCorner_fan = row['loser_fan']
                                elif(winner1 in blueCorner or blueCorner in winner1):
                                    blueCorner_wins = row['winner_wins']
                                    blueCorner_losses = row['winner_losses']
                                    blueCorner_draws = row['winner_draws']
                                    blueCorner_age = row['winner_age']
                                    blueCorner_nation = row['winner_nationality']
                                    blueCorner_fan = row['winner_fan ']
                                    redCorner_wins = row['loser_wins']
                                    redCorner_losses = row['loser_losses']
                                    redCorner_draws = row['loser_draws']
                                    redCorner_age = row['loser_age']
                                    redCorner_nation = row['loser_nationality']
                                    redCorner_fan = row['loser_fan']
                                else:
                                    if(fight[0] in redCorner or redCorner in fight[0]):
                                        redCorner_wins = row['winner_wins']
                                        redCorner_losses = row['winner_losses']
                                        redCorner_draws = row['winner_draws']
                                        redCorner_age = row['winner_age']
                                        redCorner_nation = row['winner_nationality']
                                        redCorner_fan = row['winner_fan ']
                                        blueCorner_wins = row['loser_wins']
                                        blueCorner_losses = row['loser_losses']
                                        blueCorner_draws = row['loser_draws']
                                        blueCorner_age = row['loser_age']
                                        blueCorner_nation = row['loser_nationality']
                                        blueCorner_fan = row['loser_fan']
                                    if(fight[0] in blueCorner or blueCorner in fight[0]):
                                        blueCorner_wins = row['winner_wins']
                                        blueCorner_losses = row['winner_losses']
                                        blueCorner_draws = row['winner_draws']
                                        blueCorner_age = row['winner_age']
                                        blueCorner_nation = row['winner_nationality']
                                        blueCorner_fan = row['winner_fan ']
                                        redCorner_wins = row['loser_wins']
                                        redCorner_losses = row['loser_losses']
                                        redCorner_draws = row['loser_draws']
                                        redCorner_age = row['loser_age']
                                        redCorner_nation = row['loser_nationality']
                                        redCorner_fan = row['loser_fan']
                                redCorner_knockdowns = row2['red_Knockdowns']
                                blueCorner_knockdowns = row2['blue_Knockdowns']
                                redCorner_sig_str = row2['red_sig_str']
                                blueCorner_sig_str = row2['blue_sig_str']
                                redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                                blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                                redCorner_total_str = row2['red_total_strikes']
                                blueCorner_total_str = row2['blue_total_strikes']
                                redCorner_takedowns = row2['red_takedowns']
                                blueCorner_takedowns = row2['blue_takedowns']
                                redCorner_takedown_percentage = row2['red_takedown_percentage']
                                blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                                redCorner_subs_attempted = row2['red_subs_attempted']
                                blueCorner_subs_attempted = row2['blue_subs_attempted']
                                roundA = row2['round']      
                                time = row2['time'] 
                                redCorner_height = row2['redCorner_height']
                                blueCorner_height = row2['blueCorner_height']
                                redCorner_reach = row2['redCorner_reach']
                                blueCorner_reach = row2['blueCorner_reach']
                                redCorner_stance = row2['redCorner_stance']
                                blueCorner_stance = row2['blueCorner_stance']
            else:
                fight = row['fight'].split(' vs ')
                fighter1 = str(fight[0]).replace(" ", "").lower()
                fighter2 = str(fight[1]).replace(" ", "").lower()
                redCorner = str(row2['redCorner']).replace(" ", "").lower()
                blueCorner = str(row2['blueCorner']).replace(" ", "").lower()
                winner1 = str(row['winner']).replace(" ", "").lower()
                winner2 = str(row2['winner']).replace(" ", "").lower()
                fighter1 = redCorner
                fighter2 = blueCorner
                if(fighter1 in redCorner or fighter1 in blueCorner or redCorner in fighter1 or blueCorner in fighter1):
                    if(fighter2 in redCorner or fighter2 in blueCorner or redCorner in fighter2 or blueCorner in fighter2):
                        if(winner1 in winner2 or winner2 in winner1):
                            fight = row['fight']
                            redCorner = row2['redCorner']
                            blueCorner = row2['blueCorner']
                            winner = row2['winner']
                            event = row2['event']
                            referee = row2['referee']
                            method_of_vic = row2['method_of_victory']
                            date = row['date']
                            venue = row['venue']
                            title_fight = row['title_fight']
                            billing = row['billing']
                            if(winner1 in redCorner or redCorner in winner1):
                                redCorner_wins = row['winner_wins']
                                redCorner_losses = row['winner_losses']
                                redCorner_draws = row['winner_draws']
                                redCorner_age = row['winner_age']
                                redCorner_nation = row['winner_nationality']
                                redCorner_fan = row['winner_fan ']
                                blueCorner_wins = row['loser_wins']
                                blueCorner_losses = row['loser_losses']
                                blueCorner_draws = row['loser_draws']
                                blueCorner_age = row['loser_age']
                                blueCorner_nation = row['loser_nationality']
                                blueCorner_fan = row['loser_fan']
                            elif(winner1 in blueCorner or blueCorner in winner1):
                                blueCorner_wins = row['winner_wins']
                                blueCorner_losses = row['winner_losses']
                                blueCorner_draws = row['winner_draws']
                                blueCorner_age = row['winner_age']
                                blueCorner_nation = row['winner_nationality']
                                blueCorner_fan = row['winner_fan ']
                                redCorner_wins = row['loser_wins']
                                redCorner_losses = row['loser_losses']
                                redCorner_draws = row['loser_draws']
                                redCorner_age = row['loser_age']
                                redCorner_nation = row['loser_nationality']
                                redCorner_fan = row['loser_fan']
                            else:
                                if(fight[0] in redCorner or redCorner in fight[0]):
                                    redCorner_wins = row['winner_wins']
                                    redCorner_losses = row['winner_losses']
                                    redCorner_draws = row['winner_draws']
                                    redCorner_age = row['winner_age']
                                    redCorner_nation = row['winner_nationality']
                                    redCorner_fan = row['winner_fan ']
                                    blueCorner_wins = row['loser_wins']
                                    blueCorner_losses = row['loser_losses']
                                    blueCorner_draws = row['loser_draws']
                                    blueCorner_age = row['loser_age']
                                    blueCorner_nation = row['loser_nationality']
                                    blueCorner_fan = row['loser_fan']
                                if(fight[0] in blueCorner or blueCorner in fight[0]):
                                    blueCorner_wins = row['winner_wins']
                                    blueCorner_losses = row['winner_losses']
                                    blueCorner_draws = row['winner_draws']
                                    blueCorner_age = row['winner_age']
                                    blueCorner_nation = row['winner_nationality']
                                    blueCorner_fan = row['winner_fan ']
                                    redCorner_wins = row['loser_wins']
                                    redCorner_losses = row['loser_losses']
                                    redCorner_draws = row['loser_draws']
                                    redCorner_age = row['loser_age']
                                    redCorner_nation = row['loser_nationality']
                                    redCorner_fan = row['loser_fan']
                            redCorner_knockdowns = row2['red_Knockdowns']
                            blueCorner_knockdowns = row2['blue_Knockdowns']
                            redCorner_sig_str = row2['red_sig_str']
                            blueCorner_sig_str = row2['blue_sig_str']
                            redCorner_sig_str_percentage = row2['red_sig_str_percentage']
                            blueCorner_sig_str_percentage = row2['blue_sig_str_percentage']
                            redCorner_total_str = row2['red_total_strikes']
                            blueCorner_total_str = row2['blue_total_strikes']
                            redCorner_takedowns = row2['red_takedowns']
                            blueCorner_takedowns = row2['blue_takedowns']
                            redCorner_takedown_percentage = row2['red_takedown_percentage']
                            blueCorner_takedown_percentage = row2['blue_takedown_percentage']
                            redCorner_subs_attempted = row2['red_subs_attempted']
                            blueCorner_subs_attempted = row2['blue_subs_attempted']
                            roundA = row2['round']      
                            time = row2['time'] 
                            redCorner_height = row2['redCorner_height']
                            blueCorner_height = row2['blueCorner_height']
                            redCorner_reach = row2['redCorner_reach']
                            blueCorner_reach = row2['blueCorner_reach']
                            redCorner_stance = row2['redCorner_stance']
                            blueCorner_stance = row2['blueCorner_stance']                          
    column_vals = {
        'fight': fight,
        'redCorner': redCorner,
        'blueCorner': blueCorner,
        'winner': winner,
        'event': event,
        'referee': referee,
        'method_of_victory': method_of_vic,
        'date': date,
        'venue': venue,
        'title_fight': title_fight,
        'billing': billing,
        'redCorner_wins': redCorner_wins,
        'blueCorner_wins': blueCorner_wins,
        'redCorner_losses': redCorner_losses,
        'blueCorner_losses': blueCorner_losses,
        'redCorner_draws': redCorner_draws,
        'blueCorner_draws': blueCorner_draws,
        'redCorner_age': redCorner_age,
        'blueCorner_age': blueCorner_age,
        'redCorner_nation': redCorner_nation,
        'blueCorner_nation': blueCorner_nation,
        'redCorner_fan': redCorner_fan,
        'blueCorner_fan': blueCorner_fan,
        'redCorner_knockdowns': redCorner_knockdowns,
        'blueCorner_knockdowns': blueCorner_knockdowns,
        'redCorner_sig_str': redCorner_sig_str,
        'blueCorner_sig_str': blueCorner_sig_str,
        'redCorner_sig_str_percentage': redCorner_sig_str_percentage,
        'blueCorner_sig_str_percentage': blueCorner_sig_str_percentage,
        'redCorner_total_str': redCorner_total_str,
        'blueCorner_total_str': blueCorner_total_str,
        'redCorner_takedowns': redCorner_takedowns,
        'blueCorner_takedowns': blueCorner_takedowns,
        'redCorner_takedown_percentage': redCorner_takedown_percentage,
        'blueCorner_takedown_percentage': blueCorner_takedown_percentage,
        'redCorner_subs_attempted': redCorner_subs_attempted,
        'blueCorner_subs_attempted': blueCorner_subs_attempted,
        'round': roundA,
        'time': time,
        'redCorner_height': redCorner_height,
        'blueCorner_height': blueCorner_height,
        'redCorner_reach': redCorner_reach,
        'blueCorner_reach': blueCorner_reach,
        'redCorner_stance': redCorner_stance,
        'blueCorner_stance': blueCorner_stance
    }
    dfNew.loc[len(dfNew)] = column_vals

#write new data to top of csv
dfOld = pd.read_csv(f'databaseUpdated{mostRecentDatabase}.csv')

updatedData = pd.concat([dfNew, dfOld], ignore_index=True)

updatedData.head()


#get current date to track day of update
dateToday = datetime.datetime.today().date()

#df to csv file
updatedData.to_csv(f'databaseUpdated{dateToday}.csv', index=False)


#parse site using alphabet
all_fighter_links = []
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

    #remove link dups
    fighterLinks = list(dict.fromkeys(fighterLinks))
    all_fighter_links.append(fighterLinks)

all_fighter_links = list(itertools.chain.from_iterable(all_fighter_links))
print(f'Fighters Found: {len(all_fighter_links)}')


    
#scrape individual fighter stats
fighters_statistics = []
for i in all_fighter_links:
    try:
        site = requests.get(i, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        #initialize stats
        name = None
        nickname = None
        wins = None
        losses = None
        draws = None
        height = None
        weight = None
        reach = None
        stance = None
        dOB = None
        sig_strikes_landed_per_min = None
        sig_striking_accuracy = None
        sig_strike_absorbed_per_min = None
        sig_strike_defense = None
        takedown_average = None
        takedown_accuracy = None
        takedown_defense = None
        sub_average = None


        #scrape + clean nickname
        try:
            nick = soup.find('p', class_=re.compile('b-content__Nickname'))
            nickname = nick.text.strip()
        except:
            pass

        #scrape name
        tempName = soup.find_all('span', class_=re.compile("b-content__title-highlight"))
        #clean name
        name = tempName[0].text.strip()

        #scrape records
        tempRecord = soup.find_all('span', class_=re.compile('b-content__title-record'))
        #clean wins + losses + draws
        record = tempRecord[0].text.strip()
        listRecord = record.split('-')
        for idx, ele in enumerate(listRecord):
            listRecord[idx] = ele.replace('Record: ', '')
        wins = listRecord[0]
        losses = listRecord[1]
        draws = listRecord[2]
        
        #clean soup for rest of stats
        i_tags = soup.find_all('i')
        for itags in i_tags:
            itags.decompose()
        
        #clean stats
        tempRest = soup.find_all('li', class_=re.compile('b-list__box-list-item b-list__box-list-item_type_block'))
    
    
        height = tempRest[0].text.strip()
        weight = tempRest[1].text.strip()
        reach = tempRest[2].text.strip()
        stance = tempRest[3].text.strip()
        dOB = tempRest[4].text.strip()
        sig_strikes_landed_per_min = tempRest[5].text.strip()
        sig_striking_accuracy = tempRest[6].text.strip()
        sig_strike_absorbed_per_min = tempRest[7].text.strip()
        sig_strike_defense = tempRest[8].text.strip()
        takedown_average = tempRest[10].text.strip()
        takedown_accuracy = tempRest[11].text.strip()
        takedown_defense = tempRest[12].text.strip()
        sub_average = tempRest[13].text.strip()
        
        #notification of scrape
        print(f'Scraping {name}...')
        print(i)


        #adding stats to fighters_statistics to prepare for csv
        fighters_statistics.append([name, nickname, wins, losses, draws, height, weight, reach, stance, dOB, sig_strikes_landed_per_min, sig_striking_accuracy, sig_strike_absorbed_per_min, sig_strike_defense, takedown_average, takedown_accuracy, takedown_defense, sub_average])
    except:
        pass
    


    

    #create csv file
    head = ['name', 'nickname', 'wins', 'losses', 'draws', 'height', 'weight', 'reach', 'stance', 'dOB', 'sig_strikes_landed_per_min', 'sig_striking_accuracy_%', 'sig_strike_absorbed_per_min', 'sig_strike_defense(%_of_sig_strikes_not_landed_by_opponent)', 'takedown_average(average_takedown_landed_per_fifteen_min)', 'takedown_accuracy_%', 'takedown_defense(%_of_opponent_takedown_not_landed)', 'sub_average(average_subs_attempted_per_15_mins)']

    with open(f'ufc_fighters_statistics{dateToday}.csv', 'w', encoding='UTF8', newline='') as scrapedStats:
        writer = csv.writer(scrapedStats)
        writer.writerow(head)
        writer.writerows(fighters_statistics)


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
numPages = math.ceil(int(athleteTotal)/11)
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

head = ['name', 'nickname', 'wins', 'losses', 'draws', 'height', 'reach', 'age', 'nation', 'sig_str_accuracy', 'sig_str_totals', 'takedown_accuracy', 'takedown_totals', 'sig_str_per_minute', 'takedown_avg_per_fifteen', 'sig_str_defense', 'knockdown_avg', 'sig_str_absorbed_per_min', 'submission_avg_per_fifteen', 'takedown_defense', 'avg_fight_time']

with open(f'alt_fighter_stats{dateToday}.csv', 'w', encoding='UTF8', newline='') as scrapedFighters:
    writer = csv.writer(scrapedFighters)
    writer.writerow(head)
    writer.writerows(fighterStats)

df = pd.read_csv(f'ufc_fighters_statistics{dateToday}.csv')
dfAlt = pd.read_csv(f'alt_fighter_stats{dateToday}.csv')

df.head()

#clean nicknames in dfAlt
dfAlt['nickname'] = dfAlt['nickname'].str.replace('"', '')

#giving nans characters so dups with nans for nickname cannot match
df['nickname'].fillna('!', inplace=True)
dfAlt['nickname'].fillna('~', inplace=True)


#find special characters in df
names = (df['name'].values)
nicknames = (df['nickname'].values)

chars2rep = []
for name in names:
    if(isinstance(name, str)):
        for char in name:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
for nickname in nicknames:
    if(isinstance(nickname, str)):
        for char in nickname:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)


chars2rep = list(set(chars2rep))
for char in chars2rep:
    print(char)


#clean name, nickname
for index, row in df.iterrows():
    name = row['name']
    nickname = row['nickname']
    if(isinstance(name, str)):
        cleanName = name.replace('?', '').replace('4', '').replace('9', '').replace('0', '').replace('5', '').replace('7', '').replace('1', '').replace(',', '').replace('3', '').replace('%', '').replace("'", '').replace('-', '').replace('2', '').replace('.', '')
        df.loc[index, 'name'] = cleanName
    if(isinstance(nickname, str)):
        cleanNickname = nickname.replace('?', '').replace('4', '').replace('9', '').replace('0', '').replace('5', '').replace('7', '').replace('1', '').replace(',', '').replace('3', '').replace('%', '').replace("'", '').replace('-', '').replace('2', '').replace('.', '')
        df.loc[index, 'nickname'] = cleanNickname


#find special characters in df
names = (dfAlt['name'].values)
nicknames = (dfAlt['nickname'].values)

chars2rep = []
for name in names:
    if(isinstance(name, str)):
        for char in name:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
for nickname in nicknames:
    if(isinstance(nickname, str)):
        for char in nickname:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)


chars2rep = list(set(chars2rep))
for char in chars2rep:
    print(char)


#clean name, nickname
for index, row in dfAlt.iterrows():
    name = row['name']
    nickname = row['nickname']
    if(isinstance(name, str)):
        cleanName = name.replace('2', '').replace('(', '').replace('3', '').replace('ú', 'u').replace('ç', 'c').replace('Á', 'A').replace('7', '').replace('í', 'i').replace('0', '').replace('ě', 'e').replace('4', '').replace("'", '').replace('%', '').replace('"', '').replace('á', 'a').replace(',', '').replace('ć', 'c').replace('ñ', 'n').replace(')', '').replace('ł', 'l').replace('-', '').replace('8', '').replace('ê', 'e').replace('1', '').replace('ę', 'e').replace('5', '').replace('š', '').replace('”', '').replace('ř', 'r').replace('î', 'i').replace('ö', '').replace('ã', 'a').replace('ň', 'n').replace('é', 'e').replace('.', '').replace('“', '')
        dfAlt.loc[index, 'name'] = cleanName
    if(isinstance(nickname, str)):
        cleanNickname = nickname.replace('2', '').replace('(', '').replace('3', '').replace('ú', 'u').replace('ç', 'c').replace('Á', 'A').replace('7', '').replace('í', 'i').replace('0', '').replace('ě', 'e').replace('4', '').replace("'", '').replace('%', '').replace('"', '').replace('á', 'a').replace(',', '').replace('ć', 'c').replace('ñ', 'n').replace(')', '').replace('ł', 'l').replace('-', '').replace('8', '').replace('ê', 'e').replace('1', '').replace('ę', 'e').replace('5', '').replace('š', '').replace('”', '').replace('ř', 'r').replace('î', 'i').replace('ö', '').replace('ã', 'a').replace('ň', 'n').replace('é', 'e').replace('.', '').replace('“', '')
        dfAlt.loc[index, 'nickname'] = cleanNickname

for char in chars2rep:
    for index, row in dfAlt.iterrows():
        name = row['name']
        nickname = row['nickname']
        if(char != '~'):
            if(isinstance(name, str)):
                cleanName = name.replace(char, '')
                dfAlt.loc[index, 'name'] = cleanName
            if(isinstance(nickname, str)):
                cleanNickname = nickname.replace(char, '')
                dfAlt.loc[index, 'nickname'] = cleanNickname


#assign nicknames for matching names found within dataframes
count = 1
for index, row in df.iterrows():
    name = row['name']
    nickname = row['nickname']
    dup_check = df.loc[df['name'] == name]
    dup_check2 = dfAlt.loc[dfAlt['name'] == name]
    if(len(dup_check == 1) and len(dup_check2) == 1):
        try:
            altIndex = dfAlt.loc[dfAlt['name'] == name].index[0]
            altNickname = dfAlt.loc[altIndex, 'nickname']
            if(nickname != altNickname):
                if(nickname == '!' and altNickname == '~'):
                    df.loc[index, 'nickname'] = str(count)
                    dfAlt.loc[altIndex, 'nickname'] = str(count)
                    count+=1
                elif(nickname != '!'):
                    dfAlt.loc[altIndex, 'nickname'] = nickname
                elif(altNickname != '~'):
                    df.loc[index, 'nickname'] = altNickname
        except:
            pass



#outer merge the dfs
dfMerged = pd.merge(df, dfAlt, on=['name', 'nickname'], how='outer', indicator=True)
dfMerged.head()


#query dfMerged for intersections
dfCombined = pd.DataFrame(dfMerged.query('_merge == "both"'))
dfCombined.head()

#set blank values to nan
dfCombined.replace('--', np.nan, inplace=True)


#define column headers
column_headers = [
    'name', 'nickname', 'wins', 'losses', 'draws', 'age', 'nation', 'knockdown_avg', 'sig_str_accuracy', 
    'takedown_average', 'takedown_accuracy', 'subs_attempted_average', 'height', 'reach', 
    'stance', 'sig_str_landed_per_min', 'average_fight_time', 'sig_str_absorbed_per_min', 'sig_str_defense',
    'takedown_defense'
]

#create dataframe using headers
dfCareer = pd.DataFrame(columns=column_headers)
dfCareer.head()


#populate df
for index, row in dfCombined.iterrows():
    #initalize attributes
    name = None
    nickname = None
    wins = None
    losses = None
    draws = None
    age = None
    nation = None
    knockdown_avg = None
    sig_str_accuracy = None
    takedown_average = None
    takedown_accuracy = None
    subs_attempted_average = None
    height = None
    reach = None
    stance = None
    sig_str_landed_per_min = None
    average_fight_time = None
    sig_str_absorbed_per_min = None
    sig_str_defense = None
    takedown_defense = None

    name = row['name']
    nickname = row['nickname']

    if row['wins_x'] != np.nan:
        wins = row['wins_x']
    else:
        wins = row['wins_y']
    
    if row['losses_x'] != np.nan:
        losses = row['losses_x']
    else:
        losses = row['losses_y']
    
    if row['draws_x'] != np.nan:
        draws = row['draws_x']
    else:
        draws = row['draws_y']

    if row['dOB'] != np.nan:
        age = row['dOB']
    else:
        age = row['age']
    
    nation = row['nation']

    knockdown_avg = row['knockdown_avg']

    if row['sig_striking_accuracy_%'] != np.nan:
        sig_str_accuracy = row['sig_striking_accuracy_%']
    else:
        sig_str_accuracy = row['sig_str_accuracy']

    if row['takedown_average(average_takedown_landed_per_fifteen_min)'] != np.nan:
        takedown_average = row['takedown_average(average_takedown_landed_per_fifteen_min)']
    else:
        takedown_average = row['takedown_avg_per_fifteen']

    if row['takedown_accuracy_%'] != np.nan:
        takedown_accuracy = row['takedown_accuracy_%']
    else:
        takedown_accuracy = row['takedown_accuracy']
    
    if row['sub_average(average_subs_attempted_per_15_mins)'] != np.nan:
        subs_attempted_average = row['sub_average(average_subs_attempted_per_15_mins)']
    else:
        subs_attempted_average = row['submission_avg_per_fifteen']

    if row['height_x'] != np.nan:
        height = row['height_x']
    else:
        height = row['height_y']
    
    if row['reach_x'] != np.nan:
        reach = row['reach_x']
    else:
        reach = row['reach_y']

    stance = row['stance']

    if row['sig_strikes_landed_per_min'] != np.nan:
        sig_str_landed_per_min = row['sig_strikes_landed_per_min']
    else:
        sig_str_landed_per_min = row['sig_str_per_minute']

    average_fight_time = row['avg_fight_time']

    if row['sig_strike_absorbed_per_min'] != np.nan:
        sig_str_absorbed_per_min = row['sig_strike_absorbed_per_min']
    else:
        sig_str_absorbed_per_min = row['sig_str_absorbed_per_min']

    if row['sig_strike_defense(%_of_sig_strikes_not_landed_by_opponent)'] != np.nan:
        sig_str_defense = row['sig_strike_defense(%_of_sig_strikes_not_landed_by_opponent)']
    else:
        sig_str_defense = row['sig_str_defense']

    if row['takedown_defense(%_of_opponent_takedown_not_landed)'] != np.nan:
        takedown_defense = row['takedown_defense(%_of_opponent_takedown_not_landed)']
    else:
        takedown_defense = row['takedown_defense']


    column_vals = {
        'name': name,
        'nickname': nickname,
        'wins': wins,
        'losses': losses,
        'draws': draws,
        'age': age,
        'nation': nation,
        'knockdown_avg': knockdown_avg,
        'sig_str_accuracy': sig_str_accuracy,
        'takedown_average': takedown_average,
        'takedown_accuracy': takedown_accuracy,
        'subs_attempted_average': subs_attempted_average,
        'height': height,
        'reach': reach,
        'stance': stance,
        'sig_str_landed_per_min': sig_str_landed_per_min,
        'average_fight_time': average_fight_time,
        'sig_str_absorbed_per_min': sig_str_absorbed_per_min,
        'sig_str_defense': sig_str_defense,
        'takedown_defense': takedown_defense
    }
    dfCareer.loc[len(dfCareer)] = column_vals

dfCareer.head()


#reformat age
for index, row in dfCareer.iterrows():
    age = row['age']
    if(isinstance(age, str)):
        age = age.replace(',', '')
        listAge = age.split(' ')
        year = listAge[2]
        #if int(year)>30:
            #year = f'{year}'
        #else:
            #year = f'{year}'
        listAge.pop()
        listAge.append(year)
        age = '-'.join(listAge)
        dfCareer.at[index, 'age'] = age


dfCareer.head()



dfCareer.to_csv(f'careerStatsData{dateToday}.csv', index=False)



#read new df
df = pd.read_csv(f'databaseUpdated{dateToday}.csv')

df.head()


#In this df nans ar represented as '---' - replacing this with nan
df.replace('---', np.nan, inplace=True)
df.replace('--', np.nan, inplace=True)


#Dropping all rows where red and blue corners are not recorded correctly
#Not recorded correctly until 03.21.2010
#Since this will affect the accuracy of the model I am removing it for now
#Will try and find a credible source to fix this at a later date

rows, columns = df.shape

event_condition = df['event'] == 'UFC 110: Nogueira vs Velasquez'
fight_condition = df['fight'] == 'Cain Velasquez vs Antonio Rodrigo Nogueira'

recordedIncorrectly = df.loc[event_condition & fight_condition].index[0]
recordedIncorrectly -= rows
print(recordedIncorrectly)
df = df.iloc[:recordedIncorrectly]

#if redCorner won winner set to 0
for index, row in df.iterrows():
    if(row['redCorner'] == row['winner']):
        df.at[index, 'winner'] = 0

df.head()


#set all winners from fights won by blue corner to 2
for index, row in df.iterrows():
    if(row['blueCorner'] == row['winner']):
        df.at[index, 'winner'] = 2

df.head()


#check all winners have been replaced
winner_values = df['winner'].tolist()
winner_values = list(set(winner_values))
print(winner_values)


#all fights with no winner set to 1
df['winner'].fillna(1, inplace=True)


#check all winners are now numerical
winner_values = df['winner'].tolist()
winner_values = list(set(winner_values))
print(winner_values)

#set redCorner values to 0 and blueCorner vals to 2
df['redCorner'] = 0
df['blueCorner'] = 2
df.head()

#check all redCorners were changed correctly
redCorner_values = df['redCorner'].tolist()
redCorner_values = list(set(redCorner_values))
print(redCorner_values)

#check all blueCorners were changed correctly
blueCorner_values = df['blueCorner'].tolist()
blueCorner_values = list(set(blueCorner_values))
print(blueCorner_values)


#drop column fight, event, method_of_vic, date
df.drop('fight', axis=1, inplace=True)
df.drop('event', axis=1, inplace=True)
df.drop('method_of_victory', axis=1, inplace=True)
df.drop('date', axis=1, inplace=True)
df.head()


#find special characters in referees
referees = (df['referee'].values)
chars2rep = []
for referee in referees:
    if(isinstance(referee, str)):
        for char in referee:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
chars2rep = list(set(chars2rep))
for char in chars2rep:
    print(char)


#clean referees
for index, row in df.iterrows():
    referee = row['referee']
    if isinstance(referee, str):
        cleaned_referee = referee.replace(',', '').replace('-', '').replace('.', '').replace(' ', '').lower()
        df.loc[index, 'referee'] = cleaned_referee
df.head()

#give referees numerical value
referees = df['referee'].tolist()

referees = list(set(referees))

count = 0 
for ref in referees:
    df['referee'] = df['referee'].replace(ref, count, regex=True)
    count += 1


#check all referees were assigned a numerical value
referee_values = df['referee'].tolist()
referee_values = list(set(referee_values))
print(referee_values)


#find special characters in venue
venues = (df['venue'].values)
chars2rep = []
for venue in venues:
    if(isinstance(venue, str)):
        for char in venue:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(str(char))
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(str(char))
chars2rep = list(set(chars2rep))
for char in chars2rep:
    print(char)


#clean venues
cleaned_venues = []
for index, row in df.iterrows():
    venue = row['venue']
    cleaned_venue = venue
    for char in chars2rep:
        cleaned_venue = cleaned_venue.replace(char, '')
    cleaned_venue = cleaned_venue.replace(' ', '')
    cleaned_venues.append(cleaned_venue.lower())

df['venue'] = cleaned_venues
        
df.head()


#confirm cleaning worked as intended
venue_values = df['venue'].tolist()
venue_values = list(set(venue_values))
print(venue_values)


#give venues numerical value
venues = df['venue']
venues1 = []
for venue in venues:
    venues1.append(venue)

venues1 = list(set(venues1))

count = 0 
for venue in venues1:
    df['venue'] = df['venue'].replace(venue, count, regex=True)
    count += 1
df.head()


#find special characters in billings
billings = (df['billing'].values)
chars2rep = []
for billing in billings:
    if(isinstance(billing, str)):
        for char in billing:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
chars2rep = list(set(chars2rep))
for char in chars2rep:
    print(char)


#clean billings
for index, row in df.iterrows():
    df.loc[index, 'billing'] = row['billing'].replace('-', '')


for index, row in df.iterrows():
    df.loc[index, 'billing'] = row['billing'].replace(" ", "")


#check billings
colVals = []
for index, row in df.iterrows():
    colVals.append(row['billing'])

colVals = list(set(colVals))
for val in colVals:
    print(val)



#give billings numerical value
df['billing'] = df['billing'].replace('MainEvent', 0)
df['billing'] = df['billing'].replace('CoMainEvent', 1)
df['billing'] = df['billing'].replace('MainCard', 2)
df['billing'] = df['billing'].replace('PreliminaryCard', 3)


#check billings
colVals = []
for index, row in df.iterrows():
    colVals.append(row['billing'])

colVals = list(set(colVals))
for val in colVals:
    print(val)


#make title fight binary
df['title_fight'] = df['title_fight'].replace('yes', 1)
df['title_fight'] = df['title_fight'].replace('no', 0)


#find special characters in nations
redCorner_nation = df['redCorner_nation'].values
blueCorner_nation = df['blueCorner_nation'].values
chars2rep = []
for nation in redCorner_nation:
    if(isinstance(nation, str)):
        for char in nation:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
for nation in blueCorner_nation:
    if(isinstance(nation, str)):
        for char in nation:
            if char.lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']:
                chars2rep.append(char)
            if char.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                chars2rep.append(char)
chars2rep = list(set(chars2rep))
for char in chars2rep:
    print(char)


#clean redCorner_nation
df['redCorner_nation'] = df['redCorner_nation'].replace('Croatia (Hrvatska)', 'Croatia')
df['redCorner_nation'] = df['redCorner_nation'].replace('Virgin Islands (US)', 'Virgin Islands')
#clean blueCorner_nation
df['blueCorner_nation'] = df['blueCorner_nation'].replace('Croatia (Hrvatska)', 'Croatia')
df['blueCorner_nation'] = df['blueCorner_nation'].replace('Virgin Islands (US)', 'Virgin Islands')


for index, row in df.iterrows():
    nation = row['redCorner_nation']
    if(isinstance(nation, str)):
        df.loc[index, 'redCorner_nation'] = row['redCorner_nation'].replace(" ", "").lower()

for index, row in df.iterrows():
    nation = row['blueCorner_nation']
    if(isinstance(nation, str)):
        df.loc[index, 'blueCorner_nation'] = row['blueCorner_nation'].replace(" ", "").lower()



#generate individual dicts for both - universal dictionary causing problems
redCorner_nation_values = df['redCorner_nation'].tolist()
redCorner_nation_values = list(set(redCorner_nation_values))
blueCorner_nation_values = df['blueCorner_nation'].tolist()
blueCorner_nation_values = list(set(blueCorner_nation_values))
matched = []
notMatched = []
for blueNation in blueCorner_nation_values:
    for redNation in redCorner_nation_values:
        if blueNation == redNation:
            matched.append(blueNation)
    
matched = list(set(matched))
print(redCorner_nation_values)
print(len(redCorner_nation_values))
print(blueCorner_nation_values)
print(len(blueCorner_nation_values))
print(matched)
print(len(matched))


#create list for redNations keeping order with list for blueNations
finalizedRed = []
i=0
for i in range(len(matched)):
    finalizedRed.append(matched[i])
print(len(finalizedRed))
for nation in redCorner_nation_values:
    if nation not in matched:
        finalizedRed.append(nation)
print(len(finalizedRed))


#create dict for reddNations keeping order with list for blueNations
redNationDict = {}
count = 0
for nation in finalizedRed:
    redNationDict[nation] = count
    count+=1
print(redNationDict)


#give redCorner_nation numerical val
for index, row in df.iterrows():
    redCorner_nation = row['redCorner_nation']
    numericalVal = redNationDict[redCorner_nation]
    df.loc[index, 'redCorner_nation'] = numericalVal

#confirm redCorner_nations are now numerical
print(list(set(df['redCorner_nation'].tolist())))


#create list for blueNations keeping order with list for redNations
extrasBlue = []
for nation in blueCorner_nation_values:
    if nation not in matched:
        extrasBlue.append(nation)
print(len(extrasBlue))
print(len(matched))



#create dict for blueNations keeping order with list for redNations
blueNationDict = {}
count = 0
for nation in matched:
    blueNationDict[nation] = count
    count+=1
#initalize count above highest in redValues
count =0
values_list = list(redNationDict.values())
for value in values_list:
    if int(value) > count:
        count = int(value)
count += 1
for nation in extrasBlue:
    if(nation != np.nan):
        blueNationDict[nation] = count
        count+=1

blueNationDict[np.nan] = redNationDict[np.nan]
print(blueNationDict)
print(len(blueNationDict))



#give blueCorner_nation numerical val
for index, row in df.iterrows():
    blueCorner_nation = row['blueCorner_nation']
    numericalVal = blueNationDict[blueCorner_nation]
    df.loc[index, 'blueCorner_nation'] = numericalVal

#confirm blueCorner_nations are now numerical
print(list(set(df['blueCorner_nation'].tolist())))


#build nation dict for test data
fullNationDict = blueNationDict
for key, value in redNationDict.items():
    if key not in blueNationDict:
        fullNationDict[key] = value
print(fullNationDict)

#Dropping fan votes because there is an issue in the database. Will try and fix at later date
df.drop('redCorner_fan', axis=1, inplace=True)
df.drop('blueCorner_fan', axis=1, inplace=True)


#keeping knockdowns column as is for now. But need to test it while dividing this by total fight time
nan_rows_count = df['redCorner_knockdowns'].isna().sum()
print(nan_rows_count)
nan_rows_count = df['blueCorner_knockdowns'].isna().sum()
print(nan_rows_count)
df.head()



#adding columns redCorner_sig_str_per_minute and blueCorner_sig_str_per_minute
df['redCorner_sig_str_landed_per_minute'] = float('nan')
df['blueCorner_sig_str_landed_per_minute'] = float('nan')
df['fightTime'] = float('nan')
df.head()


#confirm no rows with nan for round or time
nan_rows_count = df['time'].isna().sum()
print(nan_rows_count)
nan_rows_count = df['round'].isna().sum()
print(nan_rows_count)


#format totalTime as float
for index, row in df.iterrows():
    time = row['time']
    round = row['round']
    time = time.split(':')
    totalTime = (round-1)*5.00
    totalTime += float(time[0])
    time = float(time[1])
    time = time/60
    totalTime += time
    df.loc[index, 'fightTime'] = totalTime
    
df.head()


#calculate value and set redCorner_sig_str_per_minute
for index, row in df.iterrows():
    totals = row['redCorner_sig_str']
    if(isinstance(totals, str)):
        totals = totals.split(' ')
        landed = float(totals[0])
        fightTime = row['fightTime']
        sig_str_per_min = landed/fightTime
        df.loc[index, 'redCorner_sig_str_landed_per_minute'] = sig_str_per_min

df.head()



#calculate value and set blueCorner_sig_str_per_minute
for index, row in df.iterrows():
    totals = row['blueCorner_sig_str']
    if(isinstance(totals, str)):
        totals = totals.split(' ')
        landed = float(totals[0])
        fightTime = row['fightTime']
        sig_str_per_min = landed/fightTime
        df.loc[index, 'blueCorner_sig_str_landed_per_minute'] = sig_str_per_min

df.head()

#fix divide by zero errors
df['redCorner_sig_str_percentage'].fillna('0%', inplace=True)


#confirm no rows with nan sig_strike_accuracy
nan_rows_count = df['redCorner_sig_str_percentage'].isna().sum()
print(nan_rows_count)


#reformat redCorner_sig_str_percentage to float
for index, row in df.iterrows():
    redCorner_sig = row['redCorner_sig_str_percentage']
    listsig = redCorner_sig.split('%')
    reformatted = float(listsig[0])/100.00
    df.loc[index, 'redCorner_sig_str_percentage'] = reformatted

print(df['redCorner_sig_str_percentage'].tolist())


#fix divide by zero errors
df['blueCorner_sig_str_percentage'].fillna('0%', inplace=True)


#confirm no rows with nan sig_strike_accuracy
nan_rows_count = df['blueCorner_sig_str_percentage'].isna().sum()
print(nan_rows_count)


#reformat blueCorner_sig_str_percentage to float
for index, row in df.iterrows():
    blueCorner_sig = row['blueCorner_sig_str_percentage']
    listsig = blueCorner_sig.split('%')
    reformatted = float(listsig[0])/100.00
    df.loc[index, 'blueCorner_sig_str_percentage'] = reformatted

print(df['blueCorner_sig_str_percentage'].tolist())

#adding columns redCorner_sig_str_per_minute and blueCorner_sig_str_per_minute
df['redCorner_sig_str_absorbed_per_minute'] = float('nan')
df['blueCorner_sig_str_absorbed_per_minute'] = float('nan')

df.head()

#check for nans
nan_count = df['blueCorner_sig_str'].isna().sum()
print(nan_count)



#May not use this value as it is linearly dependent with sig_strikes_landed_per_min, will see during testing phase
#Need to round it to two dec places and test that too
for index, row in df.iterrows():
    totals = row['blueCorner_sig_str'].split(' ')
    landedByOpp = float(totals[0])
    fightTime = float(row['fightTime'])
    absorbed_per_min = landedByOpp/fightTime
    df.loc[index, 'redCorner_sig_str_absorbed_per_minute'] = absorbed_per_min

df.head()


#check for nans
nan_count = df['redCorner_sig_str'].isna().sum()
print(nan_count)



#May not use this value as it is linearly dependent with sig_strikes_landed_per_min, will see during testing phase
#Need to round it to two dec places and test that too
for index, row in df.iterrows():
    totals = row['redCorner_sig_str'].split(' ')
    landedByOpp = float(totals[0])
    fightTime = float(row['fightTime'])
    absorbed_per_min = landedByOpp/fightTime
    df.loc[index, 'blueCorner_sig_str_absorbed_per_minute'] = absorbed_per_min

df.head()


#adding columns redCorner_sig_str_defense and blueCorner_sig_str_defense
df['redCorner_sig_str_defense'] = float('nan')
df['blueCorner_sig_str_defense'] = float('nan')

df.head()


#calculate redCorner sig_str_defense
for index, row in df.iterrows():
    totals = row['blueCorner_sig_str'].split(' ')
    missed = float(totals[2]) - float(totals[0])
    try:
        sig_str_defense = float(missed/float(totals[2]))
    except:
        #if no strikes were attempted then defense is 100%
        sig_str_defense = 1
    df.loc[index, 'redCorner_sig_str_defense'] = sig_str_defense

df.head()



#calculate blueCorner sig_str_defense
for index, row in df.iterrows():
    totals = row['redCorner_sig_str'].split(' ')
    missed = float(totals[2]) - float(totals[0])
    try:
        sig_str_defense = float(missed/float(totals[2]))
    except:
        #if no strikes were attempted then defense is 100%
        sig_str_defense = 1.0
    df.loc[index, 'blueCorner_sig_str_defense'] = sig_str_defense

df.head()



#fix divide by zero errors
df['redCorner_takedown_percentage'].fillna('0%', inplace=True)
df['blueCorner_takedown_percentage'].fillna('0%', inplace=True)



#format redCorner_takedown_percentage as float
for index, row in df.iterrows():
    takedown_percent = row['redCorner_takedown_percentage'].split('%')
    takedown_percent = float(takedown_percent[0])
    takedown_float = takedown_percent/100
    df.at[index, 'redCorner_takedown_percentage'] = takedown_float

df.head()


#format blueCorner_takedown_percentage as float
for index, row in df.iterrows():
    takedown_percent = row['blueCorner_takedown_percentage'].split('%')
    takedown_percent = float(takedown_percent[0])
    takedown_float = takedown_percent/100
    df.at[index, 'blueCorner_takedown_percentage'] = takedown_float

df.head()


#adding columns redCorner_takedown_defense and blueCorner_takedown_defense
df['redCorner_takedown_defense'] = float('nan')
df['blueCorner_takedown_defense'] = float('nan')

df.head()


#redCorner_takedown_defense
#May not use this value as it is linearly dependent with takedown_percentage, will see during testing phase
for index, row in df.iterrows():
    totals = row['blueCorner_takedowns'].split(' ')
    missedByOpp = float(totals[2]) - float(totals[0])
    attempted = float(totals[2])
    try:
        defended = missedByOpp/attempted
    except:
        #if zero were attempted defense is 100%
        defended = 1.0
    df.loc[index, 'redCorner_takedown_defense'] = defended

df.head()


#blueCorner_takedown_defense
#May not use this value as it is linearly dependent with takedown_percentage, will see during testing phase
for index, row in df.iterrows():
    totals = row['redCorner_takedowns'].split(' ')
    missedByOpp = float(totals[2]) - float(totals[0])
    attempted = float(totals[2])
    try:
        defended = missedByOpp/attempted
    except:
        #if zero were attempted defense is 100%
        defended = 1.0
    df.loc[index, 'blueCorner_takedown_defense'] = defended

df.head()


#reformatting redCorner_takedowns to be purely how many they landed
for index, row in df.iterrows():
    totals = row['redCorner_takedowns'].split(' ')
    landed = float(totals[0])
    df.loc[index, 'redCorner_takedowns'] = landed

print(df['redCorner_takedowns'].tolist())


#reformatting blueCorner_takedowns to be purely how many they landed
for index, row in df.iterrows():
    totals = row['blueCorner_takedowns'].split(' ')
    landed = float(totals[0])
    df.loc[index, 'blueCorner_takedowns'] = landed

print(df['blueCorner_takedowns'].tolist())

#dropping columns no longer needed
df.drop('redCorner_sig_str', axis=1, inplace=True)
df.drop('blueCorner_sig_str', axis=1, inplace=True)
df.drop('redCorner_total_str', axis=1, inplace=True)
df.drop('blueCorner_total_str', axis=1, inplace=True)
df.drop('round', axis=1, inplace=True)
df.drop('time', axis=1, inplace=True)


print(len(df))
df.dropna(inplace=True)
print(len(df))

unique_stances = df['redCorner_stance'].unique()
uniqueStances = df['blueCorner_stance'].unique()

print(unique_stances)
print(uniqueStances)


#format stances

df['redCorner_stance'] = df['redCorner_stance'].replace('Orthodox', 0)
df['blueCorner_stance'] = df['blueCorner_stance'].replace('Orthodox', 0)

df['redCorner_stance'] = df['redCorner_stance'].replace('Southpaw', 1)
df['blueCorner_stance'] = df['blueCorner_stance'].replace('Southpaw', 1)

df['redCorner_stance'] = df['redCorner_stance'].replace('Open Stance', 2)
df['blueCorner_stance'] = df['blueCorner_stance'].replace('Open Stance', 2)

df['redCorner_stance'] = df['redCorner_stance'].replace('Switch', 3)
df['blueCorner_stance'] = df['blueCorner_stance'].replace('Switch', 3)


stances = df['blueCorner_stance'].values.tolist()
stancesred = df['redCorner_stance'].values.tolist()
print(list(set(stances)))
print(list(set(stancesred)))


#format height
for index, row in df.iterrows():
    height = row['redCorner_height']
    height = height.replace("'", '').replace('"', '')
    lHeight = height.split(' ')
    finalHeight = int(lHeight[0])*12+int(lHeight[1])
    df.loc[index, 'redCorner_height'] = int(finalHeight)


redCornerHeights = df['redCorner_height'].values.tolist()
print(list(set(redCornerHeights)))


#format height
for index, row in df.iterrows():
    height = row['blueCorner_height']
    height = height.replace("'", '').replace('"', '')
    lHeight = height.split(' ')
    finalHeight = int(lHeight[0])*12+int(lHeight[1])
    df.loc[index, 'blueCorner_height'] = int(finalHeight)


blueCornerHeights = df['blueCorner_height'].values.tolist()
print(list(set(blueCornerHeights)))

#clean reaches
for index, row in df.iterrows():
    reach = row['redCorner_reach']
    newreach = reach.replace('"', '')
    df.loc[index, 'redCorner_reach'] = int(newreach)


#confirm reaches are changed
redCornerReach = df['redCorner_reach'].values.tolist()
print(list(set(redCornerReach)))

#clean reaches
for index, row in df.iterrows():
    reach = row['blueCorner_reach']
    newreach = reach.replace('"', '')
    df.loc[index, 'blueCorner_reach'] = int(newreach)


#confirm reaches are changed
redCornerReach = df['redCorner_reach'].values.tolist()
print(list(set(redCornerReach)))


df.to_csv(f'traindata{dateToday}.csv', index=False)


dfTest = pd.read_csv(f'careerStatsData{dateToday}.csv')
dfTest.head()


#clean draws to numerical
for index, row in dfTest.iterrows():
    draw = row['draws']
    listdraw = draw.split(' ')
    dfTest.loc[index, 'draws'] = int(listdraw[0])


types = []
for index, row in dfTest.iterrows():
    types.append(type(row['age']))
print(list(set(types)))


from datetime import date
#calculate age of fighter
def calculate_age(year, month, day):
    today = date.today()
    return today.year - year - ((today.month, today.day) < (month, day))


for index, row in dfTest.iterrows():
    born = row['age']
    if(isinstance(born, str)):
        listBorn = born.split('-')
        day = listBorn[1]
        month = listBorn[0]
        year = listBorn[2]
        if month == 'Jan':
            month = 1
        if month == 'Feb':
            month = 2
        if month == 'Mar':
            month = 3
        if month == 'Apr':
            month = 4
        if month == 'May':
            month = 5
        if month == 'Jun':
            month = 6
        if month == 'Jul':
            month = 7
        if month == 'Aug':
            month = 8
        if month == 'Sep':
            month = 9
        if month == 'Oct':
            month = 10
        if month == 'Nov':
            month = 11
        if month == 'Dec':
            month = 12
        age = calculate_age(int(year), int(month), int(day))
        dfTest.loc[index, 'age'] = float(age)

dfTest.head()


#reformat nation to just the nation name
for index, row in dfTest.iterrows():
    nation = row['nation']
    if(isinstance(nation, str)):
        if ',' in nation:
            listn = nation.split(',')
            country = listn[len(listn)-1]
            countryFinal = country[1:]
            dfTest.at[index, 'nation'] = countryFinal


dfTest['nation'] = dfTest['nation'].replace("Congo - Kinshasa", "Congo", regex=True)
dfTest['nation'] = dfTest['nation'].replace("Myanmar (Burma)", "Myanmar", regex=True)

dfTest.head()


#clean nations
for index, row in dfTest.iterrows():
    nation = row['nation']
    if(isinstance(nation, str)):
        dfTest.loc[index, 'nation'] = row['nation'].replace(" ", "").lower()

dfTest.head()


#give nation numerical value
for index, row in dfTest.iterrows():
    nation = row['nation']
    vals = list(set(fullNationDict.values()))
    nextVal = max(vals)+1
    try:
        numericalvalue = fullNationDict[nation]
    except:
        fullNationDict[nation] = nextVal
        numericalvalue = fullNationDict[nation]
    dfTest.at[index, 'nation'] = numericalvalue



types = []
for index, row in dfTest.iterrows():
    types.append(type(row['height']))
print(list(set(types)))



#reformat sig_str_accuracy to float
for index, row in dfTest.iterrows():
    sig = row['sig_str_accuracy']
    sig = sig.replace('%', '')
    intsig = int(sig)
    floatsig = intsig/100
    dfTest.at[index, 'sig_str_accuracy'] = floatsig

dfTest.head()



#reformat takedown_accuracy to float
for index, row in dfTest.iterrows():
    tda = row['takedown_accuracy']
    tda = tda.replace('%', '')
    inttda = int(tda)
    floattda = inttda/100
    dfTest.at[index, 'takedown_accuracy'] = floattda

dfTest.head()



#reformat height to be displayed in inches
for index, row in dfTest.iterrows():
    height = row['height']
    if(isinstance(height, str)):
        height = height.replace('"', '').replace("'", '')
        listheight = height.split(' ')
        if len(listheight)>1:
            feet = int(listheight[0])
            inches = int(listheight[1])
            height = feet*12+inches
        dfTest.at[index, 'height'] = height
        
dfTest.head()



#reformat reach to be displayed in inches
for index, row in dfTest.iterrows():
    reach = row['reach']
    if(isinstance(reach, str)):
        reach = reach.replace('"', '').replace("'", '')
    dfTest.at[index, 'reach'] = reach

dfTest.head()



stances = []
for index, row in dfTest.iterrows():
    stance = row['stance']
    stances.append(stance)

print(list(set(stances)))


#format stances
dfTest['stance'] = dfTest['stance'].replace('Orthodox', 0)

dfTest['stance'] = dfTest['stance'].replace('Southpaw', 1)

dfTest['stance'] = dfTest['stance'].replace('Open Stance', 2)

dfTest['stance'] = dfTest['stance'].replace('Switch', 3)

dfTest['stance'] = dfTest['stance'].replace('Sideways', 4)

dfTest.head()

#format average fight time
for index, row in dfTest.iterrows():
    fightTime = row['average_fight_time']
    if(isinstance(fightTime, str)):
        timeList = fightTime.split(':')
        totalTime = float(timeList[0]) + float(timeList[1])/60
        dfTest.at[index, 'average_fight_time'] = totalTime

dfTest.head()


#reformat sig_str_defense to float
for index, row in dfTest.iterrows():
    ssd = row['sig_str_defense']
    ssd = ssd.replace('%', '')
    intssd = int(ssd)
    floatssd = intssd/100
    dfTest.at[index, 'sig_str_defense'] = floatssd

dfTest.head()



#reformat sig_str_defense to float
for index, row in dfTest.iterrows():
    td = row['takedown_defense']
    td = td.replace('%', '')
    inttd = int(td)
    floattd = inttd/100
    dfTest.at[index, 'takedown_defense'] = floattd

dfTest.head()

print(len(dfTest))
dfTest.dropna(inplace=True)
print(len(dfTest))



dfTest.to_csv(f'careerDataFormatTest{dateToday}.csv', index=False)


#define column headers
column_headers = [
    'Fight', 'Prediction', 'Predicted', 'Winner', 'Result'
]

#create dataframe using headers
dfTracking = pd.DataFrame(columns=column_headers)
dfTracking.head()


dfPrevPreds = pd.read_csv(f'predictions{mostRecentDatabase}.csv')
dfPrevPreds.head()


dfCheck = pd.read_csv(f'databaseUpdated{dateToday}.csv')
dfCheck.head()



#find index of the last fight of the previous event
change = dfCheck['event'] != dfCheck['event'].shift(1)

# Find the first index where the 'event' is different
indexDifferent = dfCheck[change].index[1] 

limitOfCheck = indexDifferent-1

print(limitOfCheck)



for index, row in dfPrevPreds.iterrows():
    winner = None
    if(type(row['Result']) != str):
        fight = row['Fight']
        redAndBlue = fight.split(' vs ')
        redCorner = redAndBlue[0]
        blueCorner = redAndBlue[1]
        prediction = row['Prediction']
        #find indexes of fight match
        try:
            redCornerCheck = dfCheck[:limitOfCheck][dfCheck['redCorner'][:limitOfCheck] == redCorner].index[0]
            blueCornerCheck = dfCheck[:limitOfCheck][dfCheck['blueCorner'][:limitOfCheck] == blueCorner].index[0]
            if(int(redCornerCheck) == int(blueCornerCheck)):
                indexCheck = int(redCornerCheck)
                winner = dfCheck.loc[indexCheck, 'winner']
                if(winner == redCorner and float(prediction) < 0.5):
                    dfPrevPreds.loc[index, 'Result'] = 'Correct'
                    dfPrevPreds.loc[index, 'Winner'] = winner
                elif(winner == blueCorner and float(prediction) > 0.5):
                    dfPrevPreds.loc[index, 'Result'] = 'Correct'
                    dfPrevPreds.loc[index, 'Winner'] = winner
                else:
                    dfPrevPreds.loc[index, 'Result'] = 'Incorrect'
                    dfPrevPreds.loc[index, 'Winner'] = winner
        except:
            #upon exception, results get scraped as names will match here
            url = 'https://www.espn.com/mma/schedule/_/league/ufc'
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    
            #site request
            site = requests.get(url, headers=headers)
            soup = BeautifulSoup(site.content, 'html.parser')  

            #get table
            tbodys = soup.find_all('tbody', class_=re.compile('Table__TBODY')) 

            #get part
            table = tbodys[len(tbodys)-1]
            links = table.find_all('a', class_=re.compile('AnchorLink'))
            lastEvent = links[0]
            part = lastEvent['href']

            url = f'https://www.espn.com{part}'
            headers = {'User-Agent': "insomnia/9.1.1"}
    
            #site request
            site = requests.get(url, headers=headers)
            soup = BeautifulSoup(site.content, 'html.parser')

            right = soup.find_all('div', class_=re.compile('MMACompetitor relative flex flex-uniform pl6 MMACompetitor--desktop'))
            left = soup.find_all('div', class_=re.compile('MMACompetitor relative flex flex-uniform pr6 flex-row-reverse MMACompetitor--desktop'))

            #find match
            for item1, item2 in zip(left, right):
                if redCorner in item1.text.strip() and blueCorner in item2.text.strip():
                    if(item1.find('svg') is not None):
                        winner = redCorner
                    if(item2.find('svg') is not None):
                        winner = blueCorner
            if(winner == redCorner and float(prediction) < 0.5):
                dfPrevPreds.loc[index, 'Result'] = 'Correct'
                dfPrevPreds.loc[index, 'Winner'] = winner
            elif(winner == blueCorner and float(prediction) > 0.5):
                dfPrevPreds.loc[index, 'Result'] = 'Correct'
                dfPrevPreds.loc[index, 'Winner'] = winner
            else:
                dfPrevPreds.loc[index, 'Result'] = 'Incorrect'
                dfPrevPreds.loc[index, 'Winner'] = winner

dfPrevPreds.head()
            
            



#scrape matchups for next event
#define url and headers
url = 'https://www.espn.com/mma/schedule/_/league/ufc'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}


#site request
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
print(site)


#find url of next card
divs = soup.find_all('div', class_=re.compile('Table__ScrollerWrapper relative overflow-hidden'))
print(divs[0])


#gt url of next card
link = divs[0]
hrefs = link.find('a')
part = hrefs['href']
print(part) 


#site request for next event
url = f'https://www.espn.com{part}'
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
print(url)
print(site)


#get fight names
sections = soup.find_all('section', class_=re.compile("Card MMAFightCard"))
print(sections[0])


h2s = sections[0].find_all('h2', class_=re.compile('h4 clr-gray-02'))
print(h2s)

fightersOnCard = []
for h2 in h2s:
    fightersOnCard.append(str(h2.text.strip()))
print(fightersOnCard)


h2s = sections[1].find_all('h2', class_=re.compile('h4 clr-gray-02'))
print(h2s)


for h2 in h2s:
    fightersOnCard.append(str(h2.text.strip()))
print(fightersOnCard)
print(len(fightersOnCard))


count = 0
fights = []
for i in range(int(len(fightersOnCard)/2)):
    fight = f'{fightersOnCard[count]} vs {fightersOnCard[count+1]}'
    fights.append(fight)
    count+=2
print(fights)


dfCareer = pd.read_csv(f'careerDataFormatTest{dateToday}.csv')
dfCareer.head()


for fight in fights:
    try:
        #define column headers for new df
        column_headers = ['redCorner', 'blueCorner', 'winner', 'redCorner_wins', 'blueCorner_wins', 'redCorner_losses', 
                        'blueCorner_losses', 'redCorner_draws', 'blueCorner_draws', 'redCorner_age', 'blueCorner_age',
                        'redCorner_nation', 'blueCorner_nation', 'redCorner_knockdowns', 'blueCorner_knockdowns',
                        'redCorner_sig_str_percentage', 'blueCorner_sig_str_percentage', 'redCorner_takedowns',
                        'blueCorner_takedowns', 'redCorner_takedown_percentage', 'blueCorner_takedown_percentage',
                        'redCorner_subs_attempted', 'blueCorner_subs_attempted', 'redCorner_height', 'blueCorner_height',
                        'redCorner_reach', 'blueCorner_reach', 'redCorner_stance', 'blueCorner_stance', 'redCorner_sig_str_landed_per_minute',
                        'blueCorner_sig_str_landed_per_minute', 'redCorner_fightTime', 'blueCorner_fightTime', 
                        'redCorner_sig_str_absorbed_per_minute', 'blueCorner_sig_str_absorbed_per_minute', 'redCorner_sig_str_defense',
                        'blueCorner_sig_str_defense', 'redCorner_takedown_defense', 'blueCorner_takedown_defense']

        #Create a new DataFrame with the specified column headers
        dfCustom = pd.DataFrame(columns=column_headers)


        fighters = fight.split(' vs ')
        fighter1 = str(fighters[0])
        fighter2 = str(fighters[1])

        #create custom input data
        redCorner = np.nan
        blueCorner = np.nan
        winner = np.nan
        redCorner_wins = np.nan
        blueCorner_wins = np.nan
        redCorner_losses = np.nan
        blueCorner_losses = np.nan
        redCorner_draws = np.nan
        blueCorner_draws = np.nan
        redCorner_age = np.nan
        blueCorner_age = np.nan
        redCorner_nation = np.nan
        blueCorner_nation = np.nan
        redCorner_knockdowns = np.nan
        blueCorner_knockdowns = np.nan
        redCorner_sig_str_percentage = np.nan
        blueCorner_sig_str_percentage = np.nan
        redCorner_takedowns = np.nan
        blueCorner_takedowns = np.nan
        redCorner_takedown_percentage = np.nan
        blueCorner_takedown_percentage = np.nan
        redCorner_subs_attempted = np.nan
        blueCorner_subs_attempted = np.nan
        redCorner_height = np.nan
        blueCorner_height = np.nan
        redCorner_reach = np.nan
        blueCorner_reach = np.nan
        redCorner_stance = np.nan
        blueCorner_stance = np.nan
        redCorner_sig_str_landed_per_minute = np.nan
        blueCorner_sig_str_landed_per_minute = np.nan 
        redCorner_fightTime = np.nan
        blueCorner_fightTime = np.nan
        redCorner_sig_str_absorbed_per_minute = np.nan
        blueCorner_sig_str_absorbed_per_minute = np.nan
        redCorner_sig_str_defense = np.nan
        blueCorner_sig_str_defense = np.nan
        redCorner_takedown_defense = np.nan 
        blueCorner_takedown_defense = np.nan
        if fighter1 in dfCareer['name'].values:
            try:
                indexCareer = dfCareer.index[dfCareer['name'] == fighter1].tolist()[0]
                redCorner = dfCareer.at[indexCareer, 'name']
                redCorner_wins = dfCareer.at[indexCareer, 'wins']
                redCorner_losses = dfCareer.at[indexCareer, 'losses']
                redCorner_draws = dfCareer.at[indexCareer, 'draws']
                redCorner_age = dfCareer.at[indexCareer, 'age']
                redCorner_nation = dfCareer.at[indexCareer, 'nation']
                redCorner_knockdowns = dfCareer.at[indexCareer, 'knockdown_avg']
                redCorner_sig_str_percentage = dfCareer.at[indexCareer, 'sig_str_accuracy']
                redCorner_takedowns = dfCareer.at[indexCareer, 'takedown_average']
                redCorner_takedown_percentage = dfCareer.at[indexCareer, 'takedown_accuracy']
                redCorner_subs_attempted = dfCareer.at[indexCareer, 'subs_attempted_average']
                redCorner_height = dfCareer.at[indexCareer, 'height']
                redCorner_reach = dfCareer.at[indexCareer, 'reach']
                redCorner_stance = dfCareer.at[indexCareer, 'stance']
                redCorner_sig_str_landed_per_minute = dfCareer.at[indexCareer, 'sig_str_landed_per_min']
                redCorner_fightTime = dfCareer.at[indexCareer, 'average_fight_time']
                redCorner_sig_str_absorbed_per_minute = dfCareer.at[indexCareer, 'sig_str_absorbed_per_min']
                redCorner_sig_str_defense = dfCareer.at[indexCareer, 'sig_str_defense']
                redCorner_takedown_defense = dfCareer.at[indexCareer, 'takedown_defense']
            except:
                pass
        else:
            raise ValueError('Not in list')
        if fighter2 in dfCareer['name'].values:
            try:
                indexCareer = dfCareer.index[dfCareer['name'] == fighter2].tolist()[0]
                blueCorner = dfCareer.at[indexCareer, 'name']
                blueCorner_wins = dfCareer.at[indexCareer, 'wins']
                blueCorner_losses = dfCareer.at[indexCareer, 'losses']
                blueCorner_draws = dfCareer.at[indexCareer, 'draws']
                blueCorner_age = dfCareer.at[indexCareer, 'age']
                blueCorner_nation = dfCareer.at[indexCareer, 'nation']
                blueCorner_knockdowns = dfCareer.at[indexCareer, 'knockdown_avg']
                blueCorner_sig_str_percentage = dfCareer.at[indexCareer, 'sig_str_accuracy']
                blueCorner_takedowns = dfCareer.at[indexCareer, 'takedown_average']
                blueCorner_takedown_percentage = dfCareer.at[indexCareer, 'takedown_accuracy']
                blueCorner_subs_attempted = dfCareer.at[indexCareer, 'subs_attempted_average']
                blueCorner_height = dfCareer.at[indexCareer, 'height']
                blueCorner_reach = dfCareer.at[indexCareer, 'reach']
                blueCorner_stance = dfCareer.at[indexCareer, 'stance']
                blueCorner_sig_str_landed_per_minute = dfCareer.at[indexCareer, 'sig_str_landed_per_min']
                blueCorner_fightTime = dfCareer.at[indexCareer, 'average_fight_time']
                blueCorner_sig_str_absorbed_per_minute = dfCareer.at[indexCareer, 'sig_str_absorbed_per_min']
                blueCorner_sig_str_defense = dfCareer.at[indexCareer, 'sig_str_defense']
                blueCorner_takedown_defense = dfCareer.at[indexCareer, 'takedown_defense']
            except:
                pass
        else:
            raise ValueError('Not in list')
        column_vals = {
            'redCorner': redCorner, 
            'blueCorner': blueCorner, 
            'winner': winner,
            'redCorner_wins': redCorner_wins, 
            'blueCorner_wins': blueCorner_wins, 
            'redCorner_losses': redCorner_losses, 
            'blueCorner_losses': blueCorner_losses, 
            'redCorner_draws': redCorner_draws, 
            'blueCorner_draws': blueCorner_draws, 
            'redCorner_age': redCorner_age, 
            'blueCorner_age': blueCorner_age,
            'redCorner_nation': redCorner_nation, 
            'blueCorner_nation': blueCorner_nation, 
            'redCorner_knockdowns': redCorner_knockdowns, 
            'blueCorner_knockdowns': blueCorner_knockdowns,
            'redCorner_sig_str_percentage': redCorner_sig_str_percentage, 
            'blueCorner_sig_str_percentage': blueCorner_sig_str_percentage, 
            'redCorner_takedowns': redCorner_takedowns,
            'blueCorner_takedowns': blueCorner_takedowns, 
            'redCorner_takedown_percentage': redCorner_takedown_percentage, 
            'blueCorner_takedown_percentage': blueCorner_takedown_percentage,
            'redCorner_subs_attempted': redCorner_subs_attempted, 
            'blueCorner_subs_attempted': blueCorner_subs_attempted, 
            'redCorner_height': redCorner_height, 
            'blueCorner_height': blueCorner_height,
            'redCorner_reach': redCorner_reach, 
            'blueCorner_reach': blueCorner_reach, 
            'redCorner_stance': redCorner_stance, 
            'blueCorner_stance': blueCorner_stance, 
            'redCorner_sig_str_landed_per_minute': redCorner_sig_str_landed_per_minute,
            'blueCorner_sig_str_landed_per_minute': blueCorner_sig_str_landed_per_minute, 
            'redCorner_fightTime': redCorner_fightTime, 
            'blueCorner_fightTime': blueCorner_fightTime, 
            'redCorner_sig_str_absorbed_per_minute': redCorner_sig_str_absorbed_per_minute, 
            'blueCorner_sig_str_absorbed_per_minute': blueCorner_sig_str_absorbed_per_minute, 
            'redCorner_sig_str_defense': redCorner_sig_str_defense,
            'blueCorner_sig_str_defense': blueCorner_sig_str_defense, 
            'redCorner_takedown_defense': redCorner_takedown_defense, 
            'blueCorner_takedown_defense': blueCorner_takedown_defense
        }
        dfCustom.loc[len(dfCustom)] = column_vals


        predictions = []
        for i in range(3):
            dfInput = dfCustom.copy()


            df = pd.read_csv(f'traindata{dateToday}.csv')


            df = df.dropna(inplace=False)


            #dropping referee
            df.drop('referee', axis=1, inplace=True)

            #drop billings
            df.drop('billing', axis=1, inplace=True)

            #drop venue
            df.drop('venue', axis=1, inplace=True)

            #drop title_fight
            df.drop('title_fight', axis=1, inplace=True)


            df.rename(columns={'fightTime': 'redCorner_fightTime'}, inplace=True)
            df.insert(32, 'blueCorner_fightTime', df['redCorner_fightTime'])

            dfColumns = df.columns


            dfInputColumns = dfInput.columns


            #one hot encode redCorner_nation
            column = df[['redCorner_nation']].copy()
            df_encoded = pd.get_dummies(column, columns=['redCorner_nation'], prefix='redCorner_nation').astype(int)
            df = pd.concat([df, df_encoded], axis=1)

            #one hot encode blueCorner_nation
            column = df[['blueCorner_nation']].copy()
            df_encoded = pd.get_dummies(column, columns=['blueCorner_nation'], prefix='blueCorner_nation').astype(int)
            df = pd.concat([df, df_encoded], axis=1)


            #one hot encode redCorner_stance
            column = df[['redCorner_stance']].copy()
            df_encoded = pd.get_dummies(column, columns=['redCorner_stance'], prefix='redCorner_stance').astype(int)
            df = pd.concat([df, df_encoded], axis=1)

            #one hot encode blueCorner_stance
            column = df[['blueCorner_stance']].copy()
            df_encoded = pd.get_dummies(column, columns=['blueCorner_stance'], prefix='blueCorner_stance').astype(int)
            df = pd.concat([df, df_encoded], axis=1)


            for index, row in df.iterrows():
                if row['winner'] == 1:
                    df.drop(index)

            df['blueCorner'] = 1
            df['winner'] = df['winner'].replace(2, 1)



            #one hot encode redCorner_nation
            column = df[['redCorner_nation']].copy()
            df_encoded = pd.get_dummies(column, columns=['redCorner_nation'], prefix='redCorner_nation').astype(int)
            dfInput.drop('redCorner_nation', axis=1, inplace=True)
            dfInput = pd.concat([dfInput, df_encoded], axis=1)

            #one hot encode blueCorner_nation
            column = df[['blueCorner_nation']].copy()
            df_encoded = pd.get_dummies(column, columns=['blueCorner_nation'], prefix='blueCorner_nation').astype(int)
            dfInput.drop('blueCorner_nation', axis=1, inplace=True)
            dfInput = pd.concat([dfInput, df_encoded], axis=1)

            df.drop('redCorner_nation', axis=1, inplace=True)
            df.drop('blueCorner_nation', axis=1, inplace=True)


            #one hot encode redCorner_stance
            column = df[['redCorner_stance']].copy()
            df_encoded = pd.get_dummies(column, columns=['redCorner_stance'], prefix='redCorner_stance').astype(int)
            dfInput.drop('redCorner_stance', axis=1, inplace=True)
            dfInput = pd.concat([dfInput, df_encoded], axis=1)

            #one hot encode blueCorner_stance
            column = df[['blueCorner_stance']].copy()
            df_encoded = pd.get_dummies(column, columns=['blueCorner_stance'], prefix='blueCorner_stance').astype(int)
            dfInput.drop('blueCorner_stance', axis=1, inplace=True)
            dfInput = pd.concat([dfInput, df_encoded], axis=1)

            df.drop('redCorner_stance', axis=1, inplace=True)
            df.drop('blueCorner_stance', axis=1, inplace=True)



            #limit the data
            dfInput = dfInput.head(1)


            #when one hot encoding, nations that have no representation in the train set have Nan values. This sets them to zero as they would have been zero if they were represented
            df.fillna(0, inplace=True)


            #dropna
            dfInput.dropna(subset=dfInput.columns.difference(['winner']), inplace=True)


            dfInput.at[0, 'redCorner'] = 0.0
            dfInput.at[0, 'blueCorner'] = 1.0

            #x,y split
            target_column = 'winner'
            y = df[target_column]
            X = df.drop(target_column, axis=1)

            #create train test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            #Define the deep learning model
            model = Sequential()
            model.add(Dense(64, activation = 'relu'))
            model.add(Dense(32, activation = 'relu'))
            model.add(Dense(16, activation = 'relu'))
            model.add(Dense(1, activation='sigmoid'))

            #earlyStopping
            earlystopping = EarlyStopping(monitor='val_loss', patience=100, restore_best_weights=True)

            # Define the ModelCheckpoint callback
            checkpoint = ModelCheckpoint(filepath='best_model_weights2.weights.h5', save_weights_only=True, monitor='val_accuracy', save_best_only=True, verbose=1)

            #compile
            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

            #train
            model.fit(X_train, y_train, epochs=1000, batch_size=124, validation_data=(X_test, y_test), callbacks=[checkpoint, earlystopping])

            # x, y split for dfMock
            target_column = 'winner'
            y_mock = dfInput[target_column]
            X_mock = dfInput.drop(target_column, axis=1)

            #accuracy
            y_hat = model.predict(X_mock)

            #store prediction
            prediction = float(y_hat[0])
            predictions.append(prediction)

        predictionsAverage = sum(predictions)/len(predictions)

        #new item to add
        item  = {'Fight': fight, 'Prediction': predictionsAverage}

        #append the new item to the DataFrame
        dfTracking.loc[len(dfTracking)] = item
    except:
        pass


for index, row in dfTracking.iterrows():
    fight = row['Fight']
    corners = fight.split(' vs ')
    redCorner = corners[0]
    blueCorner = corners[1]
    prediction = row['Prediction']
    if(prediction > 0.5):
        dfTracking.at[index, 'Predicted'] = str(blueCorner)
    if(prediction < 0.5):
        dfTracking.at[index, 'Predicted'] = str(redCorner)
dfTracking.head()


dfTrackingCompleted = pd.concat([dfTracking, dfPrevPreds], ignore_index=True)
dfTrackingCompleted.head()


dfTrackingCompleted.to_csv(f'predictions{dateToday}.csv', index=False)





















































