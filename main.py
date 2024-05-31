import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QSlider, QWidget, QVBoxLayout, QWidgetAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter, QColor

"""
文件名: main.py
版本: 1.0
用途: 使用PyQt5创建一个系统托盘应用程序，通过托盘图标上的滑块来控制屏幕亮度。
作者: 好吃的秋梨膏
更新日期: 2024-6-1
"""
class BrightnessControl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置无边框窗口并始终置顶
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, True)

        # 设置窗口透明度初始值和覆盖整个屏幕
        self.setGeometry(0, 0, QApplication.primaryScreen().size().width(),
                         QApplication.primaryScreen().size().height())
        self.brightness = 0
        self.updateBrightness()

    def updateBrightness(self):
        # 计算透明度值
        self.repaint()
        print(f"Setting brightness to: {self.brightness}%")  # 调试信息

    def paintEvent(self, event):
        # 绘制半透明黑色背景
        painter = QPainter(self)
        color = QColor(0, 0, 0)
        color.setAlphaF(self.brightness / 100.0)
        painter.fillRect(self.rect(), color)


class TrayIcon(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("bg.png"))

        self.menu = QMenu()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.change_brightness)

        self.sliderAction = QWidgetAction(self.menu)
        self.sliderAction.setDefaultWidget(self.slider)
        self.menu.addAction(self.sliderAction)

        self.quitAction = QAction("退出", self)
        self.quitAction.triggered.connect(self.exit)
        self.menu.addAction(self.quitAction)

        self.setContextMenu(self.menu)
        self.show()

        self.brightnessControl = BrightnessControl()
        self.brightnessControl.show()

    def change_brightness(self, value):
        self.brightnessControl.brightness = value
        self.brightnessControl.updateBrightness()

    def exit(self):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    trayIcon = TrayIcon()
    sys.exit(app.exec_())
