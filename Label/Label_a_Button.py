# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 10:59:26 2014

@author: obr31280
"""
import sys
from PyQt4 import QtGui,QtCore

class Ui(QtGui.QWidget):
    def __init__(self):
        super(Ui,self).__init__()
        
        self.setup()
        
    def setup(self):
        self.lbl = QtGui.QLabel("hezky text",parent = self)
        self.lbl.resize(self.lbl.sizeHint())
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.re_button = QtGui.QPushButton("red",parent=self)
        self.re_button.setCheckable(True)
        
        self.re_button.resize(self.re_button.sizeHint())
        self.re_button.clicked.connect(self.zmena)
        
        self.it_button = QtGui.QPushButton("kurziva",parent=self)
        self.it_button.setCheckable(True)
        
        self.it_button.resize(self.it_button.sizeHint())
        self.it_button.clicked.connect(self.zmena)
        
        self.tu_button = QtGui.QPushButton("tucne",parent=self)
        self.tu_button.setCheckable(True)
        
        self.tu_button.resize(self.tu_button.sizeHint())
        self.tu_button.clicked.connect(self.zmena)
        
        self.po_button = QtGui.QPushButton("podtrhnute",parent=self)
        self.po_button.setCheckable(True)
        
        self.po_button.resize(self.po_button.sizeHint())
        self.po_button.clicked.connect(self.zmena)
        
        grid=QtGui.QGridLayout()
        grid.addWidget(self.lbl,0,0,1,0)
        grid.addWidget(self.re_button,1,0,)
        grid.addWidget(self.it_button,1,1,)
        grid.addWidget(self.tu_button,2,0)
        grid.addWidget(self.po_button,2,1)      
        
        self.setLayout(grid)
        self.setWindowTitle("stisknute tlacitko")
        self.show()
    def zmena(self):
        font= QtGui.QFont()
             
        
        if self.it_button.isChecked():
            font.setItalic(True)            
            self.lbl.setFont(font)
            
        else:
            font.setItalic(False)
            self.lbl.setFont(font)
        
        if self.tu_button.isChecked():
            font.setBold(True)            
            self.lbl.setFont(font)
                        
        else:
            font.setBold(False)
            self.lbl.setFont(font)   
        
        if self.po_button.isChecked():
            font.setUnderline(True)            
            self.lbl.setFont(font)
            
        else:
            font.setUnderline(False)
            self.lbl.setFont(font)        
        
        if self.re_button.isChecked():
            self.lbl.setStyleSheet("color:red")
            
        else:
            self.lbl.setStyleSheet("color:black")
            
        
if __name__== "__main__":
    app=QtGui.QApplication(sys.argv)
    okno= Ui()
    sys.exit(app.exec_())
        
        
