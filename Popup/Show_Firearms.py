# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_ShowAllFirearms.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from configparser import ConfigParser
import mysql.connector
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from Tracker import Ui_MainWindow

class Ui_ShowFirearms(object):
    def __init__(self):
        conn = sqlite3.connect("./DATABASE/TrackerDB.db")
        print("Opened database successfully")

        sql = "SELECT * from firearm"
        cursor = conn.cursor()
        cursor.execute(sql)
        self.conn = sqlite3.connect("./DATABASE/TrackerDB.db")
        self.firearm_df = pd.read_sql("SELECT * FROM Firearm", self.conn)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 825)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ShowAllFirearms = QtWidgets.QTextBrowser(self.centralwidget)
        self.ShowAllFirearms.setText(self.firearm_df['Name'].to_string(index=False))
        self.ShowAllFirearms.setFont(QFont('Times', 20))
        self.ShowAllFirearms.setGeometry(QtCore.QRect(10, 10, 771, 781))
        self.ShowAllFirearms.setAccessibleName("")
        self.ShowAllFirearms.setObjectName("ShowAllFirearms")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
