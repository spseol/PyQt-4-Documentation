# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 21:19:09 2014

@author: Adam
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In the example, we draw randomly 1000 red points 
on the window.

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

import sys
from PyQt4 import QtGui, QtCore

class Drawing(QtGui.QWidget):
    def __init__(self):
        super(Drawing,self).__init__()
        
        self.setup()


    def setup(self):
         self.setGeometry(300, 300, 350, 300)
         self.setWindowTitle("Lines")
         self.show()
    
    
    def paintEvent(self,e):
        self.painter=QtGui.QPainter()
        self.painter.begin(self)
        self.draw()
                
        
        self.painter.end()
    
    def draw(self):
        pen=QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        
        
        pen.setColor(QtGui.QColor(100,100,100))
        
        pen.setStyle(QtCore.Qt.SolidLine)
        self.painter.setPen(pen)        
        self.painter.drawLine(10,10,340,10)


        pen.setStyle(QtCore.Qt.DashLine)
        self.painter.setPen(pen)
        self.painter.drawLine(10,30,340,30)
        
        pen.setStyle(QtCore.Qt.DashDotDotLine)
        self.painter.setPen(pen)
        self.painter.drawLine(10,50,340,50)
        
        pen.setStyle(QtCore.Qt.DashDotLine)
        self.painter.setPen(pen)
        self.painter.drawLine(10,70,340,70)
        
        pen.setStyle(QtCore.Qt.DotLine)
        self.painter.setPen(pen)
        self.painter.drawLine(10,90,340,90)
        
        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1,2,3,4,5,6,])        
        self.painter.setPen(pen)
        self.painter.drawLine(10,110,340,110)
        
        pen.setStyle(QtCore.Qt.NoPen)
        self.painter.setPen(pen)
        self.painter.setBrush(QtGui.QColor(255, 0, 0))
        self.painter.drawRect(10, 130, 90, 60)

        self.painter.setBrush(QtGui.QColor(0, 255, 0,))
        self.painter.drawRect(130, 130, 90, 60)

        self.painter.setBrush(QtGui.QColor(0, 0, 255,))
        self.painter.drawRect(250, 130, 90, 60)
        self.painter.drawEllipse(130,200,90,60)
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    
    ex = Drawing()
    
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
