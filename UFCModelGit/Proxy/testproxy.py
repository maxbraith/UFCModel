import requests
import csv
import concurrent.futures
import bs4
from bs4 import BeautifulSoup
import re


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
site = requests.get(download,headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
#add proxies to testlist
tempproxylist = soup.text.strip().split('\r')
for proxy in tempproxylist:
    proxylist.append(proxy)

print(len(proxylist))
#scrape proxies from free-proxy-list.net
url = 'https://free-proxy-list.net/'
#site + soup
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
#scrape table
table = soup.find('div', class_=re.compile('table-responsive'))
trlabels = table.find_all('tr')
#scrape proxies and add to test list
for i in trlabels:
    tdlabels = i.find_all('td')
    try:

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

    