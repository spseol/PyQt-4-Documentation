# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 14:53:20 2014

@author: Adam
"""

import sys
from PyQt4 import QtGui, QtCore


class Main_Window(QtGui.QWidget,):

    def __init__(self,):
        super(Main_Window, self).__init__()
        self.Setup_Ui()

    def Setup_Ui(self):
        QtGui.QToolTip.setFont(QtGui.QFont("Arial", 10))

        self.lbl = QtGui.QLabel(parent=self)

        btn = QtGui.QPushButton("klikni", self)
        btn.resize(btn.sizeHint())
        btn.setToolTip("tlacitko slouzici na zobrazeni textu")
        btn.clicked.connect(self.text)

        grid = QtGui.QGridLayout()
        grid.addWidget(self.lbl, 0, 0)
        grid.addWidget(btn, 1, 0)

        self.setLayout(grid)
        self.setWindowTitle("Tlacitko")
        self.show()

    def text(self):
        self.lbl.setText('klikl jste')
        self.lbl.resize(self.lbl.sizeHint())
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    okno = Main_Window()
    sys.exit(app.exec_())
