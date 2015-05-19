# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 19:22:28 2014

@author: Adam
"""

import sys
from PyQt4 import QtGui


class Main_Window(QtGui.QWidget):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.chk_box = QtGui.QCheckBox(self)
        self.chk_box.setText("potvrdte")
        self.chk_box.move(20, 30)

        self.lbl = QtGui.QLabel(parent=self)
        self.lbl.move(20, 30)

        btn = QtGui.QPushButton("kliknete", self)
        btn.clicked.connect(self.chk_state)
        btn.resize(btn.sizeHint())

        grid = QtGui.QGridLayout()
        grid.addWidget(btn, 0, 0)
        grid.addWidget(self.chk_box, 0, 1)
        grid.addWidget(self.lbl, 0, 2)

        self.setLayout(grid)
        self.setWindowTitle("chk_box")
        self.show()

    def chk_state(self):
        if self.chk_box.isChecked():
            self.lbl.setText("klikl jste")
            self.lbl.resize(self.lbl.sizeHint())
        else:
            self.lbl.setText("potvrdte tlacitko")
            self.lbl.resize(self.lbl.sizeHint())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    okno = Main_Window()
    sys.exit(app.exec_())
