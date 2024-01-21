import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import csv
import random
import time
import numpy as np


#create df
df = pd.read_csv('databaseUpdated-01.18.2024.csv')


#generate proxyList
proxylist =[]
with open('working_proxies.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])
print(f'Proxies: {len(proxylist)}')

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
            #soup = BeautifulSoup(driver.page_source, 'lxml')
            response = requests.request("GET", url, data=payload, headers=headers, proxies={'http': f"http://{i}"})
            soup = BeautifulSoup(response.content, 'html.parser')
            boutInfo = soup.find('div', class_=re.compile('right'))
            labels = boutInfo.find_all('li')
            proxyheader = [i,userAgent]
            return proxyheader
        except:
            pass
        #check to see if uesr agent was the issue
        try:
            userAgents.remove(userAgent)
            userAgent = userAgents[random.randint(0,len(userAgents)-1)]
            payload = ''
            headers = {'User-Agent':f'{userAgent}',
            "cookie": "_tapology_mma_session=TCLB17ieOPnBLmCBTuxpX8s3uBODZMN3jL3jBbFhwPoywfbzG7gyvp%252BAzbOk4gOZ%252FOCykOUwcpEoJBwoj2rJyiMxdHWSaiLFkBYjfuUDpZ2VY6ECFn6rpTPmUBY1Zr2anIqiklY6fz9yQlBkPAhcx%252BWSzVgsc%252B%252F8UCqkb6WnM6xr8GUikb8U2UkMVYZ3Nj1dIA0vbXpDhKykqgW%252BCnlyglp8rtdlQ37m0SaYWjLDthG7Tik3idUvGlSXFAU55zAnxz6UNncMNhTbo5ltINfso54j60i7hOq0utNOz9w%253D--ChZexYwNpevIJ%252BV8--HhKStLELFfNWYOTZIAKM6Q%253D%253D"}
            url = "https://www.tapology.com/fightcenter/bouts/2974-ufc-64-clay-the-carpenter-guida-vs-justin-pretty-boy-james"
        
            #site request
            #soup = BeautifulSoup(driver.page_source, 'lxml')
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
            #soup = BeautifulSoup(driver.page_source, 'lxml')
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
            #soup = BeautifulSoup(driver.page_source, 'lxml')
            response = requests.request("GET", url, data=payload, headers=headers, proxies={'http': f"http://{i}"})
            soup = BeautifulSoup(response.content, 'html.parser')
            boutInfo = soup.find('div', class_=re.compile('right'))
            labels = boutInfo.find_all('li')
            proxyheader = [i,userAgent]
            return proxyheader


df.replace('---', np.nan, inplace=True)
df.replace('--', np.nan, inplace=True)


#fill Nans
for index, row in df.loc[:6161].iterrows():
    reach = None
    if row['blueCorner_reach'] is np.nan or row['blueCorner_reach'] is np.nan:
        fighter = row['blueCorner']
        fighterList = fighter.split(' ')
        try:
            if len(fighterList) == 1:
                url = f'https://www.tapology.com/search?term={fighterList[0]}&commit=Submit&model%5Bfighters%5D=fightersSearch'

                #getProxyHeader
                proxyheader = getProxyUserAgent()
                proxy = proxyheader[0]
                userAgent = proxyheader[1]

                #define headers
                headers = {
                "cookie": "_tapology_mma_session=nUbYZsmfBxCMml3EfKnycLX59tOCxmooAxj8ifN56kFksGAYkSXxKRVIy7bT2%252FXP9kIGTPOV3O%252BN1%252B4GWiNAjhG9S8sCeUtN3W2bwuxKzi8XGqMMYBSU1NWLZnSqZSIME2kzEx4xwAIBlWjakwZAGvZYuo4mIAV1OmuP%252B6n%252FU5ps1xWx1z%252BHrPIex61hMrNZpQfSwZNsbHcOLcrEjFLxfWUeIq7knZyMBQPGrlD%252BcSOCROXMSCXkEe7DbSgmZQLI5PVfbsBzN29g6irLU4XHrtsn%252FeZ%252BWFBGkAz1fEo%253D--thae17JwlRQtS%252BZB--4vVdpKGWVPPNtOCCVdkaWg%253D%253D",
                "User-Agent": f'{userAgent}'
                }

                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')

                #get href
                linkPart = soup.find('td', class_=re.compile('altA'))
                a = linkPart.find('a')
                href = a['href']

                url = f'https://tapology.com{href}'
                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')
                
                div = soup.find('div', class_=re.compile('details details_two_columns'))
                lis = div.find_all('li')
                for li in lis:
                    if 'Reach:' in li.text.strip():
                        print(f'Scraping {fighterList[0]}...')
                        print(url)
                        spans = li.find_all('span')
                        if len(spans)>1:
                            reachTemp = spans[1].text.strip()
                            reachList = reachTemp.split(' ')
                            reach = str(reachTemp[0])
                            df.at[index, 'blueCorner_reach'] = reach
            if len(fighterList) == 2:
                url = f'https://www.tapology.com/search?term={fighterList[0]}+{fighterList[1]}&commit=Submit&model%5Bfighters%5D=fightersSearch'
                
                #getProxyHeader
                proxyheader = getProxyUserAgent()
                proxy = proxyheader[0]
                userAgent = proxyheader[1]

                #define headers
                headers = {
                "cookie": "_tapology_mma_session=nUbYZsmfBxCMml3EfKnycLX59tOCxmooAxj8ifN56kFksGAYkSXxKRVIy7bT2%252FXP9kIGTPOV3O%252BN1%252B4GWiNAjhG9S8sCeUtN3W2bwuxKzi8XGqMMYBSU1NWLZnSqZSIME2kzEx4xwAIBlWjakwZAGvZYuo4mIAV1OmuP%252B6n%252FU5ps1xWx1z%252BHrPIex61hMrNZpQfSwZNsbHcOLcrEjFLxfWUeIq7knZyMBQPGrlD%252BcSOCROXMSCXkEe7DbSgmZQLI5PVfbsBzN29g6irLU4XHrtsn%252FeZ%252BWFBGkAz1fEo%253D--thae17JwlRQtS%252BZB--4vVdpKGWVPPNtOCCVdkaWg%253D%253D",
                "User-Agent": f'{userAgent}'
                }

                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')

                #get href
                linkPart = soup.find('td', class_=re.compile('altA'))
                a = linkPart.find('a')
                href = a['href']

                url = f'https://tapology.com{href}'
                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')
                
                div = soup.find('div', class_=re.compile('details details_two_columns'))
                lis = div.find_all('li')
                for li in lis:
                    if 'Reach:' in li.text.strip():
                        print(f'Scraping {fighterList[0]} {fighterList[1]}...')
                        print(url)
                        spans = li.find_all('span')
                        if len(spans)>1:
                            reachTemp = spans[1].text.strip()
                            reachList = reachTemp.split(' ')
                            reach = str(reachTemp[0])
                            df.at[index, 'blueCorner_reach'] = reach
            if len(fighterList) == 3:
                url =f'https://www.tapology.com/search?term={fighterList[0]}+{fighterList[1]}+{fighterList[2]}&commit=Submit&model%5Bfighters%5D=fightersSearch'
                #getProxyHeader
                proxyheader = getProxyUserAgent()
                proxy = proxyheader[0]
                userAgent = proxyheader[1]

                #define headers
                headers = {
                "cookie": "_tapology_mma_session=nUbYZsmfBxCMml3EfKnycLX59tOCxmooAxj8ifN56kFksGAYkSXxKRVIy7bT2%252FXP9kIGTPOV3O%252BN1%252B4GWiNAjhG9S8sCeUtN3W2bwuxKzi8XGqMMYBSU1NWLZnSqZSIME2kzEx4xwAIBlWjakwZAGvZYuo4mIAV1OmuP%252B6n%252FU5ps1xWx1z%252BHrPIex61hMrNZpQfSwZNsbHcOLcrEjFLxfWUeIq7knZyMBQPGrlD%252BcSOCROXMSCXkEe7DbSgmZQLI5PVfbsBzN29g6irLU4XHrtsn%252FeZ%252BWFBGkAz1fEo%253D--thae17JwlRQtS%252BZB--4vVdpKGWVPPNtOCCVdkaWg%253D%253D",
                "User-Agent": f'{userAgent}'
                }

                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')

                #get href
                linkPart = soup.find('td', class_=re.compile('altA'))
                a = linkPart.find('a')
                href = a['href']

                url = f'https://tapology.com{href}'
                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')
                
                div = soup.find('div', class_=re.compile('details details_two_columns'))
                lis = div.find_all('li')
                for li in lis:
                    if 'Reach:' in li.text.strip():
                        print(f'Scraping {fighterList[0]} {fighterList[1]} {fighterList[2]}...')
                        print(url)
                        spans = li.find_all('span')
                        if len(spans)>1:
                            reachTemp = spans[1].text.strip()
                            reachList = reachTemp.split(' ')
                            reach = str(reachTemp[0])
                            df.at[index, 'blueCorner_reach'] = reach
            if len(fighterList) == 4:
                url = f'https://www.tapology.com/search?term={fighterList[0]}+{fighterList[1]}+{fighterList[2]}+{fighterList[3]}&commit=Submit&model%5Bfighters%5D=fightersSearch'
                #getProxyHeader
                proxyheader = getProxyUserAgent()
                proxy = proxyheader[0]
                userAgent = proxyheader[1]

                #define headers
                headers = {
                "cookie": "_tapology_mma_session=nUbYZsmfBxCMml3EfKnycLX59tOCxmooAxj8ifN56kFksGAYkSXxKRVIy7bT2%252FXP9kIGTPOV3O%252BN1%252B4GWiNAjhG9S8sCeUtN3W2bwuxKzi8XGqMMYBSU1NWLZnSqZSIME2kzEx4xwAIBlWjakwZAGvZYuo4mIAV1OmuP%252B6n%252FU5ps1xWx1z%252BHrPIex61hMrNZpQfSwZNsbHcOLcrEjFLxfWUeIq7knZyMBQPGrlD%252BcSOCROXMSCXkEe7DbSgmZQLI5PVfbsBzN29g6irLU4XHrtsn%252FeZ%252BWFBGkAz1fEo%253D--thae17JwlRQtS%252BZB--4vVdpKGWVPPNtOCCVdkaWg%253D%253D",
                "User-Agent": f'{userAgent}'
                }

                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')

                #get href
                linkPart = soup.find('td', class_=re.compile('altA'))
                a = linkPart.find('a')
                href = a['href']

                url = f'https://tapology.com{href}'
                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')
                
                div = soup.find('div', class_=re.compile('details details_two_columns'))
                lis = div.find_all('li')
                for li in lis:
                    if 'Reach:' in li.text.strip():
                        print(f'Scraping {fighterList[0]} {fighterList[1]} {fighterList[2]} {fighterList[3]}...')
                        print(url)
                        spans = li.find_all('span')
                        if len(spans)>1:
                            reachTemp = spans[1].text.strip()
                            reachList = reachTemp.split(' ')
                            reach = str(reachTemp[0])
                            df.at[index, 'blueCorner_reach'] = reach
        except:
            pass
        


#fill nans
for index, row in df.loc[:6161].iterrows():
    reach = None
    if row['redCorner_reach'] is np.nan or row['redCorner_reach'] is np.nan:
        fighter = row['redCorner']
        fighterList = fighter.split(' ')
        try:
            if len(fighterList) == 1:
                url = f'https://www.tapology.com/search?term={fighterList[0]}&commit=Submit&model%5Bfighters%5D=fightersSearch'

                #getProxyHeader
                proxyheader = getProxyUserAgent()
                proxy = proxyheader[0]
                userAgent = proxyheader[1]

                #define headers
                headers = {
                "cookie": "_tapology_mma_session=nUbYZsmfBxCMml3EfKnycLX59tOCxmooAxj8ifN56kFksGAYkSXxKRVIy7bT2%252FXP9kIGTPOV3O%252BN1%252B4GWiNAjhG9S8sCeUtN3W2bwuxKzi8XGqMMYBSU1NWLZnSqZSIME2kzEx4xwAIBlWjakwZAGvZYuo4mIAV1OmuP%252B6n%252FU5ps1xWx1z%252BHrPIex61hMrNZpQfSwZNsbHcOLcrEjFLxfWUeIq7knZyMBQPGrlD%252BcSOCROXMSCXkEe7DbSgmZQLI5PVfbsBzN29g6irLU4XHrtsn%252FeZ%252BWFBGkAz1fEo%253D--thae17JwlRQtS%252BZB--4vVdpKGWVPPNtOCCVdkaWg%253D%253D",
                "User-Agent": f'{userAgent}'
                }

                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')

                #get href
                linkPart = soup.find('td', class_=re.compile('altA'))
                a = linkPart.find('a')
                href = a['href']

                url = f'https://tapology.com{href}'
                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')
                
                div = soup.find('div', class_=re.compile('details details_two_columns'))
                lis = div.find_all('li')
                for li in lis:
                    if 'Reach:' in li.text.strip():
                        print(f'Scraping {fighterList[0]}...')
                        print(url)
                        spans = li.find_all('span')
                        if len(spans)>1:
                            reachTemp = spans[1].text.strip()
                            reachList = reachTemp.split(' ')
                            reach = str(reachTemp[0])
                            df.at[index, 'redCorner_reach'] = reach
            if len(fighterList) == 2:
                url = f'https://www.tapology.com/search?term={fighterList[0]}+{fighterList[1]}&commit=Submit&model%5Bfighters%5D=fightersSearch'
                
                #getProxyHeader
                proxyheader = getProxyUserAgent()
                proxy = proxyheader[0]
                userAgent = proxyheader[1]

                #define headers
                headers = {
                "cookie": "_tapology_mma_session=nUbYZsmfBxCMml3EfKnycLX59tOCxmooAxj8ifN56kFksGAYkSXxKRVIy7bT2%252FXP9kIGTPOV3O%252BN1%252B4GWiNAjhG9S8sCeUtN3W2bwuxKzi8XGqMMYBSU1NWLZnSqZSIME2kzEx4xwAIBlWjakwZAGvZYuo4mIAV1OmuP%252B6n%252FU5ps1xWx1z%252BHrPIex61hMrNZpQfSwZNsbHcOLcrEjFLxfWUeIq7knZyMBQPGrlD%252BcSOCROXMSCXkEe7DbSgmZQLI5PVfbsBzN29g6irLU4XHrtsn%252FeZ%252BWFBGkAz1fEo%253D--thae17JwlRQtS%252BZB--4vVdpKGWVPPNtOCCVdkaWg%253D%253D",
                "User-Agent": f'{userAgent}'
                }

                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')

                #get href
                linkPart = soup.find('td', class_=re.compile('altA'))
                a = linkPart.find('a')
                href = a['href']

                url = f'https://tapology.com{href}'
                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')
                
                div = soup.find('div', class_=re.compile('details details_two_columns'))
                lis = div.find_all('li')
                for li in lis:
                    if 'Reach:' in li.text.strip():
                        print(f'Scraping {fighterList[0]} {fighterList[1]}...')
                        print(url)
                        spans = li.find_all('span')
                        if len(spans)>1:
                            reachTemp = spans[1].text.strip()
                            reachList = reachTemp.split(' ')
                            reach = str(reachTemp[0])
                            df.at[index, 'redCorner_reach'] = reach
            if len(fighterList) == 3:
                url =f'https://www.tapology.com/search?term={fighterList[0]}+{fighterList[1]}+{fighterList[2]}&commit=Submit&model%5Bfighters%5D=fightersSearch'
                #getProxyHeader
                proxyheader = getProxyUserAgent()
                proxy = proxyheader[0]
                userAgent = proxyheader[1]

                #define headers
                headers = {
                "cookie": "_tapology_mma_session=nUbYZsmfBxCMml3EfKnycLX59tOCxmooAxj8ifN56kFksGAYkSXxKRVIy7bT2%252FXP9kIGTPOV3O%252BN1%252B4GWiNAjhG9S8sCeUtN3W2bwuxKzi8XGqMMYBSU1NWLZnSqZSIME2kzEx4xwAIBlWjakwZAGvZYuo4mIAV1OmuP%252B6n%252FU5ps1xWx1z%252BHrPIex61hMrNZpQfSwZNsbHcOLcrEjFLxfWUeIq7knZyMBQPGrlD%252BcSOCROXMSCXkEe7DbSgmZQLI5PVfbsBzN29g6irLU4XHrtsn%252FeZ%252BWFBGkAz1fEo%253D--thae17JwlRQtS%252BZB--4vVdpKGWVPPNtOCCVdkaWg%253D%253D",
                "User-Agent": f'{userAgent}'
                }

                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')

                #get href
                linkPart = soup.find('td', class_=re.compile('altA'))
                a = linkPart.find('a')
                href = a['href']

                url = f'https://tapology.com{href}'
                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')
                
                div = soup.find('div', class_=re.compile('details details_two_columns'))
                lis = div.find_all('li')
                for li in lis:
                    if 'Reach:' in li.text.strip():
                        spans = li.find_all('span')
                        print(f'Scraping {fighterList[0]} {fighterList[1]} {fighterList[2]}...')
                        print(url)
                        if len(spans)>1:
                            reachTemp = spans[1].text.strip()
                            reachList = reachTemp.split(' ')
                            reach = str(reachTemp[0])
                            df.at[index, 'redCorner_reach'] = reach
            if len(fighterList) == 4:
                url = f'https://www.tapology.com/search?term={fighterList[0]}+{fighterList[1]}+{fighterList[2]}+{fighterList[3]}&commit=Submit&model%5Bfighters%5D=fightersSearch'
                #getProxyHeader
                proxyheader = getProxyUserAgent()
                proxy = proxyheader[0]
                userAgent = proxyheader[1]

                #define headers
                headers = {
                "cookie": "_tapology_mma_session=nUbYZsmfBxCMml3EfKnycLX59tOCxmooAxj8ifN56kFksGAYkSXxKRVIy7bT2%252FXP9kIGTPOV3O%252BN1%252B4GWiNAjhG9S8sCeUtN3W2bwuxKzi8XGqMMYBSU1NWLZnSqZSIME2kzEx4xwAIBlWjakwZAGvZYuo4mIAV1OmuP%252B6n%252FU5ps1xWx1z%252BHrPIex61hMrNZpQfSwZNsbHcOLcrEjFLxfWUeIq7knZyMBQPGrlD%252BcSOCROXMSCXkEe7DbSgmZQLI5PVfbsBzN29g6irLU4XHrtsn%252FeZ%252BWFBGkAz1fEo%253D--thae17JwlRQtS%252BZB--4vVdpKGWVPPNtOCCVdkaWg%253D%253D",
                "User-Agent": f'{userAgent}'
                }

                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')

                #get href
                linkPart = soup.find('td', class_=re.compile('altA'))
                a = linkPart.find('a')
                href = a['href']

                url = f'https://tapology.com{href}'
                #site request
                site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
                soup = BeautifulSoup(site.content, 'html.parser')
                
                div = soup.find('div', class_=re.compile('details details_two_columns'))
                lis = div.find_all('li')
                for li in lis:
                    if 'Reach:' in li.text.strip():
                        print(f'Scraping {fighterList[0]} {fighterList[1]} {fighterList[2]} {fighterList[3]}...')
                        print(url)
                        spans = li.find_all('span')
                        if len(spans)>1:
                            reachTemp = spans[1].text.strip()
                            reachList = reachTemp.split(' ')
                            reach = str(reachTemp[0])
                            df.at[index, 'redCorner_reach'] = reach
        except:
            pass

df.to_csv('databaseUpdate-01.20.2024.csv', index=False)