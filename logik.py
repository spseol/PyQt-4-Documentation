# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 01:49:52 2014

@author: Adam
"""



import sys
from PyQt4 import QtGui, QtCore
import random

class Ui(QtGui.QWidget):
    
    def __init__(self):
        super(Ui,self).__init__()
        
        self.setup()
        
    def setup(self):
        self.buttons=[0,[],[],[],[],[],[],[],[],[],[],[],[]]
        
        self.pokusy=0
        self.barvy=["70,192,255","252,87,52","238,224,66","31,133,70","119,73,17","255,49,196","245,189,101"]
        self.hadanka=random.sample(self.barvy,5)
                
        
        
        grid=QtGui.QGridLayout()
        
        self.lbl_logik=QtGui.QLabel(self)
        self.lbl_logik.setText("Logik")
        self.lbl_logik.resize(self.lbl_logik.sizeHint())
        
        grid.addWidget(self.lbl_logik,0,0,1,5)
        
        spacer=QtGui.QSpacerItem(10,0)
        
        grid.addItem(spacer,0,5,13,1)
                
        self.lbl_barvy=QtGui.QLabel(self)
        self.lbl_barvy.setText("Barvy/Pozice")
        self.lbl_barvy.resize(self.lbl_barvy.sizeHint())
        
        grid.addWidget(self.lbl_barvy,0,6,1,1)
        
        for radek in range(1,13):
            for sloupec in range(5):
                if radek==1:
                    button=QtGui.QPushButton(self)
                    button.setDisabled(True)
                    button.setStyleSheet("* { background-color: rgb(0,0,0) }")
                    button.resize(10,5)
                    self.buttons[radek].append(button)
                    grid.addWidget(button,radek,sloupec)
                    
                    continue
                
                if radek==12:
                    
                    button=QtGui.QPushButton(self)
                    
                    button.setStyleSheet("* { background-color: rgb(70,192,255) }")
                    button.resize(10,5)
                    button.clicked.connect(self.change)
                    self.buttons[radek].append(button)
                    grid.addWidget(button,radek,sloupec)
                    
                    continue
                
                button=QtGui.QPushButton(self)
                button.setDisabled(True)
                button.setStyleSheet("* { background-color: rgb(160,160,160) }")
                button.resize(10,5)
                self.buttons[radek].append(button)
                grid.addWidget(button,radek,sloupec)
                
            if radek==12:
                button=QtGui.QPushButton(self)
                button.setText("odeslat")
                button.resize(10,5)
                button.clicked.connect(self.odeslat)
                grid.addWidget(button,radek,6)
            else:            
                lbl=QtGui.QLabel(self)
                lbl.setText("0/0")
                grid.addWidget(lbl,radek,6)
                self.buttons[radek].append(lbl)
        self.setLayout(grid)
        self.show()
    
    
    def change(self):
        red=self.sender().palette().color(1).red()        
        blue=self.sender().palette().color(1).blue()
        green=self.sender().palette().color(1).green()
        color="%s,%s,%s"%(red,green,blue)
        if self.barvy.index(color)==len(self.barvy)-1:
            self.sender().setStyleSheet("* { background-color: rgb(%s) }"%self.barvy[0])
        else:
            self.sender().setStyleSheet("* { background-color: rgb(%s) }"%self.barvy[self.barvy.index(color)+1])
    
    def odeslat(self):
        hadani=[]
        pozice=0
        barvy=0
        self.pokusy+=1
        
        for i in range(5):
            red=self.buttons[12][i].palette().color(1).red()        
            blue=self.buttons[12][i].palette().color(1).blue()
            green=self.buttons[12][i].palette().color(1).green()
            hadani.append("%s,%s,%s"%(red,green,blue))
        if hadani==self.hadanka:
            for x in range(5):
                self.buttons[1][x].setStyleSheet("* { background-color: rgb(%s) }"%self.hadanka[x])
        else:
            if self.pokusy>10:
                for x in range(5):
                    self.buttons[1][x].setStyleSheet("* { background-color: rgb(%s) }"%self.hadanka[x])
                dialog=QtGui.QDialog(self)
                grid=QtGui.QGridLayout()
                lbl=QtGui.QLabel(dialog)
                lbl.setText("Skoda, prohral jste. Prejete si hrat znovu")
                lbl.resize(lbl.sizeHint())
                grid.addWidget(lbl,0,0,1,2)
                
                button=QtGui.QPushButton(dialog)
                button.setText("Hrat znovu")
                button.clicked.connect(self.new)
                button.resize(button.sizeHint())
                grid.addWidget(button,1,0)
                button=QtGui.QPushButton(dialog)
                button.setText("Konec")
                button.clicked.connect(QtCore.QCoreApplication.instance().quit)
                button.resize(button.sizeHint())
                grid.addWidget(button,1,1)
                dialog.setLayout(grid)
                dialog.exec_()
                
            else:
                for i in range(len(hadani)):
                    if hadani[i] in self.hadanka:
                        barvy+=1
                    if hadani[i]==self.hadanka[i]:
                        pozice+=1
                    self.buttons[12-self.pokusy][i].setStyleSheet("* { background-color: rgb(%s) }"%hadani[i])
                self.buttons[12-self.pokusy][5].setText("%i/%i"%(barvy,pozice))
    
    def new(self):
        print QtCore.QCoreApplication.instance()
        QtCore.QCoreApplication.instance().quit()
        
        main()
            


def main():
    app=QtGui.QApplication(sys.argv)
    print app
    ex=Ui()
    print "ss"
    sys.exit(app.exec_())
    


if __name__=="__main__":
    main()
        
        