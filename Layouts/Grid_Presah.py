# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 15:47:27 2014

@author: edith
"""

from PyQt4 import QtGui
import sys

class Ui(QtGui.QWidget):
    def __init__(self):
        super(Ui,self).__init__()
        
        self.setup()
        
    def setup(self):
        
        grid= QtGui.QGridLayout()
        j=1
        for sloupce in range(2):
            for rady in range(2):
                button= QtGui.QLineEdit()
                grid.addWidget(button,sloupce,rady)
                j+=1
        
        button= QtGui.QTextEdit()
        
        grid.addWidget(button,0,2,2,2)
        
        self.setLayout(grid)
        self.move(200,300)
        self.show()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    okno=Ui()
    sys.exit(app.exec_())