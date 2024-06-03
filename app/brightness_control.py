"""
文件名: brightness_control.py
版本: 1.2
用途: 实现了一个无边框、全屏覆盖的小部件，用于通过改变透明度来调整屏幕亮度。
作者: 好吃的秋梨膏
更新日期: 2024-6-4
"""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

class BrightnessControl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setGeometry(0, 0, QApplication.primaryScreen().size().width(),
                         QApplication.primaryScreen().size().height())
        self.brightness = 0
        self.updateBrightness()

    def updateBrightness(self):
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        color = QColor(0, 0, 0)
        color.setAlphaF(self.brightness / 100.0)
        painter.fillRect(self.rect(), color)