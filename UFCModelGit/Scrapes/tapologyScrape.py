
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import math
import csv
from csv import writer
import itertools

import requests
def tapologyScrape():
    url = "https://www.tapology.com/fightcenter_events"

    payload = "authenticity_token=01Xl0kvparFOz6wwwg1xCzztNB%2Fn3PjN1UuAhKzRvBAVw4sGAK%2FVnJdQyXHVKAuHz62kDpMZQIafhgrpRuDUsw%3D%3D&group=ufc&schedule=results&sport=all&=region%3D"
    headers = {
        "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "usprivacy=1Y--; _au_1d=AU1D-0100-001699559408-UHN9538G-791U; _gid=GA1.2.267777754.1701026655; __gads=ID=006eef68af2069f8:T=1701057293:RT=1701067622:S=ALNI_MZOGhTIoX2sSp_mXeikO0Kw6YJChw; _au_last_seen_pixels=eyJhcG4iOjE3MDEwOTQ2OTksInR0ZCI6MTcwMTA5NDY5OSwicHViIjoxNzAxMDk0Njk5LCJydWIiOjE3MDEwOTQ2OTksInRhcGFkIjoxNzAxMDk0Njk5LCJhZHgiOjE3MDEwOTQ2OTksImdvbyI6MTcwMTA5NDY5OSwib3BlbngiOjE3MDEwNTcyNzMsInNvbiI6MTcwMTA1NzI3MywidW5ydWx5IjoxNzAxMDk0NzA3LCJwcG50IjoxNzAxMDk0Njk5LCJhbW8iOjE3MDEwOTQ2OTksImNvbG9zc3VzIjoxNzAxMDU3MjczLCJiZWVzIjoxNzAxMDU3MjczLCJ0YWJvb2xhIjoxNzAxMDU3MjczLCJpbXByIjoxNzAxMDU3MjczLCJhZG8iOjE3MDEwNTcyNzMsInNtYXJ0IjoxNzAxMDU3MjczLCJpbmRleCI6MTcwMTA1NzI5M30%3D; __qca=I0-1125826933-1701095027052; _ga=GA1.1.1827296034.1699559406; _sharedid=89deac14-215b-4803-ada4-17cf3d79240e; _pbjs_userid_consent_data=6683316680106290; _ga_DL61VSM5W1=GS1.1.1701099972.7.1.1701100068.0.0.0; cto_bundle=tSavVV9sMWJ2Tnl0eEc2UTZLcmk3aHIwTDRXa2tLU3Y2ZnA4JTJCTTNwZWoxbWJwbmlyWWxJejJIUWRid3JaSFAwQTRTUXpyWEQlMkJROWlqcXNvMFBETnJvVTc0SHFKTEY4MHhIVndQREE2Nm12ZnJqS1RKampGUmxrdlpRRGxndVFQbkZsdGlCJTJGUTF3QUNBV3JpNm12JTJGakFmYm9uR1pRcXNTMTVkOFh0VG5xcksyZ1JCcnhZaVI3QzM0ZERsaiUyQkd1blN5cDglMkI; cto_bidid=O-wksV9ydWFlcGozeFRhN1g4YXBBd0hMUXQ5OEFrOUx1TFZrOE5LYldVTWRJJTJCYTR2V00lMkJnckZGM0toUDVnZ0NpcEVXUWZuRno5cUZEWDlGRFN3ZFhaSEExVGRwZEdjS1FZY21RVXE2TGZVQWQwTkRvNVJzTSUyQno4WVFKUXFDdXpXV3ZNeWRYRkE4QlU1Z010ckdGOEJWbVdHVGclM0QlM0Q; _tapology_mma_session=%2BDuZHyszn2U1NcJNO6AKaWZnB9XohIbutDHPKoPsgvsX4Ux64VPW2lT3OYVfPG%2BdRE0W%2Fq5LGYOsxd8OfBPv%2BhBco5%2F%2FpfxqlpLgokhiesR53%2FNtx1TWvxqnAcXbo02%2FleOKYWwHZMFC6SjhXBsnNJK3Ej6xFZO1i1Hvr0hATCjxtYSt%2BAv5FXd3pfjyCyWLcqJrr2OyxEvXTas9093PGUBmaRABIVgvqX2xpNLRdhb9LK86vF%2FDpFQJel87R8mkv72KCBDWiMLeQehX%2B2YWQ8HejohCbgRyxSJhdaY%3D--1NyCqkZFaRwFiI0D--uOQez3wLrY%2BuybZ98LlgcQ%3D%3D",
        "Origin": "https://www.tapology.com",
        "Referer": "https://www.tapology.com/fightcenter",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-CSRF-Token": "01Xl0kvparFOz6wwwg1xCzztNB/n3PjN1UuAhKzRvBAVw4sGAK/VnJdQyXHVKAuHz62kDpMZQIafhgrpRuDUsw==",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"'
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

tapologyScrape()