import requests
from bs4 import BeautifulSoup
import re
import math
import csv
from csv import writer
import itertools
import time
import random
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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

        

#request API last page
url = "https://www.tapology.com/fightcenter_events"

#parameters of API
querystring = {"group":"ufc","page":"27","region":"","schedule":"results","sport":"all"}
proxyheader = getProxyUserAgent()
proxy = proxyheader[0]
userAgent = proxyheader[1]

payload = ""
#define headers
headers = {
    "cookie": "_tapology_mma_session=YwpE3Hl%252Fd87nYFh7hNCEDublK%252FyUT04FbM%252F5sNGopwcm2zPo5OqFVACrzwbXA5fw2XfTn8SmLYhwsq055NOKmkqvpMdrlmvC42ZOW5dVUwrcZq68d0X6KlSxfB3bqb0Y498omUKEmh4MLkQ%252FUjHcEovx7ZvCHjpjEWcOZpiOp6WRlyv0C4TrCtwMi9Fy5ujpocYVyw3ooGXCCwWN4j00s9Dr2Vt8vFCLS9WIA%252FWitkpqRU7VmCASX6pOiSK8l5eyB4JczeYmtdidqBvSM2Gk%252FRxhSmHec6MdHgtm4fI%253D--xZ4H%252FprAKW9s6uHk--exjScsnz5YyAvRFUdhxRsg%253D%253D",
    "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "usprivacy=1Y--; _au_1d=AU1D-0100-001699559408-UHN9538G-791U; _gid=GA1.2.267777754.1701026655; __gads=ID=006eef68af2069f8:T=1701057293:RT=1701067622:S=ALNI_MZOGhTIoX2sSp_mXeikO0Kw6YJChw; _au_last_seen_pixels=eyJhcG4iOjE3MDEwOTQ2OTksInR0ZCI6MTcwMTA5NDY5OSwicHViIjoxNzAxMDk0Njk5LCJydWIiOjE3MDEwOTQ2OTksInRhcGFkIjoxNzAxMDk0Njk5LCJhZHgiOjE3MDEwOTQ2OTksImdvbyI6MTcwMTA5NDY5OSwib3BlbngiOjE3MDEwNTcyNzMsInNvbiI6MTcwMTA1NzI3MywidW5ydWx5IjoxNzAxMDk0NzA3LCJwcG50IjoxNzAxMDk0Njk5LCJhbW8iOjE3MDEwOTQ2OTksImNvbG9zc3VzIjoxNzAxMDU3MjczLCJiZWVzIjoxNzAxMDU3MjczLCJ0YWJvb2xhIjoxNzAxMDU3MjczLCJpbXByIjoxNzAxMDU3MjczLCJhZG8iOjE3MDEwNTcyNzMsInNtYXJ0IjoxNzAxMDU3MjczLCJpbmRleCI6MTcwMTA1NzI5M30%3D; __qca=I0-1125826933-1701095027052; _ga=GA1.1.1827296034.1699559406; _sharedid=89deac14-215b-4803-ada4-17cf3d79240e; _pbjs_userid_consent_data=6683316680106290; _ga_DL61VSM5W1=GS1.1.1701099972.7.1.1701100068.0.0.0; cto_bundle=tSavVV9sMWJ2Tnl0eEc2UTZLcmk3aHIwTDRXa2tLU3Y2ZnA4JTJCTTNwZWoxbWJwbmlyWWxJejJIUWRid3JaSFAwQTRTUXpyWEQlMkJROWlqcXNvMFBETnJvVTc0SHFKTEY4MHhIVndQREE2Nm12ZnJqS1RKampGUmxrdlpRRGxndVFQbkZsdGlCJTJGUTF3QUNBV3JpNm12JTJGakFmYm9uR1pRcXNTMTVkOFh0VG5xcksyZ1JCcnhZaVI3QzM0ZERsaiUyQkd1blN5cDglMkI; cto_bidid=O-wksV9ydWFlcGozeFRhN1g4YXBBd0hMUXQ5OEFrOUx1TFZrOE5LYldVTWRJJTJCYTR2V00lMkJnckZGM0toUDVnZ0NpcEVXUWZuRno5cUZEWDlGRFN3ZFhaSEExVGRwZEdjS1FZY21RVXE2TGZVQWQwTkRvNVJzTSUyQno4WVFKUXFDdXpXV3ZNeWRYRkE4QlU1Z010ckdGOEJWbVdHVGclM0QlM0Q; _tapology_mma_session=8jxSIn32ouJKe3t%2FFjWKBx8rXBfrOEh8ivn1JxTURA33XDXsQdBKOtqmZhhsWl%2BVhINq2iDfRJOH3a4T0990Tv6i1%2FkmmqF8eGZtWWL0uCh4iaka%2Bt%2FEN4KLQg3zSnu10MsHQ90x36pW%2FLmrNqwWFLqajRve%2B8BT9wX71H3sIJBA0u17Bjt4Lyo%2Be6hi4KFvpMZypQzSKWuIEaOdf7oErBFLullN2IfaYS07f2r3sGtZGJtu4Uy1v9XSxBM%2FPZSaTFJL4NdRd4ulpFqgoE3tb3eXdbJozXsSmlKpB1k%3D--%2FM3j66rf7wE0eXOy--qsIf8Pcz7wdlPj1NtqB%2BLw%3D%3D",
    "Referer": "https://www.tapology.com/fightcenter",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": f'{userAgent}',
    "X-CSRF-Token": "01Xl0kvparFOz6wwwg1xCzztNB/n3PjN1UuAhKzRvBAVw4sGAK/VnJdQyXHVKAuHz62kDpMZQIafhgrpRuDUsw==",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"'
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})






