# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_Add_Bullet.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopUp_Add_Bullet(object):
    def setupUi(self, PopUp_Add_Bullet):
        PopUp_Add_Bullet.setObjectName("PopUp_Add_Bullet")
        PopUp_Add_Bullet.resize(1359, 825)
        PopUp_Add_Bullet.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(PopUp_Add_Bullet)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1161, 772))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 27, 2, 1, 1)

        # Name
        self.Name_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Name_LBL.setObjectName("Name_LBL")
        self.gridLayout.addWidget(self.Name_LBL, 0, 0, 1, 1)
        self.Name_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Name_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Name_TE.setObjectName("Name_TE")
        self.gridLayout.addWidget(self.Name_TE, 0, 2, 1, 1)
        # Manufacturer
        self.Manufacturer_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Manufacturer_LBL.setObjectName("Manufacturer_LBL")
        self.gridLayout.addWidget(self.Manufacturer_LBL, 1, 0, 1, 1)
        self.Manufacturer_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Manufacturer_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Manufacturer_TE.setObjectName("Manufacturer_TE")
        self.gridLayout.addWidget(self.Manufacturer_TE, 1, 2, 1, 1)
        # Model
        self.ModelLBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ModelLBL.setObjectName("ModelLBL")
        self.gridLayout.addWidget(self.ModelLBL, 2, 0, 1, 1)
        # SKU

        # Notes
        self.Notes_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Notes_LBL.setObjectName("Notes_LBL")
        self.gridLayout.addWidget(self.Notes_LBL, 25, 0, 1, 1)
        self.Notes_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Notes_TE.setMaximumSize(QtCore.QSize(16777215, 300))
        self.Notes_TE.setObjectName("Notes_TE")
        self.gridLayout.addWidget(self.Notes_TE, 25, 2, 1, 1)
        # Picture
        self.Picture_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Picture_LBL.setObjectName("Picture_LBL")
        self.gridLayout.addWidget(self.Picture_LBL, 26, 0, 1, 1)
        self.Picture_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Picture_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Picture_TE.setObjectName("Picture_TE")
        self.gridLayout.addWidget(self.Picture_TE, 26, 2, 1, 1)
        # Slot 15
        self.Slot_15_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_15_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_15_TE.setObjectName("Slot_15_TE")
        self.gridLayout.addWidget(self.Slot_15_TE, 0, 4, 1, 1)
        self.Slot_15_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_15_LBL.setObjectName("Slot_15_LBL")
        self.gridLayout.addWidget(self.Slot_15_LBL, 0, 3, 1, 1)
        # Slot 16
        self.Slot_16_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_16_LBL.setObjectName("Slot_16_LBL")
        self.gridLayout.addWidget(self.Slot_16_LBL, 1, 3, 1, 1)
        self.Slot_16_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_16_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_16_TE.setObjectName("Slot_16_TE")
        self.gridLayout.addWidget(self.Slot_16_TE, 1, 4, 1, 1)






        # Type
        self.Type_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Type_LBL.setObjectName("Type_LBL")
        self.gridLayout.addWidget(self.Type_LBL, 7, 0, 1, 1)
        self.Type_TE_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Type_TE_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Type_TE_2.setObjectName("Type_TE_2")
        self.gridLayout.addWidget(self.Type_TE_2, 7, 2, 1, 1)
        self.Model_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Model_LBL.setObjectName("Model_LBL")
        self.gridLayout.addWidget(self.Model_LBL, 6, 0, 1, 1)
        self.Model_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Model_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Model_TE.setObjectName("Model_TE")
        self.gridLayout.addWidget(self.Model_TE, 6, 2, 1, 1)
        self.Size_mm_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Size_mm_LBL.setObjectName("Size_mm_LBL")
        self.gridLayout.addWidget(self.Size_mm_LBL, 5, 0, 1, 1)
        self.Size_mm_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Size_mm_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Size_mm_TE.setObjectName("Size_mm_TE")
        self.gridLayout.addWidget(self.Size_mm_TE, 5, 2, 1, 1)
        self.Size_Inch_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Size_Inch_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Size_Inch_TE.setObjectName("Size_Inch_TE")
        self.gridLayout.addWidget(self.Size_Inch_TE, 4, 2, 1, 1)
        self.Size_Inch_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Size_Inch_LBL.setObjectName("Size_Inch_LBL")
        self.gridLayout.addWidget(self.Size_Inch_LBL, 4, 0, 1, 1)
        self.Model_TE_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Model_TE_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Model_TE_2.setObjectName("Model_TE_2")
        self.gridLayout.addWidget(self.Model_TE_2, 2, 2, 1, 1)
        self.Slot_17_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_17_LBL.setObjectName("Slot_17_LBL")
        self.gridLayout.addWidget(self.Slot_17_LBL, 2, 3, 1, 1)
        self.Slot_17_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_17_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_17_TE.setObjectName("Slot_17_TE")
        self.gridLayout.addWidget(self.Slot_17_TE, 2, 4, 1, 1)
        self.SKU_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.SKU_LBL.setObjectName("SKU_LBL")
        self.gridLayout.addWidget(self.SKU_LBL, 3, 0, 1, 1)
        self.SKU_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.SKU_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.SKU_TE.setObjectName("SKU_TE")
        self.gridLayout.addWidget(self.SKU_TE, 3, 2, 1, 1)
        self.Caliber_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Caliber_LBL.setObjectName("Caliber_LBL")
        self.gridLayout.addWidget(self.Caliber_LBL, 8, 0, 1, 1)
        self.BaseLBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.BaseLBL.setObjectName("BaseLBL")
        self.gridLayout.addWidget(self.BaseLBL, 9, 0, 1, 1)
        self.BC_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.BC_LBL.setObjectName("BC_LBL")
        self.gridLayout.addWidget(self.BC_LBL, 10, 0, 1, 1)
        self.Length_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Length_LBL.setObjectName("Length_LBL")
        self.gridLayout.addWidget(self.Length_LBL, 11, 0, 1, 1)
        self.Caliber_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Caliber_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Caliber_TE.setObjectName("Caliber_TE")
        self.gridLayout.addWidget(self.Caliber_TE, 8, 2, 1, 1)
        self.Base_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Base_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Base_TE.setObjectName("Base_TE")
        self.gridLayout.addWidget(self.Base_TE, 9, 2, 1, 1)
        self.BC_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.BC_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.BC_TE.setObjectName("BC_TE")
        self.gridLayout.addWidget(self.BC_TE, 10, 2, 1, 1)
        self.Length_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Length_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Length_TE.setObjectName("Length_TE")
        self.gridLayout.addWidget(self.Length_TE, 11, 2, 1, 1)
        self.Slot_18_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_18_LBL.setObjectName("Slot_18_LBL")
        self.gridLayout.addWidget(self.Slot_18_LBL, 3, 3, 1, 1)
        self.Slot_19_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_19_LBL.setObjectName("Slot_19_LBL")
        self.gridLayout.addWidget(self.Slot_19_LBL, 4, 3, 1, 1)
        self.Slot_20_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_20_LBL.setObjectName("Slot_20_LBL")
        self.gridLayout.addWidget(self.Slot_20_LBL, 5, 3, 1, 1)
        self.Slot_21_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_21_LBL.setObjectName("Slot_21_LBL")
        self.gridLayout.addWidget(self.Slot_21_LBL, 6, 3, 1, 1)
        self.Slot_22_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_22_LBL.setObjectName("Slot_22_LBL")
        self.gridLayout.addWidget(self.Slot_22_LBL, 7, 3, 1, 1)
        self.Slot_18_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_18_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_18_TE.setObjectName("Slot_18_TE")
        self.gridLayout.addWidget(self.Slot_18_TE, 3, 4, 1, 1)
        self.Slot_19_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_19_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_19_TE.setObjectName("Slot_19_TE")
        self.gridLayout.addWidget(self.Slot_19_TE, 4, 4, 1, 1)
        self.Slot_20_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_20_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_20_TE.setObjectName("Slot_20_TE")
        self.gridLayout.addWidget(self.Slot_20_TE, 5, 4, 1, 1)
        self.Slot_21_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_21_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_21_TE.setObjectName("Slot_21_TE")
        self.gridLayout.addWidget(self.Slot_21_TE, 6, 4, 1, 1)
        self.Slot_22_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_22_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_22_TE.setObjectName("Slot_22_TE")
        self.gridLayout.addWidget(self.Slot_22_TE, 7, 4, 1, 1)
        self.Slot_23_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_23_LBL.setObjectName("Slot_23_LBL")
        self.gridLayout.addWidget(self.Slot_23_LBL, 8, 3, 1, 1)
        self.Slot_24_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_24_LBL.setObjectName("Slot_24_LBL")
        self.gridLayout.addWidget(self.Slot_24_LBL, 9, 3, 1, 1)
        self.Slot_25_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_25_LBL.setObjectName("Slot_25_LBL")
        self.gridLayout.addWidget(self.Slot_25_LBL, 10, 3, 1, 1)
        self.Slot_26_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_26_LBL.setObjectName("Slot_26_LBL")
        self.gridLayout.addWidget(self.Slot_26_LBL, 11, 3, 1, 1)
        self.Slot_23_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_23_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_23_TE.setObjectName("Slot_23_TE")
        self.gridLayout.addWidget(self.Slot_23_TE, 8, 4, 1, 1)
        self.Slot_24_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_24_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_24_TE.setObjectName("Slot_24_TE")
        self.gridLayout.addWidget(self.Slot_24_TE, 9, 4, 1, 1)
        self.Slot_25_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_25_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_25_TE.setObjectName("Slot_25_TE")
        self.gridLayout.addWidget(self.Slot_25_TE, 10, 4, 1, 1)
        self.Slot_26_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_26_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_26_TE.setObjectName("Slot_26_TE")
        self.gridLayout.addWidget(self.Slot_26_TE, 11, 4, 1, 1)
        self.AddBullet_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.AddBullet_BTN.setGeometry(QtCore.QRect(1010, 780, 171, 32))
        self.AddBullet_BTN.setObjectName("AddBullet_BTN")
        PopUp_Add_Bullet.setCentralWidget(self.centralwidget)

        self.retranslateUi(PopUp_Add_Bullet)
        QtCore.QMetaObject.connectSlotsByName(PopUp_Add_Bullet)

    def retranslateUi(self, PopUp_Add_Bullet):
        _translate = QtCore.QCoreApplication.translate
        PopUp_Add_Bullet.setWindowTitle(_translate("PopUp_Add_Bullet", "Add Bullet"))
        self.Manufacturer_LBL.setText(_translate("PopUp_Add_Bullet", "Manufacturer"))
        self.Name_LBL.setText(_translate("PopUp_Add_Bullet", "Name"))
        self.Notes_LBL.setText(_translate("PopUp_Add_Bullet", "Notes"))
        self.ModelLBL.setText(_translate("PopUp_Add_Bullet", "Model"))
        self.Slot_16_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 16"))
        self.Slot_15_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 15"))
        self.Picture_LBL.setText(_translate("PopUp_Add_Bullet", "Picture"))
        self.Type_LBL.setText(_translate("PopUp_Add_Bullet", "Type"))
        self.Model_LBL.setText(_translate("PopUp_Add_Bullet", "Weight"))
        self.Size_mm_LBL.setText(_translate("PopUp_Add_Bullet", "Size mm"))
        self.Size_Inch_LBL.setText(_translate("PopUp_Add_Bullet", "Size Inch"))
        self.Slot_17_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 17"))
        self.SKU_LBL.setText(_translate("PopUp_Add_Bullet", "SKU"))
        self.Caliber_LBL.setText(_translate("PopUp_Add_Bullet", "Caliber"))
        self.BaseLBL.setText(_translate("PopUp_Add_Bullet", "Bullet Base"))
        self.BC_LBL.setText(_translate("PopUp_Add_Bullet", "BC"))
        self.Length_LBL.setText(_translate("PopUp_Add_Bullet", "Length"))
        self.Slot_18_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 18"))
        self.Slot_19_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 19"))
        self.Slot_20_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 20"))
        self.Slot_21_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 21"))
        self.Slot_22_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 22"))
        self.Slot_23_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 23"))
        self.Slot_24_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 24"))
        self.Slot_25_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 25"))
        self.Slot_26_LBL.setText(_translate("PopUp_Add_Bullet", "Slot 26"))
        self.AddBullet_BTN.setText(_translate("PopUp_Add_Bullet", "Add Bullet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopUp_Add_Bullet = QtWidgets.QMainWindow()
    ui = Ui_PopUp_Add_Bullet()
    ui.setupUi(PopUp_Add_Bullet)
    PopUp_Add_Bullet.show()
    sys.exit(app.exec_())
