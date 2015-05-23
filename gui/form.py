# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Sat May 23 14:56:44 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(888, 600)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 90, 871, 431))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.textFieldDados = QtGui.QPlainTextEdit(self.groupBox_2)
        self.textFieldDados.setGeometry(QtCore.QRect(10, 70, 841, 351))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textFieldDados.setFont(font)
        self.textFieldDados.setPlainText(_fromUtf8(""))
        self.textFieldDados.setObjectName(_fromUtf8("textFieldDados"))
        self.progressBar = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 30, 851, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(-10, -11, 921, 91))
        self.groupBox_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 127);\n"
"border-color: rgb(0, 85, 127);"))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.labelImagem = QtGui.QLabel(self.groupBox_3)
        self.labelImagem.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.labelImagem.setText(_fromUtf8(""))
        self.labelImagem.setObjectName(_fromUtf8("labelImagem"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Calligraphy"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(690, 530, 191, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btnIniciar = QtGui.QPushButton(self.groupBox)
        self.btnIniciar.setGeometry(QtCore.QRect(70, 10, 81, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../Google Drive/Ciência da Computação/Matemática Discreta/Aula-02/exercicios/2.3/interface-grafica/icons_buttons/add_flat.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIniciar.setIcon(icon)
        self.btnIniciar.setObjectName(_fromUtf8("btnIniciar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Dados", None))
        self.label.setText(_translate("Dialog", "Crawler_MD", None))
        self.groupBox.setTitle(_translate("Dialog", "Ações", None))
        self.btnIniciar.setText(_translate("Dialog", "Lerigou!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

