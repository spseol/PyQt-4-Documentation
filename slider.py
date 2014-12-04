# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 23:06:56 2014

@author: Adam
"""
from PyQt4 import QtGui,QtCore
import sys
class changer(QtGui.QWidget):
    def __init__(self):
        super(changer,self).__init__()
        
        self.setup()
    
    def setup(self):
        self.grid=QtGui.QGridLayout()
        self.rect=QtGui.QSpacerItem(100,50, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        print self.rect.geometry()
                
       
        self.red=QtGui.QLabel(self)
        self.grid.addWidget(self.red,2,0)
        
        self.blue=QtGui.QLabel(self)
        self.grid.addWidget(self.blue,2,2)
        
        self.green=QtGui.QLabel(self)
        self.grid.addWidget(self.green,2,1)
        
        self.setWindowTitle("slider")
        
        self.slider=QtGui.QSlider(parent=self)
        self.slider.setMaximum(255)
        self.slider.setMinimum(0)
        
        self.slider.valueChanged.connect(self.paintEvent)
        self.slider2=QtGui.QSlider(parent=self)
        self.slider2.setMaximum(255)
        self.slider2.setMinimum(0)        
    
        self.slider2.valueChanged.connect(self.paintEvent)
        self.slider3=QtGui.QSlider(parent=self)

        self.slider3.setMaximum(255)
        self.slider3.setMinimum(0)
        
        self.slider3.valueChanged.connect(self.paintEvent)
        self.grid.addWidget(self.slider,0,0)
        self.grid.addWidget(self.slider2,0,1)
        self.grid.addWidget(self.slider3,0,2)
        self.grid.addItem(QtGui.QSpacerItem(0,10),1,1)
        self.grid.addItem(QtGui.QSpacerItem(0,10),4,1)
        self.grid.addItem(self.rect,5,0,1,3)
        
        self.setLayout(self.grid)
        self.show()
        
    def paintEvent(self,e):
        self.painter=QtGui.QPainter()
        
        self.red.setText(str(self.slider.value()))
        self.green.setText(str(self.slider2.value()))
        self.blue.setText(str(self.slider3.value()))
        self.painter.begin(self)
        pen=QtGui.QPen()
        pen.setStyle(QtCore.Qt.NoPen)
        self.painter.setPen(pen)
        self.painter.setBrush(QtGui.QColor(self.slider.value(),self.slider2.value(),self.slider3.value()))
        
        self.painter.drawRect(self.rect.geometry())
        self.painter.end()        
        self.update() 
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = changer()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
        