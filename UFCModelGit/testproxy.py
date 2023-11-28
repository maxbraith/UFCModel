import requests
import csv

proxylist = []

with open('csv_test_proxies.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[2])


def extract(proxy):
    works = False
    try:
        r = requests.get('https://www.ufc.com/', proxies={'http':proxy, 'https':proxy}, timeout=2)
        print(r)
        works = True
    except:
        pass
    return works

for i in proxylist:
    tempProxy = []
    if(extract(i)):
        tempProxy.append(list(i))
        with open('workingProxies.csv', 'w', encoding='UTF8', newline='') as workingProx:
            writer = csv.writer(workingProx)
            writer.writerow(tempProxy)


    