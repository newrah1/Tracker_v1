# Created by davenew at 1/21/22
"""
Enter a description here
"""

import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk

from tkinter import (mainloop,
					 ttk)


class Test:

	def __init__(self):
		self.conn = mysql.connector.connect(host="localhost",
											user='root',
											password='marsptbn',
											database='Configuration_V1',
											auth_plugin='mysql_native_password')


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

	def plot_PowderVsFPS(self, Firearm, Bullet, Powder):
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

	def plot_Powder_Burn_Rate(self, dataframe, Firearm, Bullet, Powder,
							  Powder_Weight, CBTO, COL):
		pass

	def plot_PowderVsMOA(self, dataframe, Firearm, Bullet, Powder,
						 Powder_Weight, CBTO, COL):
		pass

	def plot_RoundsVsTime(self, dataframe, Firearm, Bullet, Powder,
							  Powder_Weight, CBTO, COL):
		pass

	def plot_RoundsPerFirearm(self):
		dataframe = self.data_query(
			"SELECT * FROM Configuration_v1.Configuration inner join "
			"Configuration_v1.Data on Configuration_v1.Configuration.ID= "
			"Configuration_v1.Data.Configuration_ID",
			"Rows of Data = ",
			"None")

		df = dataframe.groupby(['Firearm_Name']).count()["Count"]

		df = df.reset_index()
		ax = sns.barplot(x='Firearm_Name', y='Count', data=df)

		plt.ylabel('Rounds Fired')
		plt.xlabel('Firearm')
		plt.title("{}".format("Rounds Per Firearm"))

		# Show Values on Seaborn Barplot
		for i in ax.containers:
			ax.bar_label(i, )

		plt.show()

	def plot_ES(self, dataframe, Firearm, Bullet, Powder, Powder_Weight,
				CBTO, COL):
		pass

	def plot_SD(self, dataframe, Firearm, Bullet, Powder, Powder_Weight,
				CBTO, COL):
		pass

	def multiplot_data (self, Firearm, Bullet, Powder ):
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
		fig, axs = plt.subplots(ncols=3)

		# Speed Plot
		sns.regplot(x="Powder_Weight", y="AVG", data=df, fit_reg=True,
					ax=axs[0]).set_title("Powder Weight vs Speed")
		sns.lineplot(x=df.Powder_Weight, y=df.AVG, ax=axs[0])

		# SD Plot
		sns.regplot(x="Powder_Weight", y="SD", data=df, fit_reg=True,
					ax=axs[1]).set_title("Powder Weight vs SD")
		sns.lineplot(x=df.Powder_Weight, y=df.SD, ax=axs[1])

		# ES Plot
		sns.regplot(x="Powder_Weight", y="ES", data=df,	fit_reg=True,
					ax=axs[2]).set_title("Powder Weight vs Extreme Spread")
		sns.lineplot(x=df.Powder_Weight, y=df.ES, ax=axs[2])

		plt.tight_layout()
		plt.show()

	def run(self):

		configurations_df = self.config_query(
			"SELECT * FROM Configuration_V1.Configuration",
			"Number of Configurations = ",
			"None")

		powders_df = self.config_query(
			"SELECT * FROM Configuration_V1.Powder ",
			"Number of Powders = ",
			"None")

		bullets_df = self.config_query(
			"SELECT * FROM Configuration_V1.Bullet ",
			"Number of Bullets = ",
			"None")

		#print(config_data.to_string())

		self.plot_PowderVsFPS("300 BLK PSA 7.5 upper",
							  ".308 Hornady BTHP 178gn",
							  "Hodgdon LilGun")

		self.multiplot_data("6.5 Creedmore Savage 110 Elite Precision",
						    ".264 Barnes Match Burners Match BT 140gn",
						    "Hodgdon H4350")

		self.plot_RoundsPerFirearm()

Test.run()