cleanParts =[]
#loop through all API pages to get event links
for i in range(1, 29):
    #if(i%17==0):
        #time.sleep(120)
    #print(i)
    #request API page i
    url = "https://www.tapology.com/fightcenter_events"
    
    #parameters of API
    querystring = {"group":"ufc","page":i,"region":"","schedule":"results","sport":"all"}
    proxyheader = getProxyUserAgent()
    proxy = proxyheader[0]
    userAgent = proxyheader[1]

    payload = ""
    #define headers
    headers = {
        "cookie": "_tapology_mma_session=YwpE3Hl%252Fd87nYFh7hNCEDublK%252FyUT04FbM%252F5sNGopwcm2zPo5OqFVACrzwbXA5fw2XfTn8SmLYhwsq055NOKmkqvpMdrlmvC42ZOW5dVUwrcZq68d0X6KlSxfB3bqb0Y498omUKEmh4MLkQ%252FUjHcEovx7ZvCHjpjEWcOZpiOp6WRlyv0C4TrCtwMi9Fy5ujpocYVyw3ooGXCCwWN4j00s9Dr2Vt8vFCLS9WIA%252FWitkpqRU7VmCASX6pOiSK8l5eyB4JczeYmtdidqBvSM2Gk%252FRxhSmHec6MdHgtm4fI%253D--xZ4H%252FprAKW9s6uHk--exjScsnz5YyAvRFUdhxRsg%253D%253D",
        "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "usprivacy=1Y--; _au_1d=AU1D-0100-001699559408-UHN9538G-791U; _gid=GA1.2.267777754.1701026655; __gads=ID=006eef68af2069f8:T=1701057293:RT=1701067622:S=ALNI_MZOGhTIoX2sSp_mXeikO0Kw6YJChw; _au_last_seen_pixels=eyJhcG4iOjE3MDEwOTQ2OTksInR0ZCI6MTcwMTA5NDY5OSwicHViIjoxNzAxMDk0Njk5LCJydWIiOjE3MDEwOTQ2OTksInRhcGFkIjoxNzAxMDk0Njk5LCJhZHgiOjE3MDEwOTQ2OTksImdvbyI6MTcwMTA5NDY5OSwib3BlbngiOjE3MDEwNTcyNzMsInNvbiI6MTcwMTA1NzI3MywidW5ydWx5IjoxNzAxMDk0NzA3LCJwcG50IjoxNzAxMDk0Njk5LCJhbW8iOjE3MDEwOTQ2OTksImNvbG9zc3VzIjoxNzAxMDU3MjczLCJiZWVzIjoxNzAxMDU3MjczLCJ0YWJvb2xhIjoxNzAxMDU3MjczLCJpbXByIjoxNzAxMDU3MjczLCJhZG8iOjE3MDEwNTcyNzMsInNtYXJ0IjoxNzAxMDU3MjczLCJpbmRleCI6MTcwMTA1NzI5M30%3D; __qca=I0-1125826933-1701095027052; _ga=GA1.1.1827296034.1699559406; _sharedid=89deac14-215b-4803-ada4-17cf3d79240e; _pbjs_userid_consent_data=6683316680106290; _ga_DL61VSM5W1=GS1.1.1701099972.7.1.1701100068.0.0.0; cto_bundle=tSavVV9sMWJ2Tnl0eEc2UTZLcmk3aHIwTDRXa2tLU3Y2ZnA4JTJCTTNwZWoxbWJwbmlyWWxJejJIUWRid3JaSFAwQTRTUXpyWEQlMkJROWlqcXNvMFBETnJvVTc0SHFKTEY4MHhIVndQREE2Nm12ZnJqS1RKampGUmxrdlpRRGxndVFQbkZsdGlCJTJGUTF3QUNBV3JpNm12JTJGakFmYm9uR1pRcXNTMTVkOFh0VG5xcksyZ1JCcnhZaVI3QzM0ZERsaiUyQkd1blN5cDglMkI; cto_bidid=O-wksV9ydWFlcGozeFRhN1g4YXBBd0hMUXQ5OEFrOUx1TFZrOE5LYldVTWRJJTJCYTR2V00lMkJnckZGM0toUDVnZ0NpcEVXUWZuRno5cUZEWDlGRFN3ZFhaSEExVGRwZEdjS1FZY21RVXE2TGZVQWQwTkRvNVJzTSUyQno4WVFKUXFDdXpXV3ZNeWRYRkE4QlU1Z010ckdGOEJWbVdHVGclM0QlM0Q; _tapology_mma_session=8jxSIn32ouJKe3t%2FFjWKBx8rXBfrOEh8ivn1JxTURA33XDXsQdBKOtqmZhhsWl%2BVhINq2iDfRJOH3a4T0990Tv6i1%2FkmmqF8eGZtWWL0uCh4iaka%2Bt%2FEN4KLQg3zSnu10MsHQ90x36pW%2FLmrNqwWFLqajRve%2B8BT9wX71H3sIJBA0u17Bjt4Lyo%2Be6hi4KFvpMZypQzSKWuIEaOdf7oErBFLullN2IfaYS07f2r3sGtZGJtu4Uy1v9XSxBM%2FPZSaTFJL4NdRd4ulpFqgoE3tb3eXdbJozXsSmlKpB1k%3D--%2FM3j66rf7wE0eXOy--qsIf8Pcz7wdlPj1NtqB%2BLw%3D%3D",
        "Referer": "https://www.tapology.com/fightcenter",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": f'{userAgent}',
        "X-CSRF-Token": "01Xl0kvparFOz6wwwg1xCzztNB/n3PjN1UuAhKzRvBAVw4sGAK/VnJdQyXHVKAuHz62kDpMZQIafhgrpRuDUsw==",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"'
    }

    #site request + soup
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
    soup = BeautifulSoup(response.content, 'html.parser')
    

    #scrape event links
    spans = soup.find_all('span', class_=re.compile('name'))
    aheaders = []
    for span in spans:
        aheaders.extend(span.find_all("a"))
    
    
    parts = []
    for part in aheaders:
        href = part['href']
        if href:
            if 'events' in href:
                parts.append(href)
    
    #remove dups
    parts = list(dict.fromkeys(parts))
                
    #clean parts
    for part in parts:
        if 'region' not in part:
            cleanPart = part[2:-2]
            cleanParts.append(cleanPart)

