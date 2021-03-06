# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_Add_Powder.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *

import sqlite3
import logging
import traceback

class Ui_PopUp_Add_Powder(object):
    def __init__(self, powder_df):
        super().__init__()
        self.powder_df = powder_df

    def WriteToDB(self):
        try:
            name = self.Name_TE.toPlainText()
            manufacturer = self.Manufacturer_TE.toPlainText()
            model = self.Model_TE.toPlainText()
            sku = self.SKU_TE.toPlainText()
            relburnrate = self.RelBurnRate_TE.toPlainText()
            use = self.WeaponUse_TE.toPlainText()
            density = self.Density_lb_TE.toPlainText()
            bulk = self.BulkDensity_TE.toPlainText()
            note = self.Notes_TE.toPlainText()
            picture = self.Picture_TE.toPlainText()
            slot12 = self.Slot_12_TE.toPlainText()
            slot13 = self.Slot_13_TE.toPlainText()
            slot14 = self.Slot_14_TE.toPlainText()
            slot15 = self.Slot_15_TE.toPlainText()
            slot16 = self.Slot_16_TE.toPlainText()
            slot17 = self.Slot_17_TE.toPlainText()
            slot18 = self.Slot_18_TE.toPlainText()
            slot19 = self.Slot_19_TE.toPlainText()
            slot20 = self.Slot_20_TE.toPlainText()
            slot21 = self.Slot_21_TE.toPlainText()
            slot22 = self.Slot_22_TE.toPlainText()
            slot23 = self.Slot_23_TE.toPlainText()
            slot24 = self.Slot_24_TE.toPlainText()
            slot25 = self.Slot_25_TE.toPlainText()
            slot26 = self.Slot_26_TE.toPlainText()
            slot27 = self.Slot_27_TE.toPlainText()

            sql = '{}'.format("""INSERT INTO Powder 
            (Name, Manufacturer, Model, SKU, Relative_Burn_Rate, Weapon_Use, Density_lb, 
            Bulk_Density, Notes, Picture) 
            VALUES
            ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                              % (
                              name, manufacturer, model, sku, relburnrate, use, density, bulk,
                              note, picture)
                              )

            conn = sqlite3.connect("./DATABASE/TrackerDB.db")
            print("Opened database successfully")
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            logging.info(sql)

        except Exception as e:
            print("Exception = ", str(e))
            traceback.print_exc()
            logging.error("ERROR --- ", str(e))

    def setupUi(self, PopUp_Add_Powder):
        PopUp_Add_Powder.setObjectName("PopUp_Add_Powder")
        PopUp_Add_Powder.resize(1359, 825)
        PopUp_Add_Powder.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(PopUp_Add_Powder)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1161, 772))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Model_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Model_LBL.setObjectName("Model_LBL")
        self.gridLayout.addWidget(self.Model_LBL, 2, 0, 1, 1)
        self.RelBurnRate_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.RelBurnRate_LBL.setObjectName("RelBurnRate_LBL")
        self.gridLayout.addWidget(self.RelBurnRate_LBL, 4, 0, 1, 1)
        self.Slot_12_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_12_LBL.setObjectName("Slot_12_LBL")
        self.gridLayout.addWidget(self.Slot_12_LBL, 10, 0, 1, 1)
        self.WeaponUse_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.WeaponUse_LBL.setObjectName("WeaponUse_LBL")
        self.gridLayout.addWidget(self.WeaponUse_LBL, 5, 0, 1, 1)
        self.Slot_13_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_13_LBL.setObjectName("Slot_13_LBL")
        self.gridLayout.addWidget(self.Slot_13_LBL, 11, 0, 1, 1)
        self.Notes_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Notes_LBL.setObjectName("Notes_LBL")
        self.gridLayout.addWidget(self.Notes_LBL, 26, 0, 1, 1)
        self.Density_lb_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Density_lb_LBL.setObjectName("Density_lb_LBL")
        self.gridLayout.addWidget(self.Density_lb_LBL, 6, 0, 1, 1)
        self.BulkDensity_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.BulkDensity_LBL.setObjectName("BulkDensity_LBL")
        self.gridLayout.addWidget(self.BulkDensity_LBL, 7, 0, 1, 1)
        self.Slot_14_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_14_LBL.setObjectName("Slot_14_LBL")
        self.gridLayout.addWidget(self.Slot_14_LBL, 12, 0, 1, 1)
        self.Manufacturer_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Manufacturer_LBL.setObjectName("Manufacturer_LBL")
        self.gridLayout.addWidget(self.Manufacturer_LBL, 1, 0, 1, 1)
        self.Name_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Name_LBL.setObjectName("Name_LBL")
        self.gridLayout.addWidget(self.Name_LBL, 0, 0, 1, 1)
        self.Picture_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Picture_LBL.setObjectName("Picture_LBL")
        self.gridLayout.addWidget(self.Picture_LBL, 27, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 28, 1, 1, 1)
        self.BulkDensity_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.BulkDensity_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.BulkDensity_TE.setObjectName("BulkDensity_TE")
        self.gridLayout.addWidget(self.BulkDensity_TE, 7, 1, 1, 1)
        self.WeaponUse_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.WeaponUse_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.WeaponUse_TE.setObjectName("WeaponUse_TE")
        self.gridLayout.addWidget(self.WeaponUse_TE, 5, 1, 1, 1)
        self.Slot_17_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_17_LBL.setObjectName("Slot_17_LBL")
        self.gridLayout.addWidget(self.Slot_17_LBL, 1, 2, 1, 1)
        self.Slot_16_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_16_LBL.setObjectName("Slot_16_LBL")
        self.gridLayout.addWidget(self.Slot_16_LBL, 0, 2, 1, 1)
        self.Name_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Name_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Name_TE.setObjectName("Name_TE")
        self.gridLayout.addWidget(self.Name_TE, 0, 1, 1, 1)
        self.Density_lb_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Density_lb_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Density_lb_TE.setObjectName("Density_lb_TE")
        self.gridLayout.addWidget(self.Density_lb_TE, 6, 1, 1, 1)
        self.Slot_14_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_14_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_14_TE.setObjectName("Slot_14_TE")
        self.gridLayout.addWidget(self.Slot_14_TE, 12, 1, 1, 1)
        self.Slot_12_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_12_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_12_TE.setObjectName("Slot_12_TE")
        self.gridLayout.addWidget(self.Slot_12_TE, 10, 1, 1, 1)
        self.RelBurnRate_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.RelBurnRate_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.RelBurnRate_TE.setObjectName("RelBurnRate_TE")
        self.gridLayout.addWidget(self.RelBurnRate_TE, 4, 1, 1, 1)
        self.Slot_15_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_15_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_15_TE.setObjectName("Slot_15_TE")
        self.gridLayout.addWidget(self.Slot_15_TE, 13, 1, 1, 1)
        self.Slot_15_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_15_LBL.setObjectName("Slot_15_LBL")
        self.gridLayout.addWidget(self.Slot_15_LBL, 13, 0, 1, 1)
        self.Slot_24_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_24_LBL.setObjectName("Slot_24_LBL")
        self.gridLayout.addWidget(self.Slot_24_LBL, 10, 2, 1, 1)
        self.Slot_13_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_13_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_13_TE.setObjectName("Slot_13_TE")
        self.gridLayout.addWidget(self.Slot_13_TE, 11, 1, 1, 1)
        self.Slot_26_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_26_LBL.setObjectName("Slot_26_LBL")
        self.gridLayout.addWidget(self.Slot_26_LBL, 12, 2, 1, 1)
        self.Slot_27_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_27_LBL.setObjectName("Slot_27_LBL")
        self.gridLayout.addWidget(self.Slot_27_LBL, 13, 2, 1, 1)
        self.Slot_25_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_25_LBL.setObjectName("Slot_25_LBL")
        self.gridLayout.addWidget(self.Slot_25_LBL, 11, 2, 1, 1)
        self.Manufacturer_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Manufacturer_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Manufacturer_TE.setObjectName("Manufacturer_TE")
        self.gridLayout.addWidget(self.Manufacturer_TE, 1, 1, 1, 1)
        self.Slot_16_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_16_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_16_TE.setObjectName("Slot_16_TE")
        self.gridLayout.addWidget(self.Slot_16_TE, 0, 3, 1, 1)
        self.Slot_17_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_17_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_17_TE.setObjectName("Slot_17_TE")
        self.gridLayout.addWidget(self.Slot_17_TE, 1, 3, 1, 1)
        self.Slot_24_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_24_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_24_TE.setObjectName("Slot_24_TE")
        self.gridLayout.addWidget(self.Slot_24_TE, 10, 3, 1, 1)
        self.Slot_25_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_25_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_25_TE.setObjectName("Slot_25_TE")
        self.gridLayout.addWidget(self.Slot_25_TE, 11, 3, 1, 1)
        self.Slot_26_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_26_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_26_TE.setObjectName("Slot_26_TE")
        self.gridLayout.addWidget(self.Slot_26_TE, 12, 3, 1, 1)
        self.Slot_27_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_27_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_27_TE.setObjectName("Slot_27_TE")
        self.gridLayout.addWidget(self.Slot_27_TE, 13, 3, 1, 1)
        self.Notes_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Notes_TE.setMaximumSize(QtCore.QSize(16777215, 300))
        self.Notes_TE.setObjectName("Notes_TE")
        self.gridLayout.addWidget(self.Notes_TE, 26, 1, 1, 1)
        self.Picture_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Picture_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Picture_TE.setObjectName("Picture_TE")
        self.gridLayout.addWidget(self.Picture_TE, 27, 1, 1, 1)
        self.Model_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Model_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Model_TE.setObjectName("Model_TE")
        self.gridLayout.addWidget(self.Model_TE, 2, 1, 1, 1)
        self.SKU_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.SKU_LBL.setObjectName("SKU_LBL")
        self.gridLayout.addWidget(self.SKU_LBL, 3, 0, 1, 1)
        self.SKU_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.SKU_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.SKU_TE.setObjectName("SKU_TE")
        self.gridLayout.addWidget(self.SKU_TE, 3, 1, 1, 1)
        self.Slot_18_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_18_LBL.setObjectName("Slot_18_LBL")
        self.gridLayout.addWidget(self.Slot_18_LBL, 2, 2, 1, 1)
        self.Slot_18_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_18_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_18_TE.setObjectName("Slot_18_TE")
        self.gridLayout.addWidget(self.Slot_18_TE, 2, 3, 1, 1)
        self.Slot_19_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_19_LBL.setObjectName("Slot_19_LBL")
        self.gridLayout.addWidget(self.Slot_19_LBL, 3, 2, 1, 1)
        self.Slot_19_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_19_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_19_TE.setObjectName("Slot_19_TE")
        self.gridLayout.addWidget(self.Slot_19_TE, 3, 3, 1, 1)
        self.Slot_20_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_20_LBL.setObjectName("Slot_20_LBL")
        self.gridLayout.addWidget(self.Slot_20_LBL, 4, 2, 1, 1)
        self.Slot_20_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_20_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_20_TE.setObjectName("Slot_20_TE")
        self.gridLayout.addWidget(self.Slot_20_TE, 4, 3, 1, 1)
        self.Slot_21_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_21_LBL.setObjectName("Slot_21_LBL")
        self.gridLayout.addWidget(self.Slot_21_LBL, 5, 2, 1, 1)
        self.Slot_21_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_21_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_21_TE.setObjectName("Slot_21_TE")
        self.gridLayout.addWidget(self.Slot_21_TE, 5, 3, 1, 1)
        self.Slot_22_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_22_LBL.setObjectName("Slot_22_LBL")
        self.gridLayout.addWidget(self.Slot_22_LBL, 6, 2, 1, 1)
        self.Slot_22_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_22_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_22_TE.setObjectName("Slot_22_TE")
        self.gridLayout.addWidget(self.Slot_22_TE, 6, 3, 1, 1)
        self.Slot_23_LBL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Slot_23_LBL.setObjectName("Slot_23_LBL")
        self.gridLayout.addWidget(self.Slot_23_LBL, 7, 2, 1, 1)
        self.Slot_23_TE = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Slot_23_TE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Slot_23_TE.setObjectName("Slot_23_TE")
        self.gridLayout.addWidget(self.Slot_23_TE, 7, 3, 1, 1)

        self.AddPowder_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.AddPowder_BTN.setGeometry(QtCore.QRect(1010, 780, 171, 32))
        self.AddPowder_BTN.setObjectName("AddPowder_BTN")
        PopUp_Add_Powder.setCentralWidget(self.centralwidget)
        self.AddPowder_BTN.clicked.connect(lambda: self.WriteToDB())

        self.retranslateUi(PopUp_Add_Powder)
        QtCore.QMetaObject.connectSlotsByName(PopUp_Add_Powder)

    def retranslateUi(self, PopUp_Add_Powder):
        _translate = QtCore.QCoreApplication.translate
        PopUp_Add_Powder.setWindowTitle(_translate("PopUp_Add_Powder", "Add Firearm"))
        self.Model_LBL.setText(_translate("PopUp_Add_Powder", "Model"))
        self.RelBurnRate_LBL.setText(_translate("PopUp_Add_Powder", "Relative Burn Rate"))
        self.Slot_12_LBL.setText(_translate("PopUp_Add_Powder", "Slot 12"))
        self.WeaponUse_LBL.setText(_translate("PopUp_Add_Powder", "Weapon Use"))
        self.Slot_13_LBL.setText(_translate("PopUp_Add_Powder", "Slot 13"))
        self.Notes_LBL.setText(_translate("PopUp_Add_Powder", "Notes"))
        self.Density_lb_LBL.setText(_translate("PopUp_Add_Powder", "Density per Lb"))
        self.BulkDensity_LBL.setText(_translate("PopUp_Add_Powder", "Bulk Density"))
        self.Slot_14_LBL.setText(_translate("PopUp_Add_Powder", "Slot 14"))
        self.Manufacturer_LBL.setText(_translate("PopUp_Add_Powder", "Manufacturer"))
        self.Name_LBL.setText(_translate("PopUp_Add_Powder", "Name"))
        self.Picture_LBL.setText(_translate("PopUp_Add_Powder", "Picture"))
        self.Slot_17_LBL.setText(_translate("PopUp_Add_Powder", "Slot 17"))
        self.Slot_16_LBL.setText(_translate("PopUp_Add_Powder", "Slot 16"))
        self.Slot_15_LBL.setText(_translate("PopUp_Add_Powder", "Slot 15"))
        self.Slot_24_LBL.setText(_translate("PopUp_Add_Powder", "Slot 24"))
        self.Slot_26_LBL.setText(_translate("PopUp_Add_Powder", "Slot 26"))
        self.Slot_27_LBL.setText(_translate("PopUp_Add_Powder", "Slot 27"))
        self.Slot_25_LBL.setText(_translate("PopUp_Add_Powder", "Slot 25"))
        self.SKU_LBL.setText(_translate("PopUp_Add_Powder", "SKU"))
        self.Slot_18_LBL.setText(_translate("PopUp_Add_Powder", "Slot 18"))
        self.Slot_19_LBL.setText(_translate("PopUp_Add_Powder", "Slot 19"))
        self.Slot_20_LBL.setText(_translate("PopUp_Add_Powder", "Slot 20"))
        self.Slot_21_LBL.setText(_translate("PopUp_Add_Powder", "Slot 21"))
        self.Slot_22_LBL.setText(_translate("PopUp_Add_Powder", "Slot 22"))
        self.Slot_23_LBL.setText(_translate("PopUp_Add_Powder", "Slot 23"))
        self.AddPowder_BTN.setText(_translate("PopUp_Add_Powder", "Add Powder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopUp_Add_Powder = QtWidgets.QMainWindow()
    ui = Ui_PopUp_Add_Powder()
    ui.setupUi(PopUp_Add_Powder)
    PopUp_Add_Powder.show()
    sys.exit(app.exec_())
