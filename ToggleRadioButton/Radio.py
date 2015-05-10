# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 22:05:11 2014

@author: Adam
"""
from PyQt4 import QtGui,QtCore
import sys

class Ui(QtGui.QWidget):
    def __init__(self):
        super(Ui,self).__init__()
        
        self.setup()
    
    def setup(self):
        
        self.lbl = QtGui.QLabel("Hezky text", parent=self)
        self.lbl.resize(self.lbl.sizeHint())
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.radio = QtGui.QRadioButton("cervena",parent=self)        
        
        self.radio.resize(self.radio.sizeHint())
        self.radio.setChecked(True)        
        
        self.radio2 = QtGui.QRadioButton("modra",parent=self)        
        
        self.radio2.resize(self.radio2.sizeHint())
        
        self.color = QtGui.QButtonGroup(parent=self)
        self.color.addButton(self.radio)
        self.color.addButton(self.radio2)
        self.color.buttonClicked.connect(self.change)

        self.radio3 = QtGui.QRadioButton("kurziva",parent=self)        
        
        self.radio3.resize(self.radio3.sizeHint())
        self.radio3.setChecked(True)          
        
        self.radio4 = QtGui.QRadioButton("tucne",parent=self)        
        
        self.radio4.resize(self.radio4.sizeHint())
        
        self.font = QtGui.QButtonGroup(parent=self)
        self.font.addButton(self.radio3)
        self.font.addButton(self.radio4)
        self.font.buttonClicked.connect(self.change)       
        
        grid=QtGui.QGridLayout()
        grid.addWidget(self.lbl,0,0,1,0)
        grid.addWidget(self.radio,1,0)
        grid.addWidget(self.radio2,1,1)        
        grid.addWidget(self.radio3,2,0)
        grid.addWidget(self.radio4,2,1)
        
        self.setLayout(grid)
        self.show()
        
    def change(self):
        font= QtGui.QFont()
                
        
        if self.color.checkedId()==self.color.id(self.radio):
            self.lbl.setStyleSheet("color:red")
        else:
            self.lbl.setStyleSheet("color:blue")
        
        if self.font.checkedId()==self.font.id(self.radio3):
            font.setItalic(True)   
            self.lbl.setFont(font)
        else:
            font.setBold(True)
            self.lbl.setFont(font)
            
            
            
if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    okno=Ui()
    sys.exit(app.exec_())