"""
文件名: tray_icon.py
版本: 1.2
用途: 实现一个系统托盘图标应用，允许用户通过滑动条调节屏幕亮度、色温和色温透明度，并提供退出应用的选项。
作者: 好吃的秋梨膏
更新日期: 2024-6-4
"""
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QSlider, QLabel, QHBoxLayout, QWidgetAction, QAction, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import logging
from app.brightness_control import BrightnessControl
from app.color_temperature_control import ColorTemperatureControl
from config import ICON_PATH, STYLE_PATH


class TrayIcon(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(str(ICON_PATH)))
        self.menu = QMenu()

        # 初始化亮度控制相关组件
        brightness_layout = QHBoxLayout()
        brightness_label = QLabel("亮度调节:")
        brightness_layout.addWidget(brightness_label)
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setRange(0, 100)
        self.brightness_slider.setValue(0)
        self.brightness_slider.valueChanged.connect(self.change_brightness)
        self.brightness_value_label = QLabel("0%")
        self.brightness_value_label.setAlignment(Qt.AlignCenter)
        self.brightness_value_label.setFixedWidth(40)
        brightness_layout.addWidget(self.brightness_slider)
        brightness_layout.addWidget(self.brightness_value_label)
        brightness_widget = QWidget()
        brightness_widget.setLayout(brightness_layout)
        self.brightnessAction = QWidgetAction(self.menu)
        self.brightnessAction.setDefaultWidget(brightness_widget)
        self.menu.addAction(self.brightnessAction)

        # 初始化色温控制相关组件
        temperature_layout = QHBoxLayout()
        temperature_label = QLabel("色温调节:")
        temperature_layout.addWidget(temperature_label)
        self.temperature_slider = QSlider(Qt.Horizontal)
        self.temperature_slider.setRange(2000, 6500)  # 将色温范围改为2000K到6000K
        self.temperature_slider.setValue(4000)  # 默认为4000K
        self.temperature_slider.valueChanged.connect(self.change_color_temperature)
        self.temperature_value_label = QLabel("4000K")  # 初始标签值也改为4000K
        self.temperature_value_label.setAlignment(Qt.AlignCenter)
        self.temperature_value_label.setFixedWidth(60)
        temperature_layout.addWidget(self.temperature_slider)
        temperature_layout.addWidget(self.temperature_value_label)
        temperature_widget = QWidget()
        temperature_widget.setLayout(temperature_layout)
        self.temperatureAction = QWidgetAction(self.menu)
        self.temperatureAction.setDefaultWidget(temperature_widget)
        self.menu.addAction(self.temperatureAction)

        # 初始化透明度控制相关组件
        alpha_layout = QHBoxLayout()
        alpha_label = QLabel("色温透明度:")
        alpha_layout.addWidget(alpha_label)
        self.alpha_slider = QSlider(Qt.Horizontal)
        self.alpha_slider.setRange(0, 100)
        self.alpha_slider.setValue(5)
        self.alpha_slider.valueChanged.connect(self.change_alpha)
        self.alpha_value_label = QLabel("5%")
        self.alpha_value_label.setAlignment(Qt.AlignCenter)
        self.alpha_value_label.setFixedWidth(40)
        alpha_layout.addWidget(self.alpha_slider)
        alpha_layout.addWidget(self.alpha_value_label)
        alpha_widget = QWidget()
        alpha_widget.setLayout(alpha_layout)
        self.alphaAction = QWidgetAction(self.menu)
        self.alphaAction.setDefaultWidget(alpha_widget)
        self.menu.addAction(self.alphaAction)

        # 初始化退出操作相关组件
        self.quitAction = QAction("退出", self)
        self.quitAction.triggered.connect(self.exit)
        self.menu.addAction(self.quitAction)

        self.setContextMenu(self.menu)
        self.show()

        self.brightnessControl = BrightnessControl()
        self.brightnessControl.show()

        self.colorTemperatureControl = ColorTemperatureControl()
        self.colorTemperatureControl.show()

        self.loadStyles()

    def loadStyles(self):
        try:
            with open(STYLE_PATH, "r") as fh:
                self.menu.setStyleSheet(fh.read())
        except Exception as e:
            logging.error(f"Error loading styles: {e}")

    def change_brightness(self, value):
        self.brightnessControl.brightness = value
        self.brightnessControl.updateBrightness()
        self.brightness_value_label.setText(f"{value}%")
        logging.debug(f"Brightness changed to {value}%")

    def change_color_temperature(self, value):
        self.colorTemperatureControl.colorTemperature = value
        self.colorTemperatureControl.updateColorTemperature()
        self.temperature_value_label.setText(f"{value}K")
        logging.debug(f"Color temperature changed to {value}K")

    def change_alpha(self, value):
        self.colorTemperatureControl.alpha = value
        self.colorTemperatureControl.updateColorTemperature()
        self.alpha_value_label.setText(f"{value}%")
        logging.debug(f"Alpha changed to {value}%")

    def exit(self):
        logging.info("Exiting application")
        QApplication.quit()
