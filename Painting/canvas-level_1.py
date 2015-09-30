import sys
from PyQt4.QtGui import QWidget, QPainter, QPen, QApplication, QColor

# naše upravená třída, kde si čmrkáme
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

    # v C++ virtuální metoda, paint_event pouze obsahuje oblast obnovení
    def paintEvent(self, paint_event):
        # nastavíme pero na červenou barvu se šířkou 3px
        pen = QPen(QColor("red"))
        pen.setWidth(3)

        painter = QPainter(self)
        painter.setPen(pen)

        # drawLine(x1, y1, x2, y2)
        painter.drawLine(0, 0, 100, 100)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