print(f'Event Links Found: {len(cleanParts)}')



        
#scrape links of individual fights
fightLinksParts = []
count =1
for i in cleanParts:
    proxyheader = getProxyUserAgent()
    proxy = proxyheader[0]
    userAgent = proxyheader[1]
    headers = {
    "cookie": "_tapology_mma_session=YwpE3Hl%252Fd87nYFh7hNCEDublK%252FyUT04FbM%252F5sNGopwcm2zPo5OqFVACrzwbXA5fw2XfTn8SmLYhwsq055NOKmkqvpMdrlmvC42ZOW5dVUwrcZq68d0X6KlSxfB3bqb0Y498omUKEmh4MLkQ%252FUjHcEovx7ZvCHjpjEWcOZpiOp6WRlyv0C4TrCtwMi9Fy5ujpocYVyw3ooGXCCwWN4j00s9Dr2Vt8vFCLS9WIA%252FWitkpqRU7VmCASX6pOiSK8l5eyB4JczeYmtdidqBvSM2Gk%252FRxhSmHec6MdHgtm4fI%253D--xZ4H%252FprAKW9s6uHk--exjScsnz5YyAvRFUdhxRsg%253D%253D",
    "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "usprivacy=1Y--; _au_1d=AU1D-0100-001699559408-UHN9538G-791U; _gid=GA1.2.267777754.1701026655; __gads=ID=006eef68af2069f8:T=1701057293:RT=1701067622:S=ALNI_MZOGhTIoX2sSp_mXeikO0Kw6YJChw; _au_last_seen_pixels=eyJhcG4iOjE3MDEwOTQ2OTksInR0ZCI6MTcwMTA5NDY5OSwicHViIjoxNzAxMDk0Njk5LCJydWIiOjE3MDEwOTQ2OTksInRhcGFkIjoxNzAxMDk0Njk5LCJhZHgiOjE3MDEwOTQ2OTksImdvbyI6MTcwMTA5NDY5OSwib3BlbngiOjE3MDEwNTcyNzMsInNvbiI6MTcwMTA1NzI3MywidW5ydWx5IjoxNzAxMDk0NzA3LCJwcG50IjoxNzAxMDk0Njk5LCJhbW8iOjE3MDEwOTQ2OTksImNvbG9zc3VzIjoxNzAxMDU3MjczLCJiZWVzIjoxNzAxMDU3MjczLCJ0YWJvb2xhIjoxNzAxMDU3MjczLCJpbXByIjoxNzAxMDU3MjczLCJhZG8iOjE3MDEwNTcyNzMsInNtYXJ0IjoxNzAxMDU3MjczLCJpbmRleCI6MTcwMTA1NzI5M30%3D; __qca=I0-1125826933-1701095027052; _ga=GA1.1.1827296034.1699559406; _sharedid=89deac14-215b-4803-ada4-17cf3d79240e; _pbjs_userid_consent_data=6683316680106290; _ga_DL61VSM5W1=GS1.1.1701099972.7.1.1701100068.0.0.0; cto_bundle=tSavVV9sMWJ2Tnl0eEc2UTZLcmk3aHIwTDRXa2tLU3Y2ZnA4JTJCTTNwZWoxbWJwbmlyWWxJejJIUWRid3JaSFAwQTRTUXpyWEQlMkJROWlqcXNvMFBETnJvVTc0SHFKTEY4MHhIVndQREE2Nm12ZnJqS1RKampGUmxrdlpRRGxndVFQbkZsdGlCJTJGUTF3QUNBV3JpNm12JTJGakFmYm9uR1pRcXNTMTVkOFh0VG5xcksyZ1JCcnhZaVI3QzM0ZERsaiUyQkd1blN5cDglMkI; cto_bidid=O-wksV9ydWFlcGozeFRhN1g4YXBBd0hMUXQ5OEFrOUx1TFZrOE5LYldVTWRJJTJCYTR2V00lMkJnckZGM0toUDVnZ0NpcEVXUWZuRno5cUZEWDlGRFN3ZFhaSEExVGRwZEdjS1FZY21RVXE2TGZVQWQwTkRvNVJzTSUyQno4WVFKUXFDdXpXV3ZNeWRYRkE4QlU1Z010ckdGOEJWbVdHVGclM0QlM0Q; _tapology_mma_session=8jxSIn32ouJKe3t%2FFjWKBx8rXBfrOEh8ivn1JxTURA33XDXsQdBKOtqmZhhsWl%2BVhINq2iDfRJOH3a4T0990Tv6i1%2FkmmqF8eGZtWWL0uCh4iaka%2Bt%2FEN4KLQg3zSnu10MsHQ90x36pW%2FLmrNqwWFLqajRve%2B8BT9wX71H3sIJBA0u17Bjt4Lyo%2Be6hi4KFvpMZypQzSKWuIEaOdf7oErBFLullN2IfaYS07f2r3sGtZGJtu4Uy1v9XSxBM%2FPZSaTFJL4NdRd4ulpFqgoE3tb3eXdbJozXsSmlKpB1k%3D--%2FM3j66rf7wE0eXOy--qsIf8Pcz7wdlPj1NtqB%2BLw%3D%3D",
    "Referer": "https://www.tapology.com/fightcenter",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": f'{userAgent}',
    "X-CSRF-Token": "01Xl0kvparFOz6wwwg1xCzztNB/n3PjN1UuAhKzRvBAVw4sGAK/VnJdQyXHVKAuHz62kDpMZQIafhgrpRuDUsw==",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"'
    }
    #if(count%16==0):
        #time.sleep(180)
    fightParts = []
    #create url
    url = f"https://www.tapology.com{i}"
    print(url)
    
    #site request
    site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
    soup = BeautifulSoup(site.content, 'html.parser')


    #scrape parts
    billings = soup.find_all('span', class_='billing')
    for part in billings:
        fightParts.append(part.find_all('a'))    

    print(len(fightParts))
    if(len(fightParts) == 0):
        proxyheader = getProxyUserAgent()
        proxy = proxyheader[0]
        userAgent = proxyheader[1]
        headers = {
        "cookie": "_tapology_mma_session=YwpE3Hl%252Fd87nYFh7hNCEDublK%252FyUT04FbM%252F5sNGopwcm2zPo5OqFVACrzwbXA5fw2XfTn8SmLYhwsq055NOKmkqvpMdrlmvC42ZOW5dVUwrcZq68d0X6KlSxfB3bqb0Y498omUKEmh4MLkQ%252FUjHcEovx7ZvCHjpjEWcOZpiOp6WRlyv0C4TrCtwMi9Fy5ujpocYVyw3ooGXCCwWN4j00s9Dr2Vt8vFCLS9WIA%252FWitkpqRU7VmCASX6pOiSK8l5eyB4JczeYmtdidqBvSM2Gk%252FRxhSmHec6MdHgtm4fI%253D--xZ4H%252FprAKW9s6uHk--exjScsnz5YyAvRFUdhxRsg%253D%253D",
        "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "usprivacy=1Y--; _au_1d=AU1D-0100-001699559408-UHN9538G-791U; _gid=GA1.2.267777754.1701026655; __gads=ID=006eef68af2069f8:T=1701057293:RT=1701067622:S=ALNI_MZOGhTIoX2sSp_mXeikO0Kw6YJChw; _au_last_seen_pixels=eyJhcG4iOjE3MDEwOTQ2OTksInR0ZCI6MTcwMTA5NDY5OSwicHViIjoxNzAxMDk0Njk5LCJydWIiOjE3MDEwOTQ2OTksInRhcGFkIjoxNzAxMDk0Njk5LCJhZHgiOjE3MDEwOTQ2OTksImdvbyI6MTcwMTA5NDY5OSwib3BlbngiOjE3MDEwNTcyNzMsInNvbiI6MTcwMTA1NzI3MywidW5ydWx5IjoxNzAxMDk0NzA3LCJwcG50IjoxNzAxMDk0Njk5LCJhbW8iOjE3MDEwOTQ2OTksImNvbG9zc3VzIjoxNzAxMDU3MjczLCJiZWVzIjoxNzAxMDU3MjczLCJ0YWJvb2xhIjoxNzAxMDU3MjczLCJpbXByIjoxNzAxMDU3MjczLCJhZG8iOjE3MDEwNTcyNzMsInNtYXJ0IjoxNzAxMDU3MjczLCJpbmRleCI6MTcwMTA1NzI5M30%3D; __qca=I0-1125826933-1701095027052; _ga=GA1.1.1827296034.1699559406; _sharedid=89deac14-215b-4803-ada4-17cf3d79240e; _pbjs_userid_consent_data=6683316680106290; _ga_DL61VSM5W1=GS1.1.1701099972.7.1.1701100068.0.0.0; cto_bundle=tSavVV9sMWJ2Tnl0eEc2UTZLcmk3aHIwTDRXa2tLU3Y2ZnA4JTJCTTNwZWoxbWJwbmlyWWxJejJIUWRid3JaSFAwQTRTUXpyWEQlMkJROWlqcXNvMFBETnJvVTc0SHFKTEY4MHhIVndQREE2Nm12ZnJqS1RKampGUmxrdlpRRGxndVFQbkZsdGlCJTJGUTF3QUNBV3JpNm12JTJGakFmYm9uR1pRcXNTMTVkOFh0VG5xcksyZ1JCcnhZaVI3QzM0ZERsaiUyQkd1blN5cDglMkI; cto_bidid=O-wksV9ydWFlcGozeFRhN1g4YXBBd0hMUXQ5OEFrOUx1TFZrOE5LYldVTWRJJTJCYTR2V00lMkJnckZGM0toUDVnZ0NpcEVXUWZuRno5cUZEWDlGRFN3ZFhaSEExVGRwZEdjS1FZY21RVXE2TGZVQWQwTkRvNVJzTSUyQno4WVFKUXFDdXpXV3ZNeWRYRkE4QlU1Z010ckdGOEJWbVdHVGclM0QlM0Q; _tapology_mma_session=8jxSIn32ouJKe3t%2FFjWKBx8rXBfrOEh8ivn1JxTURA33XDXsQdBKOtqmZhhsWl%2BVhINq2iDfRJOH3a4T0990Tv6i1%2FkmmqF8eGZtWWL0uCh4iaka%2Bt%2FEN4KLQg3zSnu10MsHQ90x36pW%2FLmrNqwWFLqajRve%2B8BT9wX71H3sIJBA0u17Bjt4Lyo%2Be6hi4KFvpMZypQzSKWuIEaOdf7oErBFLullN2IfaYS07f2r3sGtZGJtu4Uy1v9XSxBM%2FPZSaTFJL4NdRd4ulpFqgoE3tb3eXdbJozXsSmlKpB1k%3D--%2FM3j66rf7wE0eXOy--qsIf8Pcz7wdlPj1NtqB%2BLw%3D%3D",
        "Referer": "https://www.tapology.com/fightcenter",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": f'{userAgent}',
        "X-CSRF-Token": "01Xl0kvparFOz6wwwg1xCzztNB/n3PjN1UuAhKzRvBAVw4sGAK/VnJdQyXHVKAuHz62kDpMZQIafhgrpRuDUsw==",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"'
        }
        site = requests.get(url, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
        soup = BeautifulSoup(site.content, 'html.parser')
        billings = soup.find_all('span', class_='billing')
        for part in billings:
            fightParts.append(part.find_all('a'))    
        print(len(fightParts))
    #clean parts
    for part in fightParts:
        href = part[0]['href']
        if href:
            fightLinksParts.append(href)
    print(len(fightLinksParts))
    count+=1 
print(f'Fights found: {len(fightLinksParts)}')  


#scrape individual fight statistics
count = 1
fightStats = []
for i in fightLinksParts:
    #if(count%15==0):
        #time.sleep(random.randint(180, 300))
    #if(count%99==0):
        #time.sleep(random.randint(800,1000))
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
    try:
        response = requests.request("GET", url, data=payload, headers=headers, proxies={'http': f"http://{proxy}, 'https:'https/{proxy}"})
        soup = BeautifulSoup(response.content, 'html.parser')
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

    
    try:
        #scrape event
        boutInfo = soup.find('div', class_=re.compile('right'))
        lilabels = boutInfo.find_all('li')
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
        #scrape event
        boutInfo = soup.find('div', class_=re.compile('right'))
        lilabels = boutInfo.find_all('li')
        
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

    
    for num in range(1, len(lilabels)+1):
        #scrape + clean event name
        try:
            if(lilabels[num].find('strong').text.strip() == 'Event:'):
                event = lilabels[num].find('a').text.strip()
        except:
            pass
        #scrape + clean date
        try:
            if(lilabels[num].find('strong').text.strip() == 'Date:'):
                nCleanDate = lilabels[num].find('span').text.strip()
                dateList = nCleanDate.split(' ')
                date = dateList[1]
        except:
            pass
        #scrape + clean venue
        try:
            if(lilabels[num].find('strong').text.strip() == 'Venue:'):
                venue = lilabels[num].find('span').text.strip()
        except:
            pass
        #scrape whether it is a title fight
        try:
            if(lilabels[num].find('strong').text.strip() == 'Title on Line:'):
                title_fight = 'yes'
        except:
            pass
        #scrape + clean belt status
        try:
            if(lilabels[num].find('strong').text.strip() == 'Belt Status Before Fight:'):
                belt_status = lilabels[num].find('span').text.strip()
                #needs to be cleaned
        except:
            pass
    
    
    #scrape + clean billing
    try:
        billingInfo = soup.find('h4', class_=re.compile('boutPreResult'))
        billing_info = billingInfo.text.strip()
        billList = billing_info.split('|')
        billing = billList[0][:-1]
    except:
        pass
    
    #scrape +clean winner+fightname
    try:
        fight_name = f'{soup.find('span', class_=re.compile('fName left')).find('a').text.strip()} vs {soup.find('span', class_=re.compile('fName right')).find('a').text.strip()}'
        if(soup.find('span', class_=re.compile('fName left')).find('a').text.strip().lower().__contains__(soup.find('p', class_=re.compile('results')).find('span').text.strip().lower())):
            winnerInfo = soup.find('span', class_=re.compile('fName left'))
            winner = winnerInfo.find('a').text.strip()
            loserInfo = soup.find('span', class_=re.compile('fName right'))
            loser = loserInfo.find('a').text.strip()
        else:
            pass
    except:
        pass

    #scrape + parse table
    table = soup.find('table', class_=re.compile('fighterStats spaced'))
    trLabels = table.find_all('tr')
    for tr in trLabels:
        try:
            if(tr.find('td', class_=re.compile('category')).text.strip() == 'Pro Record At Fight'):
                tdLabels = tr.find_all('td')
                #scrape +clean records
                winner_record = tdLabels[0].text.strip()
                loser_record = tdLabels[len(tdLabels)-1].text.strip()
                #clean to fit atrributes
                list_winner_record = winner_record.split('-')
                winner_wins = list_winner_record[0]
                winner_losses = list_winner_record[1]
                winner_draws = list_winner_record[2]
                list_loser_record = loser_record.split('-')
                loser_wins = list_loser_record[0]
                loser_losses = list_loser_record[1]
                loser_draws = list_loser_record[2]
        except:
            pass
        #scrape + clean nationality
        try:
            if(tr.find('td', class_=re.compile('category')).text.strip() == 'Nationality'):
                nationalities = tr.find_all('img', class_=re.compile('countryFlag mini'))
                winner_nationality = nationalities[0].text.strip()
                loser_nationality = nationalities[1].text.strip()
        except:
            pass
        #scrape + clean age
        try:
            if(tr.find('td', class_='category').text.strip()== 'Age at Fight'):
                tdLabels = tr.find_all('td')
                #scrape + clean ages
                winnerAge = tdLabels[0].text.strip()
                winnerAgeList = winnerAge.split(',')
                winner_age = winnerAgeList[0][:-6]
                loserAge = tdLabels[len(tdLabels)-1].text.strip()
                loserAgeList = loserAge.split(',')
                loser_age = loserAgeList[0][:-6]
        except:
            pass
    #find + clean tapology fan predictions
    try:
        divs = soup.find_all('div', class_='number')
        loser_fan = divs[0].text.strip()
        winner_fan = divs[1].text.strip()
    except:
        pass
    print(f'Scraping {fight_name}...{f"{count/len(fightLinksParts):.0%}"}')
    count+=1
    fightStats.append([fight_name,winner, loser, event,date,venue,title_fight,billing,winner_wins ,loser_wins ,winner_losses ,loser_losses ,winner_draws,loser_draws,winner_age ,loser_age ,belt_status ,winner_nationality ,loser_nationality ,winner_fan ,loser_fan])


head = ['fight','winner', 'loser', 'event','date','venue','title_fight','billing','winner_wins' ,'loser_wins' ,'winner_losses' ,'loser_losses' ,'winner_draws','loser_draws','winner_age' ,'loser_age' ,'belt_status' ,'winner_nationality' ,'loser_nationality' ,'winner_fan ','loser_fan']

with open('tapology_scrape.csv', 'w', encoding='UTF8', newline='') as tapologyScrape:
    writer = csv.writer(tapologyScrape)
    writer.writerow(head)
    writer.writerows(fightStats)