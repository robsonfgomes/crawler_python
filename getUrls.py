import requests
import BeautifulSoup
import os, csv, time

r = requests.get('http://ego.globo.com/famosos/')
soup = BeautifulSoup.BeautifulSoup(r.content)
for link in soup.findAll('li', attrs={'itemprop': 'itemListElement'}):
    print link
