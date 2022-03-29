# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_ShowAllFirearms.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtWidgets
import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtGui import *

class Ui_ShowBullets(object):
    def __init__(self):
        conn = sqlite3.connect("./DATABASE/TrackerDB.db")

        sql = "SELECT * from bullet"
        cursor = conn.cursor()
        cursor.execute(sql)
        self.conn = sqlite3.connect("./DATABASE/TrackerDB.db")
        self.bullet_df = pd.read_sql("SELECT * FROM bullet", self.conn)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 825)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ShowAllBullets = QtWidgets.QTextBrowser(self.centralwidget)
        # query db and display in window
        self.ShowAllBullets.setText(self.bullet_df['Name'].to_string(index=False))
        self.ShowAllBullets.setFont(QFont('Times', 15))
        self.ShowAllBullets.setGeometry(QtCore.QRect(10, 10, 771, 781))
        self.ShowAllBullets.setAccessibleName("")
        self.ShowAllBullets.setObjectName("ShowAllBullets")
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
    ui = Ui_ShowBullets()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
