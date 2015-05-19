import requests as r
import BeautifulSoup
import os, csv

r = r.get('http://ego.globo.com/famosos/tudo-sobre/abigail-breslin.html')
soup = BeautifulSoup.BeautifulSoup(r.content)

for a in soup.findAll('li', attrs={'class': 'aniversario'}):
    print(a.text)

with  open("dados/links.csv") as links:
    reader = csv.reader(links)
    for row in reader:
        print(row[0])
