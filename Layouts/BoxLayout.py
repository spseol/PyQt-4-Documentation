# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 15:01:22 2014

@author: edith
"""

from PyQt4 import QtGui
import sys

class Ui(QtGui.QWidget):
    def __init__(self):
        super(Ui,self).__init__()
        
        self.setup()
    
    def setup(self):
        btn_ok_hor = QtGui.QPushButton("ok",)
        btn_cancel_hor = QtGui.QPushButton("cancel",)
        
        hbox = QtGui.QHBoxLayout()
        
        hbox.addWidget(btn_ok_hor)
        hbox.addWidget(btn_cancel_hor)
        
        btn_ok_ver = QtGui.QPushButton("ok",)
        btn_cancel_ver = QtGui.QPushButton("cancel",)
        
        vbox = QtGui.QVBoxLayout()
        
        vbox.addWidget(btn_ok_ver)
        vbox.addWidget(btn_cancel_ver)
        
        grid=QtGui.QGridLayout()
        grid.addLayout(vbox,0,0)
        grid.addLayout(hbox,3,3)
        
        self.setLayout(grid)
        self.move(200,300)
        self.show()
        
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    okno=Ui()
    sys.exit(app.exec_())