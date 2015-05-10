# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 14:11:19 2014

@author: edith
"""

from PyQt4 import QtGui
import sys


class Ui(QtGui.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        self.setup()

    def setup(self):
        grid = QtGui.QGridLayout()
        j = 1
        tlacitka = []
        for radek in range(4):
            for sloupec in range(5):
                tlacitka.append(QtGui.QPushButton(str(j)))
                grid.addWidget(tlacitka[-1], radek, sloupec)
                j += 1
        self.move(200, 300)
        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    okno = Ui()
    sys.exit(app.exec_())
