# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_Add_Case.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopUp_Add_Case(object):
    def setupUi(self, PopUp_Add_Case):
        PopUp_Add_Case.setObjectName("PopUp_Add_Case")
        PopUp_Add_Case.resize(553, 607)
        self.centralwidget = QtWidgets.QWidget(PopUp_Add_Case)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Caliber_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Caliber_LBL.setObjectName("Caliber_LBL")
        self.gridLayout.addWidget(self.Caliber_LBL, 2, 0, 1, 1)
        self.Name_TB = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.Name_TB.setObjectName("Name_TB")
        self.gridLayout.addWidget(self.Name_TB, 0, 1, 1, 1)
        self.Manufacturer_TB = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.Manufacturer_TB.setObjectName("Manufacturer_TB")
        self.gridLayout.addWidget(self.Manufacturer_TB, 1, 1, 1, 1)
        self.Manufacturer_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Manufacturer_LBL.setObjectName("Manufacturer_LBL")
        self.gridLayout.addWidget(self.Manufacturer_LBL, 1, 0, 1, 1)
        self.Name_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Name_LBL.setObjectName("Name_LBL")
        self.gridLayout.addWidget(self.Name_LBL, 0, 0, 1, 1)
        self.Caliber_TB = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.Caliber_TB.setObjectName("Caliber_TB")
        self.gridLayout.addWidget(self.Caliber_TB, 2, 1, 1, 1)
        self.PrimerSize_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PrimerSize_LBL.setObjectName("PrimerSize_LBL")
        self.gridLayout.addWidget(self.PrimerSize_LBL, 3, 0, 1, 1)
        self.PrimerSize_TB = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.PrimerSize_TB.setObjectName("PrimerSize_TB")
        self.gridLayout.addWidget(self.PrimerSize_TB, 3, 1, 1, 1)
        self.AddCase_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.AddCase_BTN.setGeometry(QtCore.QRect(420, 570, 113, 32))
        self.AddCase_BTN.setObjectName("AddCase_BTN")
        PopUp_Add_Case.setCentralWidget(self.centralwidget)

        self.retranslateUi(PopUp_Add_Case)
        QtCore.QMetaObject.connectSlotsByName(PopUp_Add_Case)

    def retranslateUi(self, PopUp_Add_Case):
        _translate = QtCore.QCoreApplication.translate
        PopUp_Add_Case.setWindowTitle(_translate("PopUp_Add_Case", "MainWindow"))
        self.Caliber_LBL.setText(_translate("PopUp_Add_Case", "Caliber"))
        self.Manufacturer_LBL.setText(_translate("PopUp_Add_Case", "Manufacturer"))
        self.Name_LBL.setText(_translate("PopUp_Add_Case", "Name"))
        self.PrimerSize_LBL.setText(_translate("PopUp_Add_Case", "Primer Size"))
        self.AddCase_BTN.setText(_translate("PopUp_Add_Case", "Add Case"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopUp_Add_Case = QtWidgets.QMainWindow()
    ui = Ui_PopUp_Add_Case()
    ui.setupUi(PopUp_Add_Case)
    PopUp_Add_Case.show()
    sys.exit(app.exec_())