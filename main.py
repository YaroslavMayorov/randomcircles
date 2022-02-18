import sys
from random import randint
from UI import Ui_Form

from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class Calc(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.paint)
        self.flag = False
        self.circles = []

    def paintEvent(self, event):
        QWidget.paintEvent(self, event)
        if self.flag:
            painter = QPainter(self)
            pen = QPen()  # creates a default pen
            pen.setStyle(Qt.SolidLine)
            pen.setWidth(3)
            x = randint(0, 610)
            y = randint(0, 390)
            w = randint(30, 600)
            while x + w > 640 or y + w > 420:
                x = randint(0, 610)
                y = randint(0, 390)
                w = randint(30, 600)
            self.circles.append(x)
            self.circles.append(y)
            self.circles.append(w)
            r = randint(10, 255)
            g = randint(10, 255)
            b = randint(10, 255)
            self.circles.append(r)
            self.circles.append(g)
            self.circles.append(b)
            for i in range(0, len(self.circles), 6):
                tmp = self.circles[i + 2]
                pen.setBrush(QColor(self.circles[i + 3], self.circles[i + 4], self.circles[i + 5]))
                painter.setPen(pen)
                painter.drawEllipse(self.circles[i], self.circles[i + 1], tmp, tmp)
            self.flag = False

    def paint(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc()
    ex.show()
    sys.exit(app.exec())
