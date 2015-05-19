import requests as r
import BeautifulSoup

r = r.get('http://ego.globo.com/famosos/tudo-sobre/abigail-breslin.html')
soup = BeautifulSoup.BeautifulSoup(r.content)

for a in soup.findAll('li', attrs={'class': 'aniversario'}):
    print(a.text)
