import smenarnaGUI
import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow,):
    def __init__(self):
        super(Window, self).__init__()
        self.app = smenarnaGUI.Ui_MainWindow()
        self.app.setupUi(self)
        self.show()
        self.mena = {u"JPY": (20.40, 21.20, 100),
                     u"GBP": (36.80, 37.60, 1),
                     u"USD": (24.60, 25.30, 1),
                     u"EUR": (27.00, 27.60, 1),
                     u"CAD": (19.60, 20.30, 1),
                     }

    def Kurz(self):
        self.pressed = str(self.sender().text())
        mena = self.mena[str(self.sender().text())]
        if self.app.nakup.isChecked():
            self.app.kurz.setText(str(mena[0]))
        else:
            self.app.kurz.setText(str(mena[1]))
        self.app.pocet.setText(str(mena[2]))

    def Vypocet(self):
        mena = self.mena[self.pressed]
        if self.app.nakup.isChecked():
            self.app.Vysledek.setText(str(mena[0]*float(self.app.entry.text())))
        else:
            self.app.Vysledek.setText(str(mena[1]*float(self.app.entry.text())))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    exp = Window()
    sys.exit(app.exec_())
