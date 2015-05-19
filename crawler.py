import requests
import BeautifulSoup
import os, csv, time


array = []
r = []
with  open("dados/links.csv") as links:
    reader = csv.reader(links)
    for row in reader:
        array.append(str(row[0]))

for item in array:
    r = requests.get(item)    
    soup = BeautifulSoup.BeautifulSoup(r.content)
    for a in soup.findAll('li', attrs={'class': 'aniversario'}):
        print(a.text)    
        
