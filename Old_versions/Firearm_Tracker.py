# Created by davenew at 12/20/21
"""
Enter a description here
"""

import sys, shutil, datetime, os
import pandas as pd
import tkinter as tk
from tkinter import (mainloop,
                    IntVar,
                    StringVar,
                    Button,
                    Entry,
                    Label,
                    Scale,
                    INSERT,
                    ttk,
                    scrolledtext,
                    messagebox,
                    filedialog as fd
                    )

import mysql.connector
from mysql.connector import Error

class SportsTracker:
	def __init__(self):
		self.conn = mysql.connector.connect(host="localhost",
											user='root',
											password='marsptbn',
											#database='Firearms_Tracker',
											database='Configuration_V1',
									        auth_plugin='mysql_native_password')

	def desktop(self):
		main = tk.Tk()
		main.title('DH Tools')
		main.geometry('1530x700')  # Set Window Size

		# give weight to the cells in the grid
		rows = 0
		while rows < 50:
			main.rowconfigure(rows, weight=1)
			main.columnconfigure(rows, weight=1)
			rows += 1

		# -----Defines and places the notebook widget-------------------------
		nb = ttk.Notebook(main, padding=8)
		nb.grid(row=1, column=1, columnspan=50, rowspan=50, sticky='NESW')

		style = ttk.Style()
		current_theme = style.theme_use()
		style.theme_settings(current_theme,
							 {"TNotebook.Tab": {"configure": {"padding": [20,
																		  5]}}})  # add padding to the tabs

		# -----Frames---------------------------------------------------------
		PowderTab = ttk.Frame(nb)
		FirearmsTab = ttk.Frame(nb)
		BulletTab = ttk.Frame(nb)
		CartridgeTab = ttk.Frame(nb)

		# -----Tabs------------------------------------------------------------
		nb.add(PowderTab, text='Powders')
		nb.add(FirearmsTab, text="Firearms")
		nb.add(BulletTab, text='Bullets')
		nb.add(CartridgeTab, text='Cartridge')

		Label(PowderTab, text="Powders").grid(row=0,
											  column=0,
											  sticky=tk.W)
		powders_df = self.powders()

		t1 = tk.Text(PowderTab, width=40, height=20)
		t1.grid(row=1, column=1, padx=5)
		t1.insert(tk.END, powders_df.Name)

		powder_query = "SELECT Name FROM Firearms_Tracker.Powder"
		t2 = tk.Text(PowderTab, width=40, height=20)
		t2.grid(row=1, column=2, padx=5)
		t2.insert(tk.END, self.query_db(powder_query, 'True'))

		my_conn = self.conn.cursor()
		####### end of connection ####
		my_conn.execute(powder_query)
		i=0
		for powder in my_conn:
			e = Entry(PowderTab, width=100, fg='blue')
			e.grid(row=i, column=4)
			e.insert(tk.END, powder)
			i = i + 1




		mainloop()

	def powders(self):
		query = "SELECT Name FROM Firearms_Tracker.Powder"
		powder_df = pd.read_sql(query, self.conn)
		rows = powder_df.shape[0]
		print('{}{}'.format("Number of Rows = ", rows))
		return powder_df

	def bullets (self):
		#query = "SELECT Name FROM Firearms_Tracker.Bullet"
		query = "SELECT * " \
				"FROM Configuration_v1.Configuration" \
				"inner join Configuration_v1.Data" \
				"on Configuration_v1.Configuration.ID= " \
				"Configuration_v1.Data.Configuration_ID"

		bullet_df = pd.read_sql(query, self.conn)
		rows = bullet_df.shape[0]
		print('{}{}'.format("Number of Rows = ", rows))
		return bullet_df

	def test_connection(self):
		try:
			conn = self.conn

			if conn.is_connected():
				print('Connected to MySQL database', "\n")

				# Creating a cursor object using the cursor() method
				cursor = conn.cursor()

				# Executing an MYSQL function using the execute() method
				cursor.execute("SELECT DATABASE()")

				# Fetch a single row using fetchone() method.
				data = cursor.fetchone()
				print("Connection established to: ", data)

				# Closing the connection
				conn.close()

		except Error as e:
			print(e)

		finally:
			if conn is not None and conn.is_connected():
				c = conn.cursor()
				conn.close()
				return c, conn

	def query_db(self, query, return_value):
		print('Query        = ', query)

		db = mysql.connector.connect(host="localhost",
									 user='root',
									 password='marsptbn',
									 #database='Firearms_Tracker',
									 database='Configuration_V1',
									 auth_plugin='mysql_native_password')
		cursor = db.cursor()

		cursor.execute(query)
		if return_value == 'none':
			cursor.close()
			db.close()
			pass
		elif return_value == 'True':
			outfile = cursor.fetchall()
			cursor.close()
			db.close()
			return outfile
		outfile = cursor.fetchall()
		print(outfile)

	def run(self):
		# Test connection to the DB
		self.test_connection()

		self.query_db("SELECT * FROM Configuration_v1.Configuration", "True")

	# testing delete
	def unique_configurations(self, query, return_value):
		df = pd.read_sql(query, self.conn).drop_duplicates(subset=
														   ['Firearm_Name',
															'Bullet_Name',
															'Case_Name',
															'Powder_Name',
															'Primer_Name',
															'Powder_Weight',
															'CBTO']
														   )
		rows = df.shape[0]
		print('{}{}'.format("Number of Unique Configurations = ", rows))
		return df

if __name__ == "__main__":
	ST = SportsTracker()
	ST.run()
