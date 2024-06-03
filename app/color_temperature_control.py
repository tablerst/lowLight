from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication


class ColorTemperatureControl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setGeometry(0, 0, QApplication.primaryScreen().size().width(),
                         QApplication.primaryScreen().size().height())
        self.colorTemperature = 4000  # 初始值改为4000K
        self.alpha = 10  # 透明度初始值改为10%
        self.updateColorTemperature()

    def updateColorTemperature(self):
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        r = int(max(0, min(255, 255 - (self.colorTemperature - 2000) / 16)))
        g = int(max(0, min(255, 255 - (self.colorTemperature - 2000) / 16)))
        b = int(max(0, min(255, 100 - (self.colorTemperature - 2000) / 32)))
        color = QColor(r, g, b)
        color.setAlphaF(self.alpha / 100.0)
        painter.fillRect(self.rect(), color)
