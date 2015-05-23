# -*- coding: utf-8 -*-

#from PyQt4 import QtCore, QtGui, QtWidgets
from PyQt4 import QtCore, QtGui
import sys, os, glob, requests, BeautifulSoup, csv, time 
import form

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Main(QtGui.QDialog, form.Ui_Dialog):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        # aqui voce faz os bindings com funcoes do python
        self.btnIniciar.clicked.connect(self.atualizaTextField)            
   
    

    #show a message for user
    def msg(self, title, text, type = 0):
        if type == 0:
            QtWidgets.QMessageBox.information(self, title, text)
        else:
            QtWidgets.QMessageBox.critical(self, title, text)

    #iniciando os processos de requisições
    def atualizaTextField(self):                
        array = []
        arquivo = open("dados/dados.csv", 'w')
        linha = ''
        linhaText = ''
        signos = ['aries','touro', 'gemeos','cancer','leao','virgem','libra','escorpiao','sagitario','capricornio','aquario','peixes']
        with  open("dados/links.csv") as links:
            reader = csv.reader(links)
            for row in reader:
                array.append(str(row[0]))

        cont = 1
        for item in array:            
            if cont <= 100:
                r = requests.get(item)    
                soup = BeautifulSoup.BeautifulSoup(r.content)
                
                #filtrando o nome
                n = None
                for nome in soup.findAll('h2', attrs={'class': 'nome'}):
                    n = nome.text
                if(n):
                    linha = linha + nome.text + '|' + item
                else: 
                    linha = linha + 'NULL' + '|' + item                   
                    
                #filtrando os signos
                sf = None    
                for signo in signos:
                    for s in soup.findAll('a', attrs={'href': 'http://horoscopo.ego.globo.com/signos/'+signo}):
                        sf = s.text
                if(sf):
                    linha = linha + '|' + s.text
                else:
                    linha = linha + '|' + 'NULL'

                #filtrando a data de nascimento
                df = None    
                for dataNas in soup.findAll('time', attrs={'itemprop': 'birthDate'}):
                    df = dataNas.get('datetime')
                if(df):
                    linha = linha + '|' + df
                else:
                    linha = linha + '|' + 'NULL'

                #filtrando o relacionamento
                relacionamento = None    
                for status in soup.findAll('meta', attrs={'itemprop': 'spouse'}):
                    relacionamento = status.get('content')
                if(relacionamento):
                    linha = linha + '|' + relacionamento
                else:
                    linha = linha + '|' + 'NULL'                

                    
                arquivo.write(linha.encode('utf-8'))
                arquivo.write("\n")
                linhaText = linhaText + linha + '\n'
                self.textFieldDados.setPlainText(linhaText)
                self.progressBar.setValue(cont)                
                linha = ''    
                #print cont
                cont = cont + 1
                
        arquivo.close()
    


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()
