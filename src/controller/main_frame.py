"""
# coding:utf-8
@Time    : 2021/07/13
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : main_frame.py
@Desc    : main_frame
@Software: PyCharm
"""
from src.view.mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from redis import Redis


class MainFrame(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainFrame, self).__init__()
        self.setupUi(self)
        self.init_slot()
        self.host_port_lineEdit.setText('6379')
        self.host_ip_lineEdit.setText('127.0.0.1')
        self.rd = None

    def init_slot(self):
        self.connect_pushButton.clicked.connect(self.connect_redis)

    def connect_redis(self):
        ip = self.host_ip_lineEdit.text()
        port = self.host_port_lineEdit.text()
        db_name = self.dbname_lineEdit.text()
        if db_name:
            rd = Redis(host=ip, port=port, db=db_name)
        else:
            rd = Redis(host=ip, port=port)

        self.rd = rd
        for key in self.rd.keys():
            print(key)
