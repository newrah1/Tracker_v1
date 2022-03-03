import mysql.connector
import traceback
import pandas as pd
from configparser import ConfigParser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtWidgets import  QVBoxLayout, QSizePolicy,  QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from pandas import option_context
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

class ShowAllFirearms_PopUp(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def config_query(self, query, text, return_value):
        # save to DataFrame
        df = pd.read_sql(query, self.conn)

        if return_value == 'None':
            pass
        elif return_value == 'True':
            # print the query
            print("Query = ", query)

            # print the number of rows
            rows = df.shape[0]
            print('{}{}\n'.format(text, rows))

            print(df.to_string(max_rows=5))
        return df

    def __init__(self):
        # set run parameters
        self.parser = ConfigParser()
        self.parser.read("./Tracker.ini")

        self.conn = mysql.connector.connect(host=self.parser['SQL']['host'],
                                            user=self.parser['SQL']['user'],
                                            password=self.parser['SQL'][
                                                'password'],
                                            database=self.parser['SQL'][
                                                'database'],
                                            auth_plugin=self.parser['SQL'][
                                                'auth_plugin']
                                            )
        super().__init__()
        firearm_df = self.config_query(
            "SELECT * FROM Configuration_V1.Firearm",
            "Number of Configurations = ",
            "None")

        self.setWindowTitle("List of Firearms")
        layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(firearm_df['Name'].to_string(index=False))
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label)
        self.setLayout(layout)


class ShowAllBullets_PopUp(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def config_query(self, query, text, return_value):
        # save to DataFrame
        df = pd.read_sql(query, self.conn)

        if return_value == 'None':
            pass
        elif return_value == 'True':
            # print the query
            print("Query = ", query)

            # print the number of rows
            rows = df.shape[0]
            print('{}{}\n'.format(text, rows))

            print(df.to_string(max_rows=5))
        return df

    def __init__(self):
        # set run parameters
        self.parser = ConfigParser()
        self.parser.read("./Tracker.ini")

        self.conn = mysql.connector.connect(host=self.parser['SQL']['host'],
                                            user=self.parser['SQL']['user'],
                                            password=self.parser['SQL'][
                                                'password'],
                                            database=self.parser['SQL'][
                                                'database'],
                                            auth_plugin=self.parser['SQL'][
                                                'auth_plugin']
                                            )

        super().__init__()
        df = self.config_query(
            "SELECT * FROM Configuration_V1.Bullet",
            "Number of Bullets = ",
            "None")

        self.setWindowTitle("List of Bullets")
        layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(df['Name'].to_string(index=False))
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label)
        self.setLayout(layout)


class ShowAllPowders_PopUp(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def config_query(self, query, text, return_value):
        # save to DataFrame
        df = pd.read_sql(query, self.conn)

        if return_value == 'None':
            pass
        elif return_value == 'True':
            # print the query
            print("Query = ", query)

            # print the number of rows
            rows = df.shape[0]
            print('{}{}\n'.format(text, rows))

            print(df.to_string(max_rows=5))
        return df

    def __init__(self):
        # set run parameters
        self.parser = ConfigParser()
        self.parser.read("./Tracker.ini")

        self.conn = mysql.connector.connect(host=self.parser['SQL']['host'],
                                            user=self.parser['SQL']['user'],
                                            password=self.parser['SQL'][
                                                'password'],
                                            database=self.parser['SQL'][
                                                'database'],
                                            auth_plugin=self.parser['SQL'][
                                                'auth_plugin']
                                            )
        super().__init__()
        df = self.config_query(
            "SELECT * FROM Configuration_V1.Powder",
            "Number of Bullets = ",
            "None")

        self.setWindowTitle("List of Powders")
        layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(df['Name'].to_string(index=False))
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label)
        self.setLayout(layout)


class ShowAllCases_PopUp(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def config_query(self, query, text, return_value):
        # save to DataFrame
        df = pd.read_sql(query, self.conn)

        if return_value == 'None':
            pass
        elif return_value == 'True':
            # print the query
            print("Query = ", query)

            # print the number of rows
            rows = df.shape[0]
            print('{}{}\n'.format(text, rows))

            print(df.to_string(max_rows=5))
        return df

    def __init__(self):
        # set run parameters
        self.parser = ConfigParser()
        self.parser.read("./Tracker.ini")

        self.conn = mysql.connector.connect(host=self.parser['SQL']['host'],
                                            user=self.parser['SQL']['user'],
                                            password=self.parser['SQL'][
                                                'password'],
                                            database=self.parser['SQL'][
                                                'database'],
                                            auth_plugin=self.parser['SQL'][
                                                'auth_plugin']
                                            )

        super().__init__()
        df = self.config_query(
            "SELECT * FROM Configuration_V1.Case",
            "Number of Case = ",
            "None")

        self.setWindowTitle("List of Case")
        layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(df['Name'].to_string(index=False))
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label)
        self.setLayout(layout)


class ShowAllSilencers_PopUp(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def config_query(self, query, text, return_value):
        # save to DataFrame
        df = pd.read_sql(query, self.conn)

        if return_value == 'None':
            pass
        elif return_value == 'True':
            # print the query
            print("Query = ", query)

            # print the number of rows
            rows = df.shape[0]
            print('{}{}\n'.format(text, rows))

            print(df.to_string(max_rows=5))
        return df

    def __init__(self):
        # set run parameters
        self.parser = ConfigParser()
        self.parser.read("./Tracker.ini")

        self.conn = mysql.connector.connect(host=self.parser['SQL']['host'],
                                            user=self.parser['SQL']['user'],
                                            password=self.parser['SQL'][
                                                'password'],
                                            database=self.parser['SQL'][
                                                'database'],
                                            auth_plugin=self.parser['SQL'][
                                                'auth_plugin']
                                            )

        super().__init__()
        df = self.config_query(
            "SELECT * FROM Configuration_V1.Silencer",
            "Number of Silencer = ",
            "None")

        self.setWindowTitle("List of Silencer")
        layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(df['Name'].to_string(index=False))
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label)
        self.setLayout(layout)

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()


