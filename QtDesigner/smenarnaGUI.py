# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smen.ui'
#
# Created: Wed Mar 25 21:29:01 2015
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(251, 231)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.prodej = QtGui.QRadioButton(self.groupBox_2)
        self.prodej.setObjectName(_fromUtf8("prodej"))
        self.verticalLayout_2.addWidget(self.prodej)
        self.nakup = QtGui.QRadioButton(self.groupBox_2)
        self.nakup.setChecked(True)
        self.nakup.setObjectName(_fromUtf8("nakup"))
        self.verticalLayout_2.addWidget(self.nakup)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 3)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.RB_mena1 = QtGui.QRadioButton(self.groupBox)
        self.RB_mena1.setChecked(True)
        self.RB_mena1.setObjectName(_fromUtf8("RB_mena1"))
        self.verticalLayout.addWidget(self.RB_mena1)
        self.RB_mena1_2 = QtGui.QRadioButton(self.groupBox)
        self.RB_mena1_2.setChecked(False)
        self.RB_mena1_2.setObjectName(_fromUtf8("RB_mena1_2"))
        self.verticalLayout.addWidget(self.RB_mena1_2)
        self.RB_mena1_3 = QtGui.QRadioButton(self.groupBox)
        self.RB_mena1_3.setObjectName(_fromUtf8("RB_mena1_3"))
        self.verticalLayout.addWidget(self.RB_mena1_3)
        self.RB_mena1_4 = QtGui.QRadioButton(self.groupBox)
        self.RB_mena1_4.setObjectName(_fromUtf8("RB_mena1_4"))
        self.verticalLayout.addWidget(self.RB_mena1_4)
        self.RB_mena1_5 = QtGui.QRadioButton(self.groupBox)
        self.RB_mena1_5.setObjectName(_fromUtf8("RB_mena1_5"))
        self.verticalLayout.addWidget(self.RB_mena1_5)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pocet = QtGui.QLabel(self.groupBox_3)
        self.pocet.setText(_fromUtf8(""))
        self.pocet.setObjectName(_fromUtf8("pocet"))
        self.verticalLayout_3.addWidget(self.pocet)
        self.kurz = QtGui.QLabel(self.groupBox_3)
        self.kurz.setText(_fromUtf8(""))
        self.kurz.setObjectName(_fromUtf8("kurz"))
        self.verticalLayout_3.addWidget(self.kurz)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.entry = QtGui.QLineEdit(self.groupBox_4)
        self.entry.setObjectName(_fromUtf8("entry"))
        self.gridLayout_2.addWidget(self.entry, 0, 0, 1, 1)
        self.vypocet = QtGui.QPushButton(self.groupBox_4)
        self.vypocet.setObjectName(_fromUtf8("vypocet"))
        self.gridLayout_2.addWidget(self.vypocet, 0, 1, 1, 1)
        self.Vysledek = QtGui.QLabel(self.groupBox_4)
        self.Vysledek.setText(_fromUtf8(""))
        self.Vysledek.setObjectName(_fromUtf8("Vysledek"))
        self.gridLayout_2.addWidget(self.Vysledek, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_4, 1, 2, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.RB_mena1, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Kurz)
        QtCore.QObject.connect(self.RB_mena1_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Kurz)
        QtCore.QObject.connect(self.RB_mena1_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Kurz)
        QtCore.QObject.connect(self.RB_mena1_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Kurz)
        QtCore.QObject.connect(self.RB_mena1_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Kurz)
        QtCore.QObject.connect(self.RB_mena1_5, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Kurz)
        QtCore.QObject.connect(self.vypocet, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Vypocet)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Směnárna", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Transakce", None))
        self.prodej.setText(_translate("MainWindow", "Prodej", None))
        self.nakup.setText(_translate("MainWindow", "Nákup", None))
        self.groupBox.setTitle(_translate("MainWindow", "Měna", None))
        self.RB_mena1.setText(_translate("MainWindow", "GBP", None))
        self.RB_mena1_2.setText(_translate("MainWindow", "EUR", None))
        self.RB_mena1_3.setText(_translate("MainWindow", "USD", None))
        self.RB_mena1_4.setText(_translate("MainWindow", "JPY", None))
        self.RB_mena1_5.setText(_translate("MainWindow", "CAD", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Kurz", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Výpočet", None))
        self.vypocet.setText(_translate("MainWindow", "Vypocet", None))

