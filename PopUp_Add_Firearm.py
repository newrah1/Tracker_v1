# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_Add_Firearm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopUp_Add_Firearm(object):
    def setupUi(self, PopUp_Add_Firearm):
        PopUp_Add_Firearm.setObjectName("PopUp_Add_Firearm")
        PopUp_Add_Firearm.resize(1373, 825)
        PopUp_Add_Firearm.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(PopUp_Add_Firearm)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1161, 772))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Size_Inch_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Size_Inch_LBL.setObjectName("Size_Inch_LBL")
        self.gridLayout.addWidget(self.Size_Inch_LBL, 2, 0, 1, 1)
        self.Caliber_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Caliber_LBL.setObjectName("Caliber_LBL")
        self.gridLayout.addWidget(self.Caliber_LBL, 7, 0, 1, 1)
        self.Bullet_Base_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Bullet_Base_LBL.setObjectName("Bullet_Base_LBL")
        self.gridLayout.addWidget(self.Bullet_Base_LBL, 8, 0, 1, 1)
        self.SKU_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.SKU_LBL.setObjectName("SKU_LBL")
        self.gridLayout.addWidget(self.SKU_LBL, 6, 0, 1, 1)
        self.Size_mm_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Size_mm_LBL.setObjectName("Size_mm_LBL")
        self.gridLayout.addWidget(self.Size_mm_LBL, 3, 0, 1, 1)
        self.BC_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.BC_LBL.setObjectName("BC_LBL")
        self.gridLayout.addWidget(self.BC_LBL, 9, 0, 1, 1)
        self.Notes_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Notes_LBL.setObjectName("Notes_LBL")
        self.gridLayout.addWidget(self.Notes_LBL, 24, 0, 1, 1)
        self.Weight_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Weight_LBL.setObjectName("Weight_LBL")
        self.gridLayout.addWidget(self.Weight_LBL, 4, 0, 1, 1)
        self.Type_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Type_LBL.setObjectName("Type_LBL")
        self.gridLayout.addWidget(self.Type_LBL, 5, 0, 1, 1)
        self.Lengh_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Lengh_LBL.setObjectName("Lengh_LBL")
        self.gridLayout.addWidget(self.Lengh_LBL, 10, 0, 1, 1)
        self.Manufacturer_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Manufacturer_LBL.setObjectName("Manufacturer_LBL")
        self.gridLayout.addWidget(self.Manufacturer_LBL, 1, 0, 1, 1)
        self.Name_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Name_LBL.setObjectName("Name_LBL")
        self.gridLayout.addWidget(self.Name_LBL, 0, 0, 1, 1)
        self.Picture_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Picture_LBL.setObjectName("Picture_LBL")
        self.gridLayout.addWidget(self.Picture_LBL, 25, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 26, 1, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout.addWidget(self.textEdit_6, 5, 1, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.textEdit_4, 3, 1, 1, 1)
        self.textEdit_8 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_8.setObjectName("textEdit_8")
        self.gridLayout.addWidget(self.textEdit_8, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout.addWidget(self.textEdit_5, 4, 1, 1, 1)
        self.textEdit_11 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_11.setObjectName("textEdit_11")
        self.gridLayout.addWidget(self.textEdit_11, 10, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1)
        self.textEdit_9 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_9.setObjectName("textEdit_9")
        self.gridLayout.addWidget(self.textEdit_9, 8, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 2, 1, 1, 1)
        self.textEdit_12 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_12.setObjectName("textEdit_12")
        self.gridLayout.addWidget(self.textEdit_12, 11, 1, 1, 1)
        self.textEdit_7 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout.addWidget(self.textEdit_7, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 11, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 2, 1, 1)
        self.textEdit_10 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_10.setObjectName("textEdit_10")
        self.gridLayout.addWidget(self.textEdit_10, 9, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 10, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 11, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 9, 2, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.textEdit_13 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_13.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_13.setObjectName("textEdit_13")
        self.gridLayout.addWidget(self.textEdit_13, 0, 3, 1, 1)
        self.textEdit_14 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_14.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_14.setObjectName("textEdit_14")
        self.gridLayout.addWidget(self.textEdit_14, 1, 3, 1, 1)
        self.textEdit_15 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_15.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_15.setObjectName("textEdit_15")
        self.gridLayout.addWidget(self.textEdit_15, 2, 3, 1, 1)
        self.textEdit_16 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_16.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_16.setObjectName("textEdit_16")
        self.gridLayout.addWidget(self.textEdit_16, 3, 3, 1, 1)
        self.textEdit_17 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_17.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_17.setObjectName("textEdit_17")
        self.gridLayout.addWidget(self.textEdit_17, 4, 3, 1, 1)
        self.textEdit_18 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_18.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_18.setObjectName("textEdit_18")
        self.gridLayout.addWidget(self.textEdit_18, 5, 3, 1, 1)
        self.textEdit_19 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_19.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_19.setObjectName("textEdit_19")
        self.gridLayout.addWidget(self.textEdit_19, 6, 3, 1, 1)
        self.textEdit_20 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_20.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_20.setObjectName("textEdit_20")
        self.gridLayout.addWidget(self.textEdit_20, 7, 3, 1, 1)
        self.textEdit_21 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_21.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_21.setObjectName("textEdit_21")
        self.gridLayout.addWidget(self.textEdit_21, 8, 3, 1, 1)
        self.textEdit_22 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_22.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_22.setObjectName("textEdit_22")
        self.gridLayout.addWidget(self.textEdit_22, 9, 3, 1, 1)
        self.textEdit_23 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_23.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_23.setObjectName("textEdit_23")
        self.gridLayout.addWidget(self.textEdit_23, 10, 3, 1, 1)
        self.textEdit_24 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_24.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_24.setObjectName("textEdit_24")
        self.gridLayout.addWidget(self.textEdit_24, 11, 3, 1, 1)
        self.textEdit_25 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_25.setMaximumSize(QtCore.QSize(16777215, 300))
        self.textEdit_25.setObjectName("textEdit_25")
        self.gridLayout.addWidget(self.textEdit_25, 24, 1, 1, 1)
        self.textEdit_26 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_26.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_26.setObjectName("textEdit_26")
        self.gridLayout.addWidget(self.textEdit_26, 25, 1, 1, 1)
        self.AddFirearm_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.AddFirearm_BTN.setGeometry(QtCore.QRect(1010, 780, 171, 32))
        self.AddFirearm_BTN.setObjectName("AddFirearm_BTN")
        PopUp_Add_Firearm.setCentralWidget(self.centralwidget)

        self.retranslateUi(PopUp_Add_Firearm)
        QtCore.QMetaObject.connectSlotsByName(PopUp_Add_Firearm)

    def retranslateUi(self, PopUp_Add_Firearm):
        _translate = QtCore.QCoreApplication.translate
        PopUp_Add_Firearm.setWindowTitle(_translate("PopUp_Add_Firearm", "MainWindow"))
        self.Size_Inch_LBL.setText(_translate("PopUp_Add_Firearm", "Name"))
        self.Caliber_LBL.setText(_translate("PopUp_Add_Firearm", "Barrel Length"))
        self.Bullet_Base_LBL.setText(_translate("PopUp_Add_Firearm", "Weight"))
        self.SKU_LBL.setText(_translate("PopUp_Add_Firearm", "Overall Length"))
        self.Size_mm_LBL.setText(_translate("PopUp_Add_Firearm", "Manufacturer"))
        self.BC_LBL.setText(_translate("PopUp_Add_Firearm", "Action Type"))
        self.Notes_LBL.setText(_translate("PopUp_Add_Firearm", "Notes"))
        self.Weight_LBL.setText(_translate("PopUp_Add_Firearm", "Model"))
        self.Type_LBL.setText(_translate("PopUp_Add_Firearm", "Caliber"))
        self.Lengh_LBL.setText(_translate("PopUp_Add_Firearm", "Twist Rate"))
        self.Manufacturer_LBL.setText(_translate("PopUp_Add_Firearm", "SKU"))
        self.Name_LBL.setText(_translate("PopUp_Add_Firearm", "Type"))
        self.Picture_LBL.setText(_translate("PopUp_Add_Firearm", "Picture"))
        self.label_3.setText(_translate("PopUp_Add_Firearm", "Slot 2"))
        self.label_2.setText(_translate("PopUp_Add_Firearm", "Slot 1"))
        self.label_5.setText(_translate("PopUp_Add_Firearm", "Slot 4"))
        self.label_7.setText(_translate("PopUp_Add_Firearm", "Slot 6"))
        self.label_4.setText(_translate("PopUp_Add_Firearm", "Slot 3"))
        self.label_6.setText(_translate("PopUp_Add_Firearm", "Slot 5"))
        self.label.setText(_translate("PopUp_Add_Firearm", "Thread Size"))
        self.label_9.setText(_translate("PopUp_Add_Firearm", "Slot 8"))
        self.label_10.setText(_translate("PopUp_Add_Firearm", "Slot 9"))
        self.label_8.setText(_translate("PopUp_Add_Firearm", "Slot 7"))
        self.label_12.setText(_translate("PopUp_Add_Firearm", "Slot 11"))
        self.label_13.setText(_translate("PopUp_Add_Firearm", "Slot 12"))
        self.label_11.setText(_translate("PopUp_Add_Firearm", "Slot 10"))
        self.AddFirearm_BTN.setText(_translate("PopUp_Add_Firearm", "Add Firearm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopUp_Add_Firearm = QtWidgets.QMainWindow()
    ui = Ui_PopUp_Add_Firearm()
    ui.setupUi(PopUp_Add_Firearm)
    PopUp_Add_Firearm.show()
    sys.exit(app.exec_())
