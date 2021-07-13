"""
# coding:utf-8
@Time    : 2021/07/13
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : run.py
@Desc    : run
@Software: PyCharm
"""
from src.controller.main_frame import MainFrame
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainFrame()
    win.setWindowTitle('iRedis Beta Version 1.0.0')
    win.show()
    sys.exit(app.exec_())
