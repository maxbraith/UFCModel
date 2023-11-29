import requests
import csv
import concurrent.futures
import bs4
from bs4 import BeautifulSoup
import re



proxylist = []

with open('csv_proxies.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[2])

url = "https://free-proxy-list.net/"

payload = ""
headers = {"User-Agent": "insomnia/8.4.5"}

url = 'https://free-proxy-list.net/'
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
table = soup.find('div', class_=re.compile('table-responsive'))
trlabels = table.find_all('tr')
for i in trlabels:
    tdlabels = i.find_all('td')
    try:

        if(tdlabels[6].text.strip()=='yes'):
            proxylist.append(tdlabels[0].text.strip())
    except:
        pass
url = 'https://hidemy.io/en/proxy-list/'
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
table = soup.find('div',class_=re.compile('table_block'))
trlabels = table.find_all('tr')
for i in trlabels:
    tdlabels = i.find_all('td')
    try:

        if(tdlabels[4].text.strip()=='HTTP'):
            proxylist.append(tdlabels[0].text.strip())
    except:
        pass

workingProxies = []
def extract(proxy):
    works = False
    try:
        r = requests.get('https://www.ufc.com/', proxies={'http':proxy, 'https':proxy}, timeout=2)
        print(r)
        works = True
        workingProxies.append(proxy)
        with open('working_proxies.csv', 'w', encoding='UTF8', newline='') as workingProx:
            writer = csv.writer(workingProx)
            for k in workingProxies:
                writer.writerow([k])

    except:
        print('bad response')
    return works

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)

    