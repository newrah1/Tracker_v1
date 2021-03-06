import random
import sqlite3
import sys
import traceback
from configparser import ConfigParser
import logging
import mysql.connector
import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from pandas import option_context

from Popup import Add_Bullet, Add_Case, Add_Firearm, Add_Powder, Add_Primer, Add_Silencer, \
	Show_Firearms, Show_Powders, Show_Bullets, Show_Cases

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
		# Set logging parameters
		logging.basicConfig(filename="./LOGS/log.txt",
							format='%(asctime)s - %(message)s',
							datefmt='%d-%b-%y %H:%M:%S',
							level=logging.INFO)

		self.conn = sqlite3.connect("./DATABASE/TrackerDB.db")

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
			firearm_df = pd.read_sql("SELECT * FROM Firearm", self.conn)
			bullet_df = pd.read_sql("SELECT * FROM bullet", self.conn)
			powder_df = pd.read_sql("SELECT * FROM powder", self.conn)
			case_df = pd.read_sql("SELECT * FROM Case_table", self.conn)
			primer_df = pd.read_sql("SELECT * FROM Primer", self.conn)
			silencer_df = pd.read_sql("SELECT * FROM Silencer", self.conn)
			return firearm_df, bullet_df, powder_df, case_df, primer_df, silencer_df
		except Exception as e:
			print("Exception = ", str(e))
			traceback.print_exc()
			logging.error("ERROR --- ", str(e))

	# FTab --------------------------------
	def PopUp_Add_Firearm_BTN(self):
		if self.PopUp_Firearm_Add.isVisible():
			self.PopUp_Firearm_Add.hide()

		else:
			self.PopUp_Firearm_Add.show()

	def displayData_FTab(self):
		try:
			# get the value from the Firearm comboBox
			Selected_Firearm = self.FTab_Firearm_Combo.currentText()

			# query the DB save to df
			firearm_df, bullet_df, powder_df, case_df, primer_df, silencer_df = \
				self.query_databases()

			# filter by selected firearm
			query = '{}"{}"'.format("Name == ", str(Selected_Firearm))
			firearm_df = firearm_df.query(query)

			# clear the form
			self.FTab_Name_TB.clear()
			self.FTab_Manufacturer_TB.clear()
			self.FTab_Model_TB.clear()
			self.FTab_SKU_TB.clear()
			self.FTab_Caliber_TB.clear()
			self.FTab_Type_TB.clear()
			self.FTab_Action_TB.clear()
			self.FTab_OLen_TB.clear()
			self.FTab_BarrelLen_TB.clear()
			self.FTab_Weight_TB.clear()
			self.FTab_TwistRate_TB.clear()
			self.FTab_ThreadSize_TB.clear()
			self.FTab_Notes_TB.clear()
			self.FTab_Picture_LBL.clear()

			# fill in the form
			self.FTab_Name_TB.setText(firearm_df['Name'].to_string(index=False))
			self.FTab_Manufacturer_TB.setText(firearm_df['Manufacturer'].to_string(index=False))
			self.FTab_Model_TB.setText(firearm_df['Model'].to_string(index=False))
			self.FTab_SKU_TB.setText(firearm_df['SKU'].to_string(index=False))
			self.FTab_Caliber_TB.setText(firearm_df['Caliber'].to_string(index=False))
			self.FTab_Type_TB.setText(firearm_df['Firearm_Type'].to_string(index=False))
			self.FTab_Action_TB.setText(firearm_df['Action_Type'].to_string(index=False))
			self.FTab_OLen_TB.setText(firearm_df['Overall_Length_Inch'].to_string(index=False))
			self.FTab_BarrelLen_TB.setText(firearm_df['Barrel_Len_Inch'].to_string(index=False))
			self.FTab_Weight_TB.setText(firearm_df['Weight_Lb'].to_string(index=False))
			self.FTab_TwistRate_TB.setText(firearm_df['Twist_Rate'].to_string(index=False))
			self.FTab_ThreadSize_TB.setText(firearm_df['Thread_Size'].to_string(index=False))
			self.FTab_Notes_TB.setText(firearm_df['Notes'].to_string(index=False))

			# Context manager to temporarily set options in the with statement context.
			# required to display 'Notes'
			with option_context('display.max_colwidth', None):
				self.FTab_Notes_TB.setText(firearm_df['Notes'].to_string(
					index=False))
			# Display picture of firearm in GUI
			high_rez = QtCore.QSize(400, 400)
			picture = '{}{}'.format("./picts/", firearm_df['Picture'].to_string(index=False))
			pixmap = QtGui.QPixmap(picture)
			pixmap = pixmap.scaled(high_rez)
			self.FTab_Picture_LBL.setPixmap(pixmap)

		except Exception as e:
			print("Exception = ", str(e))
			traceback.print_exc()

	def PopUp_ShowAllFirearms(self, checked):
		if self.PopUp_Firearm_Show.isVisible():
			self.PopUp_Firearm_Show.hide()

		else:
			self.PopUp_Firearm_Show.show()

	def PopUp_Canvas_Test(self, checked):
		if self.FTab_BTN_3_POP.isVisible():
			self.FTab_BTN_3_POP.hide()

		else:
			self.FTab_BTN_3_POP.show()

	# FTab --------------------------------

	# BTab --------------------------------
	def PopUp_Add_Bullet_BTN(self):
		if self.PopUp_Bullet_Add.isVisible():
			self.PopUp_Bullet_Add.hide()

		else:
			self.PopUp_Bullet_Add.show()

	def displayData_BTab(self):
		try:
			# get the value from the Firearm comboBox
			Selected_Bullet = self.BTab_Bullet_Combo.currentText()

			# query the DB save to df
			firearm_df, bullet_df, powder_df, case_df, primer_df, silencer_df = \
				self.query_databases()

			# filter by selected firearm
			query = '{}"{}"'.format("Name == ", str(Selected_Bullet))
			bullet_df = bullet_df.query(query)

			# clear the form
			self.BTab_Name_TB.clear()
			self.BTab_Manufacturer_TB.clear()
			#self.BTab_Model_TB.clear()
			self.BTab_SKU_TB.clear()
			self.BTab_Size_Inch_TB.clear()
			self.BTab_Size_mm_TB.clear()
			self.BTab_Weight_TB.clear()
			self.BTab_Type_TB.clear()
			self.BTab_BBase_TB.clear()
			self.BTab_BC_TB.clear()
			self.BTab_Length_TB.clear()
			self.BTab_Notes_TB.clear()
			self.BTab_Picture_LBL.clear()

			# fill in the form
			self.BTab_Name_TB.setText(bullet_df['Name'].to_string(index=False))
			self.BTab_Manufacturer_TB.setText(bullet_df['Manufacturer'].to_string(index=False))
			#self.BTab_Model_TB.setTextt(bullet_df['Model'].to_string(index=False))
			self.BTab_SKU_TB.setText(bullet_df['SKU'].to_string(index=False))
			self.BTab_Size_Inch_TB.setText(bullet_df['Size_Inch'].to_string(index=False))
			self.BTab_Size_mm_TB.setText(bullet_df['Size_mm'].to_string(index=False))
			self.BTab_Weight_TB.setText(bullet_df['Weight'].to_string(index=False))
			self.BTab_Type_TB.setText(bullet_df['Type'].to_string(index=False))
			self.BTab_Caliber_TB.setText(bullet_df['Caliber'].to_string(index=False))
			self.BTab_BBase_TB.setText(bullet_df['Bullet_Base'].to_string(index=False))
			self.BTab_BC_TB.setText(bullet_df['BC'].to_string(index=False))
			self.BTab_Length_TB.setText(bullet_df['Length_Inch'].to_string(index=False))
			self.BTab_Notes_TB.setText(bullet_df['Notes'].to_string(index=False))

			# Context manager to temporarily set options in the with statement context.
			# required to display 'Notes'
			with option_context('display.max_colwidth', None):
				self.BTab_Notes_TB.setText(bullet_df['Notes'].to_string(
					index=False))
				# Display picture of Bullet in GUI
				high_rez = QtCore.QSize(400, 400)
				#pixmap = QtGui.QPixmap(bullet_df['Picture'].to_string(index=False))
				picture = '{}{}'.format("./picts/", bullet_df['Picture'].to_string(index=False))
				pixmap = QtGui.QPixmap(picture)
				pixmap = pixmap.scaled(high_rez, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.BTab_Picture_LBL.setPixmap(pixmap)

		except Exception as e:
			print("Exception = ", str(e))
			traceback.print_exc()

	def PopUp_ShowAllBullets(self, checked):
		if self.PopUp_Bullet_Show.isVisible():
			self.PopUp_Bullet_Show.hide()

		else:
			self.PopUp_Bullet_Show.show()

	# PTab --------------------------------
	def displayData_PTab(self):
		try:
			# get the value from the Powder comboBox
			Selected_Powder = self.PTab_Powder_Combo.currentText()

			# query the DB save to df
			firearm_df, bullet_df, powder_df, case_df, primer_df, silencer_df = \
				self.query_databases()

			# filter by selected firearm
			query = '{}"{}"'.format("Name == ", str(Selected_Powder))
			powder_df = powder_df.query(query)

			# clear the form
			self.PTab_Name_TB.clear()
			self.PTab_Manufacturer_TB.clear()
			self.PTab_Model_TB.clear()
			self.PTab_SKU_TB.clear()
			self.PTab_BurnRate_TB.clear()
			self.PTab_WeaponUse_TB.clear()
			self.PTab_Density_TB.clear()
			self.PTab_BulkDensity_TB.clear()
			self.PTab_Notes_TB.clear()
			self.PTab_Picture_LBL.clear()

			# fill in the form
			self.PTab_Name_TB.setText(powder_df['Name'].to_string(index=False))
			self.PTab_Manufacturer_TB.setText(powder_df['Manufacturer'].to_string(index=False))
			self.PTab_Model_TB.setText(powder_df['Model'].to_string(index=False))
			self.PTab_SKU_TB.setText(powder_df['SKU'].to_string(index=False))
			self.PTab_BurnRate_TB.setText(powder_df['Relative_Burn_Rate'].to_string(index=False))
			self.PTab_WeaponUse_TB.setText(powder_df['Weapon_Use'].to_string(index=False))
			self.PTab_Density_TB.setText(powder_df['Density_lb'].to_string(index=False))
			self.PTab_BulkDensity_TB.setText(powder_df['Bulk_Density'].to_string(index=False))
			self.PTab_Notes_TB.setText(powder_df['Notes'].to_string(index=False))

			# Context manager to temporarily set options in the with statement context.
			# required to display 'Notes'
			with option_context('display.max_colwidth', None):
				self.PTab_Notes_TB.setText(powder_df['Notes'].to_string(
					index=False))
				# Display picture of Bullet in GUI
				high_rez = QtCore.QSize(400, 400)
				picture = '{}{}'.format("./picts/", powder_df['Picture'].to_string(index=False))
				pixmap = QtGui.QPixmap(picture)
				pixmap = pixmap.scaled(high_rez, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.PTab_Picture_LBL.setPixmap(pixmap)

		except Exception as e:
			print("Exception = ", str(e))
			traceback.print_exc()

	def PopUp_ShowAllPowders(self, checked):
		if self.PopUp_Powder_Show.isVisible():
			self.PopUp_Powder_Show.hide()

		else:
			self.PopUp_Powder_Show.show()

	def PopUp_Add_Powder_BTN(self):
		if self.PopUp_Powder_Add.isVisible():
			self.PopUp_Popwder_Add.hide()

		else:
			self.PopUp_Powder_Add.show()

	# PTab --------------------------------

	# CTab --------------------------------
	def displayData_CTab(self):
		try:
			# get the value from the Powder comboBox
			Selected_Case = self.CTab_Cases_Combo.currentText()

			# query the DB save to df
			firearm_df, bullets_df, powders_df, case_df, primers_df, silencer_df = \
				self.query_databases()

			# filter by selected firearm
			query = '{}"{}"'.format("Name == ", str(Selected_Case))
			case_df = case_df.query(query)

			# clear the form
			self.CTab_Name_TB.clear()
			self.CTab_Manufacturer_TB.clear()
			self.CTab_Model_TB.clear()
			self.CTab_SKU_TB.clear()
			self.CTab_Finish_TB.clear()
			self.CTab_PrimerSize_TB.clear()
			self.CTab_Notes_TB.clear()
			self.CTab_Picture_LBL.clear()

			# fill in the form
			self.CTab_Name_TB.setText(case_df['Name'].to_string(index=False))
			self.CTab_Manufacturer_TB.setText(case_df['Manufacturer'].to_string(index=False))
			self.CTab_Model_TB.setText(case_df['Model'].to_string(index=False))
			self.CTab_SKU_TB.setText(case_df['SKU'].to_string(index=False))
			self.CTab_Finish_TB.setText(case_df['Finish'].to_string(index=False))
			self.CTab_PrimerSize_TB.setText(case_df['Primer_Size'].to_string(index=False))
			self.CTab_Notes_TB.setText(case_df['Notes'].to_string(index=False))

			# Context manager to temporarily set options in the with statement context.
			# required to display 'Notes'
			with option_context('display.max_colwidth', None):
				self.CTab_Notes_TB.setText(case_df['Notes'].to_string(index=False))
				# Display picture of Bullet in GUI
				high_rez = QtCore.QSize(400, 400)
				picture = '{}{}'.format("./picts/", case_df['Picture'].to_string(index=False))
				pixmap = QtGui.QPixmap(picture)
				pixmap = pixmap.scaled(high_rez, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.CTab_Picture_LBL.setPixmap(pixmap)

		except Exception as e:
			print("Exception = ", str(e))
			traceback.print_exc()

	def PopUp_Add_Case_BTN(self):
		if self.PopUp_Case_Add.isVisible():
			self.PopUp_Case_Add.hide()

		else:
			self.PopUp_Case_Add.show()

	def PopUp_ShowAllCases(self, checked):
		if self.PopUp_Case_Show.isVisible():
			self.PopUp_Case_Show.hide()

		else:
			self.PopUp_Case_Show.show()

	# CTab --------------------------------

	# PRTab --------------------------------
	def displayData_PRTab(self):
		try:
			# get the value from the Powder comboBox
			Selected_Primer = self.PRTab_Primer_Combo.currentText()

			# query the DB save to df
			firearm_df, bullet_df, powder_df, case_df, primer_df, silencer_df = \
				self.query_databases()

			# filter by selected firearm
			query = '{}"{}"'.format("Name == ", str(Selected_Primer))
			primer_df = primer_df.query(query)

			# clear the form
			self.PRTab_Name_TB.clear()
			self.PRTab_Manufacturer_TB.clear()
			self.PRTab_Model_TB.clear()
			self.PRTab_SKU_TB.clear()
			self.PRTab_Size_TB.clear()
			self.PRTab_Type_TB.clear()
			self.PRTab_Notes_TB.clear()
			self.PRTab_Picture_LBL.clear()

			# fill in the form
			self.PRTab_Name_TB.setText(primer_df['Name'].to_string(index=False))
			self.PRTab_Manufacturer_TB.setText(primer_df['Manufacturer'].to_string(index=False))
			self.PRTab_Model_TB.setText(primer_df['Model'].to_string(index=False))
			self.PRTab_SKU_TB.setText(primer_df['SKU'].to_string(index=False))
			self.PRTab_Size_TB.setText(primer_df['Size'].to_string(index=False))
			self.PRTab_Type_TB.setText(primer_df['PrimerType'].to_string(index=False))
			self.PRTab_Notes_TB.setText(primer_df['Notes'].to_string(index=False))

			# Context manager to temporarily set options in the with statement context.
			# required to display 'Notes'
			with option_context('display.max_colwidth', None):
				self.PRTab_Notes_TB.setText(primer_df['Notes'].to_string(index=False))
				# Display picture of Bullet in GUI
				high_rez = QtCore.QSize(400, 400)
				picture = '{}{}'.format("./picts/", primer_df['Picture'].to_string(index=False))
				pixmap = QtGui.QPixmap(picture)
				pixmap = pixmap.scaled(high_rez, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.PRTab_Picture_LBL.setPixmap(pixmap)

		except Exception as e:
			print("Exception = ", str(e))
			traceback.print_exc()

	def PopUp_Add_Primer_BTN(self):
		if self.PopUp_Primer_Add.isVisible():
			self.PopUp_Primer_Add.hide()

		else:
			self.PopUp_Primer_Add.show()

	def PopUp_ShowAllPrimers(self, checked):
		if self.PopUp_Primer_Show.isVisible():
			self.PopUp_Primer_Show.hide()

		else:
			self.PopUp_Primer_Show.show()

	# PRTab --------------------------------

	# DTab --------------------------------
	def displayData_DTab(self):
		pass

	# DTab --------------------------------

	# STab --------------------------------
	def PopUp_ShowAllSilencers(self, checked):
		if self.STab_ShowSilencers_POP.isVisible():
			self.STab_ShowSilencers_POP.hide()
		else:
			self.STab_ShowSilencers_POP.show()

	def displayData_STab(self):
		try:
			# get the value from the Silencer comboBox
			Selected_Silencer = self.STab_SILIENCER_Combo.currentText()

			# query the DB save to df
			firearm_df, bullet_df, powder_df, case_df, primer_df, silencer_df = \
				self.query_databases()

			# filter by selected Silencer
			query = '{}"{}"'.format("Name == ", str(Selected_Silencer))
			silencer_df = silencer_df.query(query)

			# clear the form
			self.STab_Name_TB.clear()
			self.STab_Manufacturer_TB.clear()
			self.STab_Model_TB.clear()
			self.STab_SKU_TB.clear()
			self.STab_Caliber_TB.clear()
			self.STab_OLenght_TB.clear()
			self.STab_Weight_TB.clear()
			self.STab_Diameter_TB.clear()

			# fill in the form
			self.STab_Name_TB.setText(silencer_df['Name'].to_string(index=False))
			self.STab_Manufacturer_TB.setText(silencer_df['Manufacturer'].to_string(index=False))
			self.STab_Model_TB.setText(silencer_df['Model'].to_string(index=False))
			self.STab_SKU_TB.setText(silencer_df['SKU'].to_string(index=False))
			self.STab_Caliber_TB.setText(silencer_df['Caliber'].to_string(index=False))
			self.STab_OLenght_TB.setText(silencer_df['Overall_Len_Inch'].to_string(index=False))
			self.STab_Weight_TB.setText(silencer_df['Weight_lb'].to_string(index=False))
			self.STab_Diameter_TB.setText(silencer_df['Diameter_Inch'].to_string(index=False))


			# Context manager to temporarily set options in the with statement context.
			# required to display 'Notes'
			with option_context('display.max_colwidth', None):
				self.STab_Notes_TB.setText(silencer_df['Notes'].to_string(
					index=False))
				# Display picture of Bullet in GUI
				high_rez = QtCore.QSize(400, 400)
				# pixmap = QtGui.QPixmap(bullet_df['Picture'].to_string(index=False))
				picture = '{}{}'.format("./picts/", silencer_df['Picture'].to_string(index=False))
				pixmap = QtGui.QPixmap(picture)
				pixmap = pixmap.scaled(high_rez, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.BTab_Picture_LBL.setPixmap(pixmap)

		except Exception as e:
			print("Exception = ", str(e))
			traceback.print_exc()

	def PopUp_Add_Silencer_BTN(self):
		if self.PopUp_Silencer_Add.isVisible():
			self.PopUp_Silencer_Add.hide()

		else:
			self.PopUp_Silencer_Add.show()

	# STab --------------------------------

	# MTab --------------------------------
	def displayData_MTab(self):
		pass

	# MTab --------------------------------

	def setupUi(self, MainWindow):
		# retrieve data from MySQL
		firearms_df, bullets_df, powders_df, cases_df, primers_df, silencer_df = \
			self.query_databases()
		# Generate unique lists of data
		firearms_list = firearms_df['Name'].unique().tolist()
		bullets_list = bullets_df['Name'].unique().tolist()
		powders_list = powders_df['Name'].unique().tolist()
		cases_list = cases_df['Name'].unique().tolist()
		primers_list = primers_df['Name'].unique().tolist()
		silencer_list = silencer_df['Name'].unique().tolist()

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
		# change font type and size
		# self.tabWidget.setFont(QtGui.QFont('SansSerif', 15))
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
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(490, 80, 160, 361))
		self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
		self.FTab_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
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
		# FTab Name
		self.FTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Name_TB.setObjectName("FTab_Name_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Name_TB, 0, 1, 1, 1)
		self.FTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Name_LBL.setObjectName("FTab_Name_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Name_LBL, 0, 0, 1, 1)
		# FTab Manufacturer
		self.FTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Manufacturer_LBL.setObjectName("FTab_Manufacturer_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Manufacturer_LBL, 1, 0, 1, 1)
		self.FTab_Manufacturer_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Manufacturer_TB.setObjectName("FTab_Manufacturer_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Manufacturer_TB, 1, 1, 1, 1)
		# FTab Model
		self.FTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Model_LBL.setObjectName("FTab_Model_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Model_LBL, 2, 0, 1, 1)
		self.FTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Model_TB.setObjectName("FTab_Model_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Model_TB, 2, 1, 1, 1)
		# FTab SKU
		self.FTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_SKU_TB.setObjectName("FTab_SKU_TB")
		self.FTab_gridLayout.addWidget(self.FTab_SKU_TB, 3, 1, 1, 1)
		self.FTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_SKU_LBL.setObjectName("FTab_SKU_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_SKU_LBL, 3, 0, 1, 1)
		# Caliber
		self.FTab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Caliber_LBL.setObjectName("FTab_Caliber_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Caliber_LBL, 4, 0, 1, 1)
		self.FTab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Caliber_TB.setObjectName("FTab_Caliber_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Caliber_TB, 4, 1, 1, 1)
		# FTab Type
		self.FTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Type_TB.setObjectName("FTab_Type_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Type_TB, 5, 1, 1, 1)
		self.FTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Type_LBL.setObjectName("FTab_Type_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Type_LBL, 5, 0, 1, 1)
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
		self.FTab_BarrelLen_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
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
		self.FTab_TwistRate_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_TwistRate_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_TwistRate_TB.setObjectName("FTab_TwistRate_TB")
		self.FTab_gridLayout.addWidget(self.FTab_TwistRate_TB, 10, 1, 1, 1)
		# FTab ThreadSize
		self.FTab_ThreadSize_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_ThreadSize_LBL.setObjectName("FTab_ThreadSize_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_ThreadSize_LBL, 11, 0, 1, 1)
		self.FTab_ThreadSize_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_ThreadSize_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_ThreadSize_TB.setObjectName("FTab_ThreadSize_TB")
		self.FTab_gridLayout.addWidget(self.FTab_ThreadSize_TB, 11, 1, 1, 1)
		# FTab Slot 16
		self.FTab_Slot_16_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_16_LBL.setObjectName("FTab_Slot_16_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_16_LBL, 13, 0, 1, 1)
		self.FTab_Slot_16_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_16_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_16_TB.setObjectName("FTab_Slot_16_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_16_TB, 13, 1, 1, 1)
		# FTab Slot 17
		self.FTab_Slot_17_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_17_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_17_TB.setObjectName("FTab_Slot_17_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_17_TB, 14, 1, 1, 1)
		self.FTab_Slot_17_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_17_LBL.setObjectName("FTab_Slot_17_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_17_LBL, 14, 0, 1, 1)
		# FTab Slot 18
		self.FTab_Slot_18_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_18_LBL.setObjectName("FTab_Slot_18_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_18_LBL, 15, 0, 1, 1)
		self.FTab_Slot_18_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_18_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_18_TB.setObjectName("FTab_Slot_18_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_18_TB, 15, 1, 1, 1)
		# FTab Slot 19
		self.FTab_Slot_19_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_19_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_19_TB.setObjectName("FTab_Slot_19_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_19_TB, 16, 1, 1, 1)
		self.FTab_Slot_19_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_19_LBL.setObjectName("FTab_Slot_19_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_19_LBL, 16, 0, 1, 1)
		# FTab Slot 20
		self.FTab_Slot_20_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_20_LBL.setObjectName("FTab_Slot_20_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_20_LBL, 18, 0, 1, 1)
		self.FTab_Slot_20_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_20_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_20_TB.setObjectName("FTab_Slot_20_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_20_TB, 18, 1, 1, 1)
		# FTab Slot 21
		self.FTab_Slot_21_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_21_LBL.setObjectName("FTab_Slot_21_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_21_LBL, 19, 0, 1, 1)
		self.FTab_Slot_21_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_21_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_21_TB.setObjectName("FTab_Slot_21_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_21_TB, 19, 1, 1, 1)
		# FTab Slot 22
		self.FTab_Slot_22_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_22_LBL.setObjectName("FTab_Slot_22_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_22_LBL, 21, 0, 1, 1)
		self.FTab_Slot_22_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_22_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_22_TB.setObjectName("FTab_Slot_22_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_22_TB, 21, 1, 1, 1)
		# FTab Slot 23
		self.FTab_Slot_23_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_23_LBL.setObjectName("FTab_Slot_23_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_23_LBL, 23, 0, 1, 1)
		self.FTab_Slot_23_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_23_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_23_TB.setObjectName("FTab_Slot_23_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_23_TB, 23, 1, 1, 1)
		# FTab Slot 24
		self.FTab_Slot_24_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_24_LBL.setObjectName("FTab_Slot_24_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_24_LBL, 25, 0, 1, 1)
		self.FTab_Slot_24_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_24_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_24_TB.setObjectName("FTab_Slot_24_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_24_TB, 25, 1, 1, 1)
		# FTab Slot 25
		self.FTab_Slot_25_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_25_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_25_TB.setObjectName("FTab_Slot_25_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_25_TB, 26, 1, 1, 1)
		self.FTab_Slot_25_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_25_LBL.setObjectName("FTab_Slot_25_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_25_LBL, 26, 0, 1, 1)
		# FTab Slot 26
		self.FTab_Slot_26_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_26_LBL.setObjectName("FTab_Slot_26_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_26_LBL, 28, 0, 1, 1)
		self.FTab_Slot_26_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_26_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_26_TB.setObjectName("FTab_Slot_26_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_26_TB, 28, 1, 1, 1)
		# FTab Slot 27
		self.FTab_Slot_27_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
		self.FTab_Slot_27_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.FTab_Slot_27_TB.setObjectName("FTab_Slot_27_TB")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_27_TB, 30, 1, 1, 1)
		self.FTab_Slot_27_LBL = QtWidgets.QLabel(self.formLayoutWidget_2)
		self.FTab_Slot_27_LBL.setObjectName("FTab_Slot_27_LBL")
		self.FTab_gridLayout.addWidget(self.FTab_Slot_27_LBL, 30, 0, 1, 1)
		# FTab Spacer

		# FTab Add Firearm BTN
		self.FTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
		self.FTab_Add_BTN.setDefault(True)
		self.FTab_Add_BTN.setObjectName("FTab_Add_BTN")
		self.FTab_verticalLayout.addWidget(self.FTab_Add_BTN)

		self.PopUp_Firearm_Add = QtWidgets.QMainWindow()
		# import class UI_PopUp_Add_Firearm from .\PopUp_Add_Firearm.py
		addFirearm = Add_Firearm.Ui_PopUp_Add_Firearm(firearms_df)
		addFirearm.setupUi(self.PopUp_Firearm_Add)
		self.FTab_Add_BTN.clicked.connect(self.PopUp_Add_Firearm_BTN)

		# FTab Show All Button
		self.FTab_View_All_BTN = QtWidgets.QPushButton(
			self.verticalLayoutWidget_2)
		self.FTab_View_All_BTN.setDefault(True)
		self.FTab_View_All_BTN.setObjectName("FTab_View_All_BTN")
		self.FTab_verticalLayout.addWidget(self.FTab_View_All_BTN)
				# Call Popup.Show_Firearms
		self.PopUp_Firearm_Show = QtWidgets.QMainWindow()
		ShowAllFirearms = Show_Firearms.Ui_ShowFirearms()
		ShowAllFirearms.setupUi(self.PopUp_Firearm_Show)
		self.FTab_View_All_BTN.clicked.connect(self.PopUp_ShowAllFirearms)
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
		# self.FTab_Picture_LBL.setPixmap(
		# QtGui.QPixmap(firearms_df['Picture']))
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
		# Model
		self.BTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Model_LBL.setObjectName("BTab_Model_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Model_LBL, 2, 0, 1, 1)
		self.BTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Model_TB.setObjectName("BTab_Model_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Model_TB, 2, 1, 1, 1)
		# BTab SKU
		self.BTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_SKU_LBL.setObjectName("BTab_SKU_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_SKU_LBL, 3, 0, 1, 1)
		self.BTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_SKU_TB.setObjectName("BTab_SKU_TB")
		self.BTab_gridLayout.addWidget(self.BTab_SKU_TB, 3, 1, 1, 1)
		# BTab Caliber
		self.BTab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Caliber_LBL.setObjectName("BTab_Caliber_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Caliber_LBL, 4, 0, 1, 1)
		self.BTab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Caliber_TB.setObjectName("BTab_Caliber_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Caliber_TB, 4, 1, 1, 1)
		# BTab Type
		self.BTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Type_TB.setObjectName("BTab_Type_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Type_TB, 5, 1, 1, 1)
		self.BTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Type_LBL.setObjectName("BTab_Type_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Type_LBL, 5, 0, 1, 1)
		# BTab Size_Inch
		self.BTab_Size_Inch_TB = QtWidgets.QTextBrowser(
			self.formLayoutWidget_3)
		self.BTab_Size_Inch_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Size_Inch_TB.setObjectName("BTab_Size_Inch_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Size_Inch_TB, 6, 1, 1, 1)
		self.BTab_Size_Inch_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Size_Inch_LBL.setObjectName("BTab_Size_Inch_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Size_Inch_LBL, 6, 0, 1, 1)
		# BTab Size_mm
		self.BTab_Size_mm_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Size_mm_LBL.setObjectName("BTab_Size_mm_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Size_mm_LBL, 7, 0, 1, 1)
		self.BTab_Size_mm_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Size_mm_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Size_mm_TB.setObjectName("BTab_Size_mm_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Size_mm_TB, 7, 1, 1, 1)
		# BTab BBase
		self.BTab_BBase_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_BBase_LBL.setObjectName("BTab_BBase_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_BBase_LBL, 8, 0, 1, 1)
		self.BTab_BBase_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_BBase_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_BBase_TB.setObjectName("BTab_BBase_TB")
		self.BTab_gridLayout.addWidget(self.BTab_BBase_TB, 8, 1, 1, 1)
		# BTab Weight
		self.BTab_Weight_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Weight_LBL.setObjectName("BTab_Weight_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Weight_LBL, 9, 0, 1, 1)
		self.BTab_Weight_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Weight_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Weight_TB.setObjectName("BTab_Weight_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Weight_TB, 9, 1, 1, 1)
		# BTab BC
		self.BTab_BC_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_BC_LBL.setObjectName("BTab_BC_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_BC_LBL, 10, 0, 1, 1)
		self.BTab_BC_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_BC_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_BC_TB.setObjectName("BTab_BC_TB")
		self.BTab_gridLayout.addWidget(self.BTab_BC_TB, 10, 1, 1, 1)
		# BTab Length
		self.BTab_Length_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Length_LBL.setObjectName("BTab_Length_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Length_LBL, 11, 0, 1, 1)
		self.BTab_Length_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Length_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Length_TB.setObjectName("BTab_Length_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Length_TB, 11, 1, 1, 1)
		# BTab Slot 16
		self.BTab_Slot_16_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_16_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_16_TB.setObjectName("BTab_Slot_16_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_16_TB, 12, 1, 1, 1)
		self.BTab_Slot_16_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_16_LBL.setObjectName("BTab_Slot_16_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_16_LBL, 12, 0, 1, 1)
		# BTab Slot 17
		self.BTab_Slot_17_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_17_LBL.setObjectName("BTab_Slot_17_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_17_LBL, 13, 0, 1, 1)
		self.BTab_Slot_17_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_17_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_17_TB.setObjectName("BTab_Slot_17_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_17_TB, 13, 1, 1, 1)
		# BTab Slot 18
		self.BTab_Slot_18_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_18_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_18_TB.setObjectName("BTab_Slot_18_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_18_TB, 14, 1, 1, 1)
		self.BTab_Slot_18_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_18_LBL.setObjectName("BTab_Slot_18_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_18_LBL, 14, 0, 1, 1)
		# BTab Slot 19
		self.BTab_Slot_19_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_19_LBL.setObjectName("BTab_Slot_19_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_19_LBL, 15, 0, 1, 1)
		self.BTab_Slot_19_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_19_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_19_TB.setObjectName("BTab_Slot_19_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_19_TB, 15, 1, 1, 1)
		# BTab Slot 20
		self.BTab_Slot_20_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_20_LBL.setObjectName("BTab_Slot_20_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_20_LBL, 16, 0, 1, 1)
		self.BTab_Slot_20_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_20_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_20_TB.setObjectName("BTab_Slot_20_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_20_TB, 16, 1, 1, 1)
		# BTab Slot 21
		self.BTab_Slot_21_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_21_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_21_TB.setObjectName("BTab_Slot_21_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_21_TB, 17, 1, 1, 1)
		self.BTab_Slot_21_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_21_LBL.setObjectName("BTab_Slot_21_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_21_LBL, 17, 0, 1, 1)
		# BTab Slot 22
		self.BTab_Slot_22_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_22_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_22_TB.setObjectName("BTab_Slot_22_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_22_TB, 18, 1, 1, 1)
		self.BTab_Slot_22_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_22_LBL.setObjectName("BTab_Slot_22_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_22_LBL, 18, 0, 1, 1)
		# BTab Slot 23
		self.BTab_Slot_23_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_23_LBL.setObjectName("BTab_Slot_23_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_23_LBL, 19, 0, 1, 1)
		self.BTab_Slot_23_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_23_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_23_TB.setObjectName("BTab_Slot_23_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_23_TB, 19, 1, 1, 1)
		# BTab Slot 24
		self.BTab_Slot_24_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_24_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_24_TB.setObjectName("BTab_Slot_24_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_24_TB, 20, 1, 1, 1)
		self.BTab_Slot_24_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_24_LBL.setObjectName("BTab_Slot_24_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_24_LBL, 20, 0, 1, 1)
		# BTab Slot 25
		self.BTab_Slot_25_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_25_LBL.setObjectName("BTab_Slot_25_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_25_LBL, 21, 0, 1, 1)
		self.BTab_Slot_25_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_25_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_25_TB.setObjectName("BTab_Slot_25_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_25_TB, 21, 1, 1, 1)
		# BTab Slot 26
		self.BTab_Slot_26_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_26_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_26_TB.setObjectName("BTab_Slot_26_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_26_TB, 22, 1, 1, 1)
		self.BTab_Slot_26_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_26_LBL.setObjectName("BTab_Slot_26_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_26_LBL, 22, 0, 1, 1)
		# BTab Slot 27
		self.BTab_Slot_27_LBL = QtWidgets.QLabel(self.formLayoutWidget_3)
		self.BTab_Slot_27_LBL.setObjectName("BTab_Slot_27_LBL")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_27_LBL, 23, 0, 1, 1)
		self.BTab_Slot_27_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
		self.BTab_Slot_27_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.BTab_Slot_27_TB.setObjectName("BTab_Slot_27_TB")
		self.BTab_gridLayout.addWidget(self.BTab_Slot_27_TB, 23, 1, 1, 1)
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
		self.BTab_Picture_LBL.setPixmap(QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
		self.BTab_Picture_LBL.setScaledContents(True)
		self.BTab_Picture_LBL.setObjectName("BTab_Picture_LBL")
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

		self.PopUp_Bullet_Add = QtWidgets.QMainWindow()
		# import class UI_PopUp_Add_Bullet from .\PopUp_Add_Bullet.py
		addBullet = Add_Bullet.Ui_PopUp_Add_Bullet(bullets_df)
		addBullet.setupUi(self.PopUp_Bullet_Add)
		self.BTab_Add_BTN.clicked.connect(self.PopUp_Add_Bullet_BTN)

		# BTab View All BTN
		self.BTab_View_All_BTN = QtWidgets.QPushButton(
			self.verticalLayoutWidget_3)
		self.BTab_View_All_BTN.setAutoDefault(False)
		self.BTab_View_All_BTN.setDefault(True)
		self.BTab_View_All_BTN.setObjectName("BTab_View_All_BTN")
		self.BTab_verticalLayout.addWidget(self.BTab_View_All_BTN)
		self.PopUp_Bullet_Show = QtWidgets.QMainWindow()
		ShowAllBullets = Show_Bullets.Ui_ShowBullets()
		ShowAllBullets.setupUi(self.PopUp_Bullet_Show)
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
		self.PTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Name_TB.setObjectName("PTab_Name_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Name_TB, 0, 1, 1, 1)
		self.PTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Name_LBL.setObjectName("PTab_Name_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Name_LBL, 0, 0, 1, 1)
		# PTab Manufacturer
		self.PTab_Manufacturer_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Manufacturer_TB.setObjectName("PTab_Manufacturer_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Manufacturer_TB, 1, 1, 1, 1)
		self.PTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Manufacturer_LBL.setObjectName("PTab_Manufacturer_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Manufacturer_LBL, 1, 0, 1, 1)
		# Model
		self.PTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Model_TB.setObjectName("PTab_Model_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Model_TB, 2, 1, 1, 1)
		self.PTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Model_LBL.setObjectName("PTab_Model_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Model_LBL, 2, 0, 1, 1)
		# SKU
		self.PTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_SKU_LBL.setObjectName("PTab_SKU_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_SKU_LBL, 3, 0, 1, 1)
		self.PTab_SKU_TB = QtWidgets.QTextBrowser(
			self.formLayoutWidget_4)
		self.PTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_SKU_TB.setObjectName("PTab_SKU_TB")
		self.PTab_gridLayout.addWidget(self.PTab_SKU_TB, 3, 1, 1, 1)
		# PTab Relitive Burn Rate
		self.PTab_BurnRate_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_BurnRate_LBL.setObjectName("PTab_BurnRate_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_BurnRate_LBL, 4, 0, 1, 1)
		self.PTab_BurnRate_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_BurnRate_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_BurnRate_TB.setObjectName("PTab_BurnRate_TB")
		self.PTab_gridLayout.addWidget(self.PTab_BurnRate_TB, 4, 1, 1, 1)
		# PTab Weapon Use
		self.PTab_WeaponUse_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_WeaponUse_LBL.setObjectName("PTab_WeaponUse_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_WeaponUse_LBL, 5, 0, 1, 1)
		self.PTab_WeaponUse_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_WeaponUse_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_WeaponUse_TB.setObjectName("PTab_Caliber_TB")
		self.PTab_gridLayout.addWidget(self.PTab_WeaponUse_TB, 5, 1, 1, 1)
		# PTab Density 
		self.PTab_Density_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Density_LBL.setObjectName("PTab_Density_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Density_LBL, 6, 0, 1, 1)
		self.PTab_Density_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Density_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Density_TB.setObjectName("PTab_Density_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Density_TB, 6, 1, 1, 1)
		# PTab Bulk Density
		self.PTab_BulkDensity_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_BulkDensity_LBL.setObjectName("PTab_BulkDensity_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_BulkDensity_LBL, 7, 0, 1, 1)
		self.PTab_BulkDensity_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_BulkDensity_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_BulkDensity_TB.setObjectName("PTab_BulkDensity_TB")
		self.PTab_gridLayout.addWidget(self.PTab_BulkDensity_TB, 7, 1, 1, 1)
		# PTab Slot 12
		self.PTab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_12_LBL.setObjectName("PTab_Slot_12_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_12_LBL, 8, 0, 1, 1)
		self.PTab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_12_TB.setObjectName("PTab_Slot_12_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_12_TB, 8, 1, 1, 1)
		# PTab Slot 13
		self.PTab_Slot_13_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_13_LBL.setObjectName("PTab_Slot_13_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_13_LBL, 9, 0, 1, 1)
		self.PTab_Slot_13_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_13_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_13_TB.setObjectName("PTab_Slot_13_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_13_TB, 9, 1, 1, 1)
		# PTab Slot 14
		self.PTab_Slot_14_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_14_LBL.setObjectName("PTab_Slot_14_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_14_LBL, 10, 0, 1, 1)
		self.PTab_Slot_14_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_14_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_14_TB.setObjectName("PTab_Slot_14_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_14_TB, 10, 1, 1, 1)
		# PTab Slot 15
		self.PTab_Slot_15_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_15_LBL.setObjectName("PTab_Slot_15_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_15_LBL, 11, 0, 1, 1)
		self.PTab_Slot_15_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_15_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_15_TB.setObjectName("PTab_Slot_15_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_15_TB, 11, 1, 1, 1)
		# PTab Slot 16
		self.PTab_Slot_16_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_16_LBL.setObjectName("PTab_Slot_16_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_16_LBL, 13, 0, 1, 1)
		self.PTab_Slot_16_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_16_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_16_TB.setObjectName("PTab_Slot_16_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_16_TB, 13, 1, 1, 1)
		# PTab Slot 17
		self.PTab_Slot_17_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_17_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_17_TB.setObjectName("PTab_Slot_17_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_17_TB, 14, 1, 1, 1)
		self.PTab_Slot_17_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_17_LBL.setObjectName("PTab_Slot_17_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_17_LBL, 14, 0, 1, 1)
		# PTab Slot 18
		self.PTab_Slot_18_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_18_LBL.setObjectName("PTab_Slot_18_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_18_LBL, 15, 0, 1, 1)
		self.PTab_Slot_18_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_18_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_18_TB.setObjectName("PTab_Slot_18_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_18_TB, 15, 1, 1, 1)
		# PTab Slot 19
		self.PTab_Slot_19_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_19_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_19_TB.setObjectName("PTab_Slot_19_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_19_TB, 16, 1, 1, 1)
		self.PTab_Slot_19_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_19_LBL.setObjectName("PTab_Slot_19_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_19_LBL, 16, 0, 1, 1)
		# PTab Slot 20
		self.PTab_Slot_20_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_20_LBL.setObjectName("PTab_Slot_20_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_20_LBL, 18, 0, 1, 1)
		self.PTab_Slot_20_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_20_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_20_TB.setObjectName("PTab_Slot_20_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_20_TB, 18, 1, 1, 1)
		# PTab Slot 21
		self.PTab_Slot_21_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_21_LBL.setObjectName("PTab_Slot_21_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_21_LBL, 19, 0, 1, 1)
		self.PTab_Slot_21_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_21_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_21_TB.setObjectName("PTab_Slot_21_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_21_TB, 19, 1, 1, 1)
		# PTab Slot 22
		self.PTab_Slot_22_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_22_LBL.setObjectName("PTab_Slot_22_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_22_LBL, 21, 0, 1, 1)
		self.PTab_Slot_22_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_22_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_22_TB.setObjectName("PTab_Slot_22_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_22_TB, 21, 1, 1, 1)
		# PTab Slot 23
		self.PTab_Slot_23_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_23_LBL.setObjectName("PTab_Slot_23_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_23_LBL, 23, 0, 1, 1)
		self.PTab_Slot_23_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_23_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_23_TB.setObjectName("PTab_Slot_23_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_23_TB, 23, 1, 1, 1)
		# PTab Slot 24
		self.PTab_Slot_24_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_24_LBL.setObjectName("PTab_Slot_24_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_24_LBL, 25, 0, 1, 1)
		self.PTab_Slot_24_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_24_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_24_TB.setObjectName("PTab_Slot_24_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_24_TB, 25, 1, 1, 1)
		# pTab Slot 25
		self.PTab_Slot_25_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_25_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_25_TB.setObjectName("PTab_Slot_25_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_25_TB, 26, 1, 1, 1)
		self.PTab_Slot_25_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_25_LBL.setObjectName("PTab_Slot_25_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_25_LBL, 26, 0, 1, 1)
		# BTab Slot 26
		self.PTab_Slot_26_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_26_LBL.setObjectName("PTab_Slot_26_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_26_LBL, 28, 0, 1, 1)
		self.PTab_Slot_26_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_26_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_26_TB.setObjectName("PTab_Slot_26_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_26_TB, 28, 1, 1, 1)
		# PTab Slot 27
		self.PTab_Slot_27_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_4)
		self.PTab_Slot_27_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PTab_Slot_27_TB.setObjectName("PTab_Slot_27_TB")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_27_TB, 30, 1, 1, 1)
		self.PTab_Slot_27_LBL = QtWidgets.QLabel(self.formLayoutWidget_4)
		self.PTab_Slot_27_LBL.setObjectName("PTab_Slot_27_LBL")
		self.PTab_gridLayout.addWidget(self.PTab_Slot_27_LBL, 30, 0, 1, 1)

		# PTab Notes
		self.PTab_Notes_LBL = QtWidgets.QLabel(self.PTab_tab)
		self.PTab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
		self.PTab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
		self.PTab_Notes_LBL.setObjectName("PTab_Notes_LBL")
		self.PTab_Notes_TB = QtWidgets.QTextBrowser(self.PTab_tab)
		self.PTab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
		self.PTab_Notes_TB.setObjectName("PTab_Notes_TB")
		# PTab Picture
		self.PTab_Picture_LBL = QtWidgets.QLabel(self.PTab_tab)
		self.PTab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
		self.PTab_Picture_LBL.setText("")
		self.PTab_Picture_LBL.setScaledContents(True)
		self.PTab_Picture_LBL.setObjectName("PTab_Picture_LBL")

		# PTab Show Data BTN
		self.PTab_ShowData_BTN = QtWidgets.QPushButton(self.PTab_tab)
		self.PTab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
		self.PTab_ShowData_BTN.setDefault(True)
		self.PTab_ShowData_BTN.setObjectName("PTab_ShowData_BTN")
		self.PTab_ShowData_BTN.clicked.connect(self.displayData_PTab)
		# PTab Add BTN
		self.PTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
		self.PTab_Add_BTN.setDefault(True)
		self.PTab_Add_BTN.setObjectName("PTab_Add_BTN")
		self.PTab_verticalLayout.addWidget(self.PTab_Add_BTN)

		self.PopUp_Powder_Add = QtWidgets.QMainWindow()
		addPowder = Add_Powder.Ui_PopUp_Add_Powder(powders_df)
		addPowder.setupUi(self.PopUp_Powder_Add)
		self.PTab_Add_BTN.clicked.connect(self.PopUp_Add_Powder_BTN)

		# PTab View All BTN
		self.PTab_View_All_BTN = QtWidgets.QPushButton(
			self.verticalLayoutWidget_4)
		self.PTab_View_All_BTN.setAutoDefault(False)
		self.PTab_View_All_BTN.setDefault(True)
		self.PTab_View_All_BTN.setObjectName("PTab_View_All_BTN")
		self.PTab_verticalLayout.addWidget(self.PTab_View_All_BTN)
		self.PopUp_Powder_Show = QtWidgets.QMainWindow()
		ShowAllPowders = Show_Powders.Ui_ShowPowders()
		ShowAllPowders.setupUi(self.PopUp_Powder_Show)
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

		self.formLayoutWidget_5 = QtWidgets.QWidget(self.CTab_tab)
		self.formLayoutWidget_5.setGeometry(QtCore.QRect(10, 60, 471, 928))
		self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
		self.CTab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_5)
		self.CTab_gridLayout.setContentsMargins(0, 0, 0, 0)
		self.CTab_gridLayout.setObjectName("CTab_gridLayout")
		spacerItem3 = QtWidgets.QSpacerItem(20, 40,
											QtWidgets.QSizePolicy.Minimum,
											QtWidgets.QSizePolicy.Expanding)
		self.CTab_gridLayout.addItem(spacerItem3, 34, 1, 1, 1)

		# CTab ComboBox
		self.CTab_Cases_Combo = QtWidgets.QComboBox(self.CTab_tab)
		self.CTab_Cases_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
		self.CTab_Cases_Combo.setObjectName("CTab_Cases_Combo")
		self.CTab_Cases_Combo.addItems(cases_list)
		# CTab Name
		self.CTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Name_TB.setObjectName("CTab_Name_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Name_TB, 0, 1, 1, 1)
		self.CTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Name_LBL.setObjectName("CTab_Name_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Name_LBL, 0, 0, 1, 1)
		# CTab Manufacturer
		self.CTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Manufacturer_LBL.setObjectName("CTab_Manufacturer_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Manufacturer_LBL, 1, 0, 1, 1)
		self.CTab_Manufacturer_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Manufacturer_TB.setObjectName("CTab_Manufacturer_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Manufacturer_TB, 1, 1, 1, 1)
		# CTab Model
		self.CTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Model_TB.setObjectName("CTab_Model_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Model_TB, 2, 1, 1, 1)
		self.CTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Model_LBL.setObjectName("CTab_Model_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Model_LBL, 2, 0, 1, 1)
		# CTab SKU
		self.CTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_SKU_TB.setObjectName("CTab_SKU_TB")
		self.CTab_gridLayout.addWidget(self.CTab_SKU_TB, 3, 1, 1, 1)
		self.CTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_SKU_LBL.setObjectName("CTab_SKU_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_SKU_LBL, 3, 0, 1, 1)
		# CTab Finish
		self.CTab_Finish_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Finish_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Finish_TB.setObjectName("CTab_Finish_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Finish_TB, 4, 1, 1, 1)
		self.CTab_Finish_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Finish_LBL.setObjectName("CTab_Finish_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Finish_LBL, 4, 0, 1, 1)
		# CTab Primer Size
		self.CTab_PrimerSize_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_PrimerSize_LBL.setObjectName("CTab_PrimerSize_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_PrimerSize_LBL, 5, 0, 1, 1)
		self.CTab_PrimerSize_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_PrimerSize_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_PrimerSize_TB.setObjectName("CTab_PrimerSize_TB")
		self.CTab_gridLayout.addWidget(self.CTab_PrimerSize_TB, 5, 1, 1, 1)
		# CTab Type
		self.CTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Type_LBL.setObjectName("CTab_Type_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Type_LBL, 6, 0, 1, 1)
		self.CTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Type_TB.setObjectName("CTab_Type_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Type_TB, 6, 1, 1, 1)
		# CTab Slot 10
		self.CTab_Slot_10_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_10_LBL.setObjectName("CTab_Slot_10_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_10_LBL, 7, 0, 1, 1)
		self.CTab_Slot_10_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_10_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_10_TB.setObjectName("CTab_Slot_10_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_10_TB, 7, 1, 1, 1)
		# CTab Slot 11
		self.CTab_Slot_11_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_11_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_11_TB.setObjectName("CTab_Slot_11_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_11_TB, 8, 1, 1, 1)
		self.CTab_Slot_11_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_11_LBL.setObjectName("CTab_Slot_11_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_11_LBL, 8, 0, 1, 1)
		# CTab Slot 12
		self.CTab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_12_LBL.setObjectName("CTab_Slot_12_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_12_LBL, 9, 0, 1, 1)
		self.CTab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_12_TB.setObjectName("CTab_Slot_12_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_12_TB, 9, 1, 1, 1)
		# CTab Slot 13
		self.CTab_Slot_13_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_13_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_13_TB.setObjectName("CTab_Slot_13_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_13_TB, 10, 1, 1, 1)
		self.CTab_Slot_13_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_13_LBL.setObjectName("CTab_Slot_13_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_13_LBL, 10, 0, 1, 1)
		# CTab Slot 14
		self.CTab_Slot_14_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_14_LBL.setObjectName("CTab_Slot_14_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_14_LBL, 11, 0, 1, 1)
		self.CTab_Slot_14_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_14_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_14_TB.setObjectName("CTab_Slot_14_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_14_TB, 11, 1, 1, 1)
		# CTab Slot 15
		self.CTab_Slot_15_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_15_LBL.setObjectName("CTab_Slot_15_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_15_LBL, 12, 0, 1, 1)
		self.CTab_Slot_15_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_15_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_15_TB.setObjectName("CTab_Slot_15_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_15_TB, 12, 1, 1, 1)
		# CTab Slot 16
		self.CTab_Slot_16_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_16_LBL.setObjectName("CTab_Slot_16_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_16_LBL, 13, 0, 1, 1)
		self.CTab_Slot_16_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_16_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_16_TB.setObjectName("CTab_Slot_16_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_16_TB, 13, 1, 1, 1)
		# CTab Slot 17
		self.CTab_Slot_17_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_17_LBL.setObjectName("CTab_Slot_17_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_17_LBL, 14, 0, 1, 1)
		self.CTab_Slot_17_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_17_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_17_TB.setObjectName("CTab_Slot_17_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_17_TB, 14, 1, 1, 1)
		# CTab Slot 18
		self.CTab_Slot_18_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_18_LBL.setObjectName("CTab_Slot_18_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_18_LBL, 15, 0, 1, 1)
		self.CTab_Slot_18_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_18_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_18_TB.setObjectName("CTab_Slot_18_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_18_TB, 15, 1, 1, 1)
		# CTab Slot 19
		self.CTab_Slot_19_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_19_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_19_TB.setObjectName("CTab_Slot_19_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_19_TB, 16, 1, 1, 1)
		self.CTab_Slot_19_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_19_LBL.setObjectName("CTab_Slot_19_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_19_LBL, 16, 0, 1, 1)
		# CTab Slot 20
		self.CTab_Slot_20_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_20_LBL.setObjectName("CTab_Slot_20_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_20_LBL, 17, 0, 1, 1)
		self.CTab_Slot_20_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_20_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_20_TB.setObjectName("CTab_Slot_20_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_20_TB, 17, 1, 1, 1)
		# CTab Slot 21
		self.CTab_Slot_21_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_21_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_21_TB.setObjectName("CTab_Slot_21_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_21_TB, 18, 1, 1, 1)
		self.CTab_Slot_21_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_21_LBL.setObjectName("CTab_Slot_21_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_21_LBL, 18, 0, 1, 1)
		# CTab Slot 22
		self.CTab_Slot_22_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_22_LBL.setObjectName("CTab_Slot_22_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_22_LBL, 19, 0, 1, 1)
		self.CTab_Slot_22_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_22_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_22_TB.setObjectName("CTab_Slot_22_TBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_22_TB, 19, 1, 1, 1)
		# CTab Slot 23
		self.CTab_Slot_23_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_23_LBL.setObjectName("CTab_Slot_23_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_23_LBL, 20, 0, 1, 1)
		self.CTab_Slot_23_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_23_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_23_TB.setObjectName("CTab_Slot_23_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_23_TB, 20, 1, 1, 1)
		# CTab Slot 24
		self.CTab_Slot_24_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_24_LBL.setObjectName("CTab_Slot_24_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_24_LBL, 21, 0, 1, 1)
		self.CTab_Slot_24_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_24_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_24_TB.setObjectName("CTab_Slot_24_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_24_TB, 21, 1, 1, 1)
		# CTab Slot 25
		self.CTab_Slot_25_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_25_LBL.setObjectName("CTab_Slot_25_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_25_LBL, 22, 0, 1, 1)
		self.CTab_Slot_25_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_25_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_25_TB.setObjectName("CTab_Slot_25_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_25_TB, 22, 1, 1, 1)
		# CTab Slot 26
		self.CTab_Slot_26_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_26_LBL.setObjectName("CTab_Slot_26_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_26_LBL, 23, 0, 1, 1)
		self.CTab_Slot_26_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_26_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_26_TB.setObjectName("CTab_Slot_26_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_26_TB, 23, 1, 1, 1)
		# CTab Slot 27
		self.CTab_Slot_27_LBL = QtWidgets.QLabel(self.formLayoutWidget_5)
		self.CTab_Slot_27_LBL.setObjectName("CTab_Slot_27_LBL")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_27_LBL, 24, 0, 1, 1)
		self.CTab_Slot_27_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_5)
		self.CTab_Slot_27_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.CTab_Slot_27_TB.setObjectName("CTab_Slot_27_TB")
		self.CTab_gridLayout.addWidget(self.CTab_Slot_27_TB, 24, 1, 1, 1)
		# CTab Notes
		self.CTab_Notes_TB = QtWidgets.QTextBrowser(self.CTab_tab)
		self.CTab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
		self.CTab_Notes_TB.setObjectName("CTab_Notes_TB")
		self.CTab_Notes_LBL = QtWidgets.QLabel(self.CTab_tab)
		self.CTab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
		self.CTab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
		self.CTab_Notes_LBL.setObjectName("CTab_Notes_LBL")
		# CTab Picture
		self.CTab_Picture_LBL = QtWidgets.QLabel(self.CTab_tab)
		self.CTab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
		self.CTab_Picture_LBL.setText("")
		#self.CTab_Picture_LBL.setPixmap(QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
		self.CTab_Picture_LBL.setScaledContents(True)
		self.CTab_Picture_LBL.setObjectName("CTab_Picture_LBL")

		self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.CTab_tab)
		self.verticalLayoutWidget_5.setGeometry(
			QtCore.QRect(490, 80, 160, 361))
		self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
		self.CTab_verticalLayout = QtWidgets.QVBoxLayout(
			self.verticalLayoutWidget_5)
		self.CTab_verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.CTab_verticalLayout.setObjectName("CTab_verticalLayout")
		# CTab Show Data BTN
		self.CTab_ShowData_BTN = QtWidgets.QPushButton(self.CTab_tab)
		self.CTab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
		self.CTab_ShowData_BTN.setDefault(True)
		self.CTab_ShowData_BTN.setObjectName("CTab_ShowData_BTN")
		self.CTab_ShowData_BTN.clicked.connect(self.displayData_CTab)
		# CTab Add Case to DB BTN
		self.CTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
		self.CTab_Add_BTN.setDefault(True)
		self.CTab_Add_BTN.setObjectName("CTab_Add_BTN")
		self.CTab_verticalLayout.addWidget(self.CTab_Add_BTN)
		# CTab Add Case
		self.PopUp_Case_Add = QtWidgets.QMainWindow()
		# import class UI_PopUp_Add_Case from .\PopUp_Add_Case.py
		addCase = Add_Case.Ui_PopUp_Add_Case(cases_df)
		addCase.setupUi(self.PopUp_Case_Add)
		self.CTab_Add_BTN.clicked.connect(self.PopUp_Add_Case_BTN)
		# CTab View All cases BTN
		self.CTab_View_All_BTN = QtWidgets.QPushButton(
			self.verticalLayoutWidget_5)
		self.CTab_View_All_BTN.setAutoDefault(False)
		self.CTab_View_All_BTN.setDefault(True)
		self.CTab_View_All_BTN.setObjectName("CTab_View_All_BTN")
		self.CTab_verticalLayout.addWidget(self.CTab_View_All_BTN)
		self.CTab_verticalLayout.addWidget(self.CTab_View_All_BTN)
		self.PopUp_Case_Show = QtWidgets.QMainWindow()
		ShowAllCases = Show_Cases.Ui_ShowCases()
		ShowAllCases.setupUi(self.PopUp_Case_Show)
		self.CTab_View_All_BTN.clicked.connect(self.PopUp_ShowAllCases)
		# CTab BTN 3
		self.CTab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
		self.CTab_BTN_3.setDefault(True)
		self.CTab_BTN_3.setObjectName("Import Test")
		self.CTab_verticalLayout.addWidget(self.CTab_BTN_3)
		# CTab BTN 4
		self.CTab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
		self.CTab_BTN_4.setDefault(True)
		self.CTab_BTN_4.setObjectName("CTab_BTN_4")
		self.CTab_verticalLayout.addWidget(self.CTab_BTN_4)
		# CTab BTN 5
		self.CTab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
		self.CTab_BTN_5.setDefault(True)
		self.CTab_BTN_5.setObjectName("CTab_BTN_5")
		self.CTab_verticalLayout.addWidget(self.CTab_BTN_5)
		# CTab BTN 6
		self.CTab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
		self.CTab_BTN_6.setDefault(True)
		self.CTab_BTN_6.setObjectName("CTab_BTN_6")
		self.CTab_verticalLayout.addWidget(self.CTab_BTN_6)
		# CTab BTN 7
		self.CTab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
		self.CTab_BTN_7.setDefault(True)
		self.CTab_BTN_7.setObjectName("CTab_BTN_7")
		self.CTab_verticalLayout.addWidget(self.CTab_BTN_7)
		# CTab BTN 8
		self.CTab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
		self.CTab_BTN_8.setAutoDefault(False)
		self.CTab_BTN_8.setDefault(True)
		self.CTab_BTN_8.setObjectName("CTab_BTN_8")
		self.CTab_verticalLayout.addWidget(self.CTab_BTN_8)
		# CTab BTN 9
		self.CTab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
		self.CTab_BTN_9.setAutoDefault(False)
		self.CTab_BTN_9.setDefault(True)
		self.CTab_BTN_9.setObjectName("CTab_BTN_9")
		self.CTab_verticalLayout.addWidget(self.CTab_BTN_9)
		# CTab BTN 10
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


		self.formLayoutWidget_6 = QtWidgets.QWidget(self.PRTab_tab)
		self.formLayoutWidget_6.setGeometry(QtCore.QRect(10, 60, 471, 928))
		self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")

		self.PRTab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_6)
		self.PRTab_gridLayout.setContentsMargins(0, 0, 0, 0)
		self.PRTab_gridLayout.setObjectName("PRTab_gridLayout")
		spacerItem4 = QtWidgets.QSpacerItem(20, 40,
											QtWidgets.QSizePolicy.Minimum,
											QtWidgets.QSizePolicy.Expanding)
		self.PRTab_gridLayout.addItem(spacerItem4, 34, 1, 1, 1)
		# PRTab Combo Box
		self.PRTab_Primer_LBL = QtWidgets.QLabel(self.PRTab_tab)
		self.PRTab_Primer_LBL.setGeometry(QtCore.QRect(20, 10, 451, 20))
		self.PRTab_Primer_LBL.setAlignment(QtCore.Qt.AlignCenter)
		self.PRTab_Primer_LBL.setObjectName("PRTab_Primer_LBL")
		self.PRTab_Primer_Combo = QtWidgets.QComboBox(self.PRTab_tab)
		self.PRTab_Primer_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
		self.PRTab_Primer_Combo.setObjectName("PRTab_Primer_Combo")
		self.PRTab_Primer_Combo.addItems(primers_list)

		# PRTab Name
		self.PRTab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Name_LBL.setObjectName("PRTab_Name_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Name_LBL, 0, 0, 1, 1)
		self.PRTab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Name_TB.setObjectName("PRTab_Name_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Name_TB, 0, 1, 1, 1)
		# PRTab Manufacturer
		self.PRTab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Manufacturer_LBL.setObjectName("PRTab_Manufacturer_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Manufacturer_LBL, 1, 0, 1, 1)
		self.PRTab_Manufacturer_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Manufacturer_TB.setObjectName("PRTab_Manufacturer_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Manufacturer_TB, 1, 1, 1, 1)
		# PRTab Model
		self.PRTab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Model_LBL.setObjectName("PRTab_Model_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Model_LBL, 2, 0, 1, 1)
		self.PRTab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Model_TB.setObjectName("PRTab_Model_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Model_TB, 2, 1, 1, 1)
		# PRTab SKU
		self.PRTab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_SKU_TB.setObjectName("PRTab_SKU_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_SKU_TB, 3, 1, 1, 1)
		self.PRTab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_SKU_LBL.setObjectName("PRTab_SKU_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_SKU_LBL, 3, 0, 1, 1)
		# PRTab Size
		self.PRTab_Size_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Size_LBL.setObjectName("PRTab_Size_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Size_LBL, 4, 0, 1, 1)
		self.PRTab_Size_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Size_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Size_TB.setObjectName("PRTab_Size_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Size_TB, 4, 1, 1, 1)
		# PRTab Type
		self.PRTab_Type_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Type_LBL.setObjectName("PRTab_Type_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Type_LBL, 5, 0, 1, 1)
		self.PRTab_Type_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Type_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Type_TB.setObjectName("PRTab_Type_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Type_TB, 5, 1, 1, 1)
		# PRTab Slot 10
		self.PRTab_Slot_10_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_10_LBL.setObjectName("PRTab_Slot_10_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_10_LBL, 6, 0, 1, 1)
		self.PRTab_Slot_10_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_10_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_10_TB.setObjectName("PRTab_Slot_10_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_10_TB, 6, 1, 1, 1)
		# PRTab Slot 11
		self.PRTab_Slot_11_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_11_LBL.setObjectName("PRTab_Slot_11_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_11_LBL, 7, 0, 1, 1)
		self.PRTab_Slot_11_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_11_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_11_TB.setObjectName("PRTab_Slot_11_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_11_TB, 7, 1, 1, 1)
		# PRTab Slot 12
		self.PRTab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_12_LBL.setObjectName("PRTab_Slot_12_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_12_LBL, 8, 0, 1, 1)
		self.PRTab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_12_TB.setObjectName("PRTab_Slot_12_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_12_TB, 8, 1, 1, 1)
		# PRTab Slot 13
		self.PRTab_Slot_13_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_13_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_13_TB.setObjectName("PRTab_Slot_13_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_13_TB, 9, 1, 1, 1)
		self.PRTab_Slot_13_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_13_LBL.setObjectName("PRTab_Slot_13_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_13_LBL, 9, 0, 1, 1)
		# PRTab Slot 14
		self.PRTab_Slot_14_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_14_LBL.setObjectName("PRTab_Slot_14_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_14_LBL, 10, 0, 1, 1)
		self.PRTab_Slot_14_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_14_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_14_TB.setObjectName("PRTab_Slot_14_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_14_TB, 10, 1, 1, 1)
		# PRTab Slot 15
		self.PRTab_Slot_15_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_15_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_15_TB.setObjectName("PRTab_Slot_15_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_15_TB, 11, 1, 1, 1)
		self.PRTab_Slot_15_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_15_LBL.setObjectName("PRTab_Slot_15_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_15_LBL, 11, 0, 1, 1)
		# PRTab Slot 16
		self.PRTab_Slot_16_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_16_LBL.setObjectName("PRTab_Slot_16_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_16_LBL, 12, 0, 1, 1)
		self.PRTab_Slot_16_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_16_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_16_TB.setObjectName("PRTab_Slot_16_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_16_TB, 12, 1, 1, 1)
		# PRTab Slot 17
		self.PRTab_Slot_17_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_17_LBL.setObjectName("PRTab_Slot_17_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_17_LBL, 13, 0, 1, 1)
		self.PRTab_Slot_17_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_17_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_17_TB.setObjectName("PRTab_Slot_17_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_17_TB, 13, 1, 1, 1)
		# PRTab Slot 18
		self.PRTab_Slot_18_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_18_LBL.setObjectName("PRTab_Slot_18_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_18_LBL, 14, 0, 1, 1)
		self.PRTab_Slot_18_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_18_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_18_TB.setObjectName("PRTab_Slot_18_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_18_TB, 14, 1, 1, 1)
		# PRTab Slot 19
		self.PRTab_Slot_19_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_19_LBL.setObjectName("PRTab_Slot_19_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_19_LBL, 15, 0, 1, 1)
		self.PRTab_Slot_19_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_19_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_19_TB.setObjectName("PRTab_Slot_19_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_19_TB, 15, 1, 1, 1)
		# PRTab Slot 20
		self.PRTab_Slot_20_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_20_LBL.setObjectName("PRTab_Slot_20_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_20_LBL, 16, 0, 1, 1)
		self.PRTab_Slot_20_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_20_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_20_TB.setObjectName("PRTab_Slot_20_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_20_TB, 16, 1, 1, 1)
		# PRTab Slot 21
		self.PRTab_Slot_21_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_21_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_21_TB.setObjectName("PRTab_Slot_21_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_21_TB, 17, 1, 1, 1)
		self.PRTab_Slot_21_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_21_LBL.setObjectName("PRTab_Slot_21_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_21_LBL, 17, 0, 1, 1)
		# PRTab Slot 22
		self.PRTab_Slot_22_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_22_LBL.setObjectName("PRTab_Slot_22_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_22_LBL, 18, 0, 1, 1)
		self.PRTab_Slot_22_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_22_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_22_TB.setObjectName("PRTab_Slot_22_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_22_TB, 18, 1, 1, 1)
		# PRTab Slot 23
		self.PRTab_Slot_23_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_23_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_23_TB.setObjectName("PRTab_Slot_23_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_23_TB, 19, 1, 1, 1)
		self.PRTab_Slot_23_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_23_LBL.setObjectName("PRTab_Slot_23_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_23_LBL, 19, 0, 1, 1)
		# PRTab Slot 24
		self.PRTab_Slot_24_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_24_LBL.setObjectName("PRTab_Slot_24_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_24_LBL, 20, 0, 1, 1)
		self.PRTab_Slot_24_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_24_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_24_TB.setObjectName("PRTab_Slot_24_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_24_TB, 20, 1, 1, 1)
		# PRTab Slot 25
		self.PRTab_Slot_25_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_25_LBL.setObjectName("PRTab_Slot_25_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_25_LBL, 21, 0, 1, 1)
		self.PRTab_Slot_25_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_25_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_25_TB.setObjectName("PRTab_Slot_25_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_25_TB, 21, 1, 1, 1)
		# PRTab Slot 26
		self.PRTab_Slot_26_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_26_LBL.setObjectName("PRTab_Slot_26_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_26_LBL, 22, 0, 1, 1)
		self.PRTab_Slot_26_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_26_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_26_TB.setObjectName("PRTab_Slot_26_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_26_TB, 22, 1, 1, 1)
		# PRTab Slot 27
		self.PRTab_Slot_27_LBL = QtWidgets.QLabel(self.formLayoutWidget_6)
		self.PRTab_Slot_27_LBL.setObjectName("PRTab_Slot_27_LBL")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_27_LBL, 23, 0, 1, 1)
		self.PRTab_Slot_27_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_6)
		self.PRTab_Slot_27_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.PRTab_Slot_27_TB.setObjectName("PRTab_Slot_27_TB")
		self.PRTab_gridLayout.addWidget(self.PRTab_Slot_27_TB, 23, 1, 1, 1)
		# PRTab Notes
		self.PRTab_Notes_TB = QtWidgets.QTextBrowser(self.PRTab_tab)
		self.PRTab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
		self.PRTab_Notes_TB.setObjectName("PRTab_Notes_TB")
		self.PRTab_Notes_LBL = QtWidgets.QLabel(self.PRTab_tab)
		self.PRTab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
		self.PRTab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
		self.PRTab_Notes_LBL.setObjectName("PRTab_Notes_LBL")
		# PRTab Pictrue
		self.PRTab_Picture_LBL = QtWidgets.QLabel(self.PRTab_tab)
		self.PRTab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
		self.PRTab_Picture_LBL.setText("")
		self.PRTab_Picture_LBL.setPixmap(QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
		self.PRTab_Picture_LBL.setScaledContents(True)
		self.PRTab_Picture_LBL.setObjectName("PRTab_Picture_LBL")

		self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.PRTab_tab)
		self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(490, 80, 160, 361))
		self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
		self.PRTab_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
		self.PRTab_verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.PRTab_verticalLayout.setObjectName("PRTab_verticalLayout")
		# PRTab Show Primer Data
		self.PRTab_ShowData_BTN = QtWidgets.QPushButton(self.PRTab_tab)
		self.PRTab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
		self.PRTab_ShowData_BTN.setDefault(True)
		self.PRTab_ShowData_BTN.setObjectName("PRTab_ShowData_BTN")
		self.PRTab_ShowData_BTN.clicked.connect(self.displayData_PRTab)
		# PRTab Add Primer BTN
		self.PRTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
		self.PRTab_Add_BTN.setDefault(True)
		self.PRTab_Add_BTN.setObjectName("PRTab_Add_BTN")
		self.PRTab_verticalLayout.addWidget(self.PRTab_Add_BTN)
		self.PopUp_Primer_Add = QtWidgets.QMainWindow()
		# import class UI_PopUp_Add_Firearm from .\PopUp_Add_Firearm.py
		addPrimer = Add_Primer.Ui_PopUp_Add_Primer(primers_df)
		addPrimer.setupUi(self.PopUp_Primer_Add)
		self.PRTab_Add_BTN.clicked.connect(self.PopUp_Add_Primer_BTN)
		# PRTab View All BTN
		self.PRTab_View_All_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
		self.PRTab_View_All_BTN.setAutoDefault(False)
		self.PRTab_View_All_BTN.setDefault(True)
		self.PRTab_View_All_BTN.setObjectName("PRTab_View_All_BTN")
		self.PRTab_verticalLayout.addWidget(self.PRTab_View_All_BTN)
		# PRTab BTN 3
		self.PRTab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
		self.PRTab_BTN_3.setDefault(True)
		self.PRTab_BTN_3.setObjectName("PRTab_BTN_3")
		self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_3)
		# PRTab BTN 4
		self.PRTab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
		self.PRTab_BTN_4.setDefault(True)
		self.PRTab_BTN_4.setObjectName("PRTab_BTN_4")
		self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_4)
		# PRTab BTN 5
		self.PRTab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
		self.PRTab_BTN_5.setDefault(True)
		self.PRTab_BTN_5.setObjectName("PRTab_BTN_5")
		self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_5)
		# PRTab BTN 6
		self.PRTab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
		self.PRTab_BTN_6.setDefault(True)
		self.PRTab_BTN_6.setObjectName("PRTab_BTN_6")
		self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_6)
		# PRTab BTN 7
		self.PRTab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
		self.PRTab_BTN_7.setDefault(True)
		self.PRTab_BTN_7.setObjectName("PRTab_BTN_7")
		self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_7)
		# PRTab BTN 8
		self.PRTab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
		self.PRTab_BTN_8.setAutoDefault(False)
		self.PRTab_BTN_8.setDefault(True)
		self.PRTab_BTN_8.setObjectName("PRTab_BTN_8")
		self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_8)
		# PRTab BTN 9
		self.PRTab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
		self.PRTab_BTN_9.setAutoDefault(False)
		self.PRTab_BTN_9.setDefault(True)
		self.PRTab_BTN_9.setObjectName("PRTab_BTN_9")
		self.PRTab_verticalLayout.addWidget(self.PRTab_BTN_9)
		# PRTab BTN 10
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
		self.DTab_Picture_LBL.setPixmap(QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
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
		self.DTab_TwistRate_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
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
		self.DTab_ThreadSize_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
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
		self.DTab_Manufacturer_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
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
		self.DTab_BarrelLen_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_7)
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
		self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(490, 80, 160, 361))
		self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
		self.DTab_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
		self.DTab_verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.DTab_verticalLayout.setObjectName("DTab_verticalLayout")
		self.DTab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
		self.DTab_Add_BTN.setDefault(True)
		self.DTab_Add_BTN.setObjectName("DTab_Add_BTN")
		self.DTab_verticalLayout.addWidget(self.DTab_Add_BTN)
		self.DTab_View_All_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
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

		self.formLayoutWidget_8 = QtWidgets.QWidget(self.STab_tab)
		self.formLayoutWidget_8.setGeometry(QtCore.QRect(10, 60, 471, 928))
		self.formLayoutWidget_8.setObjectName("formLayoutWidget_8")
		self.STab_gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_8)
		self.STab_gridLayout.setContentsMargins(0, 0, 0, 0)
		self.STab_gridLayout.setObjectName("STab_gridLayout")
		spacerItem6 = QtWidgets.QSpacerItem(20, 40,
											QtWidgets.QSizePolicy.Minimum,
											QtWidgets.QSizePolicy.Expanding)
		self.STab_gridLayout.addItem(spacerItem6, 34, 1, 1, 1)

		self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.STab_tab)
		self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(490, 80, 160, 361))
		self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
		self.STab_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
		self.STab_verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.STab_verticalLayout.setObjectName("STab_verticalLayout")
		# STab Combo Box
		self.STab_SILIENCER_Combo = QtWidgets.QComboBox(self.STab_tab)
		self.STab_SILIENCER_Combo.setGeometry(QtCore.QRect(10, 30, 471, 26))
		self.STab_SILIENCER_Combo.setObjectName("STab_SILIENCER_Combo")
		self.STab_SILIENCER_Combo.addItems(silencer_list)
		self.STab_SILIENCER_LBL = QtWidgets.QLabel(self.STab_tab)
		self.STab_SILIENCER_LBL.setGeometry(QtCore.QRect(20, 10, 451, 20))
		self.STab_SILIENCER_LBL.setAlignment(QtCore.Qt.AlignCenter)
		self.STab_SILIENCER_LBL.setObjectName("STab_SILIENCER_LBL")

		# STab ShowData BTN
		self.STab_ShowData_BTN = QtWidgets.QPushButton(self.STab_tab)
		self.STab_ShowData_BTN.setGeometry(QtCore.QRect(490, 30, 191, 31))
		self.STab_ShowData_BTN.setDefault(True)
		self.STab_ShowData_BTN.setObjectName("STab_ShowData_BTN")
		self.STab_ShowData_BTN.clicked.connect(self.displayData_STab)
		# Name
		self.STab_Name_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Name_LBL.setObjectName("STab_Name_LBL")
		self.STab_gridLayout.addWidget(self.STab_Name_LBL, 0, 0, 1, 1)
		self.STab_Name_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Name_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Name_TB.setObjectName("STab_Name_TB")
		self.STab_gridLayout.addWidget(self.STab_Name_TB, 0, 1, 1, 1)
		# Manufacturer
		self.STab_Manufacturer_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Manufacturer_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Manufacturer_TB.setObjectName("STab_Manufacturer_TB")
		self.STab_gridLayout.addWidget(self.STab_Manufacturer_TB, 1, 1, 1, 1)
		self.STab_Manufacturer_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Manufacturer_LBL.setObjectName("STab_Manufacturer_LBL")
		self.STab_gridLayout.addWidget(self.STab_Manufacturer_LBL, 1, 0, 1, 1)
		# Model
		self.STab_Model_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Model_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Model_TB.setObjectName("STab_Model_TB")
		self.STab_gridLayout.addWidget(self.STab_Model_TB, 2, 1, 1, 1)
		self.STab_Model_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Model_LBL.setObjectName("STab_Model_LBL")
		self.STab_gridLayout.addWidget(self.STab_Model_LBL, 2, 0, 1, 1)
		# SKU
		self.STab_SKU_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_SKU_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_SKU_TB.setObjectName("STab_SKU_TB")
		self.STab_gridLayout.addWidget(self.STab_SKU_TB, 3, 1, 1, 1)
		self.STab_SKU_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_SKU_LBL.setObjectName("STab_SKU_LBL")
		self.STab_gridLayout.addWidget(self.STab_SKU_LBL, 3, 0, 1, 1)
		# Caliber
		self.STab_Caliber_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Caliber_LBL.setObjectName("STab_Caliber_LBL")
		self.STab_gridLayout.addWidget(self.STab_Caliber_LBL, 4, 0, 1, 1)
		self.STab_Caliber_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Caliber_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Caliber_TB.setObjectName("STab_Caliber_TB")
		self.STab_gridLayout.addWidget(self.STab_Caliber_TB, 4, 1, 1, 1)
		# Overall Length
		self.STab_OLenght_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_OLenght_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_OLenght_TB.setObjectName("STab_Type_TB")
		self.STab_gridLayout.addWidget(self.STab_OLenght_TB, 5, 1, 1, 1)
		self.STab_OLenght_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_OLenght_LBL.setObjectName("STab_Type_LBL")
		self.STab_gridLayout.addWidget(self.STab_OLenght_LBL, 5, 0, 1, 1)
		# Weight
		self.STab_Weight_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Weight_LBL.setObjectName("STab_Weight_LBL")
		self.STab_gridLayout.addWidget(self.STab_Weight_LBL, 6, 0, 1, 1)
		self.STab_Weight_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Weight_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Weight_TB.setObjectName("STab_Weight_TB")
		self.STab_gridLayout.addWidget(self.STab_Weight_TB, 6, 1, 1, 1)
		# Diameter
		self.STab_Diameter_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Diameter_LBL.setObjectName("STab_TwistRate_LBL")
		self.STab_gridLayout.addWidget(self.STab_Diameter_LBL, 7, 0, 1, 1)
		self.STab_Diameter_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Diameter_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Diameter_TB.setObjectName("STab_TwistRate_TB")
		self.STab_gridLayout.addWidget(self.STab_Diameter_TB, 7, 1, 1, 1)
		# STab Notes
		self.STab_Notes_LBL = QtWidgets.QLabel(self.STab_tab)
		self.STab_Notes_LBL.setGeometry(QtCore.QRect(490, 430, 601, 20))
		self.STab_Notes_LBL.setAlignment(QtCore.Qt.AlignCenter)
		self.STab_Notes_LBL.setObjectName("STab_Notes_LBL")
		self.STab_Notes_TB = QtWidgets.QTextBrowser(self.STab_tab)
		self.STab_Notes_TB.setGeometry(QtCore.QRect(490, 450, 601, 501))
		self.STab_Notes_TB.setObjectName("STab_Notes_TB")
		# Stab Picture
		self.STab_Picture_LBL = QtWidgets.QLabel(self.STab_tab)
		self.STab_Picture_LBL.setGeometry(QtCore.QRect(660, 100, 431, 231))
		self.STab_Picture_LBL.setText("")
		self.STab_Picture_LBL.setPixmap(QtGui.QPixmap("../picts/Savage_110_Elite_Precision.png"))
		self.STab_Picture_LBL.setScaledContents(True)
		self.STab_Picture_LBL.setObjectName("STab_Picture_LBL")
		# Slot 12
		self.STab_Slot_12_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_12_LBL.setObjectName("STab_Slot_12_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_12_LBL, 8, 0, 1, 1)
		self.STab_Slot_12_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_12_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_12_TB.setObjectName("STab_Slot_12_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_12_TB, 8, 1, 1, 1)
		# Slot 13
		self.STab_Slot_13_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_13_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_13_TB.setObjectName("STab_Slot_13_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_13_TB, 9, 1, 1, 1)
		self.STab_Slot_13_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_13_LBL.setObjectName("STab_Slot_13_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_13_LBL, 9, 0, 1, 1)
		# Slot 14
		self.STab_Slot_14_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_14_LBL.setObjectName("STab_Slot_14_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_14_LBL, 10, 0, 1, 1)
		self.STab_Slot_14_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_14_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_14_TB.setObjectName("STab_Slot_14_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_14_TB, 10, 1, 1, 1)
		# Slot 15
		self.STab_Slot_15_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_15_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_15_TB.setObjectName("STab_Slot_15_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_15_TB, 11, 1, 1, 1)
		self.STab_Slot_15_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_15_LBL.setObjectName("STab_Slot_15_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_15_LBL, 11, 0, 1, 1)
		# Slot 16
		self.STab_Slot_16_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_16_LBL.setObjectName("STab_Slot_16_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_16_LBL, 12, 0, 1, 1)
		self.STab_Slot_16_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_16_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_16_TB.setObjectName("STab_Slot_16_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_16_TB, 12, 1, 1, 1)
		# Slot 17
		self.STab_Slot_17_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_17_LBL.setObjectName("STab_Slot_17_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_17_LBL, 13, 0, 1, 1)
		self.STab_Slot_17_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_17_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_17_TB.setObjectName("STab_Slot_17_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_17_TB, 13, 1, 1, 1)
		# Slot 18
		self.STab_Slot_18_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_18_LBL.setObjectName("STab_Slot_18_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_18_LBL, 14, 0, 1, 1)
		self.STab_Slot_18_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_18_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_18_TB.setObjectName("STab_Slot_18_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_18_TB, 14, 1, 1, 1)
		# Slot 19
		self.STab_Slot_19_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_19_LBL.setObjectName("STab_Slot_19_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_19_LBL, 15, 0, 1, 1)
		self.STab_Slot_19_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_19_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_19_TB.setObjectName("STab_Slot_19_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_19_TB, 15, 1, 1, 1)
		# Slot 20
		self.STab_Slot_20_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_20_LBL.setObjectName("STab_Slot_20_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_20_LBL, 16, 0, 1, 1)
		self.STab_Slot_20_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_20_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_20_TB.setObjectName("STab_Slot_20_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_20_TB, 16, 1, 1, 1)
		# Slot 21
		self.STab_Slot_21_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_21_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_21_TB.setObjectName("STab_Slot_21_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_21_TB, 17, 1, 1, 1)
		self.STab_Slot_21_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_21_LBL.setObjectName("STab_Slot_21_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_21_LBL, 17, 0, 1, 1)
		# Slot 22
		self.STab_Slot_22_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_22_LBL.setObjectName("STab_Slot_22_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_22_LBL, 18, 0, 1, 1)
		self.STab_Slot_22_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_22_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_22_TB.setObjectName("STab_Slot_22_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_22_TB, 18, 1, 1, 1)
		# Slot 23
		self.STab_Slot_23_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_23_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_23_TB.setObjectName("STab_Slot_23_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_23_TB, 19, 1, 1, 1)
		self.STab_Slot_23_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_23_LBL.setObjectName("STab_Slot_23_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_23_LBL, 19, 0, 1, 1)
		# Slot 24
		self.STab_Slot_24_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_24_LBL.setObjectName("STab_Slot_24_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_24_LBL, 20, 0, 1, 1)
		self.STab_Slot_24_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_24_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_24_TB.setObjectName("STab_Slot_24_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_24_TB, 20, 1, 1, 1)
		# Slot 25
		self.STab_Slot_25_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_25_LBL.setObjectName("STab_Slot_25_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_25_LBL, 21, 0, 1, 1)
		self.STab_Slot_25_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_25_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_25_TB.setObjectName("STab_Slot_25_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_25_TB, 21, 1, 1, 1)
		# Slot 26
		self.STab_Slot_26_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_26_LBL.setObjectName("STab_Slot_26_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_26_LBL, 22, 0, 1, 1)
		self.STab_Slot_26_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_26_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_26_TB.setObjectName("STab_Slot_26_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_26_TB, 22, 1, 1, 1)
		# Slot 27
		self.STab_Slot_27_LBL = QtWidgets.QLabel(self.formLayoutWidget_8)
		self.STab_Slot_27_LBL.setObjectName("STab_Slot_27_LBL")
		self.STab_gridLayout.addWidget(self.STab_Slot_27_LBL, 23, 0, 1, 1)
		self.STab_Slot_27_TB = QtWidgets.QTextBrowser(self.formLayoutWidget_8)
		self.STab_Slot_27_TB.setMaximumSize(QtCore.QSize(362, 26))
		self.STab_Slot_27_TB.setObjectName("STab_Slot_27_TB")
		self.STab_gridLayout.addWidget(self.STab_Slot_27_TB, 23, 1, 1, 1)

		# STab Show All BTN
		self.STab_View_All_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
		self.STab_View_All_BTN.setAutoDefault(False)
		self.STab_View_All_BTN.setDefault(True)
		self.STab_View_All_BTN.setObjectName("STab_View_All_BTN")
		self.STab_verticalLayout.addWidget(self.STab_View_All_BTN)
		self.STab_ShowSilencers_POP = ShowAllSilencers_PopUp()
		self.STab_View_All_BTN.clicked.connect(self.PopUp_ShowAllSilencers)
		# STab Add Silencer BTN
		self.STab_Add_BTN = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
		self.STab_Add_BTN.setDefault(True)
		self.STab_Add_BTN.setObjectName("STab_Add_BTN")
		self.STab_verticalLayout.addWidget(self.STab_Add_BTN)
		self.PopUp_Silencer_Add = QtWidgets.QMainWindow()
		# import class UI_PopUp_Add_Firearm from .\PopUp_Add_Firearm.py
		addSilencer = Add_Silencer.Ui_PopUp_Add_Silencer(silencer_df)
		addSilencer.setupUi(self.PopUp_Silencer_Add)
		self.STab_Add_BTN.clicked.connect(self.PopUp_Add_Silencer_BTN)

		# STab BTN 3
		self.STab_BTN_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
		self.STab_BTN_3.setDefault(True)
		self.STab_BTN_3.setObjectName("STab_BTN_3")
		self.STab_verticalLayout.addWidget(self.STab_BTN_3)
		# STab BTN 4
		self.STab_BTN_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
		self.STab_BTN_4.setDefault(True)
		self.STab_BTN_4.setObjectName("STab_BTN_4")
		self.STab_verticalLayout.addWidget(self.STab_BTN_4)
		# STab BTN 5
		self.STab_BTN_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
		self.STab_BTN_5.setDefault(True)
		self.STab_BTN_5.setObjectName("STab_BTN_5")
		self.STab_verticalLayout.addWidget(self.STab_BTN_5)
		# STab BTN 6
		self.STab_BTN_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
		self.STab_BTN_6.setDefault(True)
		self.STab_BTN_6.setObjectName("STab_BTN_6")
		self.STab_verticalLayout.addWidget(self.STab_BTN_6)
		# STab BTN 7
		self.STab_BTN_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
		self.STab_BTN_7.setDefault(True)
		self.STab_BTN_7.setObjectName("STab_BTN_7")
		self.STab_verticalLayout.addWidget(self.STab_BTN_7)
		# STab BTN 8
		self.STab_BTN_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
		self.STab_BTN_8.setAutoDefault(False)
		self.STab_BTN_8.setDefault(True)
		self.STab_BTN_8.setObjectName("STab_BTN_8")
		self.STab_verticalLayout.addWidget(self.STab_BTN_8)
		# STab BTN 9
		self.STab_BTN_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
		self.STab_BTN_9.setAutoDefault(False)
		self.STab_BTN_9.setDefault(True)
		self.STab_BTN_9.setObjectName("STab_BTN_9")
		self.STab_verticalLayout.addWidget(self.STab_BTN_9)
		# STab BTN 10
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
		self.MTab_ShotsOverTime_BTN = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.MTab_ShotsOverTime_BTN.setDefault(True)
		self.MTab_ShotsOverTime_BTN.setObjectName("MTab_ShotsOverTime_BTN")
		self.MTab_gridLayout.addWidget(self.MTab_ShotsOverTime_BTN, 1, 4, 1, 1)
		self.MTab_Plot_Shots_Powder_Charge = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.MTab_Plot_Shots_Powder_Charge.setDefault(True)
		self.MTab_Plot_Shots_Powder_Charge.setObjectName("MTab_Plot_Shots_Powder_Charge")
		self.MTab_gridLayout.addWidget(self.MTab_Plot_Shots_Powder_Charge, 0,3, 1, 1)
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
		self.MTab_Plot_Powder_Speed_Multi = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.MTab_Plot_Powder_Speed_Multi.setDefault(True)
		self.MTab_Plot_Powder_Speed_Multi.setObjectName("MTab_Plot_Powder_Speed_Multi")
		self.MTab_gridLayout.addWidget(self.MTab_Plot_Powder_Speed_Multi, 0, 0,1, 1)
		self.MTab_ShotsPerFirearm_BTN = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.MTab_ShotsPerFirearm_BTN.setDefault(True)
		self.MTab_ShotsPerFirearm_BTN.setObjectName("MTab_ShotsPerFirearm_BTN")
		self.MTab_gridLayout.addWidget(self.MTab_ShotsPerFirearm_BTN, 0, 4, 1,1)
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
		self.MTab_Plot_Powder_Speed_Single = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.MTab_Plot_Powder_Speed_Single.setDefault(True)
		self.MTab_Plot_Powder_Speed_Single.setObjectName("MTab_Plot_Powder_Speed_Single")
		self.MTab_gridLayout.addWidget(self.MTab_Plot_Powder_Speed_Single, 1,									   0, 1, 1)
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

		# pulldown label
		self.FTab_Firearm_LBL.setText(_translate("MainWindow", "Firearm"))
		# Label names
		self.FTab_Name_LBL.setText(_translate("MainWindow", "Name"))
		self.FTab_Manufacturer_LBL.setText(_translate("MainWindow", "Manufacturer"))
		self.FTab_Model_LBL.setText(_translate("MainWindow", "Model"))
		self.FTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
		self.FTab_Type_LBL.setText(_translate("MainWindow", "Type"))
		self.FTab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
		self.FTab_OLen_LBL.setText(_translate("MainWindow", "Overall Length"))
		self.FTab_BarrelLen_LBL.setText(_translate("MainWindow", "Barrel Length"))
		self.FTab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
		self.FTab_Action_LBL.setText(_translate("MainWindow", "Action Type"))
		self.FTab_TwistRate_LBL.setText(_translate("MainWindow", "Twist Rate"))
		self.FTab_ThreadSize_LBL.setText(_translate("MainWindow", "Thread Size"))
		self.FTab_Slot_16_LBL.setText(_translate("MainWindow", "Slot 16"))
		self.FTab_Slot_17_LBL.setText(_translate("MainWindow", "Slot 17"))
		self.FTab_Slot_18_LBL.setText(_translate("MainWindow", "Slot 18"))
		self.FTab_Slot_19_LBL.setText(_translate("MainWindow", "Slot 19"))
		self.FTab_Slot_20_LBL.setText(_translate("MainWindow", "Slot 20"))
		self.FTab_Slot_21_LBL.setText(_translate("MainWindow", "Slot 21"))
		self.FTab_Slot_22_LBL.setText(_translate("MainWindow", "Slot 22"))
		self.FTab_Slot_23_LBL.setText(_translate("MainWindow", "Slot 23"))
		self.FTab_Slot_24_LBL.setText(_translate("MainWindow", "Slot 24"))
		self.FTab_Slot_25_LBL.setText(_translate("MainWindow", "Slot 25"))
		self.FTab_Slot_26_LBL.setText(_translate("MainWindow", "Slot 26"))
		self.FTab_Slot_27_LBL.setText(_translate("MainWindow", "Slot 27"))

		# Button Names
		self.FTab_Add_BTN.setText(_translate("MainWindow", "Add Firearm"))
		self.FTab_View_All_BTN.setText(_translate("MainWindow", "View All Firearms"))
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
		# pull down lable
		self.BTab_Bullet_LBL.setText(_translate("MainWindow", "Bullet"))

		self.BTab_Name_LBL.setText(_translate("MainWindow", "Name"))
		self.BTab_Manufacturer_LBL.setText(_translate("MainWindow", "Manufacturer"))
		self.BTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
		self.BTab_Size_Inch_LBL.setText(_translate("MainWindow", "Size_Inch"))
		self.BTab_Size_mm_LBL.setText(_translate("MainWindow", "Size_mm"))
		self.BTab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
		self.BTab_Type_LBL.setText(_translate("MainWindow", "Type"))
		self.BTab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
		self.BTab_BBase_LBL.setText(_translate("MainWindow", "Bullet Base"))
		self.BTab_BC_LBL.setText(_translate("MainWindow", "BC"))
		self.BTab_Length_LBL.setText(_translate("MainWindow", "Length"))
		self.BTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
		self.BTab_Model_LBL.setText(_translate("MainWindow", "Model"))
		self.BTab_Slot_16_LBL.setText(_translate("MainWindow", "Slot 16"))
		self.BTab_Slot_17_LBL.setText(_translate("MainWindow", "Slot 17"))
		self.BTab_Slot_18_LBL.setText(_translate("MainWindow", "Slot 18"))
		self.BTab_Slot_19_LBL.setText(_translate("MainWindow", "Slot 19"))
		self.BTab_Slot_20_LBL.setText(_translate("MainWindow", "Slot 20"))
		self.BTab_Slot_21_LBL.setText(_translate("MainWindow", "Slot 21"))
		self.BTab_Slot_22_LBL.setText(_translate("MainWindow", "Slot 22"))
		self.BTab_Slot_23_LBL.setText(_translate("MainWindow", "Slot 23"))
		self.BTab_Slot_24_LBL.setText(_translate("MainWindow", "Slot 24"))
		self.BTab_Slot_25_LBL.setText(_translate("MainWindow", "Slot 25"))
		self.BTab_Slot_26_LBL.setText(_translate("MainWindow", "Slot 26"))
		self.BTab_Slot_27_LBL.setText(_translate("MainWindow", "Slot 27"))

		# buttons
		self.BTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
		self.BTab_Add_BTN.setText(_translate("MainWindow", "Add Bullet"))
		self.BTab_View_All_BTN.setText(_translate("MainWindow", "View All Bullets"))
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

		self.PTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
		
		self.PTab_Name_LBL.setText(_translate("MainWindow", "Name"))
		self.PTab_Manufacturer_LBL.setText(_translate("MainWindow", "Manufacturer"))
		self.PTab_Model_LBL.setText(_translate("MainWindow", "Model"))
		self.PTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
		self.PTab_BurnRate_LBL.setText(_translate("MainWindow", "Relative Burn Rate"))
		self.PTab_WeaponUse_LBL.setText(_translate("MainWindow", "Weapon Use"))
		self.PTab_Density_LBL.setText(_translate("MainWindow", "Density per lb"))
		self.PTab_BulkDensity_LBL.setText(_translate("MainWindow", "Bulk Density"))
		self.PTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
		self.PTab_Powder_LBL.setText(_translate("MainWindow", "Powder"))
		self.PTab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
		self.PTab_Slot_13_LBL.setText(_translate("MainWindow", "Slot 13"))
		self.PTab_Slot_14_LBL.setText(_translate("MainWindow", "Slot 14"))
		self.PTab_Slot_15_LBL.setText(_translate("MainWindow", "Slot 15"))
		self.PTab_Slot_16_LBL.setText(_translate("MainWindow", "Slot 16"))
		self.PTab_Slot_17_LBL.setText(_translate("MainWindow", "Slot 17"))
		self.PTab_Slot_18_LBL.setText(_translate("MainWindow", "Slot 18"))
		self.PTab_Slot_19_LBL.setText(_translate("MainWindow", "Slot 19"))
		self.PTab_Slot_20_LBL.setText(_translate("MainWindow", "Slot 20"))
		self.PTab_Slot_21_LBL.setText(_translate("MainWindow", "Slot 21"))
		self.PTab_Slot_22_LBL.setText(_translate("MainWindow", "Slot 22"))
		self.PTab_Slot_23_LBL.setText(_translate("MainWindow", "Slot 23"))
		self.PTab_Slot_24_LBL.setText(_translate("MainWindow", "Slot 24"))
		self.PTab_Slot_25_LBL.setText(_translate("MainWindow", "Slot 25"))
		self.PTab_Slot_26_LBL.setText(_translate("MainWindow", "Slot 26"))
		self.PTab_Slot_27_LBL.setText(_translate("MainWindow", "Slot 27"))

		self.PTab_Add_BTN.setText(_translate("MainWindow", "Add Powder"))
		self.PTab_View_All_BTN.setText(_translate("MainWindow", "View All Powders"))
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

		self.CTab_Name_LBL.setText(_translate("MainWindow", "Name"))
		self.CTab_Manufacturer_LBL.setText(_translate("MainWindow", "Manufacturer"))
		self.CTab_Model_LBL.setText(_translate("MainWindow", "Model"))
		self.CTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
		self.CTab_Finish_LBL.setText(_translate("MainWindow", "Finish"))
		self.CTab_PrimerSize_LBL.setText(_translate("MainWindow", "Primer Size"))
		self.CTab_Type_LBL.setText(_translate("MainWindow", "Type"))
		self.CTab_Slot_10_LBL.setText(_translate("MainWindow", "Slot 10"))
		self.CTab_Slot_11_LBL.setText(_translate("MainWindow", "Slot 11"))
		self.CTab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
		self.CTab_Slot_13_LBL.setText(_translate("MainWindow", "Slot 13"))
		self.CTab_Slot_14_LBL.setText(_translate("MainWindow", "Slot 14"))
		self.CTab_Slot_15_LBL.setText(_translate("MainWindow", "Slot 15"))
		self.CTab_Slot_16_LBL.setText(_translate("MainWindow", "Slot 16"))
		self.CTab_Slot_17_LBL.setText(_translate("MainWindow", "Slot 17"))
		self.CTab_Slot_18_LBL.setText(_translate("MainWindow", "Slot 18"))
		self.CTab_Slot_19_LBL.setText(_translate("MainWindow", "Slot 19"))
		self.CTab_Slot_20_LBL.setText(_translate("MainWindow", "Slot 20"))
		self.CTab_Slot_21_LBL.setText(_translate("MainWindow", "Slot 21"))
		self.CTab_Slot_22_LBL.setText(_translate("MainWindow", "Slot 22"))
		self.CTab_Slot_23_LBL.setText(_translate("MainWindow", "Slot 23"))
		self.CTab_Slot_24_LBL.setText(_translate("MainWindow", "Slot 24"))
		self.CTab_Slot_25_LBL.setText(_translate("MainWindow", "Slot 25"))
		self.CTab_Slot_26_LBL.setText(_translate("MainWindow", "Slot 26"))
		self.CTab_Slot_27_LBL.setText(_translate("MainWindow", "Slot 27"))
		self.CTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))

		self.CTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
		self.CTab_Add_BTN.setText(_translate("MainWindow", "Add Case Data"))
		self.CTab_View_All_BTN.setText(_translate("MainWindow", "View All Cases"))
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


		# Primer Tab
		self.PRTab_Name_LBL.setText(_translate("MainWindow", "Name"))
		self.PRTab_Manufacturer_LBL.setText(_translate("MainWindow", "Manufacturer"))
		self.PRTab_Model_LBL.setText(_translate("MainWindow", "Model"))
		self.PRTab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
		self.PRTab_Size_LBL.setText(_translate("MainWindow", "Size"))
		self.PRTab_Type_LBL.setText(_translate("MainWindow", "Type"))
		self.PRTab_Slot_10_LBL.setText(_translate("MainWindow", "Slot_10"))
		self.PRTab_Slot_11_LBL.setText(_translate("MainWindow", "Slot 11"))
		self.PRTab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
		self.PRTab_Slot_13_LBL.setText(_translate("MainWindow", "Slot 13"))
		self.PRTab_Slot_14_LBL.setText(_translate("MainWindow", "Slot 14"))
		self.PRTab_Slot_15_LBL.setText(_translate("MainWindow", "Slot 15"))
		self.PRTab_Slot_16_LBL.setText(_translate("MainWindow", "Slot 16"))
		self.PRTab_Slot_17_LBL.setText(_translate("MainWindow", "Slot 17"))
		self.PRTab_Slot_18_LBL.setText(_translate("MainWindow", "Slot 18"))
		self.PRTab_Slot_19_LBL.setText(_translate("MainWindow", "Slot 19"))
		self.PRTab_Slot_20_LBL.setText(_translate("MainWindow", "Slot 20"))
		self.PRTab_Slot_21_LBL.setText(_translate("MainWindow", "Slot 21"))
		self.PRTab_Slot_22_LBL.setText(_translate("MainWindow", "Slot 22"))
		self.PRTab_Slot_23_LBL.setText(_translate("MainWindow", "Slot 23"))
		self.PRTab_Slot_24_LBL.setText(_translate("MainWindow", "Slot 24"))
		self.PRTab_Slot_25_LBL.setText(_translate("MainWindow", "Slot 25"))
		self.PRTab_Slot_26_LBL.setText(_translate("MainWindow", "Slot 26"))
		self.PRTab_Slot_27_LBL.setText(_translate("MainWindow", "Slot 27"))
		self.PRTab_Notes_LBL.setText(_translate("MainWindow", "Notes"))

		self.PRTab_Primer_LBL.setText(_translate("MainWindow", "Primer"))

		self.PRTab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
		self.PRTab_Add_BTN.setText(_translate("MainWindow", "Add Primer"))
		self.PRTab_View_All_BTN.setText(_translate("MainWindow", "View All Primers"))
		self.PRTab_BTN_3.setText(_translate("MainWindow", "Button 3"))
		self.PRTab_BTN_4.setText(_translate("MainWindow", "Button 4"))
		self.PRTab_BTN_5.setText(_translate("MainWindow", "Button 5"))
		self.PRTab_BTN_6.setText(_translate("MainWindow", "Button 6"))
		self.PRTab_BTN_7.setText(_translate("MainWindow", "Button 7"))
		self.PRTab_BTN_8.setText(_translate("MainWindow", "Button 8"))
		self.PRTab_BTN_9.setText(_translate("MainWindow", "Button 9"))
		self.PRTab_BTN_10.setText(_translate("MainWindow", "Button 10"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.PRTab_tab), _translate(
			"MainWindow", "Primers"))

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
		# STab
		self.STab_SILIENCER_LBL.setText(_translate("MainWindow", "Silencer"))

		self.STab_Name_LBL.setText(_translate("MainWindow", "Name"))
		self.STab_Manufacturer_LBL.setText(_translate("MainWindow", "Manufacturer"))
		self.STab_Model_LBL.setText(_translate("MainWindow", "Model"))
		self.STab_SKU_LBL.setText(_translate("MainWindow", "SKU"))
		self.STab_Caliber_LBL.setText(_translate("MainWindow", "Caliber"))
		self.STab_OLenght_LBL.setText(_translate("MainWindow", "Overall Length"))
		self.STab_Weight_LBL.setText(_translate("MainWindow", "Weight"))
		self.STab_Diameter_LBL.setText(_translate("MainWindow", "Diameter"))
		self.STab_Slot_12_LBL.setText(_translate("MainWindow", "Slot 12"))
		self.STab_Slot_13_LBL.setText(_translate("MainWindow", "Slot 13"))
		self.STab_Slot_14_LBL.setText(_translate("MainWindow", "Slot 14"))
		self.STab_Slot_15_LBL.setText(_translate("MainWindow", "Slot 15"))
		self.STab_Slot_16_LBL.setText(_translate("MainWindow", "Slot 16"))
		self.STab_Slot_17_LBL.setText(_translate("MainWindow", "Slot 17"))
		self.STab_Slot_18_LBL.setText(_translate("MainWindow", "Slot 18"))
		self.STab_Slot_19_LBL.setText(_translate("MainWindow", "Slot 19"))
		self.STab_Slot_20_LBL.setText(_translate("MainWindow", "Slot 20"))
		self.STab_Slot_21_LBL.setText(_translate("MainWindow", "Slot 21"))
		self.STab_Slot_22_LBL.setText(_translate("MainWindow", "Slot 22"))
		self.STab_Slot_23_LBL.setText(_translate("MainWindow", "Slot 23"))
		self.STab_Slot_24_LBL.setText(_translate("MainWindow", "Slot 24"))
		self.STab_Slot_25_LBL.setText(_translate("MainWindow", "Slot 25"))
		self.STab_Slot_26_LBL.setText(_translate("MainWindow", "Slot 26"))
		self.STab_Slot_27_LBL.setText(_translate("MainWindow", "Slot 27"))
		self.STab_Notes_LBL.setText(_translate("MainWindow", "Notes"))
		# BTNs
		self.STab_ShowData_BTN.setText(_translate("MainWindow", "Show Data"))
		self.STab_Add_BTN.setText(_translate("MainWindow", "Add Silencer"))
		self.STab_View_All_BTN.setText(_translate("MainWindow", "View All Silencers"))
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

		# MTab
		self.MTab_ShotsOverTime_BTN.setText(_translate("MainWindow", "Shots Over Time"))
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
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
