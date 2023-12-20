#generate proxyList
proxylist =[]
with open('working_proxies.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])
print(f'Proxies: {len(proxylist)}')

def getProxyHeader():
    for i in proxylist:
        userAgents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0','Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188','insomnia/8.4.5']
        userAgent = userAgents[random.randint(0,len(userAgents)-1)]
        try:
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
            proxyheader = [i,headers,userAgent]
            return proxyheader
        except:
            print("Waiting for new IP")
            time.sleep(350)
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
            proxyheader = [i,headers,userAgent]
            return proxyheader
        