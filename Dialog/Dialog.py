# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
D:\Users\edith\.spyder2\.temp.py
"""

from PyQt4 import QtGui
import sys

class Ui(QtGui.QWidget):
    def __init__(self):
        super(Ui,self).__init__()
        
        self.setup()
        
    def setup(self):
        
        self.btn = QtGui.QPushButton("Exit",parent=self)
        self.btn.move(20,30)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.exit_)
        
        self.setGeometry(200,300,400,500)
        self.show()
    
    def exit_(self):
        dialog=QtGui.QDialog(parent=self)
        
        dialog.lbl = QtGui.QLabel("Jste si jsit ze chcete ukoncit aplikaci",parent= dialog)
        dialog.lbl.resize(dialog.lbl.sizeHint())        
        
        
        dialog.btn = QtGui.QPushButton("Ano",parent=dialog)
        
        dialog.btn.resize(dialog.btn.sizeHint())
        dialog.btn.clicked.connect(self.close)
        
        dialog.btn1= QtGui.QPushButton("Ne",parent=dialog)
        
        dialog.btn1.resize(dialog.btn1.sizeHint())
        dialog.btn1.clicked.connect(dialog.close)
        
        grid=QtGui.QGridLayout()
        grid.addWidget(dialog.lbl,0,0,1,0)
        grid.addWidget(dialog.btn,1,0)
        grid.addWidget(dialog.btn1,1,1)
        
        dialog.setLayout(grid)       
        dialog.exec_()
        
if __name__=="__main__":
    app= QtGui.QApplication(sys.argv)
    okno=Ui()
    sys.exit(app.exec_())
        