# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 12:43:03 2014

@author: Adam
"""

# import vsech potrebnych modulu ktere budeme potrebovat
# modul QtGui obsahuje tridy ruznych widgetu pro tvorbu Gui
import sys
from PyQt4 import QtGui


# vytvoreni podtridy z tridy QWidget (obsahuje metody pro pro praci s okny
# i ostatnimi widgety,jako napriklad zachyceni udalosti a skryvani udelatek)
class main_window(QtGui.QWidget):
    # vytvoreni metody __init__ ktera se spusti pri vytvoreni objektu z teto
    # tridy.Funkce super slouzi pro volani metody pro potomka i pro rodice
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi()

    # v teto metode vytvorime samotne okno metoda move posouva okno po
    # obrazovce v nasem pripade na souradnici 300 vertikalne a souradnici 200
    # horizontalne metoda resize nastavi velikost okna na 300x150px
    # setWindowTitle nastavuje jmeno okna a setWindowIcon vytvari za pomoci
    # fuknce QIcon( umoznuje mnoho ruznych vytvoreni objektu icony v nasem
    # pripade jsme vytvorily iconu pomoci cesty k dane ikone) ikonu v horni
    # casti okna a nakonec nejdulezitejsi metoda a to medota show ktera zobrazi
    # cele okno
    def setupUi(self):
        self.move(100, 200)
        self.resize(300, 150)
        self.setWindowTitle("Hello world")
        self.setWindowIcon(QtGui.QIcon("world.jpg"))
        self.show()

# pomoci teto podminky vztvorime instance jednolivich trid, ktere pote vztvori
# okno. je dobre jsi vsimnout podminky, tato podminka je mozna diky funkci
# jazyka Python, ktery si pri spusteni tohoto souboru tento soubor pojmenuje
# __main__ toto je dobre vedet. jako prvni vytvorime objekt app za pomoci tridy
# QApplication,ktera jsi bere informace z prikazove radky pote vzztvorime
# objekt okno z nasi tridy a nakonec funkce sys,exit, ktera zajisti apby bylo
# okno radne vypnu po stisknuti krizku
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    okno = main_window()
    sys.exit(app.exec_())