class Ui_MainWindow(object):
    def __init__(self):
        # set run parameters
        self.parser = ConfigParser()
        self.parser.read("./Tracker.ini")

        self.conn = mysql.connector.connect(host=self.parser['SQL']['host'],
                                            user=self.parser['SQL']['user'],
                                            password=self.parser['SQL'][
                                                'password'],
                                            database=self.parser['SQL'][
                                                'database'],
                                            auth_plugin=self.parser['SQL'][
                                                'auth_plugin']
                                            )

    # Not currently used - config_query
    def config_query(self, query, text, return_value):
        # save to DataFrame
        df = pd.read_sql(query, self.conn)

        if return_value == 'None':
            pass
        elif return_value == 'True':
            # print the query
            print("Query = ", query)

            # print the number of rows
            rows = df.shape[0]
            print('{}{}\n'.format(text, rows))

            print(df.to_string(max_rows=5))
        return df

    def query_databases(self):
        "Read SQL DB's and return dataframes of the data "
        try:
            firearm_db = pd.read_sql("SELECT * FROM Configuration_V1.Firearm",
                                     self.conn)
            bullets_db = pd.read_sql("SELECT * FROM Configuration_V1.bullet",
                                     self.conn)
            powders_db = pd.read_sql("SELECT * FROM Configuration_V1.powder",
                                     self.conn)
            cases_db = pd.read_sql("SELECT * FROM Configuration_V1.case",
                                   self.conn)
            return firearm_db, bullets_db, powders_db, cases_db
        except Exception as e:
            print("Exception = ", str(e))
            traceback.print_exc()

    # FTab --------------------------------
    def displayData_FTab(self):
        try:
            # get the value from the Firearm comboBox
            Selected_Firearm = self.FTab_Firearm_Combo.currentText()

            # query the DB save to df
            firearm_df = self.config_query(
                "SELECT * FROM Configuration_V1.Firearm",
                "Number of Configurations = ",
                "None")
            # filter by selected firearm
            query = '{}"{}"'.format("Name == ", str(Selected_Firearm))
            firearm_df = firearm_df.query(query)

            # clear the form
            self.FTab_Name_TB.clear()
            self.FTab_Type_TB.clear()
            self.FTab_Manufacturer_TB.clear()
            self.FTab_SKU_TB.clear()
            self.FTab_Model_TB.clear()
            self.FTab_Caliber_TB.clear()
            self.FTab_OLen_TB.clear()
            self.FTab_BarrelLen_TB.clear()
            self.FTab_Weight_TB.clear()
            self.FTab_Notes_TB.clear()
            self.FTab_Picture_LBL.clear()

            # fill in the form
            self.FTab_Name_TB.setText(
                firearm_df['Name'].to_string(index=False))
            self.FTab_Type_TB.setText(
                firearm_df['Firearm_Type'].to_string(index=False))
            self.FTab_Manufacturer_TB.setText(
                firearm_df['Manufacturer'].to_string(index=False))
            self.FTab_SKU_TB.setText(firearm_df['SKU'].to_string(index=False))
            self.FTab_Model_TB.setText(
                firearm_df['Model'].to_string(index=False))
            self.FTab_Caliber_TB.setText(
                firearm_df['Caliber'].to_string(index=False))
            self.FTab_OLen_TB.setText(
                firearm_df['Overall_Length_Inch'].to_string(index=False))
            self.FTab_BarrelLen_TB.setText(
                firearm_df['Barrel_Len_Inch'].to_string(index=False))
            self.FTab_Weight_TB.setText(
                firearm_df['Weight_lb'].to_string(index=False))

            # Context manager to temporarily set options in the with statement context.
            # required to display 'Notes'
            with option_context('display.max_colwidth', None):
                self.FTab_Notes_TB.setText(firearm_df['Notes'].to_string(
                    index=False))
            # Display picture of firearm in GUI
            high_rez = QtCore.QSize(400, 400)
            pixmap = QtGui.QPixmap(firearm_df['Picture'].to_string(index=False))
            pixmap = pixmap.scaled(high_rez)
            self.FTab_Picture_LBL.setPixmap(pixmap)

        except Exception as e:
            print("Exception = ", str(e))
            traceback.print_exc()

    def PopUp_ShowAllFirearms(self, checked):
        if self.FTab_ShowFirearms_POP.isVisible():
            self.FTab_ShowFirearms_POP.hide()

        else:
            self.FTab_ShowFirearms_POP.show()

    def PopUp_Canvas_Test(self, checked):
        if self.FTab_BTN_3_POP.isVisible():
            self.FTab_BTN_3_POP.hide()

        else:
            self.FTab_BTN_3_POP.show()
    # FTab --------------------------------

    # BTab --------------------------------
    def displayData_BTab(self):
        try:
            # get the value from the Firearm comboBox
            Selected_Bullet = self.BTab_Bullet_Combo.currentText()
            # query the DB save to df
            firearm_df = self.config_query(
                "SELECT * FROM Configuration_V1.bullet",
                "Number of Configurations = ",
                "None")
            # filter by selected firearm
            query = '{}"{}"'.format("Name == ", str(Selected_Bullet))
            bullet_df = firearm_df.query(query)

            # clear the form
            self.BTab_Name_TB.clear()
            self.BTab_Manufacturer_TB.clear()
            self.BTab_Size_Inch_TB.clear()
            self.BTab_Size_mm_TB.clear()
            self.BTab_Weight_TB.clear()
            self.BTab_Type_TB.clear()
            self.BTab_SKU_TB.clear()
            self.BTab_BBase_TB.clear()
            self.BTab_BC_TB.clear()
            self.BTab_Length_TB.clear()
            self.BTab_Notes_TB.clear()
            self.BTab_Picture_LBL.clear()

            # fill in the form
            self.BTab_Name_TB.setText(
                bullet_df['Name'].to_string(index=False))
            self.BTab_Manufacturer_TB.setText(
                bullet_df['Manufacturer'].to_string(index=False))
            self.BTab_Size_Inch_TB.setText(
                bullet_df['Size_Inch'].to_string(index=False))
            self.BTab_Size_mm_TB.setText(
                bullet_df['Size_mm'].to_string(index=False))
            self.BTab_Weight_TB.setText(
                bullet_df['Weight'].to_string(index=False))
            self.BTab_Type_TB.setText(
                bullet_df['Type'].to_string(index=False))
            self.BTab_SKU_TB.setText(
                bullet_df['SKU'].to_string(index=False))
            self.BTab_Caliber_TB.setText(
                bullet_df['Caliber'].to_string(index=False))
            self.BTab_BBase_TB.setText(
                bullet_df['Bullet_Base'].to_string(index=False))
            self.BTab_BC_TB.setText(
                bullet_df['Ballistic_Coefficient'].to_string(index=False))
            self.BTab_Length_TB.setText(
                bullet_df['Length_Inch'].to_string(index=False))
            self.BTab_Notes_TB.setText(
                bullet_df['Notes'].to_string(index=False))

            # Context manager to temporarily set options in the with statement context.
            # required to display 'Notes'
            with option_context('display.max_colwidth', None):
                self.BTab_Notes_TB.setText(bullet_df['Notes'].to_string(
                    index=False))
                print(bullet_df)
                # Display picture of Bullet in GUI
                high_rez = QtCore.QSize(400, 400)
                pixmap = QtGui.QPixmap(
                    bullet_df['Picture'].to_string(index=False))
                pixmap = pixmap.scaled(high_rez)
                self.BTab_Picture_LBL.setPixmap(pixmap)

        except Exception as e:
            print("Exception = ", str(e))
            traceback.print_exc()

    def PopUp_ShowAllBullets(self, checked):
        if self.BTab_ShowBullets_POP.isVisible():
            self.BTab_ShowBullets_POP.hide()

        else:
            self.BTab_ShowBullets_POP.show()
    # BTab --------------------------------

    # PTab --------------------------------
    def displayData_PTab(self):
        pass

    def PopUp_ShowAllPowders(self, checked):
        if self.PTab_ShowPowders_POP.isVisible():
            self.PTab_ShowPowders_POP.hide()

        else:
            self.PTab_ShowPowders_POP.show()
    # PTab --------------------------------

    # CTab --------------------------------
    def displayData_CTab(self):
        pass

    def PopUp_ShowAllCases(self, checked):
        if self.CTab_ShowCases_POP.isVisible():
            self.CTab_ShowCases_POP.hide()

        else:
            self.CTab_ShowCases_POP.show()
    # CTab --------------------------------

    # PRTab --------------------------------
    def displayData_PRTab(self):
        pass
    # PRTab --------------------------------

    # DTab --------------------------------
    def displayData_DTab(self):
        pass
    # DTab --------------------------------

    # STab --------------------------------
    def displayData_STab(self):
        pass

    def PopUp_ShowAllSilencers(self, checked):
        if self.STab_ShowSilencers_POP.isVisible():
            self.STab_ShowSilencers_POP.hide()
        else:
            self.STab_ShowSilencers_POP.show()
    # STab --------------------------------

    # MTab --------------------------------
    def displayData_MTab(self):
        pass
    # MTab --------------------------------

    def setupUi(self, MainWindow):
        # retrieve data from MySQL
        firearms_df, bullets_df, powders_df, cases_df= self.query_databases()
        # Generate unique lists of data
        firearms_list = firearms_df['Name'].unique().tolist()
        bullets_list = bullets_df['Name'].unique().tolist()
        powders_list = powders_df['Name'].unique().tolist()
        cases_list = cases_df['Name'].unique().tolist()

        # Main Window setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 1009)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1101, 981))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")

        # FTab --------------------------------
        self.FTab_tab = QtWidgets.QWidget()
        self.FTab_tab.setObjectName("FTab_tab")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.FTab_tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 471, 928))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.FTab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_2)
        self.FTab_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.FTab_gridLayout.setObjectName("FTab_gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.FTab_gridLayout.addItem(spacerItem, 34, 1, 1, 1)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.FTab_tab)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(490, 80, 160, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.FTab_verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.FTab_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.FTab_verticalLayout.setObjectName("FTab_verticalLayout")
        # Firearms Combo Box
        self.FTab_Firearm_Combo = QtWidgets.QComboBox(self.FTab_tab)
        self.FTab_Firearm_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
        self.FTab_Firearm_Combo.setObjectName("FTab_Firearm_Combo")
        self.FTab_Firearm_Combo.addItems(firearms_list)
        self.FTab_Firearm_LBL = QtWidgets.QLabel(self.FTab_tab)
        self.FTab_Firearm_LBL.setGeometry(QtCore.QRect(20, 10, 451, 20))
        self.FTab_Firearm_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.FTab_Firearm_LBL.setObjectName("FTab_Firearm_LBL")
        # FTab Type
        self.FTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Type_TB.setObjectName("FTab_Type_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Type_TB, 0, 1, 1, 1)
        self.FTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Type_LBL.setObjectName("FTab_Type_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Type_LBL, 0, 0, 1, 1)
        # FTab SKU
        self.FTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_SKU_TB.setObjectName("FTab_SKU_TB")
        self.FTab_gridLayout.addWidget(self.FTab_SKU_TB, 1, 1, 1, 1)
        self.FTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_SKU_LBL.setObjectName("FTab_SKU_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_SKU_LBL, 1, 0, 1, 1)
        # FTab Name
        self.FTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Name_TB.setObjectName("FTab_Name_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Name_TB, 2, 1, 1, 1)
        self.FTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Name_LBL.setObjectName("FTab_Name_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Name_LBL, 2, 0, 1, 1)
        # FTab Manufacturer
        self.FTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Manufacturer_LBL.setObjectName("FTab_Manufacturer_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Manufacturer_LBL, 3, 0, 1, 1)
        self.FTab_Manufacturer_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_2)
        self.FTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Manufacturer_TB.setObjectName("FTab_Manufacturer_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Manufacturer_TB, 3, 1, 1, 1)
        # FTab Model
        self.FTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Model_LBL.setObjectName("FTab_Model_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Model_LBL, 4, 0, 1, 1)
        self.FTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Model_TB.setObjectName("FTab_Model_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Model_TB, 4, 1, 1, 1)
        # Caliber
        self.FTab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Caliber_LBL.setObjectName("FTab_Caliber_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Caliber_LBL, 5, 0, 1, 1)
        self.FTab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Caliber_TB.setObjectName("FTab_Caliber_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Caliber_TB, 5, 1, 1, 1)
        # Overall Length
        self.FTab_OLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_OLen_LBL.setObjectName("FTab_OLen_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_OLen_LBL, 6, 0, 1, 1)
        self.FTab_OLen_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_OLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_OLen_TB.setObjectName("FTab_OLen_TB")
        self.FTab_gridLayout.addWidget(self.FTab_OLen_TB, 6, 1, 1, 1)
        # Barrel Length
        self.FTab_BarrelLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_BarrelLen_LBL.setObjectName("FTab_BarrelLen_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_BarrelLen_LBL, 7, 0, 1, 1)
        self.FTab_BarrelLen_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_2)
        self.FTab_BarrelLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_BarrelLen_TB.setObjectName("FTab_BarrelLen_TB")
        self.FTab_gridLayout.addWidget(self.FTab_BarrelLen_TB, 7, 1, 1, 1)
        # Weight
        self.FTab_Weight_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Weight_LBL.setObjectName("FTab_Weight_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Weight_LBL, 8, 0, 1, 1)
        self.FTab_Weight_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Weight_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Weight_TB.setObjectName("FTab_Weight_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Weight_TB, 8, 1, 1, 1)
        # Action Type
        self.FTab_Action_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Action_LBL.setObjectName("FTab_Action_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Action_LBL, 9, 0, 1, 1)
        self.FTab_Action_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Action_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Action_TB.setObjectName("FTab_Action_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Action_TB, 9, 1, 1, 1)
        # FTab TwistRate
        self.FTab_TwistRate_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_TwistRate_LBL.setObjectName("FTab_TwistRate_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_TwistRate_LBL, 10, 0, 1, 1)
        self.FTab_TwistRate_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_2)
        self.FTab_TwistRate_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_TwistRate_TB.setObjectName("FTab_TwistRate_TB")
        self.FTab_gridLayout.addWidget(self.FTab_TwistRate_TB, 10, 1, 1, 1)
        # FTab ThreadSize
        self.FTab_ThreadSize_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_ThreadSize_LBL.setObjectName("FTab_ThreadSize_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_ThreadSize_LBL, 11, 0, 1, 1)
        self.FTab_ThreadSize_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_2)
        self.FTab_ThreadSize_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_ThreadSize_TB.setObjectName("FTab_ThreadSize_TB")
        self.FTab_gridLayout.addWidget(self.FTab_ThreadSize_TB, 11, 1, 1, 1)
        # FTab Slot 1
        self.FTab_Slot_1_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_1_LBL.setObjectName("FTab_Slot_1_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_1_LBL, 13, 0, 1, 1)
        self.FTab_Slot_1_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_1_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_1_TB.setObjectName("FTab_Slot_1_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_1_TB, 13, 1, 1, 1)
        # FTab Slot 2
        self.FTab_Slot_2_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_2_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_2_TB.setObjectName("FTab_Slot_2_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_2_TB, 14, 1, 1, 1)
        self.FTab_Slot_2_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_2_LBL.setObjectName("FTab_Slot_2_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_2_LBL, 14, 0, 1, 1)
        # FTab Slot 3
        self.FTab_Slot_3_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_3_LBL.setObjectName("FTab_Slot_3_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_3_LBL, 15, 0, 1, 1)
        self.FTab_Slot_3_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_3_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_3_TB.setObjectName("FTab_Slot_3_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_3_TB, 15, 1, 1, 1)
        # FTab Slot 4
        self.FTab_Slot_4_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_4_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_4_TB.setObjectName("FTab_Slot_4_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_4_TB, 16, 1, 1, 1)
        self.FTab_Slot_4_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_4_LBL.setObjectName("FTab_Slot_4_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_4_LBL, 16, 0, 1, 1)
        # FTab Slot 5
        self.FTab_Slot_5_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_5_LBL.setObjectName("FTab_Slot_5_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_5_LBL, 18, 0, 1, 1)
        self.FTab_Slot_5_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_5_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_5_TB.setObjectName("FTab_Slot_5_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_5_TB, 18, 1, 1, 1)
        # FTab Slot 6
        self.FTab_Slot_6_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_6_LBL.setObjectName("FTab_Slot_6_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_6_LBL, 19, 0, 1, 1)
        self.FTab_Slot_6_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_6_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_6_TB.setObjectName("FTab_Slot_6_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_6_TB, 19, 1, 1, 1)
        # FTab Slot 7
        self.FTab_Slot_7_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_7_LBL.setObjectName("FTab_Slot_7_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_7_LBL, 21, 0, 1, 1)
        self.FTab_Slot_7_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_7_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_7_TB.setObjectName("FTab_Slot_7_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_7_TB, 21, 1, 1, 1)
        # FTab Slot 8
        self.FTab_Slot_8_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_8_LBL.setObjectName("FTab_Slot_8_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_8_LBL, 23, 0, 1, 1)
        self.FTab_Slot_8_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_8_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_8_TB.setObjectName("FTab_Slot_8_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_8_TB, 23, 1, 1, 1)
        # FTab Slot 9
        self.FTab_Slot_9_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_9_LBL.setObjectName("FTab_Slot_9_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_9_LBL, 25, 0, 1, 1)
        self.FTab_Slot_9_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_9_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_9_TB.setObjectName("FTab_Slot_9_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_9_TB, 25, 1, 1, 1)
        # FTab Slot 10
        self.FTab_Slot_10_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_10_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_10_TB.setObjectName("FTab_Slot_10_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_10_TB, 26, 1, 1, 1)
        self.FTab_Slot_10_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_10_LBL.setObjectName("FTab_Slot_10_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_10_LBL, 26, 0, 1, 1)
        # FTab Slot 11
        self.FTab_Slot_11_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_11_LBL.setObjectName("FTab_Slot_11_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_11_LBL, 28, 0, 1, 1)
        self.FTab_Slot_11_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_11_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_11_TB.setObjectName("FTab_Slot_11_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_11_TB, 28, 1, 1, 1)
        # FTab Slot 12
        self.FTab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.FTab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.FTab_Slot_12_TB.setObjectName("FTab_Slot_12_TB")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_12_TB, 30, 1, 1, 1)
        self.FTab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FTab_Slot_12_LBL.setObjectName("FTab_Slot_12_LBL")
        self.FTab_gridLayout.addWidget(self.FTab_Slot_12_LBL, 30, 0, 1, 1)
        # FTab Spacer

        # FTab Add BTN
        self.FTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FTab_Add_BTN.setDefault(True)
        self.FTab_Add_BTN.setObjectName("FTab_Add_BTN")
        self.FTab_verticalLayout.addWidget(self.FTab_Add_BTN)
        # FTab Show All Button
        self.FTab_View_All_BTN = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.FTab_View_All_BTN.setAutoDefault(False)
        self.FTab_View_All_BTN.setDefault(True)
        self.FTab_View_All_BTN.setObjectName("FTab_View_All_BTN")
        self.FTab_ShowFirearms_POP = ShowAllFirearms_PopUp()
        self.FTab_View_All_BTN.clicked.connect(self.PopUp_ShowAllFirearms)
        self.FTab_verticalLayout.addWidget(self.FTab_View_All_BTN)
        # FTab BTN 3
        self.FTab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FTab_BTN_3.setDefault(True)
        self.FTab_BTN_3.setObjectName("FTab_BTN_3")
        self.FTab_verticalLayout.addWidget(self.FTab_BTN_3)
        self.FTab_BTN_3_POP = PlotCanvas()
        self.FTab_BTN_3.clicked.connect(self.PopUp_Canvas_Test)
        self.FTab_verticalLayout.addWidget(self.FTab_BTN_3)
        # FTab BTN 4
        self.FTab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FTab_BTN_4.setDefault(True)
        self.FTab_BTN_4.setObjectName("FTab_BTN_4")
        self.FTab_verticalLayout.addWidget(self.FTab_BTN_4)
        # FTab BTN 5
        self.FTab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FTab_BTN_5.setDefault(True)
        self.FTab_BTN_5.setObjectName("FTab_BTN_5")
        self.FTab_verticalLayout.addWidget(self.FTab_BTN_5)
        # FTab BTN 6
        self.FTab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FTab_BTN_6.setDefault(True)
        self.FTab_BTN_6.setObjectName("FTab_BTN_6")
        self.FTab_verticalLayout.addWidget(self.FTab_BTN_6)
        # FTab BTN 7
        self.FTab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FTab_BTN_7.setDefault(True)
        self.FTab_BTN_7.setObjectName("FTab_BTN_7")
        self.FTab_verticalLayout.addWidget(self.FTab_BTN_7)
        # FTab BTN 8
        self.FTab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FTab_BTN_8.setAutoDefault(False)
        self.FTab_BTN_8.setDefault(True)
        self.FTab_BTN_8.setObjectName("FTab_BTN_8")
        self.FTab_verticalLayout.addWidget(self.FTab_BTN_8)
        # FTab BTN 9
        self.FTab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FTab_BTN_9.setAutoDefault(False)
        self.FTab_BTN_9.setDefault(True)
        self.FTab_BTN_9.setObjectName("FTab_BTN_9")
        self.FTab_verticalLayout.addWidget(self.FTab_BTN_9)
        # FTab BTN 10
        self.FTab_BTN_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FTab_BTN_10.setAutoDefault(False)
        self.FTab_BTN_10.setDefault(True)
        self.FTab_BTN_10.setObjectName("FTab_BTN_10")
        self.FTab_verticalLayout.addWidget(self.FTab_BTN_10)
        # FTab Notes
        self.FTab_Notes_TB = QtWidgets.QTextBrowser(self.FTab_tab)
        self.FTab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
        self.FTab_Notes_TB.setObjectName("FTab_Notes_TB")
        self.FTab_Notes_LBL = QtWidgets.QLabel(self.FTab_tab)
        self.FTab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
        self.FTab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.FTab_Notes_LBL.setObjectName("FTab_Notes_LBL")
        # FTab Picture
        self.FTab_Picture_LBL = QtWidgets.QLabel(self.FTab_tab)
        self.FTab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
        self.FTab_Picture_LBL.setText("")
        #self.FTab_Picture_LBL.setPixmap(
            #QtGui.QPixmap(firearms_df['Picture']))
        #    QtGui.QPixmap("./picts/Savage_110_Elite_Precision.png"))
        self.FTab_Picture_LBL.setScaledContents(True)
        self.FTab_Picture_LBL.setObjectName("FTab_Picture_LBL")
        # FTab ShowData
        self.FTab_ShowData_BTN = QtWidgets.QPushButton(self.FTab_tab)
        self.FTab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
        self.FTab_ShowData_BTN.setDefault(True)
        self.FTab_ShowData_BTN.setObjectName("FTab_ShowData_BTN")
        self.FTab_ShowData_BTN.clicked.connect(self.displayData_FTab)
        # FTab --------------------------------

        # BTab --------------------------------
        self.tabWidget.addTab(self.FTab_tab, "")
        self.BTab_tab = QtWidgets.QWidget()
        self.BTab_tab.setObjectName("BTab_tab")
        # BTab Setup
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.BTab_tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 60, 471, 928))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.BTab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_3)
        self.BTab_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.BTab_gridLayout.setObjectName("BTab_gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.BTab_gridLayout.addItem(spacerItem1, 34, 1, 1, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.BTab_tab)
        self.verticalLayoutWidget_3.setGeometry(
            QtCore.QRect(490, 80, 160, 361))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.BTab_verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.BTab_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.BTab_verticalLayout.setObjectName("BTab_verticalLayout")
        # BTab Combo Box
        self.BTab_Bullet_Combo = QtWidgets.QComboBox(self.BTab_tab)
        self.BTab_Bullet_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
        self.BTab_Bullet_Combo.setObjectName("BTab_Bullet_Combo")
        self.BTab_Bullet_Combo.addItems(bullets_list)
        self.BTab_Bullet_LBL = QtWidgets.QLabel(self.BTab_tab)
        self.BTab_Bullet_LBL.setGeometry(QtCore.QRect(20, 10, 451, 20))
        self.BTab_Bullet_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.BTab_Bullet_LBL.setObjectName("BTab_Bullet_LBL")
        # BTab Notes
        self.BTab_Notes_LBL = QtWidgets.QLabel(self.BTab_tab)
        self.BTab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
        self.BTab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.BTab_Notes_LBL.setObjectName("BTab_Notes_LBL")
        self.BTab_Notes_TB = QtWidgets.QTextBrowser(self.BTab_tab)
        self.BTab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
        self.BTab_Notes_TB.setObjectName("BTab_Notes_TB")
        # BTab Picture
        self.BTab_Picture_LBL = QtWidgets.QLabel(self.BTab_tab)
        self.BTab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
        self.BTab_Picture_LBL.setText("")
        self.BTab_Picture_LBL.setPixmap(
            QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
        self.BTab_Picture_LBL.setScaledContents(True)
        self.BTab_Picture_LBL.setObjectName("BTab_Picture_LBL")
        # BTab Name
        self.BTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Name_TB.setObjectName("BTab_Name_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Name_TB, 0, 1, 1, 1)
        self.BTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Name_LBL.setObjectName("BTab_Name_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Name_LBL, 0, 0, 1, 1)
        # BTab Manufacturer
        self.BTab_Manufacturer_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_3)
        self.BTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Manufacturer_TB.setObjectName("BTab_Manufacturer_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Manufacturer_TB, 1, 1, 1, 1)
        self.BTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Manufacturer_LBL.setObjectName("BTab_Manufacturer_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Manufacturer_LBL, 1, 0, 1, 1)
        # BTab Size_Inch
        self.BTab_Size_Inch_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_3)
        self.BTab_Size_Inch_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Size_Inch_TB.setObjectName("BTab_Size_Inch_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Size_Inch_TB, 2, 1, 1, 1)
        self.BTab_Size_Inch_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Size_Inch_LBL.setObjectName("BTab_Size_Inch_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Size_Inch_LBL, 2, 0, 1, 1)
        # BTab Size_mm
        self.BTab_Size_mm_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Size_mm_LBL.setObjectName("BTab_Size_mm_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Size_mm_LBL, 3, 0, 1, 1)
        self.BTab_Size_mm_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_3)
        self.BTab_Size_mm_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Size_mm_TB.setObjectName("BTab_Size_mm_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Size_mm_TB, 3, 1, 1, 1)
        # BTab Weight
        self.BTab_Weight_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Weight_LBL.setObjectName("BTab_Weight_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Weight_LBL, 4, 0, 1, 1)
        self.BTab_Weight_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Weight_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Weight_TB.setObjectName("BTab_Weight_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Weight_TB, 4, 1, 1, 1)
        # BTab Type
        self.BTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Type_TB.setObjectName("BTab_Type_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Type_TB, 5, 1, 1, 1)
        self.BTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Type_LBL.setObjectName("BTab_Type_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Type_LBL, 5, 0, 1, 1)
        # BTab SKU
        self.BTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_SKU_LBL.setObjectName("BTab_SKU_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_SKU_LBL, 6, 0, 1, 1)
        self.BTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_SKU_TB.setObjectName("BTab_SKU_TB")
        self.BTab_gridLayout.addWidget(self.BTab_SKU_TB, 6, 1, 1, 1)
        # BTab Caliber
        self.BTab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Caliber_LBL.setObjectName("BTab_Caliber_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Caliber_LBL, 7, 0, 1, 1)
        self.BTab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Caliber_TB.setObjectName("BTab_Caliber_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Caliber_TB, 7, 1, 1, 1)
        # BTab BBase
        self.BTab_BBase_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_BBase_LBL.setObjectName("BTab_BBase_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_BBase_LBL, 8, 0, 1, 1)
        self.BTab_BBase_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_BBase_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_BBase_TB.setObjectName("BTab_BBase_TB")
        self.BTab_gridLayout.addWidget(self.BTab_BBase_TB, 8, 1, 1, 1)
        # BTab BC
        self.BTab_BC_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_BC_LBL.setObjectName("BTab_BC_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_BC_LBL, 9, 0, 1, 1)
        self.BTab_BC_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_BC_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_BC_TB.setObjectName("BTab_BC_TB")
        self.BTab_gridLayout.addWidget(self.BTab_BC_TB, 9, 1, 1, 1)
        # BTab Length
        self.BTab_Length_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Length_LBL.setObjectName("BTab_Length_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Length_LBL, 10, 0, 1, 1)
        self.BTab_Length_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_3)
        self.BTab_Length_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Length_TB.setObjectName("BTab_Length_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Length_TB, 10, 1, 1, 1)
        # BTab Slot 1
        self.BTab_Slot_1_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_1_LBL.setObjectName("BTab_Slot_1_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_1_LBL, 13, 0, 1, 1)
        self.BTab_Slot_1_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_1_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_1_TB.setObjectName("BTab_Slot_1_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_1_TB, 13, 1, 1, 1)
        # BTab Slot 2
        self.BTab_Slot_2_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_2_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_2_TB.setObjectName("BTab_Slot_2_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_2_TB, 14, 1, 1, 1)
        self.BTab_Slot_2_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_2_LBL.setObjectName("BTab_Slot_2_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_2_LBL, 14, 0, 1, 1)
        # BTab Slot 3
        self.BTab_Slot_3_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_3_LBL.setObjectName("BTab_Slot_3_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_3_LBL, 15, 0, 1, 1)
        self.BTab_Slot_3_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_3_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_3_TB.setObjectName("BTab_Slot_3_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_3_TB, 15, 1, 1, 1)
        # BTab Slot 4
        self.BTab_Slot_4_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_4_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_4_TB.setObjectName("BTab_Slot_4_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_4_TB, 16, 1, 1, 1)
        self.BTab_Slot_4_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_4_LBL.setObjectName("BTab_Slot_4_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_4_LBL, 16, 0, 1, 1)
        # BTab Slot 5
        self.BTab_Slot_5_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_5_LBL.setObjectName("BTab_Slot_5_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_5_LBL, 18, 0, 1, 1)
        self.BTab_Slot_5_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_5_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_5_TB.setObjectName("BTab_Slot_5_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_5_TB, 18, 1, 1, 1)
        # BTab Slot 6
        self.BTab_Slot_6_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_6_LBL.setObjectName("BTab_Slot_6_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_6_LBL, 19, 0, 1, 1)
        self.BTab_Slot_6_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_6_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_6_TB.setObjectName("BTab_Slot_6_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_6_TB, 19, 1, 1, 1)
        # BTab Slot 7
        self.BTab_Slot_7_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_7_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_7_TB.setObjectName("BTab_Slot_7_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_7_TB, 21, 1, 1, 1)
        self.BTab_Slot_7_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_7_LBL.setObjectName("BTab_Slot_7_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_7_LBL, 21, 0, 1, 1)
        # BTab Slot 8
        self.BTab_Slot_8_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_8_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_8_TB.setObjectName("BTab_Slot_8_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_8_TB, 23, 1, 1, 1)
        self.BTab_Slot_8_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_8_LBL.setObjectName("BTab_Slot_8_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_8_LBL, 23, 0, 1, 1)
        # BTab Slot 9
        self.BTab_Slot_9_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_9_LBL.setObjectName("BTab_Slot_9_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_9_LBL, 25, 0, 1, 1)
        self.BTab_Slot_9_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_9_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_9_TB.setObjectName("BTab_Slot_9_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_9_TB, 25, 1, 1, 1)
        # BTab Slot 10
        self.BTab_Slot_10_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_10_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_10_TB.setObjectName("BTab_Slot_10_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_10_TB, 26, 1, 1, 1)
        self.BTab_Slot_10_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_10_LBL.setObjectName("BTab_Slot_10_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_10_LBL, 26, 0, 1, 1)
        # BTab Slot 11
        self.BTab_Slot_11_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_11_LBL.setObjectName("BTab_Slot_11_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_11_LBL, 28, 0, 1, 1)
        self.BTab_Slot_11_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_11_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_11_TB.setObjectName("BTab_Slot_11_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_11_TB, 28, 1, 1, 1)
        # BTab Slot 12
        self.BTab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.BTab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_12_TB.setObjectName("BTab_Slot_12_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_12_TB, 30, 1, 1, 1)
        self.BTab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_12_LBL.setObjectName("BTab_Slot_12_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_12_LBL, 30, 0, 1, 1)
        # BTab Slot 13
        self.BTab_Slot_13_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.BTab_Slot_13_LBL.setObjectName("BTab_Slot_13_LBL")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_13_LBL, 11, 0, 1, 1)
        self.BTab_Slot_13_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_3)
        self.BTab_Slot_13_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.BTab_Slot_13_TB.setObjectName("BTab_Slot_13_TB")
        self.BTab_gridLayout.addWidget(self.BTab_Slot_13_TB, 11, 1, 1, 1)
        # BTab Show Data BTN
        self.BTab_ShowData_BTN = QtWidgets.QPushButton(self.BTab_tab)
        self.BTab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
        self.BTab_ShowData_BTN.setDefault(True)
        self.BTab_ShowData_BTN.setObjectName("BTab_ShowData_BTN")
        self.BTab_ShowData_BTN.clicked.connect(self.displayData_BTab)

        # BTab Add BTN
        self.BTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BTab_Add_BTN.setDefault(True)
        self.BTab_Add_BTN.setObjectName("BTab_Add_BTN")
        self.BTab_verticalLayout.addWidget(self.BTab_Add_BTN)
        # BTab View All BTN
        self.BTab_View_All_BTN = QtWidgets.QPushButton(
            self.verticalLayoutWidget_3)
        self.BTab_View_All_BTN.setAutoDefault(False)
        self.BTab_View_All_BTN.setDefault(True)
        self.BTab_View_All_BTN.setObjectName("BTab_View_All_BTN")
        self.BTab_verticalLayout.addWidget(self.BTab_View_All_BTN)
        self.BTab_ShowBullets_POP = ShowAllBullets_PopUp()
        self.BTab_View_All_BTN.clicked.connect(self.PopUp_ShowAllBullets)
        # BTab BTN 3
        self.BTab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BTab_BTN_3.setDefault(True)
        self.BTab_BTN_3.setObjectName("BTab_BTN_3")
        self.BTab_verticalLayout.addWidget(self.BTab_BTN_3)
        # BTab BTN 4
        self.BTab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BTab_BTN_4.setDefault(True)
        self.BTab_BTN_4.setObjectName("BTab_BTN_4")
        self.BTab_verticalLayout.addWidget(self.BTab_BTN_4)
        # BTab BTN 5
        self.BTab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BTab_BTN_5.setDefault(True)
        self.BTab_BTN_5.setObjectName("BTab_BTN_5")
        self.BTab_verticalLayout.addWidget(self.BTab_BTN_5)
        # BTab BTN 6
        self.BTab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BTab_BTN_6.setDefault(True)
        self.BTab_BTN_6.setObjectName("BTab_BTN_6")
        self.BTab_verticalLayout.addWidget(self.BTab_BTN_6)
        # BTab BTN 7
        self.BTab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BTab_BTN_7.setDefault(True)
        self.BTab_BTN_7.setObjectName("BTab_BTN_7")
        self.BTab_verticalLayout.addWidget(self.BTab_BTN_7)
        # BTab BTN 8
        self.BTab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BTab_BTN_8.setAutoDefault(False)
        self.BTab_BTN_8.setDefault(True)
        self.BTab_BTN_8.setObjectName("BTab_BTN_8")
        self.BTab_verticalLayout.addWidget(self.BTab_BTN_8)
        # BTab BTN 9
        self.BTab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BTab_BTN_9.setAutoDefault(False)
        self.BTab_BTN_9.setDefault(True)
        self.BTab_BTN_9.setObjectName("BTab_BTN_9")
        self.BTab_verticalLayout.addWidget(self.BTab_BTN_9)
        # BTab BTN 10
        self.BTab_BTN_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BTab_BTN_10.setAutoDefault(False)
        self.BTab_BTN_10.setDefault(True)
        self.BTab_BTN_10.setObjectName("BTab_BTN_10")
        self.BTab_verticalLayout.addWidget(self.BTab_BTN_10)
        # BTab Add Tab
        self.tabWidget.addTab(self.BTab_tab, "")
        # BTab --------------------------------

        # PTab --------------------------------
        self.PTab_tab = QtWidgets.QWidget()
        self.PTab_tab.setObjectName("PTab_tab")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.PTab_tab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 60, 471, 928))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.PTab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_4)
        self.PTab_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PTab_gridLayout.setObjectName("PTab_gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.PTab_gridLayout.addItem(spacerItem2, 34, 1, 1, 1)

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.PTab_tab)
        self.verticalLayoutWidget_4.setGeometry(
            QtCore.QRect(490, 80, 160, 361))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.PTab_verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_4)
        self.PTab_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.PTab_verticalLayout.setObjectName("PTab_verticalLayout")


        # PTab Powder ComboBox
        self.PTab_Powder_Combo = QtWidgets.QComboBox(self.PTab_tab)
        self.PTab_Powder_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
        self.PTab_Powder_Combo.setObjectName("PTab_Powder_Combo")
        self.PTab_Powder_Combo.addItems(powders_list)
        self.PTab_Powder_LBL = QtWidgets.QLabel(self.PTab_tab)
        self.PTab_Powder_LBL.setGeometry(QtCore.QRect(20, 10, 451, 20))
        self.PTab_Powder_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.PTab_Powder_LBL.setObjectName("PTab_Powder_LBL")
        # PTab Name
        self.PTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Type_TB.setObjectName("PTab_Type_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Type_TB, 0, 1, 1, 1)
        self.PTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Type_LBL.setObjectName("PTab_Type_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Type_LBL, 0, 0, 1, 1)
        # PTab Manufacturer
        self.PTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_SKU_TB.setObjectName("PTab_SKU_TB")
        self.PTab_gridLayout.addWidget(self.PTab_SKU_TB, 1, 1, 1, 1)
        self.PTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_SKU_LBL.setObjectName("PTab_SKU_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_SKU_LBL, 1, 0, 1, 1)
        # PTab Relative Burn Rate
        self.PTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Name_TB.setObjectName("PTab_Name_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Name_TB, 2, 1, 1, 1)
        self.PTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Name_LBL.setObjectName("PTab_Name_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Name_LBL, 2, 0, 1, 1)
        # PTab Weapon Use
        self.PTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Manufacturer_LBL.setObjectName("PTab_Manufacturer_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Manufacturer_LBL, 3, 0, 1, 1)
        self.PTab_Manufacturer_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_4)
        self.PTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Manufacturer_TB.setObjectName("PTab_Manufacturer_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Manufacturer_TB, 3, 1, 1, 1)
        # PTab Density lb
        self.PTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Model_LBL.setObjectName("PTab_Model_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Model_LBL, 4, 0, 1, 1)
        self.PTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Model_TB.setObjectName("PTab_Model_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Model_TB, 4, 1, 1, 1)
        # PTab Bulk Density
        self.PTab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Caliber_LBL.setObjectName("PTab_Caliber_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Caliber_LBL, 5, 0, 1, 1)
        self.PTab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Caliber_TB.setObjectName("PTab_Caliber_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Caliber_TB, 5, 1, 1, 1)
        # PTab SKU
        self.PTab_OLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_OLen_LBL.setObjectName("PTab_OLen_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_OLen_LBL, 6, 0, 1, 1)
        self.PTab_OLen_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_OLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_OLen_TB.setObjectName("PTab_OLen_TB")
        self.PTab_gridLayout.addWidget(self.PTab_OLen_TB, 6, 1, 1, 1)
        # BTab Slot 8
        self.PTab_BarrelLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_BarrelLen_LBL.setObjectName("PTab_BarrelLen_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_BarrelLen_LBL, 7, 0, 1, 1)
        self.PTab_BarrelLen_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_4)
        self.PTab_BarrelLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_BarrelLen_TB.setObjectName("PTab_BarrelLen_TB")
        self.PTab_gridLayout.addWidget(self.PTab_BarrelLen_TB, 7, 1, 1, 1)
        # BTab Slot 9
        self.PTab_Weight_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Weight_LBL.setObjectName("PTab_Weight_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Weight_LBL, 8, 0, 1, 1)
        self.PTab_Weight_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Weight_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Weight_TB.setObjectName("PTab_Weight_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Weight_TB, 8, 1, 1, 1)
        # BTab Slot 10
        self.PTab_Action_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Action_LBL.setObjectName("PTab_Action_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Action_LBL, 9, 0, 1, 1)
        self.PTab_Action_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Action_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Action_TB.setObjectName("PTab_Action_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Action_TB, 9, 1, 1, 1)
        # BTab Slot 11
        self.PTab_TwistRate_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_TwistRate_LBL.setObjectName("PTab_TwistRate_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_TwistRate_LBL, 10, 0, 1, 1)
        self.PTab_TwistRate_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_4)
        self.PTab_TwistRate_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_TwistRate_TB.setObjectName("PTab_TwistRate_TB")
        self.PTab_gridLayout.addWidget(self.PTab_TwistRate_TB, 10, 1, 1, 1)
        # BTab Slot 12
        self.PTab_ThreadSize_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_ThreadSize_LBL.setObjectName("PTab_ThreadSize_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_ThreadSize_LBL, 11, 0, 1, 1)
        self.PTab_ThreadSize_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_4)
        self.PTab_ThreadSize_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_ThreadSize_TB.setObjectName("PTab_ThreadSize_TB")
        self.PTab_gridLayout.addWidget(self.PTab_ThreadSize_TB, 11, 1, 1, 1)
        # BTab Slot 13
        self.PTab_Slot_1_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_1_LBL.setObjectName("PTab_Slot_1_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_1_LBL, 13, 0, 1, 1)
        self.PTab_Slot_1_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_1_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_1_TB.setObjectName("PTab_Slot_1_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_1_TB, 13, 1, 1, 1)
        # BTab Slot 14
        self.PTab_Slot_2_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_2_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_2_TB.setObjectName("PTab_Slot_2_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_2_TB, 14, 1, 1, 1)
        self.PTab_Slot_2_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_2_LBL.setObjectName("PTab_Slot_2_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_2_LBL, 14, 0, 1, 1)
        # BTab Slot 15
        self.PTab_Slot_3_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_3_LBL.setObjectName("PTab_Slot_3_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_3_LBL, 15, 0, 1, 1)
        self.PTab_Slot_3_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_3_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_3_TB.setObjectName("PTab_Slot_3_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_3_TB, 15, 1, 1, 1)
        # BTab Slot 16
        self.PTab_Slot_4_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_4_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_4_TB.setObjectName("PTab_Slot_4_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_4_TB, 16, 1, 1, 1)
        self.PTab_Slot_4_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_4_LBL.setObjectName("PTab_Slot_4_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_4_LBL, 16, 0, 1, 1)
        # BTab Slot 17
        self.PTab_Slot_5_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_5_LBL.setObjectName("PTab_Slot_5_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_5_LBL, 18, 0, 1, 1)
        self.PTab_Slot_5_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_5_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_5_TB.setObjectName("PTab_Slot_5_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_5_TB, 18, 1, 1, 1)
        # BTab Slot 18
        self.PTab_Slot_6_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_6_LBL.setObjectName("PTab_Slot_6_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_6_LBL, 19, 0, 1, 1)
        self.PTab_Slot_6_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_6_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_6_TB.setObjectName("PTab_Slot_6_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_6_TB, 19, 1, 1, 1)
        # BTab Slot 19
        self.PTab_Slot_7_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_7_LBL.setObjectName("PTab_Slot_7_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_7_LBL, 21, 0, 1, 1)
        self.PTab_Slot_7_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_7_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_7_TB.setObjectName("PTab_Slot_7_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_7_TB, 21, 1, 1, 1)
        # BTab Slot 20
        self.PTab_Slot_8_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_8_LBL.setObjectName("PTab_Slot_8_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_8_LBL, 23, 0, 1, 1)
        self.PTab_Slot_8_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_8_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_8_TB.setObjectName("PTab_Slot_8_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_8_TB, 23, 1, 1, 1)
        # BTab Slot 21
        self.PTab_Slot_9_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_9_LBL.setObjectName("PTab_Slot_9_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_9_LBL, 25, 0, 1, 1)
        self.PTab_Slot_9_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_9_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_9_TB.setObjectName("PTab_Slot_9_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_9_TB, 25, 1, 1, 1)
        # BTab Slot 22
        self.PTab_Slot_10_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_10_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_10_TB.setObjectName("PTab_Slot_10_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_10_TB, 26, 1, 1, 1)
        self.PTab_Slot_10_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_10_LBL.setObjectName("PTab_Slot_10_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_10_LBL, 26, 0, 1, 1)
        # BTab Slot 23
        self.PTab_Slot_11_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_11_LBL.setObjectName("PTab_Slot_11_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_11_LBL, 28, 0, 1, 1)
        self.PTab_Slot_11_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_11_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_11_TB.setObjectName("PTab_Slot_11_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_11_TB, 28, 1, 1, 1)
        # BTab Slot 24
        self.PTab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
        self.PTab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PTab_Slot_12_TB.setObjectName("PTab_Slot_12_TB")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_12_TB, 30, 1, 1, 1)
        self.PTab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.PTab_Slot_12_LBL.setObjectName("PTab_Slot_12_LBL")
        self.PTab_gridLayout.addWidget(self.PTab_Slot_12_LBL, 30, 0, 1, 1)
        # BTab Notes
        self.PTab_Notes_LBL = QtWidgets.QLabel(self.PTab_tab)
        self.PTab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
        self.PTab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.PTab_Notes_LBL.setObjectName("PTab_Notes_LBL")
        self.PTab_Notes_TB = QtWidgets.QTextBrowser(self.PTab_tab)
        self.PTab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
        self.PTab_Notes_TB.setObjectName("PTab_Notes_TB")
        # BTab Picture
        self.PTab_Picture_LBL = QtWidgets.QLabel(self.PTab_tab)
        self.PTab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
        self.PTab_Picture_LBL.setText("")
        self.PTab_Picture_LBL.setPixmap(
            QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
        self.PTab_Picture_LBL.setScaledContents(True)
        self.PTab_Picture_LBL.setObjectName("PTab_Picture_LBL")
        # BTab Show Data BTN
        self.PTab_ShowData_BTN = QtWidgets.QPushButton(self.PTab_tab)
        self.PTab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
        self.PTab_ShowData_BTN.setDefault(True)
        self.PTab_ShowData_BTN.setObjectName("PTab_ShowData_BTN")
        # BTab Add BTN
        self.PTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.PTab_Add_BTN.setDefault(True)
        self.PTab_Add_BTN.setObjectName("PTab_Add_BTN")
        self.PTab_verticalLayout.addWidget(self.PTab_Add_BTN)
        # PTab View All BTN
        self.PTab_View_All_BTN = QtWidgets.QPushButton(
            self.verticalLayoutWidget_4)
        self.PTab_View_All_BTN.setAutoDefault(False)
        self.PTab_View_All_BTN.setDefault(True)
        self.PTab_View_All_BTN.setObjectName("PTab_View_All_BTN")
        self.PTab_verticalLayout.addWidget(self.PTab_View_All_BTN)
        self.PTab_ShowPowders_POP = ShowAllPowders_PopUp()
        self.PTab_View_All_BTN.clicked.connect(self.PopUp_ShowAllPowders)
        # PTab BTN 3
        self.PTab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.PTab_BTN_3.setDefault(True)
        self.PTab_BTN_3.setObjectName("PTab_BTN_3")
        self.PTab_verticalLayout.addWidget(self.PTab_BTN_3)
        # PTab BTN 4
        self.PTab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.PTab_BTN_4.setDefault(True)
        self.PTab_BTN_4.setObjectName("PTab_BTN_4")
        self.PTab_verticalLayout.addWidget(self.PTab_BTN_4)
        # PTab BTN 5
        self.PTab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.PTab_BTN_5.setDefault(True)
        self.PTab_BTN_5.setObjectName("PTab_BTN_5")
        self.PTab_verticalLayout.addWidget(self.PTab_BTN_5)
        # PTab BTN 6
        self.PTab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.PTab_BTN_6.setDefault(True)
        self.PTab_BTN_6.setObjectName("PTab_BTN_6")
        self.PTab_verticalLayout.addWidget(self.PTab_BTN_6)
        # PTab BTN 7
        self.PTab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.PTab_BTN_7.setDefault(True)
        self.PTab_BTN_7.setObjectName("PTab_BTN_7")
        self.PTab_verticalLayout.addWidget(self.PTab_BTN_7)
        # PTab BTN 8
        self.PTab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.PTab_BTN_8.setAutoDefault(False)
        self.PTab_BTN_8.setDefault(True)
        self.PTab_BTN_8.setObjectName("PTab_BTN_8")
        self.PTab_verticalLayout.addWidget(self.PTab_BTN_8)
        # PTab BTN 9
        self.PTab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.PTab_BTN_9.setAutoDefault(False)
        self.PTab_BTN_9.setDefault(True)
        self.PTab_BTN_9.setObjectName("PTab_BTN_9")
        self.PTab_verticalLayout.addWidget(self.PTab_BTN_9)
        # PTab BTN 10
        self.PTab_BTN_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.PTab_BTN_10.setAutoDefault(False)
        self.PTab_BTN_10.setDefault(True)
        self.PTab_BTN_10.setObjectName("PTab_BTN_10")
        self.PTab_verticalLayout.addWidget(self.PTab_BTN_10)

        self.tabWidget.addTab(self.PTab_tab, "")
        # PTab --------------------------------

        # CTab --------------------------------
        self.CTab_tab = QtWidgets.QWidget()
        self.CTab_tab.setObjectName("CTab_tab")
        self.CTab_Notes_LBL = QtWidgets.QLabel(self.CTab_tab)
        self.CTab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
        self.CTab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.CTab_Notes_LBL.setObjectName("CTab_Notes_LBL")
        # CTab ComboBox
        self.CTab_Cases_Combo = QtWidgets.QComboBox(self.CTab_tab)
        self.CTab_Cases_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
        self.CTab_Cases_Combo.setObjectName("CTab_Cases_Combo")
        self.CTab_Cases_Combo.addItems(cases_list)

        self.CTab_Firearm_LBL = QtWidgets.QLabel(self.CTab_tab)
        self.CTab_Firearm_LBL.setGeometry(QtCore.QRect(20, 10, 451, 20))
        self.CTab_Firearm_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.CTab_Firearm_LBL.setObjectName("CTab_Firearm_LBL")
        self.CTab_Notes_TB = QtWidgets.QTextBrowser(self.CTab_tab)
        self.CTab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
        self.CTab_Notes_TB.setObjectName("CTab_Notes_TB")
        self.CTab_ShowData_BTN = QtWidgets.QPushButton(self.CTab_tab)
        self.CTab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
        self.CTab_ShowData_BTN.setDefault(True)
        self.CTab_ShowData_BTN.setObjectName("CTab_ShowData_BTN")
        self.CTab_Picture_LBL = QtWidgets.QLabel(self.CTab_tab)
        self.CTab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
        self.CTab_Picture_LBL.setText("")
        self.CTab_Picture_LBL.setPixmap(
            QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
        self.CTab_Picture_LBL.setScaledContents(True)
        self.CTab_Picture_LBL.setObjectName("CTab_Picture_LBL")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.CTab_tab)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(10, 60, 471, 928))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.CTab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_5)
        self.CTab_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.CTab_gridLayout.setObjectName("CTab_gridLayout")
        self.CTab_TwistRate_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_TwistRate_LBL.setObjectName("CTab_TwistRate_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_TwistRate_LBL, 10, 0, 1, 1)
        self.CTab_ThreadSize_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_ThreadSize_LBL.setObjectName("CTab_ThreadSize_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_ThreadSize_LBL, 11, 0, 1, 1)
        self.CTab_Slot_10_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_10_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_10_TB.setObjectName("CTab_Slot_10_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_10_TB, 26, 1, 1, 1)
        self.CTab_Slot_8_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_8_LBL.setObjectName("CTab_Slot_8_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_8_LBL, 23, 0, 1, 1)
        self.CTab_Slot_7_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_7_LBL.setObjectName("CTab_Slot_7_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_7_LBL, 21, 0, 1, 1)
        self.CTab_TwistRate_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_5)
        self.CTab_TwistRate_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_TwistRate_TB.setObjectName("CTab_TwistRate_TB")
        self.CTab_gridLayout.addWidget(self.CTab_TwistRate_TB, 10, 1, 1, 1)
        self.CTab_Slot_1_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_1_LBL.setObjectName("CTab_Slot_1_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_1_LBL, 13, 0, 1, 1)
        self.CTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Name_TB.setObjectName("CTab_Name_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Name_TB, 2, 1, 1, 1)
        self.CTab_ThreadSize_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_5)
        self.CTab_ThreadSize_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_ThreadSize_TB.setObjectName("CTab_ThreadSize_TB")
        self.CTab_gridLayout.addWidget(self.CTab_ThreadSize_TB, 11, 1, 1, 1)
        self.CTab_Slot_4_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_4_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_4_TB.setObjectName("CTab_Slot_4_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_4_TB, 16, 1, 1, 1)
        self.CTab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_12_TB.setObjectName("CTab_Slot_12_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_12_TB, 30, 1, 1, 1)
        self.CTab_Slot_3_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_3_LBL.setObjectName("CTab_Slot_3_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_3_LBL, 15, 0, 1, 1)
        self.CTab_Slot_11_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_11_LBL.setObjectName("CTab_Slot_11_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_11_LBL, 28, 0, 1, 1)
        self.CTab_Slot_9_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_9_LBL.setObjectName("CTab_Slot_9_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_9_LBL, 25, 0, 1, 1)
        self.CTab_Slot_9_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_9_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_9_TB.setObjectName("CTab_Slot_9_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_9_TB, 25, 1, 1, 1)
        self.CTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Type_TB.setObjectName("CTab_Type_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Type_TB, 0, 1, 1, 1)
        self.CTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_SKU_TB.setObjectName("CTab_SKU_TB")
        self.CTab_gridLayout.addWidget(self.CTab_SKU_TB, 1, 1, 1, 1)
        self.CTab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Caliber_LBL.setObjectName("CTab_Caliber_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Caliber_LBL, 5, 0, 1, 1)
        self.CTab_OLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_OLen_LBL.setObjectName("CTab_OLen_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_OLen_LBL, 6, 0, 1, 1)
        self.CTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_SKU_LBL.setObjectName("CTab_SKU_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_SKU_LBL, 1, 0, 1, 1)
        self.CTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Type_LBL.setObjectName("CTab_Type_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Type_LBL, 0, 0, 1, 1)
        self.CTab_Weight_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Weight_LBL.setObjectName("CTab_Weight_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Weight_LBL, 8, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.CTab_gridLayout.addItem(spacerItem3, 34, 1, 1, 1)
        self.CTab_Action_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Action_LBL.setObjectName("CTab_Action_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Action_LBL, 9, 0, 1, 1)
        self.CTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Name_LBL.setObjectName("CTab_Name_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Name_LBL, 2, 0, 1, 1)
        self.CTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Manufacturer_LBL.setObjectName("CTab_Manufacturer_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Manufacturer_LBL, 3, 0, 1, 1)
        self.CTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Model_LBL.setObjectName("CTab_Model_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Model_LBL, 4, 0, 1, 1)
        self.CTab_BarrelLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_BarrelLen_LBL.setObjectName("CTab_BarrelLen_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_BarrelLen_LBL, 7, 0, 1, 1)
        self.CTab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_12_LBL.setObjectName("CTab_Slot_12_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_12_LBL, 30, 0, 1, 1)
        self.CTab_Manufacturer_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_5)
        self.CTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Manufacturer_TB.setObjectName("CTab_Manufacturer_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Manufacturer_TB, 3, 1, 1, 1)
        self.CTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Model_TB.setObjectName("CTab_Model_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Model_TB, 4, 1, 1, 1)
        self.CTab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Caliber_TB.setObjectName("CTab_Caliber_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Caliber_TB, 5, 1, 1, 1)
        self.CTab_OLen_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_OLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_OLen_TB.setObjectName("CTab_OLen_TB")
        self.CTab_gridLayout.addWidget(self.CTab_OLen_TB, 6, 1, 1, 1)
        self.CTab_BarrelLen_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_5)
        self.CTab_BarrelLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_BarrelLen_TB.setObjectName("CTab_BarrelLen_TB")
        self.CTab_gridLayout.addWidget(self.CTab_BarrelLen_TB, 7, 1, 1, 1)
        self.CTab_Weight_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Weight_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Weight_TB.setObjectName("CTab_Weight_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Weight_TB, 8, 1, 1, 1)
        self.CTab_Action_TBL = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Action_TBL.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Action_TBL.setObjectName("CTab_Action_TBL")
        self.CTab_gridLayout.addWidget(self.CTab_Action_TBL, 9, 1, 1, 1)
        self.CTab_Slot_10_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_10_LBL.setObjectName("CTab_Slot_10_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_10_LBL, 26, 0, 1, 1)
        self.CTab_Slot_7_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_7_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_7_TB.setObjectName("CTab_Slot_7_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_7_TB, 21, 1, 1, 1)
        self.CTab_Slot_2_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_2_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_2_TB.setObjectName("CTab_Slot_2_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_2_TB, 14, 1, 1, 1)
        self.CTab_Slot_4_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_4_LBL.setObjectName("CTab_Slot_4_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_4_LBL, 16, 0, 1, 1)
        self.CTab_Slot_2_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_2_LBL.setObjectName("CTab_Slot_2_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_2_LBL, 14, 0, 1, 1)
        self.CTab_Slot_6_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_6_LBL.setObjectName("CTab_Slot_6_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_6_LBL, 19, 0, 1, 1)
        self.CTab_Slot_8_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_8_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_8_TB.setObjectName("CTab_Slot_8_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_8_TB, 23, 1, 1, 1)
        self.CTab_Slot_3_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_3_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_3_TB.setObjectName("CTab_Slot_3_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_3_TB, 15, 1, 1, 1)
        self.CTab_Slot_5_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.CTab_Slot_5_LBL.setObjectName("CTab_Slot_5_LBL")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_5_LBL, 18, 0, 1, 1)
        self.CTab_Slot_1_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_1_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_1_TB.setObjectName("CTab_Slot_1_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_1_TB, 13, 1, 1, 1)
        self.CTab_Slot_5_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_5_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_5_TB.setObjectName("CTab_Slot_5_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_5_TB, 18, 1, 1, 1)
        self.CTab_Slot_6_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_6_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_6_TB.setObjectName("CTab_Slot_6_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_6_TB, 19, 1, 1, 1)
        self.CTab_Slot_11_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
        self.CTab_Slot_11_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.CTab_Slot_11_TB.setObjectName("CTab_Slot_11_TB")
        self.CTab_gridLayout.addWidget(self.CTab_Slot_11_TB, 28, 1, 1, 1)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.CTab_tab)
        self.verticalLayoutWidget_5.setGeometry(
            QtCore.QRect(490, 80, 160, 361))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.CTab_verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_5)
        self.CTab_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CTab_verticalLayout.setObjectName("CTab_verticalLayout")
        self.CTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CTab_Add_BTN.setDefault(True)
        self.CTab_Add_BTN.setObjectName("CTab_Add_BTN")
        self.CTab_verticalLayout.addWidget(self.CTab_Add_BTN)
        # CTab View All BTN
        self.CTab_View_All_BTN = QtWidgets.QPushButton(
            self.verticalLayoutWidget_5)
        self.CTab_View_All_BTN.setAutoDefault(False)
        self.CTab_View_All_BTN.setDefault(True)
        self.CTab_View_All_BTN.setObjectName("CTab_View_All_BTN")
        self.CTab_verticalLayout.addWidget(self.CTab_View_All_BTN)
        self.CTab_ShowCases_POP = ShowAllCases_PopUp()
        self.CTab_View_All_BTN.clicked.connect(self.PopUp_ShowAllCases)

        self.CTab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CTab_BTN_3.setDefault(True)
        self.CTab_BTN_3.setObjectName("CTab_BTN_3")
        self.CTab_verticalLayout.addWidget(self.CTab_BTN_3)
        self.CTab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CTab_BTN_4.setDefault(True)
        self.CTab_BTN_4.setObjectName("CTab_BTN_4")
        self.CTab_verticalLayout.addWidget(self.CTab_BTN_4)
        self.CTab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CTab_BTN_5.setDefault(True)
        self.CTab_BTN_5.setObjectName("CTab_BTN_5")
        self.CTab_verticalLayout.addWidget(self.CTab_BTN_5)
        self.CTab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CTab_BTN_6.setDefault(True)
        self.CTab_BTN_6.setObjectName("CTab_BTN_6")
        self.CTab_verticalLayout.addWidget(self.CTab_BTN_6)
        self.CTab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CTab_BTN_7.setDefault(True)
        self.CTab_BTN_7.setObjectName("CTab_BTN_7")
        self.CTab_verticalLayout.addWidget(self.CTab_BTN_7)
        self.CTab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CTab_BTN_8.setAutoDefault(False)
        self.CTab_BTN_8.setDefault(True)
        self.CTab_BTN_8.setObjectName("CTab_BTN_8")
        self.CTab_verticalLayout.addWidget(self.CTab_BTN_8)
        self.CTab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CTab_BTN_9.setAutoDefault(False)
        self.CTab_BTN_9.setDefault(True)
        self.CTab_BTN_9.setObjectName("CTab_BTN_9")
        self.CTab_verticalLayout.addWidget(self.CTab_BTN_9)
        self.CTab_BTN_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CTab_BTN_10.setAutoDefault(False)
        self.CTab_BTN_10.setDefault(True)
        self.CTab_BTN_10.setObjectName("CTab_BTN_10")
        self.CTab_verticalLayout.addWidget(self.CTab_BTN_10)
        self.tabWidget.addTab(self.CTab_tab, "")
        # CTab --------------------------------

        # PRTab --------------------------------
        self.PRTab_tab = QtWidgets.QWidget()
        self.PRTab_tab.setObjectName("PRTab_tab")
        self.PRTab_Notes_LBL = QtWidgets.QLabel(self.PRTab_tab)
        self.PRTab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
        self.PRTab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.PRTab_Notes_LBL.setObjectName("PRTab_Notes_LBL")
        self.PRTab_Firearm_Combo = QtWidgets.QComboBox(self.PRTab_tab)
        self.PRTab_Firearm_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
        self.PRTab_Firearm_Combo.setObjectName("PRTab_Firearm_Combo")
        self.PRTab_Firearm_LBL = QtWidgets.QLabel(self.PRTab_tab)
        self.PRTab_Firearm_LBL.setGeometry(QtCore.QRect(20, 10, 451, 20))
        self.PRTab_Firearm_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.PRTab_Firearm_LBL.setObjectName("PRTab_Firearm_LBL")
        self.PRTab_Notes_TB = QtWidgets.QTextBrowser(self.PRTab_tab)
        self.PRTab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
        self.PRTab_Notes_TB.setObjectName("PRTab_Notes_TB")
        self.PRTab_ShowData_BTN = QtWidgets.QPushButton(self.PRTab_tab)
        self.PRTab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
        self.PRTab_ShowData_BTN.setDefault(True)
        self.PRTab_ShowData_BTN.setObjectName("PRTab_ShowData_BTN")
        self.PRTab_Picture_LBL = QtWidgets.QLabel(self.PRTab_tab)
        self.PRTab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
        self.PRTab_Picture_LBL.setText("")
        self.PRTab_Picture_LBL.setPixmap(
            QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
        self.PRTab_Picture_LBL.setScaledContents(True)
        self.PRTab_Picture_LBL.setObjectName("PRTab_Picture_LBL")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.PRTab_tab)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(10, 60, 471, 928))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.PRTab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_6)
        self.PRTab_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PRTab_gridLayout.setObjectName("PRTab_gridLayout")
        self.PRTab_TwistRate_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_TwistRate_LBL.setObjectName("PRTab_TwistRate_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_TwistRate_LBL, 10, 0, 1, 1)
        self.PRTab_ThreadSize_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_ThreadSize_LBL.setObjectName("PRTab_ThreadSize_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_ThreadSize_LBL, 11, 0, 1, 1)
        self.PRTab_Slot_10_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_10_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_10_TB.setObjectName("PRTab_Slot_10_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_10_TB, 26, 1, 1, 1)
        self.PRTab_Slot_8_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_8_LBL.setObjectName("PRTab_Slot_8_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_8_LBL, 23, 0, 1, 1)
        self.PRTab_Slot_7_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_7_LBL.setObjectName("PRTab_Slot_7_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_7_LBL, 21, 0, 1, 1)
        self.PRTab_TwistRate_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_6)
        self.PRTab_TwistRate_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_TwistRate_TB.setObjectName("PRTab_TwistRate_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_TwistRate_TB, 10, 1, 1, 1)
        self.PRTab_Slot_1_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_1_LBL.setObjectName("PRTab_Slot_1_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_1_LBL, 13, 0, 1, 1)
        self.PRTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Name_TB.setObjectName("PRTab_Name_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Name_TB, 2, 1, 1, 1)
        self.PRTab_ThreadSize_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_6)
        self.PRTab_ThreadSize_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_ThreadSize_TB.setObjectName("PRTab_ThreadSize_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_ThreadSize_TB, 11, 1, 1, 1)
        self.PRTab_Slot_4_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_4_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_4_TB.setObjectName("PRTab_Slot_4_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_4_TB, 16, 1, 1, 1)
        self.PRTab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_12_TB.setObjectName("PRTab_Slot_12_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_12_TB, 30, 1, 1, 1)
        self.PRTab_Slot_3_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_3_LBL.setObjectName("PRTab_Slot_3_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_3_LBL, 15, 0, 1, 1)
        self.PRTab_Slot_11_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_11_LBL.setObjectName("PRTab_Slot_11_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_11_LBL, 28, 0, 1, 1)
        self.PRTab_Slot_9_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_9_LBL.setObjectName("PRTab_Slot_9_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_9_LBL, 25, 0, 1, 1)
        self.PRTab_Slot_9_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_9_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_9_TB.setObjectName("PRTab_Slot_9_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_9_TB, 25, 1, 1, 1)
        self.PRTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Type_TB.setObjectName("PRTab_Type_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Type_TB, 0, 1, 1, 1)
        self.PRTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_SKU_TB.setObjectName("PRTab_SKU_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_SKU_TB, 1, 1, 1, 1)
        self.PRTab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Caliber_LBL.setObjectName("PRTab_Caliber_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Caliber_LBL, 5, 0, 1, 1)
        self.PRTab_OLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_OLen_LBL.setObjectName("PRTab_OLen_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_OLen_LBL, 6, 0, 1, 1)
        self.PRTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_SKU_LBL.setObjectName("PRTab_SKU_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_SKU_LBL, 1, 0, 1, 1)
        self.PRTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Type_LBL.setObjectName("PRTab_Type_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Type_LBL, 0, 0, 1, 1)
        self.PRTab_Weight_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Weight_LBL.setObjectName("PRTab_Weight_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Weight_LBL, 8, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.PRTab_gridLayout.addItem(spacerItem4, 34, 1, 1, 1)
        self.PRTab_Action_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Action_LBL.setObjectName("PRTab_Action_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Action_LBL, 9, 0, 1, 1)
        self.PRTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Name_LBL.setObjectName("PRTab_Name_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Name_LBL, 2, 0, 1, 1)
        self.PRTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Manufacturer_LBL.setObjectName("PRTab_Manufacturer_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Manufacturer_LBL, 3, 0, 1,
                                        1)
        self.PRTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Model_LBL.setObjectName("PRTab_Model_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Model_LBL, 4, 0, 1, 1)
        self.PRTab_BarrelLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_BarrelLen_LBL.setObjectName("PRTab_BarrelLen_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_BarrelLen_LBL, 7, 0, 1, 1)
        self.PRTab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_12_LBL.setObjectName("PRTab_Slot_12_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_12_LBL, 30, 0, 1, 1)
        self.PRTab_Manufacturer_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_6)
        self.PRTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Manufacturer_TB.setObjectName("PRTab_Manufacturer_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Manufacturer_TB, 3, 1, 1, 1)
        self.PRTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Model_TB.setObjectName("PRTab_Model_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Model_TB, 4, 1, 1, 1)
        self.PRTab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Caliber_TB.setObjectName("PRTab_Caliber_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Caliber_TB, 5, 1, 1, 1)
        self.PRTab_OLen_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_OLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_OLen_TB.setObjectName("PRTab_OLen_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_OLen_TB, 6, 1, 1, 1)
        self.PRTab_BarrelLen_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_6)
        self.PRTab_BarrelLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_BarrelLen_TB.setObjectName("PRTab_BarrelLen_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_BarrelLen_TB, 7, 1, 1, 1)
        self.PRTab_Weight_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Weight_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Weight_TB.setObjectName("PRTab_Weight_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Weight_TB, 8, 1, 1, 1)
        self.PRTab_Action_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Action_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Action_TB.setObjectName("PRTab_Action_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Action_TB, 9, 1, 1, 1)
        self.PRTab_Slot_10_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_10_LBL.setObjectName("PRTab_Slot_10_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_10_LBL, 26, 0, 1, 1)
        self.PRTab_Slot_7_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_7_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_7_TB.setObjectName("PRTab_Slot_7_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_7_TB, 21, 1, 1, 1)
        self.PRTab_Slot_2_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_2_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_2_TB.setObjectName("PRTab_Slot_2_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_2_TB, 14, 1, 1, 1)
        self.PRTab_Slot_4_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_4_LBL.setObjectName("PRTab_Slot_4_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_4_LBL, 16, 0, 1, 1)
        self.PRTab_Slot_2_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_2_LBL.setObjectName("PRTab_Slot_2_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_2_LBL, 14, 0, 1, 1)
        self.PRTab_Slot_6_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_6_LBL.setObjectName("PRTab_Slot_6_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_6_LBL, 19, 0, 1, 1)
        self.PRTab_Slot_8_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_8_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_8_TB.setObjectName("PRTab_Slot_8_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_8_TB, 23, 1, 1, 1)
        self.PRTab_Slot_3_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_3_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_3_TB.setObjectName("PRTab_Slot_3_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_3_TB, 15, 1, 1, 1)
        self.PRTab_Slot_5_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.PRTab_Slot_5_LBL.setObjectName("PRTab_Slot_5_LBL")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_5_LBL, 18, 0, 1, 1)
        self.PRTab_Slot_1_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_1_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_1_TB.setObjectName("PRTab_Slot_1_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_1_TB, 13, 1, 1, 1)
        self.PRTab_Slot_5_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_5_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_5_TB.setObjectName("PRTab_Slot_5_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_5_TB, 18, 1, 1, 1)
        self.PRTab_Slot_6_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_6_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_6_TB.setObjectName("PRTab_Slot_6_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_6_TB, 19, 1, 1, 1)
        self.PRTab_Slot_11_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
        self.PRTab_Slot_11_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.PRTab_Slot_11_TB.setObjectName("PRTab_Slot_11_TB")
        self.PRTab_gridLayout.addWidget(self.PRTab_Slot_11_TB, 28, 1, 1, 1)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.PRTab_tab)
        self.verticalLayoutWidget_6.setGeometry(
            QtCore.QRect(490, 80, 160, 361))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.PRTab_verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_6)
        self.PRTab_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.PRTab_verticalLayout.setObjectName("PRTab_verticalLayout")
        self.PRTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.PRTab_Add_BTN.setDefault(True)
        self.PRTab_Add_BTN.setObjectName("PRTab_Add_BTN")
        self.PRTab_verticalLayout.addWidget(self.PRTab_Add_BTN)
        self.PRTab_View_All_BTN = QtWidgets.QPushButton(
            self.verticalLayoutWidget_6)
        self.PRTab_View_All_BTN.setAutoDefault(False)
        self.PRTab_View_All_BTN.setDefault(True)
        self.PRTab_View_All_BTN.setObjectName("PRTab_View_All_BTN")
        self.PRTab_verticalLayout.addWidget(self.PRTab_View_All_BTN)
        self.PRTab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.PRTab_BTN_3.setDefault(True)
        self.PRTab_BTN_3.setObjectName("PRTab_BTN_3")
        self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_3)
        self.PRTab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.PRTab_BTN_4.setDefault(True)
        self.PRTab_BTN_4.setObjectName("PRTab_BTN_4")
        self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_4)
        self.PRTab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.PRTab_BTN_5.setDefault(True)
        self.PRTab_BTN_5.setObjectName("PRTab_BTN_5")
        self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_5)
        self.PRTab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.PRTab_BTN_6.setDefault(True)
        self.PRTab_BTN_6.setObjectName("PRTab_BTN_6")
        self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_6)
        self.PRTab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.PRTab_BTN_7.setDefault(True)
        self.PRTab_BTN_7.setObjectName("PRTab_BTN_7")
        self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_7)
        self.PRTab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.PRTab_BTN_8.setAutoDefault(False)
        self.PRTab_BTN_8.setDefault(True)
        self.PRTab_BTN_8.setObjectName("PRTab_BTN_8")
        self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_8)
        self.PRTab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.PRTab_BTN_9.setAutoDefault(False)
        self.PRTab_BTN_9.setDefault(True)
        self.PRTab_BTN_9.setObjectName("PRTab_BTN_9")
        self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_9)
        self.PRTab_BTN_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.PRTab_BTN_10.setAutoDefault(False)
        self.PRTab_BTN_10.setDefault(True)
        self.PRTab_BTN_10.setObjectName("PRTab_BTN_10")
        self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_10)
        self.tabWidget.addTab(self.PRTab_tab, "")
        # PRTab --------------------------------

        # DTab --------------------------------
        self.DTab_tab = QtWidgets.QWidget()
        self.DTab_tab.setObjectName("DTab_tab")
        self.DTab_Notes_LBL = QtWidgets.QLabel(self.DTab_tab)
        self.DTab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
        self.DTab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.DTab_Notes_LBL.setObjectName("DTab_Notes_LBL")
        self.DTab_Data_Combo = QtWidgets.QComboBox(self.DTab_tab)
        self.DTab_Data_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
        self.DTab_Data_Combo.setObjectName("DTab_Data_Combo")
        self.DTab_Firearm_LBL = QtWidgets.QLabel(self.DTab_tab)
        self.DTab_Firearm_LBL.setGeometry(QtCore.QRect(20, 10, 451, 20))
        self.DTab_Firearm_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.DTab_Firearm_LBL.setObjectName("DTab_Firearm_LBL")
        self.DTab_Notes_TB = QtWidgets.QTextBrowser(self.DTab_tab)
        self.DTab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
        self.DTab_Notes_TB.setObjectName("DTab_Notes_TB")
        self.DTab_ShowData_BTN = QtWidgets.QPushButton(self.DTab_tab)
        self.DTab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
        self.DTab_ShowData_BTN.setDefault(True)
        self.DTab_ShowData_BTN.setObjectName("DTab_ShowData_BTN")
        self.DTab_Picture_LBL = QtWidgets.QLabel(self.DTab_tab)
        self.DTab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
        self.DTab_Picture_LBL.setText("")
        self.DTab_Picture_LBL.setPixmap(
            QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
        self.DTab_Picture_LBL.setScaledContents(True)
        self.DTab_Picture_LBL.setObjectName("DTab_Picture_LBL")
        self.formLayoutWidget_7 = QtWidgets.QWidget(self.DTab_tab)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(10, 60, 471, 928))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")
        self.DTab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_7)
        self.DTab_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.DTab_gridLayout.setObjectName("DTab_gridLayout")
        self.DTab_TwistRate_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_TwistRate_LBL.setObjectName("DTab_TwistRate_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_TwistRate_LBL, 10, 0, 1, 1)
        self.DTab_ThreadSize_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_ThreadSize_LBL.setObjectName("DTab_ThreadSize_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_ThreadSize_LBL, 11, 0, 1, 1)
        self.DTab_Slot_10_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_10_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_10_TB.setObjectName("DTab_Slot_10_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_10_TB, 26, 1, 1, 1)
        self.DTab_Slot_8_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_8_LBL.setObjectName("DTab_Slot_8_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_8_LBL, 23, 0, 1, 1)
        self.DTab_Slot_7_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_7_LBL.setObjectName("DTab_Slot_7_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_7_LBL, 21, 0, 1, 1)
        self.DTab_TwistRate_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_7)
        self.DTab_TwistRate_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_TwistRate_TB.setObjectName("DTab_TwistRate_TB")
        self.DTab_gridLayout.addWidget(self.DTab_TwistRate_TB, 10, 1, 1, 1)
        self.DTab_Slot_1_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_1_LBL.setObjectName("DTab_Slot_1_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_1_LBL, 13, 0, 1, 1)
        self.DTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Name_TB.setObjectName("DTab_Name_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Name_TB, 2, 1, 1, 1)
        self.DTab_ThreadSize_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_7)
        self.DTab_ThreadSize_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_ThreadSize_TB.setObjectName("DTab_ThreadSize_TB")
        self.DTab_gridLayout.addWidget(self.DTab_ThreadSize_TB, 11, 1, 1, 1)
        self.DTab_Slot_4_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_4_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_4_TB.setObjectName("DTab_Slot_4_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_4_TB, 16, 1, 1, 1)
        self.DTab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_12_TB.setObjectName("DTab_Slot_12_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_12_TB, 30, 1, 1, 1)
        self.DTab_Slot_3_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_3_LBL.setObjectName("DTab_Slot_3_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_3_LBL, 15, 0, 1, 1)
        self.DTab_Slot_11_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_11_LBL.setObjectName("DTab_Slot_11_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_11_LBL, 28, 0, 1, 1)
        self.DTab_Slot_9_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_9_LBL.setObjectName("DTab_Slot_9_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_9_LBL, 25, 0, 1, 1)
        self.DTab_Slot_9_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_9_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_9_TB.setObjectName("DTab_Slot_9_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_9_TB, 25, 1, 1, 1)
        self.DTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Type_TB.setObjectName("DTab_Type_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Type_TB, 0, 1, 1, 1)
        self.DTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_SKU_TB.setObjectName("DTab_SKU_TB")
        self.DTab_gridLayout.addWidget(self.DTab_SKU_TB, 1, 1, 1, 1)
        self.DTab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Caliber_LBL.setObjectName("DTab_Caliber_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Caliber_LBL, 5, 0, 1, 1)
        self.DTab_OLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_OLen_LBL.setObjectName("DTab_OLen_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_OLen_LBL, 6, 0, 1, 1)
        self.DTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_SKU_LBL.setObjectName("DTab_SKU_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_SKU_LBL, 1, 0, 1, 1)
        self.DTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Type_LBL.setObjectName("DTab_Type_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Type_LBL, 0, 0, 1, 1)
        self.DTab_Weight_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Weight_LBL.setObjectName("DTab_Weight_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Weight_LBL, 8, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.DTab_gridLayout.addItem(spacerItem5, 34, 1, 1, 1)
        self.DTab_Action_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Action_LBL.setObjectName("DTab_Action_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Action_LBL, 9, 0, 1, 1)
        self.DTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Name_LBL.setObjectName("DTab_Name_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Name_LBL, 2, 0, 1, 1)
        self.DTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Manufacturer_LBL.setObjectName("DTab_Manufacturer_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Manufacturer_LBL, 3, 0, 1, 1)
        self.DTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Model_LBL.setObjectName("DTab_Model_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Model_LBL, 4, 0, 1, 1)
        self.DTab_BarrelLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_BarrelLen_LBL.setObjectName("DTab_BarrelLen_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_BarrelLen_LBL, 7, 0, 1, 1)
        self.DTab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_12_LBL.setObjectName("DTab_Slot_12_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_12_LBL, 30, 0, 1, 1)
        self.DTab_Manufacturer_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_7)
        self.DTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Manufacturer_TB.setObjectName("DTab_Manufacturer_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Manufacturer_TB, 3, 1, 1, 1)
        self.DTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Model_TB.setObjectName("DTab_Model_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Model_TB, 4, 1, 1, 1)
        self.DTab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Caliber_TB.setObjectName("DTab_Caliber_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Caliber_TB, 5, 1, 1, 1)
        self.DTab_OLen_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_OLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_OLen_TB.setObjectName("DTab_OLen_TB")
        self.DTab_gridLayout.addWidget(self.DTab_OLen_TB, 6, 1, 1, 1)
        self.DTab_BarrelLen_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_7)
        self.DTab_BarrelLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_BarrelLen_TB.setObjectName("DTab_BarrelLen_TB")
        self.DTab_gridLayout.addWidget(self.DTab_BarrelLen_TB, 7, 1, 1, 1)
        self.DTab_Weight_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Weight_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Weight_TB.setObjectName("DTab_Weight_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Weight_TB, 8, 1, 1, 1)
        self.DTab_Action_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Action_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Action_TB.setObjectName("DTab_Action_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Action_TB, 9, 1, 1, 1)
        self.DTab_Slot_10_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_10_LBL.setObjectName("DTab_Slot_10_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_10_LBL, 26, 0, 1, 1)
        self.DTab_Slot_7_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_7_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_7_TB.setObjectName("DTab_Slot_7_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_7_TB, 21, 1, 1, 1)
        self.DTab_Slot_2_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_2_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_2_TB.setObjectName("DTab_Slot_2_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_2_TB, 14, 1, 1, 1)
        self.DTab_Slot_4_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_4_LBL.setObjectName("DTab_Slot_4_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_4_LBL, 16, 0, 1, 1)
        self.DTab_Slot_2_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_2_LBL.setObjectName("DTab_Slot_2_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_2_LBL, 14, 0, 1, 1)
        self.DTab_Slot_6_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_6_LBL.setObjectName("DTab_Slot_6_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_6_LBL, 19, 0, 1, 1)
        self.DTab_Slot_8_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_8_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_8_TB.setObjectName("DTab_Slot_8_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_8_TB, 23, 1, 1, 1)
        self.DTab_Slot_3_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_3_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_3_TB.setObjectName("DTab_Slot_3_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_3_TB, 15, 1, 1, 1)
        self.DTab_Slot_5_LBL = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.DTab_Slot_5_LBL.setObjectName("DTab_Slot_5_LBL")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_5_LBL, 18, 0, 1, 1)
        self.DTab_Slot_1_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_1_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_1_TB.setObjectName("DTab_Slot_1_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_1_TB, 13, 1, 1, 1)
        self.DTab_Slot_5_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_5_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_5_TB.setObjectName("DTab_Slot_5_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_5_TB, 18, 1, 1, 1)
        self.DTab_Slot_6_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_6_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_6_TB.setObjectName("DTab_Slot_6_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_6_TB, 19, 1, 1, 1)
        self.DTab_Slot_11_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
        self.DTab_Slot_11_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.DTab_Slot_11_TB.setObjectName("DTab_Slot_11_TB")
        self.DTab_gridLayout.addWidget(self.DTab_Slot_11_TB, 28, 1, 1, 1)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.DTab_tab)
        self.verticalLayoutWidget_7.setGeometry(
            QtCore.QRect(490, 80, 160, 361))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.DTab_verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_7)
        self.DTab_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.DTab_verticalLayout.setObjectName("DTab_verticalLayout")
        self.DTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.DTab_Add_BTN.setDefault(True)
        self.DTab_Add_BTN.setObjectName("DTab_Add_BTN")
        self.DTab_verticalLayout.addWidget(self.DTab_Add_BTN)
        self.DTab_View_All_BTN = QtWidgets.QPushButton(
            self.verticalLayoutWidget_7)
        self.DTab_View_All_BTN.setAutoDefault(False)
        self.DTab_View_All_BTN.setDefault(True)
        self.DTab_View_All_BTN.setObjectName("DTab_View_All_BTN")
        self.DTab_verticalLayout.addWidget(self.DTab_View_All_BTN)
        self.DTab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.DTab_BTN_3.setDefault(True)
        self.DTab_BTN_3.setObjectName("DTab_BTN_3")
        self.DTab_verticalLayout.addWidget(self.DTab_BTN_3)
        self.DTab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.DTab_BTN_4.setDefault(True)
        self.DTab_BTN_4.setObjectName("DTab_BTN_4")
        self.DTab_verticalLayout.addWidget(self.DTab_BTN_4)
        self.DTab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.DTab_BTN_5.setDefault(True)
        self.DTab_BTN_5.setObjectName("DTab_BTN_5")
        self.DTab_verticalLayout.addWidget(self.DTab_BTN_5)
        self.DTab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.DTab_BTN_6.setDefault(True)
        self.DTab_BTN_6.setObjectName("DTab_BTN_6")
        self.DTab_verticalLayout.addWidget(self.DTab_BTN_6)
        self.DTab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.DTab_BTN_7.setDefault(True)
        self.DTab_BTN_7.setObjectName("DTab_BTN_7")
        self.DTab_verticalLayout.addWidget(self.DTab_BTN_7)
        self.DTab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.DTab_BTN_8.setAutoDefault(False)
        self.DTab_BTN_8.setDefault(True)
        self.DTab_BTN_8.setObjectName("DTab_BTN_8")
        self.DTab_verticalLayout.addWidget(self.DTab_BTN_8)
        self.DTab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.DTab_BTN_9.setAutoDefault(False)
        self.DTab_BTN_9.setDefault(True)
        self.DTab_BTN_9.setObjectName("DTab_BTN_9")
        self.DTab_verticalLayout.addWidget(self.DTab_BTN_9)
        self.DTab_BTN_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.DTab_BTN_10.setAutoDefault(False)
        self.DTab_BTN_10.setDefault(True)
        self.DTab_BTN_10.setObjectName("DTab_BTN_10")
        self.DTab_verticalLayout.addWidget(self.DTab_BTN_10)
        self.tabWidget.addTab(self.DTab_tab, "")
        # DTab --------------------------------

        # STab --------------------------------
        self.STab_tab = QtWidgets.QWidget()
        self.STab_tab.setObjectName("STab_tab")
        self.STab_Notes_LBL = QtWidgets.QLabel(self.STab_tab)
        self.STab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
        self.STab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.STab_Notes_LBL.setObjectName("STab_Notes_LBL")
        self.STab_SILIENCER_Combo = QtWidgets.QComboBox(self.STab_tab)
        self.STab_SILIENCER_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
        self.STab_SILIENCER_Combo.setObjectName("STab_SILIENCER_Combo")
        self.STab_SILIENCER_LBL = QtWidgets.QLabel(self.STab_tab)
        self.STab_SILIENCER_LBL.setGeometry(QtCore.QRect(20, 10, 451, 20))
        self.STab_SILIENCER_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.STab_SILIENCER_LBL.setObjectName("STab_SILIENCER_LBL")
        self.STab_Notes_TB = QtWidgets.QTextBrowser(self.STab_tab)
        self.STab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
        self.STab_Notes_TB.setObjectName("STab_Notes_TB")
        self.STab_ShowData_BTN = QtWidgets.QPushButton(self.STab_tab)
        self.STab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
        self.STab_ShowData_BTN.setDefault(True)
        self.STab_ShowData_BTN.setObjectName("STab_ShowData_BTN")
        self.STab_Picture_LBL = QtWidgets.QLabel(self.STab_tab)
        self.STab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
        self.STab_Picture_LBL.setText("")
        self.STab_Picture_LBL.setPixmap(
            QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
        self.STab_Picture_LBL.setScaledContents(True)
        self.STab_Picture_LBL.setObjectName("STab_Picture_LBL")
        self.formLayoutWidget_8 = QtWidgets.QWidget(self.STab_tab)
        self.formLayoutWidget_8.setGeometry(QtCore.QRect(10, 60, 471, 928))
        self.formLayoutWidget_8.setObjectName("formLayoutWidget_8")
        self.STab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_8)
        self.STab_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.STab_gridLayout.setObjectName("STab_gridLayout")
        self.STab_TwistRate_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_TwistRate_LBL.setObjectName("STab_TwistRate_LBL")
        self.STab_gridLayout.addWidget(self.STab_TwistRate_LBL, 10, 0, 1, 1)
        self.STab_ThreadSize_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_ThreadSize_LBL.setObjectName("STab_ThreadSize_LBL")
        self.STab_gridLayout.addWidget(self.STab_ThreadSize_LBL, 11, 0, 1, 1)
        self.STab_Slot_10_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_10_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_10_TB.setObjectName("STab_Slot_10_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_10_TB, 26, 1, 1, 1)
        self.STab_Slot_8_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_8_LBL.setObjectName("STab_Slot_8_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_8_LBL, 23, 0, 1, 1)
        self.STab_Slot_7_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_7_LBL.setObjectName("STab_Slot_7_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_7_LBL, 21, 0, 1, 1)
        self.STab_TwistRate_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_8)
        self.STab_TwistRate_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_TwistRate_TB.setObjectName("STab_TwistRate_TB")
        self.STab_gridLayout.addWidget(self.STab_TwistRate_TB, 10, 1, 1, 1)
        self.STab_Slot_1_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_1_LBL.setObjectName("STab_Slot_1_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_1_LBL, 13, 0, 1, 1)
        self.STab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Name_TB.setObjectName("STab_Name_TB")
        self.STab_gridLayout.addWidget(self.STab_Name_TB, 2, 1, 1, 1)
        self.STab_ThreadSize_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_8)
        self.STab_ThreadSize_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_ThreadSize_TB.setObjectName("STab_ThreadSize_TB")
        self.STab_gridLayout.addWidget(self.STab_ThreadSize_TB, 11, 1, 1, 1)
        self.STab_Slot_4_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_4_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_4_TB.setObjectName("STab_Slot_4_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_4_TB, 16, 1, 1, 1)
        self.STab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_12_TB.setObjectName("STab_Slot_12_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_12_TB, 30, 1, 1, 1)
        self.STab_Slot_3_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_3_LBL.setObjectName("STab_Slot_3_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_3_LBL, 15, 0, 1, 1)
        self.STab_Slot_11_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_11_LBL.setObjectName("STab_Slot_11_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_11_LBL, 28, 0, 1, 1)
        self.STab_Slot_9_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_9_LBL.setObjectName("STab_Slot_9_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_9_LBL, 25, 0, 1, 1)
        self.STab_Slot_9_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_9_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_9_TB.setObjectName("STab_Slot_9_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_9_TB, 25, 1, 1, 1)
        self.STab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Type_TB.setObjectName("STab_Type_TB")
        self.STab_gridLayout.addWidget(self.STab_Type_TB, 0, 1, 1, 1)
        self.STab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_SKU_TB.setObjectName("STab_SKU_TB")
        self.STab_gridLayout.addWidget(self.STab_SKU_TB, 1, 1, 1, 1)
        self.STab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Caliber_LBL.setObjectName("STab_Caliber_LBL")
        self.STab_gridLayout.addWidget(self.STab_Caliber_LBL, 5, 0, 1, 1)
        self.STab_OLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_OLen_LBL.setObjectName("STab_OLen_LBL")
        self.STab_gridLayout.addWidget(self.STab_OLen_LBL, 6, 0, 1, 1)
        self.STab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_SKU_LBL.setObjectName("STab_SKU_LBL")
        self.STab_gridLayout.addWidget(self.STab_SKU_LBL, 1, 0, 1, 1)
        self.STab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Type_LBL.setObjectName("STab_Type_LBL")
        self.STab_gridLayout.addWidget(self.STab_Type_LBL, 0, 0, 1, 1)
        self.STab_Weight_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Weight_LBL.setObjectName("STab_Weight_LBL")
        self.STab_gridLayout.addWidget(self.STab_Weight_LBL, 8, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.STab_gridLayout.addItem(spacerItem6, 34, 1, 1, 1)
        self.STab_Action_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Action_LBL.setObjectName("STab_Action_LBL")
        self.STab_gridLayout.addWidget(self.STab_Action_LBL, 9, 0, 1, 1)
        self.STab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Name_LBL.setObjectName("STab_Name_LBL")
        self.STab_gridLayout.addWidget(self.STab_Name_LBL, 2, 0, 1, 1)
        self.STab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Manufacturer_LBL.setObjectName("STab_Manufacturer_LBL")
        self.STab_gridLayout.addWidget(self.STab_Manufacturer_LBL, 3, 0, 1, 1)
        self.STab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Model_LBL.setObjectName("STab_Model_LBL")
        self.STab_gridLayout.addWidget(self.STab_Model_LBL, 4, 0, 1, 1)
        self.STab_BarrelLen_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_BarrelLen_LBL.setObjectName("STab_BarrelLen_LBL")
        self.STab_gridLayout.addWidget(self.STab_BarrelLen_LBL, 7, 0, 1, 1)
        self.STab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_12_LBL.setObjectName("STab_Slot_12_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_12_LBL, 30, 0, 1, 1)
        self.STab_Manufacturer_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_8)
        self.STab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Manufacturer_TB.setObjectName("STab_Manufacturer_TB")
        self.STab_gridLayout.addWidget(self.STab_Manufacturer_TB, 3, 1, 1, 1)
        self.STab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Model_TB.setObjectName("STab_Model_TB")
        self.STab_gridLayout.addWidget(self.STab_Model_TB, 4, 1, 1, 1)
        self.STab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Caliber_TB.setObjectName("STab_Caliber_TB")
        self.STab_gridLayout.addWidget(self.STab_Caliber_TB, 5, 1, 1, 1)
        self.STab_OLen_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_OLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_OLen_TB.setObjectName("STab_OLen_TB")
        self.STab_gridLayout.addWidget(self.STab_OLen_TB, 6, 1, 1, 1)
        self.STab_BarrelLen_TB = QtWidgets.QTextBrowser(
            self.formLayoutWidget_8)
        self.STab_BarrelLen_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_BarrelLen_TB.setObjectName("STab_BarrelLen_TB")
        self.STab_gridLayout.addWidget(self.STab_BarrelLen_TB, 7, 1, 1, 1)
        self.STab_Weight_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Weight_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Weight_TB.setObjectName("STab_Weight_TB")
        self.STab_gridLayout.addWidget(self.STab_Weight_TB, 8, 1, 1, 1)
        self.STab_Action_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Action_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Action_TB.setObjectName("STab_Action_TB")
        self.STab_gridLayout.addWidget(self.STab_Action_TB, 9, 1, 1, 1)
        self.STab_Slot_10_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_10_LBL.setObjectName("STab_Slot_10_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_10_LBL, 26, 0, 1, 1)
        self.STab_Slot_7_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_7_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_7_TB.setObjectName("STab_Slot_7_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_7_TB, 21, 1, 1, 1)
        self.STab_Slot_2_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_2_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_2_TB.setObjectName("STab_Slot_2_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_2_TB, 14, 1, 1, 1)
        self.STab_Slot_4_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_4_LBL.setObjectName("STab_Slot_4_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_4_LBL, 16, 0, 1, 1)
        self.STab_Slot_2_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_2_LBL.setObjectName("STab_Slot_2_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_2_LBL, 14, 0, 1, 1)
        self.STab_Slot_6_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_6_LBL.setObjectName("STab_Slot_6_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_6_LBL, 19, 0, 1, 1)
        self.STab_Slot_8_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_8_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_8_TB.setObjectName("STab_Slot_8_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_8_TB, 23, 1, 1, 1)
        self.STab_Slot_3_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_3_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_3_TB.setObjectName("STab_Slot_3_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_3_TB, 15, 1, 1, 1)
        self.STab_Slot_5_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.STab_Slot_5_LBL.setObjectName("STab_Slot_5_LBL")
        self.STab_gridLayout.addWidget(self.STab_Slot_5_LBL, 18, 0, 1, 1)
        self.STab_Slot_1_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_1_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_1_TB.setObjectName("STab_Slot_1_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_1_TB, 13, 1, 1, 1)
        self.STab_Slot_5_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_5_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_5_TB.setObjectName("STab_Slot_5_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_5_TB, 18, 1, 1, 1)
        self.STab_Slot_6_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_6_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_6_TB.setObjectName("STab_Slot_6_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_6_TB, 19, 1, 1, 1)
        self.STab_Slot_11_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
        self.STab_Slot_11_TB.setMaximumSize(QtCore.QSize(362, 26))
        self.STab_Slot_11_TB.setObjectName("STab_Slot_11_TB")
        self.STab_gridLayout.addWidget(self.STab_Slot_11_TB, 28, 1, 1, 1)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.STab_tab)
        self.verticalLayoutWidget_8.setGeometry(
            QtCore.QRect(490, 80, 160, 361))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.STab_verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_8)
        self.STab_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.STab_verticalLayout.setObjectName("STab_verticalLayout")
        self.STab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.STab_Add_BTN.setDefault(True)
        self.STab_Add_BTN.setObjectName("STab_Add_BTN")
        self.STab_verticalLayout.addWidget(self.STab_Add_BTN)
        # STab Show All BTN
        self.STab_View_All_BTN = QtWidgets.QPushButton(
            self.verticalLayoutWidget_8)
        self.STab_View_All_BTN.setAutoDefault(False)
        self.STab_View_All_BTN.setDefault(True)
        self.STab_View_All_BTN.setObjectName("STab_View_All_BTN")
        self.STab_verticalLayout.addWidget(self.STab_View_All_BTN)
        self.STab_ShowSilencers_POP = ShowAllSilencers_PopUp()
        self.STab_View_All_BTN.clicked.connect(self.PopUp_ShowAllSilencers)

        self.STab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.STab_BTN_3.setDefault(True)
        self.STab_BTN_3.setObjectName("STab_BTN_3")
        self.STab_verticalLayout.addWidget(self.STab_BTN_3)
        self.STab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.STab_BTN_4.setDefault(True)
        self.STab_BTN_4.setObjectName("STab_BTN_4")
        self.STab_verticalLayout.addWidget(self.STab_BTN_4)
        self.STab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.STab_BTN_5.setDefault(True)
        self.STab_BTN_5.setObjectName("STab_BTN_5")
        self.STab_verticalLayout.addWidget(self.STab_BTN_5)
        self.STab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.STab_BTN_6.setDefault(True)
        self.STab_BTN_6.setObjectName("STab_BTN_6")
        self.STab_verticalLayout.addWidget(self.STab_BTN_6)
        self.STab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.STab_BTN_7.setDefault(True)
        self.STab_BTN_7.setObjectName("STab_BTN_7")
        self.STab_verticalLayout.addWidget(self.STab_BTN_7)
        self.STab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.STab_BTN_8.setAutoDefault(False)
        self.STab_BTN_8.setDefault(True)
        self.STab_BTN_8.setObjectName("STab_BTN_8")
        self.STab_verticalLayout.addWidget(self.STab_BTN_8)
        self.STab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.STab_BTN_9.setAutoDefault(False)
        self.STab_BTN_9.setDefault(True)
        self.STab_BTN_9.setObjectName("STab_BTN_9")
        self.STab_verticalLayout.addWidget(self.STab_BTN_9)
        self.STab_BTN_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.STab_BTN_10.setAutoDefault(False)
        self.STab_BTN_10.setDefault(True)
        self.STab_BTN_10.setObjectName("STab_BTN_10")
        self.STab_verticalLayout.addWidget(self.STab_BTN_10)
        self.tabWidget.addTab(self.STab_tab, "")
        # STab --------------------------------

        # MTab --------------------------------
        self.MTab_tab = QtWidgets.QWidget()
        self.MTab_tab.setObjectName("MTab_tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.MTab_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1001, 781))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MTab_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MTab_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MTab_gridLayout.setObjectName("MTab_gridLayout")
        self.MTab_ShotsOverTime_BTN = QtWidgets.QPushButton(
            self.gridLayoutWidget)
        self.MTab_ShotsOverTime_BTN.setDefault(True)
        self.MTab_ShotsOverTime_BTN.setObjectName("MTab_ShotsOverTime_BTN")
        self.MTab_gridLayout.addWidget(self.MTab_ShotsOverTime_BTN, 1, 4, 1, 1)
        self.MTab_Plot_Shots_Powder_Charge = QtWidgets.QPushButton(
            self.gridLayoutWidget)
        self.MTab_Plot_Shots_Powder_Charge.setDefault(True)
        self.MTab_Plot_Shots_Powder_Charge.setObjectName(
            "MTab_Plot_Shots_Powder_Charge")
        self.MTab_gridLayout.addWidget(self.MTab_Plot_Shots_Powder_Charge, 0,
                                       3, 1, 1)
        self.MTab_BTN_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_20.setDefault(True)
        self.MTab_BTN_20.setObjectName("MTab_BTN_20")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_20, 3, 4, 1, 1)
        self.MTab_BTN_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_23.setDefault(True)
        self.MTab_BTN_23.setObjectName("MTab_BTN_23")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_23, 4, 2, 1, 1)
        self.MTab_BTN_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_2.setDefault(True)
        self.MTab_BTN_2.setObjectName("MTab_BTN_2")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_2, 0, 1, 1, 1)
        self.MTab_BTN_30 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_30.setDefault(True)
        self.MTab_BTN_30.setObjectName("MTab_BTN_30")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_30, 5, 4, 1, 1)
        self.MTab_BTN_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_11.setDefault(True)
        self.MTab_BTN_11.setObjectName("MTab_BTN_11")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_11, 2, 0, 1, 1)
        self.MTab_BTN_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_21.setDefault(True)
        self.MTab_BTN_21.setObjectName("MTab_BTN_21")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_21, 4, 0, 1, 1)
        self.MTab_BTN_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_7.setDefault(True)
        self.MTab_BTN_7.setObjectName("MTab_BTN_7")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_7, 1, 1, 1, 1)
        self.MTab_BTN_31 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_31.setDefault(True)
        self.MTab_BTN_31.setObjectName("MTab_BTN_31")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_31, 6, 0, 1, 1)
        self.MTab_BTN_26 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_26.setDefault(True)
        self.MTab_BTN_26.setObjectName("MTab_BTN_26")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_26, 5, 0, 1, 1)
        self.MTab_BTN_41 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_41.setDefault(True)
        self.MTab_BTN_41.setObjectName("MTab_BTN_41")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_41, 8, 0, 1, 1)
        self.MTab_BTN_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_9.setDefault(True)
        self.MTab_BTN_9.setObjectName("MTab_BTN_9")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_9, 1, 3, 1, 1)
        self.MTab_BTN_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_22.setDefault(True)
        self.MTab_BTN_22.setObjectName("MTab_BTN_22")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_22, 4, 1, 1, 1)
        self.MTab_BTN_25 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_25.setDefault(True)
        self.MTab_BTN_25.setObjectName("MTab_BTN_25")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_25, 4, 4, 1, 1)
        self.MTab_BTN_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_12.setDefault(True)
        self.MTab_BTN_12.setObjectName("MTab_BTN_12")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_12, 2, 1, 1, 1)
        self.MTab_BTN_29 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_29.setDefault(True)
        self.MTab_BTN_29.setObjectName("MTab_BTN_29")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_29, 5, 3, 1, 1)
        self.MTab_BTN_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_15.setDefault(True)
        self.MTab_BTN_15.setObjectName("MTab_BTN_15")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_15, 2, 4, 1, 1)
        self.MTab_BTN_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_3.setDefault(True)
        self.MTab_BTN_3.setObjectName("MTab_BTN_3")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_3, 0, 2, 1, 1)
        self.MTab_Plot_Powder_Speed_Multi = QtWidgets.QPushButton(
            self.gridLayoutWidget)
        self.MTab_Plot_Powder_Speed_Multi.setDefault(True)
        self.MTab_Plot_Powder_Speed_Multi.setObjectName(
            "MTab_Plot_Powder_Speed_Multi")
        self.MTab_gridLayout.addWidget(self.MTab_Plot_Powder_Speed_Multi, 0, 0,
                                       1, 1)
        self.MTab_ShotsPerFirearm_BTN = QtWidgets.QPushButton(
            self.gridLayoutWidget)
        self.MTab_ShotsPerFirearm_BTN.setDefault(True)
        self.MTab_ShotsPerFirearm_BTN.setObjectName("MTab_ShotsPerFirearm_BTN")
        self.MTab_gridLayout.addWidget(self.MTab_ShotsPerFirearm_BTN, 0, 4, 1,
                                       1)
        self.MTab_BTN_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_14.setDefault(True)
        self.MTab_BTN_14.setObjectName("MTab_BTN_14")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_14, 2, 3, 1, 1)
        self.MTab_BTN_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_18.setDefault(True)
        self.MTab_BTN_18.setObjectName("MTab_BTN_18")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_18, 3, 2, 1, 1)
        self.MTab_BTN_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_8.setDefault(True)
        self.MTab_BTN_8.setObjectName("MTab_BTN_8")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_8, 1, 2, 1, 1)
        self.MTab_BTN_27 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_27.setDefault(True)
        self.MTab_BTN_27.setObjectName("MTab_BTN_27")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_27, 5, 1, 1, 1)
        self.MTab_BTN_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_19.setDefault(True)
        self.MTab_BTN_19.setObjectName("MTab_BTN_19")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_19, 3, 3, 1, 1)
        self.MTab_BTN_24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_24.setDefault(True)
        self.MTab_BTN_24.setObjectName("MTab_BTN_24")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_24, 4, 3, 1, 1)
        self.MTab_BTN_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_17.setDefault(True)
        self.MTab_BTN_17.setObjectName("MTab_BTN_17")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_17, 3, 1, 1, 1)
        self.MTab_Plot_Powder_Speed_Single = QtWidgets.QPushButton(
            self.gridLayoutWidget)
        self.MTab_Plot_Powder_Speed_Single.setDefault(True)
        self.MTab_Plot_Powder_Speed_Single.setObjectName(
            "MTab_Plot_Powder_Speed_Single")
        self.MTab_gridLayout.addWidget(self.MTab_Plot_Powder_Speed_Single, 1,
                                       0, 1, 1)
        self.MTab_BTN_36 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_36.setDefault(True)
        self.MTab_BTN_36.setObjectName("MTab_BTN_36")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_36, 7, 0, 1, 1)
        self.MTab_BTN_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_16.setDefault(True)
        self.MTab_BTN_16.setObjectName("MTab_BTN_16")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_16, 3, 0, 1, 1)
        self.MTab_BTN_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_13.setDefault(True)
        self.MTab_BTN_13.setObjectName("MTab_BTN_13")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_13, 2, 2, 1, 1)
        self.MTab_BTN_28 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_28.setDefault(True)
        self.MTab_BTN_28.setObjectName("MTab_BTN_28")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_28, 5, 2, 1, 1)
        self.MTab_BTN_46 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_46.setDefault(True)
        self.MTab_BTN_46.setObjectName("MTab_BTN_46")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_46, 9, 0, 1, 1)
        self.MTab_BTN_32 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_32.setDefault(True)
        self.MTab_BTN_32.setObjectName("MTab_BTN_32")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_32, 6, 1, 1, 1)
        self.MTab_BTN_37 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_37.setDefault(True)
        self.MTab_BTN_37.setObjectName("MTab_BTN_37")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_37, 7, 1, 1, 1)
        self.MTab_BTN_42 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_42.setDefault(True)
        self.MTab_BTN_42.setObjectName("MTab_BTN_42")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_42, 8, 1, 1, 1)
        self.MTab_BTN_47 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_47.setDefault(True)
        self.MTab_BTN_47.setObjectName("MTab_BTN_47")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_47, 9, 1, 1, 1)
        self.MTab_BTN_33 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_33.setDefault(True)
        self.MTab_BTN_33.setObjectName("MTab_BTN_33")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_33, 6, 2, 1, 1)
        self.MTab_BTN_38 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_38.setDefault(True)
        self.MTab_BTN_38.setObjectName("MTab_BTN_38")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_38, 7, 2, 1, 1)
        self.MTab_BTN_43 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_43.setDefault(True)
        self.MTab_BTN_43.setObjectName("MTab_BTN_43")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_43, 8, 2, 1, 1)
        self.MTab_BTN_48 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_48.setDefault(True)
        self.MTab_BTN_48.setObjectName("MTab_BTN_48")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_48, 9, 2, 1, 1)
        self.MTab_BTN_34 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_34.setDefault(True)
        self.MTab_BTN_34.setObjectName("MTab_BTN_34")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_34, 6, 3, 1, 1)
        self.MTab_BTN_39 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_39.setDefault(True)
        self.MTab_BTN_39.setObjectName("MTab_BTN_39")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_39, 7, 3, 1, 1)
        self.MTab_BTN_44 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_44.setDefault(True)
        self.MTab_BTN_44.setObjectName("MTab_BTN_44")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_44, 8, 3, 1, 1)
        self.MTab_BTN_49 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_49.setDefault(True)
        self.MTab_BTN_49.setObjectName("MTab_BTN_49")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_49, 9, 3, 1, 1)
        self.MTab_BTN_35 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_35.setDefault(True)
        self.MTab_BTN_35.setObjectName("MTab_BTN_35")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_35, 6, 4, 1, 1)
        self.MTab_BTN_40 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_40.setDefault(True)
        self.MTab_BTN_40.setObjectName("MTab_BTN_40")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_40, 7, 4, 1, 1)
        self.MTab_BTN_45 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_45.setDefault(True)
        self.MTab_BTN_45.setObjectName("MTab_BTN_45")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_45, 8, 4, 1, 1)
        self.MTab_BTN_50 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MTab_BTN_50.setDefault(True)
        self.MTab_BTN_50.setObjectName("MTab_BTN_50")
        self.MTab_gridLayout.addWidget(self.MTab_BTN_50, 9, 4, 1, 1)
        self.tabWidget.addTab(self.MTab_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # MTab --------------------------------

        self.retranslateUi(MainWindow)
        # Set opening tab to Index 0 (Firearms)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FTab_TwistRate_LBL.setText(_translate("MainWindow", "Twist Rate"))
        self.FTab_ThreadSize_LBL.setText(
            _translate("MainWindow", "Thread Size"))
        self.FTab_Slot_8_LBL.setText(_translate("MainWindow", "Slot 8"))
        self.FTab_Slot_7_LBL.setText(_translate("MainWindow", "Slot 7"))
        self.FTab_Slot_1_LBL.setText(_translate("MainWindow", "Slot 1"))
        self.FTab_Slot_3_LBL.setText(_translate("MainWindow", "Slot 3"))
        self.FTab_Slot_11_LBL.setText(_translate("MainWindow", "Slot 11"))
        self.FTab_Slot_9_LBL.setText(_translate("MainWindow", "Slot 9"))
        self.FTab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
        self.FTab_OLen_LBL.setText(_translate("MainWindow", "Overall Length"))
        self.FTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
        self.FTab_Type_LBL.setText(_translate("MainWindow", "Type"))
        self.FTab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
        self.FTab_Action_LBL.setText(_translate("MainWindow", "Action Type"))
        self.FTab_Name_LBL.setText(_translate("MainWindow", "Name"))
        self.FTab_Manufacturer_LBL.setText(
            _translate("MainWindow", "Manufacturer"))
        self.FTab_Model_LBL.setText(_translate("MainWindow", "Model"))
        self.FTab_BarrelLen_LBL.setText(
            _translate("MainWindow", "Barrel Length"))
        self.FTab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
        self.FTab_Slot_10_LBL.setText(_translate("MainWindow", "Slot 10"))
        self.FTab_Slot_4_LBL.setText(_translate("MainWindow", "Slot 4"))
        self.FTab_Slot_2_LBL.setText(_translate("MainWindow", "Slot 2"))
        self.FTab_Slot_6_LBL.setText(_translate("MainWindow", "Slot 6"))
        self.FTab_Slot_5_LBL.setText(_translate("MainWindow", "Slot 5"))
        self.FTab_Firearm_LBL.setText(_translate("MainWindow", "Firearm"))
        self.FTab_Add_BTN.setText(_translate("MainWindow", "Add Firearm"))
        self.FTab_View_All_BTN.setText(
            _translate("MainWindow", "View All Firearms"))
        self.FTab_BTN_3.setText(_translate("MainWindow", "Button 3"))
        self.FTab_BTN_4.setText(_translate("MainWindow", "Button 4"))
        self.FTab_BTN_5.setText(_translate("MainWindow", "Button 5"))
        self.FTab_BTN_6.setText(_translate("MainWindow", "Button 6"))
        self.FTab_BTN_7.setText(_translate("MainWindow", "Button 7"))
        self.FTab_BTN_8.setText(_translate("MainWindow", "Button 8"))
        self.FTab_BTN_9.setText(_translate("MainWindow", "Button 9"))
        self.FTab_BTN_10.setText(_translate("MainWindow", "Button 10"))
        self.FTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
        self.FTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FTab_tab),
                                  _translate("MainWindow", "Firearms"))
        # BTab-------------------------
        self.BTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
        self.BTab_Bullet_LBL.setText(_translate("MainWindow", "Bullet"))
        self.BTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
        self.BTab_Length_LBL.setText(_translate("MainWindow", "Length"))
        self.BTab_Slot_13_LBL.setText(
            _translate("MainWindow", "Slot_13"))
        self.BTab_Slot_8_LBL.setText(_translate("MainWindow", "Slot 8"))
        self.BTab_Slot_7_LBL.setText(_translate("MainWindow", "Slot 7"))
        self.BTab_Slot_1_LBL.setText(_translate("MainWindow", "Slot 1"))
        self.BTab_Slot_3_LBL.setText(_translate("MainWindow", "Slot 3"))
        self.BTab_Slot_11_LBL.setText(_translate("MainWindow", "Slot 11"))
        self.BTab_Slot_9_LBL.setText(_translate("MainWindow", "Slot 9"))
        self.BTab_Type_LBL.setText(_translate("MainWindow", "Type"))
        self.BTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
        self.BTab_Manufacturer_LBL.setText(
            _translate("MainWindow", "Manufacturer"))
        self.BTab_Name_LBL.setText(_translate("MainWindow", "Name"))
        self.BTab_BBase_LBL.setText(_translate("MainWindow", "Bullet Base"))
        self.BTab_BC_LBL.setText(_translate("MainWindow", "BC"))
        self.BTab_Size_Inch_LBL.setText(_translate("MainWindow", "Size_Inch"))
        self.BTab_Size_mm_LBL.setText(_translate("MainWindow", "Size_mm"))
        self.BTab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
        self.BTab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
        self.BTab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
        self.BTab_Slot_10_LBL.setText(_translate("MainWindow", "Slot 10"))
        self.BTab_Slot_4_LBL.setText(_translate("MainWindow", "Slot 4"))
        self.BTab_Slot_2_LBL.setText(_translate("MainWindow", "Slot 2"))
        self.BTab_Slot_6_LBL.setText(_translate("MainWindow", "Slot 6"))
        self.BTab_Slot_5_LBL.setText(_translate("MainWindow", "Slot 5"))
        self.BTab_Add_BTN.setText(_translate("MainWindow", "Add Bullet"))
        self.BTab_View_All_BTN.setText(
            _translate("MainWindow", "View All Bullets"))
        self.BTab_BTN_3.setText(_translate("MainWindow", "Button 3"))
        self.BTab_BTN_4.setText(_translate("MainWindow", "Button 4"))
        self.BTab_BTN_5.setText(_translate("MainWindow", "Button 5"))
        self.BTab_BTN_6.setText(_translate("MainWindow", "Button 6"))
        self.BTab_BTN_7.setText(_translate("MainWindow", "Button 7"))
        self.BTab_BTN_8.setText(_translate("MainWindow", "Button 8"))
        self.BTab_BTN_9.setText(_translate("MainWindow", "Button 9"))
        self.BTab_BTN_10.setText(_translate("MainWindow", "Button 10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BTab_tab),
                                  _translate("MainWindow", "Bullets"))
        self.PTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
        self.PTab_Powder_LBL.setText(_translate("MainWindow", "Powder"))
        self.PTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
        self.PTab_TwistRate_LBL.setText(_translate("MainWindow", "Twist Rate"))
        self.PTab_ThreadSize_LBL.setText(
            _translate("MainWindow", "Thread Size"))
        self.PTab_Slot_8_LBL.setText(_translate("MainWindow", "Slot 8"))
        self.PTab_Slot_7_LBL.setText(_translate("MainWindow", "Slot 7"))
        self.PTab_Slot_1_LBL.setText(_translate("MainWindow", "Slot 1"))
        self.PTab_Slot_3_LBL.setText(_translate("MainWindow", "Slot 3"))
        self.PTab_Slot_11_LBL.setText(_translate("MainWindow", "Slot 11"))
        self.PTab_Slot_9_LBL.setText(_translate("MainWindow", "Slot 9"))
        self.PTab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
        self.PTab_OLen_LBL.setText(_translate("MainWindow", "Overall Length"))
        self.PTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
        self.PTab_Type_LBL.setText(_translate("MainWindow", "Type"))
        self.PTab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
        self.PTab_Action_LBL.setText(_translate("MainWindow", "Action Type"))
        self.PTab_Name_LBL.setText(_translate("MainWindow", "Name"))
        self.PTab_Manufacturer_LBL.setText(
            _translate("MainWindow", "Manufacturer"))
        self.PTab_Model_LBL.setText(_translate("MainWindow", "Model"))
        self.PTab_BarrelLen_LBL.setText(
            _translate("MainWindow", "Barrel Length"))
        self.PTab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
        self.PTab_Slot_10_LBL.setText(_translate("MainWindow", "Slot 10"))
        self.PTab_Slot_4_LBL.setText(_translate("MainWindow", "Slot 4"))
        self.PTab_Slot_2_LBL.setText(_translate("MainWindow", "Slot 2"))
        self.PTab_Slot_6_LBL.setText(_translate("MainWindow", "Slot 6"))
        self.PTab_Slot_5_LBL.setText(_translate("MainWindow", "Slot 5"))
        self.PTab_Add_BTN.setText(_translate("MainWindow", "Add Firearm"))
        self.PTab_View_All_BTN.setText(
            _translate("MainWindow", "View All Firearms"))
        self.PTab_BTN_3.setText(_translate("MainWindow", "Button 3"))
        self.PTab_BTN_4.setText(_translate("MainWindow", "Button 4"))
        self.PTab_BTN_5.setText(_translate("MainWindow", "Button 5"))
        self.PTab_BTN_6.setText(_translate("MainWindow", "Button 6"))
        self.PTab_BTN_7.setText(_translate("MainWindow", "Button 7"))
        self.PTab_BTN_8.setText(_translate("MainWindow", "Button 8"))
        self.PTab_BTN_9.setText(_translate("MainWindow", "Button 9"))
        self.PTab_BTN_10.setText(_translate("MainWindow", "Button 10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PTab_tab),
                                  _translate("MainWindow", "Powders"))
        self.CTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
        self.CTab_Firearm_LBL.setText(_translate("MainWindow", "Firearm"))
        self.CTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
        self.CTab_TwistRate_LBL.setText(_translate("MainWindow", "Twist Rate"))
        self.CTab_ThreadSize_LBL.setText(
            _translate("MainWindow", "Thread Size"))
        self.CTab_Slot_8_LBL.setText(_translate("MainWindow", "Slot 8"))
        self.CTab_Slot_7_LBL.setText(_translate("MainWindow", "Slot 7"))
        self.CTab_Slot_1_LBL.setText(_translate("MainWindow", "Slot 1"))
        self.CTab_Slot_3_LBL.setText(_translate("MainWindow", "Slot 3"))
        self.CTab_Slot_11_LBL.setText(_translate("MainWindow", "Slot 11"))
        self.CTab_Slot_9_LBL.setText(_translate("MainWindow", "Slot 9"))
        self.CTab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
        self.CTab_OLen_LBL.setText(_translate("MainWindow", "Overall Length"))
        self.CTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
        self.CTab_Type_LBL.setText(_translate("MainWindow", "Type"))
        self.CTab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
        self.CTab_Action_LBL.setText(_translate("MainWindow", "Action Type"))
        self.CTab_Name_LBL.setText(_translate("MainWindow", "Name"))
        self.CTab_Manufacturer_LBL.setText(
            _translate("MainWindow", "Manufacturer"))
        self.CTab_Model_LBL.setText(_translate("MainWindow", "Model"))
        self.CTab_BarrelLen_LBL.setText(
            _translate("MainWindow", "Barrel Length"))
        self.CTab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
        self.CTab_Slot_10_LBL.setText(_translate("MainWindow", "Slot 10"))
        self.CTab_Slot_4_LBL.setText(_translate("MainWindow", "Slot 4"))
        self.CTab_Slot_2_LBL.setText(_translate("MainWindow", "Slot 2"))
        self.CTab_Slot_6_LBL.setText(_translate("MainWindow", "Slot 6"))
        self.CTab_Slot_5_LBL.setText(_translate("MainWindow", "Slot 5"))
        self.CTab_Add_BTN.setText(_translate("MainWindow", "Add Firearm"))
        self.CTab_View_All_BTN.setText(
            _translate("MainWindow", "View All Firearms"))
        self.CTab_BTN_3.setText(_translate("MainWindow", "Button 3"))
        self.CTab_BTN_4.setText(_translate("MainWindow", "Button 4"))
        self.CTab_BTN_5.setText(_translate("MainWindow", "Button 5"))
        self.CTab_BTN_6.setText(_translate("MainWindow", "Button 6"))
        self.CTab_BTN_7.setText(_translate("MainWindow", "Button 7"))
        self.CTab_BTN_8.setText(_translate("MainWindow", "Button 8"))
        self.CTab_BTN_9.setText(_translate("MainWindow", "Button 9"))
        self.CTab_BTN_10.setText(_translate("MainWindow", "Button 10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CTab_tab),
                                  _translate("MainWindow", "Cases"))
        self.PRTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
        self.PRTab_Firearm_LBL.setText(_translate("MainWindow", "Firearm"))
        self.PRTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
        self.PRTab_TwistRate_LBL.setText(
            _translate("MainWindow", "Twist Rate"))
        self.PRTab_ThreadSize_LBL.setText(
            _translate("MainWindow", "Thread Size"))
        self.PRTab_Slot_8_LBL.setText(_translate("MainWindow", "Slot 8"))
        self.PRTab_Slot_7_LBL.setText(_translate("MainWindow", "Slot 7"))
        self.PRTab_Slot_1_LBL.setText(_translate("MainWindow", "Slot 1"))
        self.PRTab_Slot_3_LBL.setText(_translate("MainWindow", "Slot 3"))
        self.PRTab_Slot_11_LBL.setText(_translate("MainWindow", "Slot 11"))
        self.PRTab_Slot_9_LBL.setText(_translate("MainWindow", "Slot 9"))
        self.PRTab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
        self.PRTab_OLen_LBL.setText(_translate("MainWindow", "Overall Length"))
        self.PRTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
        self.PRTab_Type_LBL.setText(_translate("MainWindow", "Type"))
        self.PRTab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
        self.PRTab_Action_LBL.setText(_translate("MainWindow", "Action Type"))
        self.PRTab_Name_LBL.setText(_translate("MainWindow", "Name"))
        self.PRTab_Manufacturer_LBL.setText(
            _translate("MainWindow", "Manufacturer"))
        self.PRTab_Model_LBL.setText(_translate("MainWindow", "Model"))
        self.PRTab_BarrelLen_LBL.setText(
            _translate("MainWindow", "Barrel Length"))
        self.PRTab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
        self.PRTab_Slot_10_LBL.setText(_translate("MainWindow", "Slot 10"))
        self.PRTab_Slot_4_LBL.setText(_translate("MainWindow", "Slot 4"))
        self.PRTab_Slot_2_LBL.setText(_translate("MainWindow", "Slot 2"))
        self.PRTab_Slot_6_LBL.setText(_translate("MainWindow", "Slot 6"))
        self.PRTab_Slot_5_LBL.setText(_translate("MainWindow", "Slot 5"))
        self.PRTab_Add_BTN.setText(_translate("MainWindow", "Add Firearm"))
        self.PRTab_View_All_BTN.setText(
            _translate("MainWindow", "View All Firearms"))
        self.PRTab_BTN_3.setText(_translate("MainWindow", "Button 3"))
        self.PRTab_BTN_4.setText(_translate("MainWindow", "Button 4"))
        self.PRTab_BTN_5.setText(_translate("MainWindow", "Button 5"))
        self.PRTab_BTN_6.setText(_translate("MainWindow", "Button 6"))
        self.PRTab_BTN_7.setText(_translate("MainWindow", "Button 7"))
        self.PRTab_BTN_8.setText(_translate("MainWindow", "Button 8"))
        self.PRTab_BTN_9.setText(_translate("MainWindow", "Button 9"))
        self.PRTab_BTN_10.setText(_translate("MainWindow", "Button 10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PRTab_tab),
                                  _translate("MainWindow", "Primers"))
        self.DTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
        self.DTab_Firearm_LBL.setText(_translate("MainWindow", "Firearm"))
        self.DTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
        self.DTab_TwistRate_LBL.setText(_translate("MainWindow", "Twist Rate"))
        self.DTab_ThreadSize_LBL.setText(
            _translate("MainWindow", "Thread Size"))
        self.DTab_Slot_8_LBL.setText(_translate("MainWindow", "Slot 8"))
        self.DTab_Slot_7_LBL.setText(_translate("MainWindow", "Slot 7"))
        self.DTab_Slot_1_LBL.setText(_translate("MainWindow", "Slot 1"))
        self.DTab_Slot_3_LBL.setText(_translate("MainWindow", "Slot 3"))
        self.DTab_Slot_11_LBL.setText(_translate("MainWindow", "Slot 11"))
        self.DTab_Slot_9_LBL.setText(_translate("MainWindow", "Slot 9"))
        self.DTab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
        self.DTab_OLen_LBL.setText(_translate("MainWindow", "Overall Length"))
        self.DTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
        self.DTab_Type_LBL.setText(_translate("MainWindow", "Type"))
        self.DTab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
        self.DTab_Action_LBL.setText(_translate("MainWindow", "Action Type"))
        self.DTab_Name_LBL.setText(_translate("MainWindow", "Name"))
        self.DTab_Manufacturer_LBL.setText(
            _translate("MainWindow", "Manufacturer"))
        self.DTab_Model_LBL.setText(_translate("MainWindow", "Model"))
        self.DTab_BarrelLen_LBL.setText(
            _translate("MainWindow", "Barrel Length"))
        self.DTab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
        self.DTab_Slot_10_LBL.setText(_translate("MainWindow", "Slot 10"))
        self.DTab_Slot_4_LBL.setText(_translate("MainWindow", "Slot 4"))
        self.DTab_Slot_2_LBL.setText(_translate("MainWindow", "Slot 2"))
        self.DTab_Slot_6_LBL.setText(_translate("MainWindow", "Slot 6"))
        self.DTab_Slot_5_LBL.setText(_translate("MainWindow", "Slot 5"))
        self.DTab_Add_BTN.setText(_translate("MainWindow", "Add Firearm"))
        self.DTab_View_All_BTN.setText(
            _translate("MainWindow", "View All Firearms"))
        self.DTab_BTN_3.setText(_translate("MainWindow", "Button 3"))
        self.DTab_BTN_4.setText(_translate("MainWindow", "Button 4"))
        self.DTab_BTN_5.setText(_translate("MainWindow", "Button 5"))
        self.DTab_BTN_6.setText(_translate("MainWindow", "Button 6"))
        self.DTab_BTN_7.setText(_translate("MainWindow", "Button 7"))
        self.DTab_BTN_8.setText(_translate("MainWindow", "Button 8"))
        self.DTab_BTN_9.setText(_translate("MainWindow", "Button 9"))
        self.DTab_BTN_10.setText(_translate("MainWindow", "Button 10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DTab_tab),
                                  _translate("MainWindow", "Data"))
        self.STab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
        self.STab_SILIENCER_LBL.setText(_translate("MainWindow", "Firearm"))
        self.STab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
        self.STab_TwistRate_LBL.setText(_translate("MainWindow", "Twist Rate"))
        self.STab_ThreadSize_LBL.setText(
            _translate("MainWindow", "Thread Size"))
        self.STab_Slot_8_LBL.setText(_translate("MainWindow", "Slot 8"))
        self.STab_Slot_7_LBL.setText(_translate("MainWindow", "Slot 7"))
        self.STab_Slot_1_LBL.setText(_translate("MainWindow", "Slot 1"))
        self.STab_Slot_3_LBL.setText(_translate("MainWindow", "Slot 3"))
        self.STab_Slot_11_LBL.setText(_translate("MainWindow", "Slot 11"))
        self.STab_Slot_9_LBL.setText(_translate("MainWindow", "Slot 9"))
        self.STab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
        self.STab_OLen_LBL.setText(_translate("MainWindow", "Overall Length"))
        self.STab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
        self.STab_Type_LBL.setText(_translate("MainWindow", "Type"))
        self.STab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
        self.STab_Action_LBL.setText(_translate("MainWindow", "Action Type"))
        self.STab_Name_LBL.setText(_translate("MainWindow", "Name"))
        self.STab_Manufacturer_LBL.setText(
            _translate("MainWindow", "Manufacturer"))
        self.STab_Model_LBL.setText(_translate("MainWindow", "Model"))
        self.STab_BarrelLen_LBL.setText(
            _translate("MainWindow", "Barrel Length"))
        self.STab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
        self.STab_Slot_10_LBL.setText(_translate("MainWindow", "Slot 10"))
        self.STab_Slot_4_LBL.setText(_translate("MainWindow", "Slot 4"))
        self.STab_Slot_2_LBL.setText(_translate("MainWindow", "Slot 2"))
        self.STab_Slot_6_LBL.setText(_translate("MainWindow", "Slot 6"))
        self.STab_Slot_5_LBL.setText(_translate("MainWindow", "Slot 5"))
        self.STab_Add_BTN.setText(_translate("MainWindow", "Add Firearm"))
        self.STab_View_All_BTN.setText(
            _translate("MainWindow", "View All Firearms"))
        self.STab_BTN_3.setText(_translate("MainWindow", "Button 3"))
        self.STab_BTN_4.setText(_translate("MainWindow", "Button 4"))
        self.STab_BTN_5.setText(_translate("MainWindow", "Button 5"))
        self.STab_BTN_6.setText(_translate("MainWindow", "Button 6"))
        self.STab_BTN_7.setText(_translate("MainWindow", "Button 7"))
        self.STab_BTN_8.setText(_translate("MainWindow", "Button 8"))
        self.STab_BTN_9.setText(_translate("MainWindow", "Button 9"))
        self.STab_BTN_10.setText(_translate("MainWindow", "Button 10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.STab_tab),
                                  _translate("MainWindow", "Silencers"))
        self.MTab_ShotsOverTime_BTN.setText(
            _translate("MainWindow", "Shots Over Time"))
        self.MTab_Plot_Shots_Powder_Charge.setText(
            _translate("MainWindow", "Shots Per Powder Charge"))
        self.MTab_BTN_20.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_23.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_2.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_30.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_11.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_21.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_7.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_31.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_26.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_41.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_9.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_22.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_25.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_12.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_29.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_15.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_3.setText(_translate("MainWindow", "PushButton"))
        self.MTab_Plot_Powder_Speed_Multi.setText(
            _translate("MainWindow", "Plot Powder Speed Multi"))
        self.MTab_ShotsPerFirearm_BTN.setText(
            _translate("MainWindow", "Shots Per Firearm"))
        self.MTab_BTN_14.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_18.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_8.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_27.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_19.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_24.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_17.setText(_translate("MainWindow", "PushButton"))
        self.MTab_Plot_Powder_Speed_Single.setText(
            _translate("MainWindow", "Plot Powder Speed Single"))
        self.MTab_BTN_36.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_16.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_13.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_28.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_46.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_32.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_37.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_42.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_47.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_33.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_38.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_43.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_48.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_34.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_39.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_44.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_49.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_35.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_40.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_45.setText(_translate("MainWindow", "PushButton"))
        self.MTab_BTN_50.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MTab_tab),
                                  _translate("MainWindow", "Metrics"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
