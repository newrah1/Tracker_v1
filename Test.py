import sqlite3
import pandas as pd

conn = sqlite3.connect('./Database/TrackerDB.db')
print("Opened database successfully")
firearm_db = pd.read_sql("SELECT * FROM Case_table",
									 conn)
print(firearm_db)
conn.close()
