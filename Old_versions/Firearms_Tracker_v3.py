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
					 BOTH,
					 Canvas,
					 Frame,
					 mainloop,
					 RIGHT,
					 LEFT,
					 Listbox,
					 Tk,
					 ttk,
					 LEFT)

LARGE_FONT = ("Verdana", 12)


class FirearmsTracker(tk.Tk):
	"""
	tkinter example app with OOP
	"""

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.winfo_geometry()
		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(1, weight=1)
		container.grid_columnconfigure(1, weight=3)


		self.frames = {}

		for frame_class in (StartPage,
							Firearms_Page,
							Data_Page,
							Powder_Page,
							Primers_Page):
			frame = frame_class(container, self)

			self.frames[frame_class] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		"""
		Put specific frame on top
		"""

		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):
	"""
	Starting frame for app
	"""

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, bg='red')
		label = tk.Label(self, text="Start Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)


		button_Firearms = tk.Button(self, text='Firearms',
								 command=lambda: controller.show_frame(
									 Firearms_Page))
		button_Firearms.pack()

		button_Data = tk.Button(self,
								text='Shot Data',
								command=lambda: controller.show_frame(
										Data_Page))
		button_Data.pack()

		button_Powder = tk.Button(self, text='Powder',
								 command=lambda: controller.show_frame(
									 Powder_Page))
		button_Powder.pack()

		button_Powder = tk.Button(self, text='Primers',
								  command=lambda: controller.show_frame(
									  Primers_Page))
		button_Powder.pack()


		tk.Frame.__init__(self, parent, bg='light blue')
		label = tk.Label(self, text="Firearms", font=LARGE_FONT)
		label.pack(pady=1, padx=1)

		button_home = tk.Button(self, text='Back to Home',
								command=lambda: controller.show_frame(
									StartPage))
		button_home.pack()

		configurations_df = self.config_query(
			"SELECT * FROM Configuration_V1.Configuration",
			"Number of Configurations = ",
			"None")

		firearms_unique = configurations_df['Firearm_Name'].unique()
		firearms_list = firearms_unique.tolist()

		Combo = ttk.Combobox(self, values=firearms_list)
		Combo.set("Pick an Option")
		Combo.pack(padx=10, pady=10, fill="both", expand=True)


		#self.PVS_Button = Button(self, text="Powder vs Speed",
		#						 command=self.PVS_click())
		#self.PVS_Button.pack(pady=2, padx=2)
		#self.PVS_Button.focus_force()

	def PVS_click(self):
		query = self.plot_PowderVsFPS("300 BLK PSA 7.5 upper",
							  ".308 Hornady BTHP 178gn",
							  "Hodgdon LilGun")

		self.PVS_Button.bind("<Button-1>", query)

	def data_query(self, query, text, return_value):
		# use the query to get the data from the DB
		df = pd.read_sql(query, self.conn)

		# Columns containing the speed of each shot in FPS
		cols = ['Shot_1',
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
		df['ES'] = (df[cols].max(axis=1) - df[cols].min(axis=1))

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
				  "{}".format(Firearm, Bullet, Powder))

		plot = plt.plot(df.Powder_Weight, df.AVG)

		plt.show()
		return plot

class Data_Page(tk.Frame):
	"""
	First page of program
	"""

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, bg='light green')
		label = tk.Label(self, text="Shot Data", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button_home = tk.Button(self, text='Back to Home',
								command=lambda: controller.show_frame(
									StartPage))
		button_home.pack()

class Powder_Page(tk.Frame):
	"""
	First page of program
	"""

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, bg='light green')
		label = tk.Label(self, text="Powder", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button_home = tk.Button(self, text='Back to Home',
								command=lambda: controller.show_frame(
									StartPage))
		button_home.pack()

class Primers_Page(tk.Frame):
	"""
	First page of program
	"""

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, bg='light green')
		label = tk.Label(self, text="Primers", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button_home = tk.Button(self, text='Back to Home',
								command=lambda: controller.show_frame(
									StartPage))
		button_home.pack()




app = FirearmsTracker()
app.mainloop()
