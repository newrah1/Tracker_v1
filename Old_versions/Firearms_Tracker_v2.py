# Created by davenew at 1/31/22
"""
Enter a description here
"""

import mysql.connector
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk

from tkinter import (Button,
					 Frame,
					 mainloop,
					 RIGHT,
					 LEFT,
					 Tk,
					 ttk,
					 LEFT)


class Cartridge_Tab():

class App:
	def __init__(self, master):
		self.conn = mysql.connector.connect(host="localhost",
											user='root',
											password='marsptbn',
											database='Configuration_V1',
											auth_plugin='mysql_native_password')
		master.title('DH Tools')
		master.geometry('1530x700')  # Set Window Size

		style = ttk.Style()
		current_theme = style.theme_use()
		style.theme_settings(current_theme,
							 {"TNotebook.Tab": {"configure": {"padding": [20,
							 5]}}})  # add padding to the tabs

		nb = ttk.Notebook(master, padding=8)
		nb.grid(row=1, column=1, columnspan=50, rowspan=50, sticky='NESW')

		# -----Frames---------------------------------------------------------
		MainTab = ttk.Frame(nb)
		PowderTab = ttk.Frame(nb)
		FirearmsTab = ttk.Frame(nb)
		BulletTab = ttk.Frame(nb)
		CartridgeTab = ttk.Frame(nb)

		# -----Tabs------------------------------------------------------------
		nb.add(MainTab, text="Main Menu")
		nb.add(PowderTab, text='Powders')
		nb.add(FirearmsTab, text="Firearms")
		nb.add(BulletTab, text='Bullets')
		nb.add(CartridgeTab, text='Cartridge')

		self.MainTab_Quit = Button(MainTab, text="Quit")
		self.MainTab_Quit.grid(row=1, column=1)

		self.MainTab_Quit.bind("<Button-1>", self.click_quit)

		# Cartridge Tab
		self.PVS_Button = Button(CartridgeTab, text="Powder vs Speed")
		self.PVS_Button.grid(row=1, column=0)
		query = self.plot_PowderVsFPS
		self.PVS_Button.bind("<Button-1>", query)

		self.CartridgeTab_Quit = Button(CartridgeTab, text="Quit")
		self.CartridgeTab_Quit.grid(row=10, column=10, sticky='se')

		self.CartridgeTab_Quit.bind("<Button-1>", self.click_quit)

		#self.Quit_Button = Button(MainTab, text="Quit")
		#self.Quit_Button.grid(row=1, column=1)

	def click_quit(self, event):
		sys.exit()

	def plot_PowderVsFPS(self, event):
		dataframe = self.data_query(
			"SELECT * FROM Configuration_v1.Configuration inner join "
			"Configuration_v1.Data on Configuration_v1.Configuration.ID= "
			"Configuration_v1.Data.Configuration_ID",
			"Rows of Data = ",
			"None")

		# filter the dataframe
		df = dataframe[
			(dataframe.Firearm_Name == Firearm) &
			(dataframe.Bullet_Name == Bullet) &
			(dataframe.Powder_Name == Powder)
			]

		# performs the linear regression and plots the fit (line) with a
		# 95% confidence interval (shades, default value)
		sns.regplot(x="Powder_Weight", y="AVG", data=df, fit_reg=True)

		plt.xlabel('Powder Weight')
		plt.ylabel('Speed (FPS)')
		plt.title("{}\n"
				  "{}\n"
				  "{}".format(Firearm,Bullet,Powder))

		plt.plot(df.Powder_Weight, df.AVG)

		plt.show()

	def data_query(self, query, text, return_value):
		# use the query to get the data from the DB
		df = pd.read_sql(query, self.conn)

		# Columns containing the speed of each shot in FPS
		cols = 	['Shot_1',
				   'Shot_2',
				   'Shot_3',
				   'Shot_4',
				   'Shot_5',
				   'Shot_6',
				   'Shot_7',
				   'Shot_8',
				   'Shot_9',
				   'Shot_10']

		# Calculate the Average speed of each shot in the row
		df['AVG'] = df[cols].mean(axis=1).astype(int)

		# Calculate the Standard deviation of each shot in the row
		df['SD'] = df[cols].std(axis=1)

		# Calculate the Extreme Spread of each shot in the row
		df['ES'] = (df[cols].max(axis=1)-df[cols].min(axis=1))

		# Calculate the number of shots in row
		df['Count'] = (10 - (df[cols].isnull().sum(axis=1)))

		if return_value == 'None':
			pass
		elif return_value == 'True':
			# print the query
			print("Query = ", query)

			# print the number of rows
			rows = df.shape[0]
			print('{}{}\n'.format(text, rows))

			# print example data
			print(df.to_string(max_rows=5))

		return df


root = Tk()
app = App(root)
root.mainloop()