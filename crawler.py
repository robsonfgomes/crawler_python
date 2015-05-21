import requests
import BeautifulSoup
import os, csv, time


array = []
arquivo = open("dados/dados.csv", 'w')
linha = ''
signos = ['aries','touro', 'gemeos','cancer','leao','virgem','libra','escorpiao','sagitario','capricornio','aquario','peixes']
with  open("dados/links.csv") as links:
    reader = csv.reader(links)
    for row in reader:
        array.append(str(row[0]))

cont = 1
for item in array:    
    r = requests.get(item)    
    soup = BeautifulSoup.BeautifulSoup(r.content)
    
    #filtrando o nome
    n = None
    for nome in soup.findAll('h2', attrs={'class': 'nome'}):
        n = nome.text
    if(n):
        linha = linha + nome.text
    else: 
        linha = linha + 'NULL'
        
    #filtrando o nome completo
    nc = None    
    for nomeCompleto in soup.findAll('p', attrs={'class': 'nome-completo'}):
        nc = nomeCompleto.text
    if(nc):
        linha = linha + ',' + nomeCompleto.text + ',' + item
    else:
        linha = linha + ',' + 'NULL' + ',' + item        
        
    #filtrando o link da foto
    ft = None    
    for urlFoto in soup.findAll('img', attrs={'class': 'img-perfil'}):
        ft = urlFoto.get('src')
    if(ft):
        linha = linha + ',' + urlFoto.get('src')
    else:
        linha = linha + ',' + 'NULL'
        
    #filtrando os signos
    sf = None    
    for signo in signos:
        for s in soup.findAll('a', attrs={'href': 'http://horoscopo.ego.globo.com/signos/'+signo}):
            sf = s.text
    if(sf):
        linha = linha + ',' + s.text
    else:
        linha = linha + ',' + 'NULL'

    #filtrando a data de nascimento
    df = None    
    for dataNas in soup.findAll('li', attrs={'class': 'aniversario'}):
        df = dataNas.text
    if(df):
        linha = linha + ',' + dataNas.text  
    else:
        linha = linha + ',' + 'NULL'

    #filtrando o relacionamento
    relacionamento = None    
    for status in soup.findAll('meta', attrs={'itemprop': 'spouse'}):
        relacionamento = status.get('content')
    if(relacionamento):
        linha = linha + ',' + relacionamento
    else:
        linha = linha + ',' + 'NULL'

    #filtrando a biografia
    bio = None    
    for biografia in soup.findAll('p', attrs={'class': 'biografia'}):
        bio = biografia.text
    if(bio):
        linha = linha + ',' + bio
    else:
        linha = linha + ',' + 'NULL'

        
    arquivo.write(linha.encode('utf-8'))
    arquivo.write("\n")
    linha = ''    
    print cont
    cont = cont + 1
        
arquivo.close()
print('fim')


        
#.encode('utf-8')   
