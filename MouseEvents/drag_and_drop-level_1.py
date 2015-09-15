# -*- coding: utf-8 -*-
"""
Je potřeba nejdříve se kouknout na vykreslování přes QPainter
"""

import sys
from PyQt4.QtGui import QWidget, QPainter, QPen, QApplication, QColor, QMouseEvent, QBrush
from PyQt4.QtCore import QRectF, QPointF, QSizeF

# naše upravená třída, kde si tahame
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # na pozici [0, 0] se šířkou 50px  a výškou 50px
        # musíme ho vykreslit my, protože je to pouze abstraktní objekt (abstrakní ve smyslu, že nám pouze uchovává data a poskytuje potřebné výpočty)
        self.__drag_and_drop_rect = QRectF(QPointF(), QSizeF(50, 50))
        self.__rect_color = QColor("red")
        self.__mouse_pressed = False

    def paintEvent(self, _):
        """
        :type _: QPaintEvent
        """

        painter = QPainter(self)
        painter.setBrush(QBrush(self.__rect_color))
        painter.setPen(QPen(self.__rect_color))
        painter.drawRect(self.__drag_and_drop_rect)

    def mousePressEvent(self, mouse_event):
        """
        :type mouse_event: QMouseEvent
        """

        # je v bod kliknutí v obdelníku?
        self.__mouse_pressed = self.__drag_and_drop_rect.contains(mouse_event.pos())

    def mouseReleaseEvent(self, _):
        """
        :type _: QMouseEvent
        """

        self.__mouse_pressed = False

    def mouseMoveEvent(self, mouse_event):
        """
        :type mouse_event: QMouseEvent
        """

        if not self.__mouse_pressed:
            return

        # přesuň obdelník na pozici kurzoru
        self.__drag_and_drop_rect.moveTo(mouse_event.pos())
        # obnov okno(zavolá se metoda paintEvent)
        self.update()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())