"""
文件名: main.py
版本: 1.2
用途: 使用PyQt5创建一个系统托盘应用程序，通过托盘图标上的滑块来控制屏幕亮度。
作者: 好吃的秋梨膏
更新日期: 2024-6-4
"""

import sys
import logging
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from app.tray_icon import TrayIcon
from config import ROOT_DIR

# 配置日志记录
log_file = ROOT_DIR / 'app.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    try:
        trayIcon = TrayIcon()
        sys.exit(app.exec_())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)
