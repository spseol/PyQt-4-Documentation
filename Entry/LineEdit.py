# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 11:23:28 2014

@author: obr31280
"""
from PyQt4 import QtGui,QtCore
import sys

class Ui(QtGui.QWidget,):
      
    def __init__(self):
        super(Ui,self).__init__()
        self.dict={}        
        self.setup()
        
        
    def setup(self):
        self.font = QtGui.QFont()
        self.font.setItalic(True)
        
        self.form_name = QtGui.QLineEdit("Jmeno",parent=self,)        
        self.form_name.setFont(self.font)
        
        self.form_name.resize(100,20)
        
        self.form_pass = QtGui.QLineEdit("Heslo",parent=self,)
        self.form_pass.setEchoMode(2)
        
        self.form_pass.resize(100,20)
        
        self.btn_prihlas = QtGui.QPushButton("potvrdit",parent=self,)
        
        self.btn_prihlas.resize(self.btn_prihlas.sizeHint())
        self.btn_prihlas.clicked.connect(self.prihlas)
        
        self.btn= QtGui.QPushButton("nemate registraci",parent=self,)
        
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.registrace)        
    
        self.lbl = QtGui.QLabel(parent=self)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setMinimumSize(220, 13)
        
        grid=QtGui.QGridLayout()
        grid.addWidget(self.form_name,0,0,1,0)
        grid.addWidget(self.form_pass,1,0,1,0)
        grid.addWidget(self.btn_prihlas,2,0)
        grid.addWidget(self.btn,2,1)      
        grid.addWidget(self.lbl,3,0,1,0)         
        
        self.setLayout(grid)
        self.show()
    
    def prihlas(self):
        
        if self.form_name.text() in self.dict.keys() and self.form_pass.text()==self.dict[self.form_name.text()]:
            self.lbl.setText("Byli jste uspesne prihlaseni")
            self.lbl.resize(self.lbl.sizeHint())
            
        
        else:
            self.lbl.setText("Prihlaseni se nezdarilo heslo nebo jmeno se lisi")
            self.lbl.resize(self.lbl.sizeHint())
            
            
    
    def registrace(self):
        
        okenko=popup()
        self.dict[okenko.line_name.text()]= okenko.line_pass.text()
        
    
class popup(QtGui.QDialog,):
    def __init__(self):
        super(popup,self).__init__()
        
        self.setup()
    
    def setup(self,):
        self.line_name = QtGui.QLineEdit("Jmeno",parent=self)
        
        self.line_name.resize(100,20)
        
        
        self.line_pass = QtGui.QLineEdit("Heslo",parent=self)
        
        self.line_pass.resize(100,20)
        self.line_pass.setEchoMode(2)
       
        
        self.btn_potvrdit = QtGui.QPushButton("potvrdit",parent=self)
        
        self.btn_potvrdit.resize(self.btn_potvrdit.sizeHint())
        self.btn_potvrdit.clicked.connect(self.close)
        
        grid=QtGui.QGridLayout()
        grid.addWidget(self.line_name,0,0,1,0)
        grid.addWidget(self.line_pass,1,0,1,0)
        grid.addWidget(self.btn_potvrdit,2,0)
        
        self.setLayout(grid)
        self.exec_()
        
        
    
        
    
if __name__=="__main__":
    app= QtGui.QApplication(sys.argv)
    okno=Ui()
    sys.exit(app.exec_())
