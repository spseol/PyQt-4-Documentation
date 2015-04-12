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
    
    def dialogs(self):
        self.dialog=QtGui.QDialog(parent=self)
        self.dialog.setModal(True)
        self.dialog.lbl = QtGui.QLabel("Jste si jsit ze chcete ukoncit aplikaci",parent= self.dialog)
        self.dialog.lbl.resize(self.dialog.lbl.sizeHint())        
        
        
        self.dialog.btn = QtGui.QPushButton("Ano",parent=self.dialog)
        
        self.dialog.btn.resize(self.dialog.btn.sizeHint())
        self.dialog.btn.clicked.connect(self.dialog.accept)
        
        self.dialog.btn1= QtGui.QPushButton("Ne",parent=self.dialog)
        
        self.dialog.btn1.resize(self.dialog.btn1.sizeHint())
        self.dialog.btn1.clicked.connect(self.dialog.reject)
        
        grid=QtGui.QGridLayout()
        grid.addWidget(self.dialog.lbl,0,0,1,0)
        grid.addWidget(self.dialog.btn,1,0)
        grid.addWidget(self.dialog.btn1,1,1)
        
        self.dialog.setLayout(grid)
        
        
    def exit_(self):
            self.dialogs()
            if self.dialog.exec_():
                self.close()
            else:
                self.dialog.close()
            
        
if __name__=="__main__":
    app= QtGui.QApplication(sys.argv)
    okno=Ui()
    sys.exit(app.exec_())
        
