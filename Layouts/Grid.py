# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 14:11:19 2014

@author: edith
"""

from PyQt4 import QtGui
import sys

class Ui(QtGui.QWidget):
    def __init__(self):
        super(Ui,self).__init__()
        
        self.setup()
    
    def setup(self):
        cisla= (str(x) for x in range(1,17))
        
        pozice = [(x,y) for y in range(4) for x in range(4)]
        
        grid= QtGui.QGridLayout()
        j=0
        for x in cisla:
            
            button= QtGui.QPushButton(x)
            
            grid.addWidget(button, pozice[j][1],pozice[j][0])
            
            j+=1
        
        self.move(200,300)
        self.setLayout(grid)
        self.show()


if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    okno=Ui()
    sys.exit(app.exec_())