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
        self.barvy=["70,192,255","252,87,52","238,224,66","31,133,70","119,73,17","255,49,196","245,189,101"]
        
        self.setup()
        
    def setup(self):
        self.widgets=[[],[],[],[],[],[],[],[],[],[],[],[]]
        self.new()
        
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
        
        for radek in range(0,12):
            for sloupec in range(5):
                if radek==0:
                    button=QtGui.QPushButton(self)
                    button.setDisabled(True)
                    button.setStyleSheet("* { background-color: rgb(0,0,0) }")
                    button.resize(10,5)
                    self.widgets[radek].append(button)
                    grid.addWidget(button,radek+1,sloupec)
                    
                    continue
                
                if radek==11:
                    
                    button=QtGui.QPushButton(self)
                    
                    button.setStyleSheet("* { background-color: rgb(70,192,255) }")
                    button.resize(10,5)
                    button.clicked.connect(self.change)
                    self.widgets[radek].append(button)
                    grid.addWidget(button,radek+1,sloupec)
                    
                    continue
                
                button=QtGui.QPushButton(self)
                button.setDisabled(True)
                button.setStyleSheet("* { background-color: rgb(160,160,160) }")
                button.resize(10,5)
                self.widgets[radek].append(button)
                grid.addWidget(button,radek+1,sloupec)
                
            if radek==11:
                button=QtGui.QPushButton(self)
                button.setText("odeslat")
                button.resize(10,5)
                button.clicked.connect(self.odeslat)
                grid.addWidget(button,radek+1,6)
            else:            
                lbl=QtGui.QLabel(self)
                lbl.setText("0/0")
                grid.addWidget(lbl,radek+1,6)
                self.widgets[radek].append(lbl)
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
            red=self.widgets[11][i].palette().color(1).red()        
            blue=self.widgets[11][i].palette().color(1).blue()
            green=self.widgets[11][i].palette().color(1).green()
            hadani.append("%s,%s,%s"%(red,green,blue))
        if hadani==self.hadanka:
            for x in range(5):
                self.widgets[0][x].setStyleSheet("* { background-color: rgb(%s) }"%self.hadanka[x])
            self.dialog(1)
        else:
            if self.pokusy>10:
                for x in range(5):
                    self.widgets[0][x].setStyleSheet("* { background-color: rgb(%s) }"%self.hadanka[x])
                self.dialog(0)
                
            else:
                for i in range(len(hadani)):
                    if hadani[i] in self.hadanka:
                        barvy+=1
                    if hadani[i]==self.hadanka[i]:
                        pozice+=1
                    self.widgets[11-self.pokusy][i].setStyleSheet("* { background-color: rgb(%s) }"%hadani[i])
                self.widgets[11-self.pokusy][5].setText("%i/%i"%(barvy,pozice))
    def dialog(self,vyhra):
        if vyhra:
            text="Gratulace, vyhral jste. Prejete si hrat znovu"
        else:
            text="Skoda, prohral jste. Prejete si hrat znovu"
                
        dialog=QtGui.QDialog(self)
        grid=QtGui.QGridLayout()
        lbl=QtGui.QLabel(dialog)
        lbl.setText(text)
        lbl.resize(lbl.sizeHint())
        grid.addWidget(lbl,0,0,1,2)        
        button=QtGui.QPushButton(dialog)
        button.setText("Hrat znovu")
        button.clicked.connect(self.change_color)
        button.clicked.connect(dialog.close)
        button.resize(button.sizeHint())
        grid.addWidget(button,1,0)
        button=QtGui.QPushButton(dialog)
        button.setText("Konec")
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        button.resize(button.sizeHint())
        grid.addWidget(button,1,1)
        dialog.setLayout(grid)
        dialog.exec_()
            
    def new(self):
        self.pokusy=0
        self.hadanka=random.sample(self.barvy,5)

    def change_color(self):
        for radek in range(len(self.widgets)):
            for sloupec in range(len(self.widgets[radek])):
                widget=self.widgets[radek][sloupec]
                if radek==0 and sloupec!=5:
                    widget.setStyleSheet("* { background-color: rgb(0,0,0) }")
                    continue
                if radek==11:
                    widget.setStyleSheet("* { background-color: rgb(70,192,255) }")
                    continue
                if radek<11 and sloupec==5:
                    widget.setText("0/0")
                else:
                    widget.setStyleSheet("* {  background-color: rgb(160,160,160) }")
        self.new()
            
            


def main():
    app=QtGui.QApplication(sys.argv)
    ex=Ui()
    sys.exit(app.exec_())
    


if __name__=="__main__":
    main()
        
        
