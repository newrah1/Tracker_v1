import sqlite3

conn = sqlite3.connect('Database/TrackerDB.db')
print("Opened database successfully")


def bullet_table():
	try:
		conn.execute('''CREATE TABLE bullet
				 (bullet_id 	INT PRIMARY KEY     NOT NULL,
				 Name           TEXT,
				 Manufacturer   TEXT,
				 Size_Inch      TEXT,
				 Size_mm		TEXT,
				 Weight			INT,
				 Type			TEXT,
				 SKU			TEXT,
				 Caliber		TEXT,
				 Bullet_Base	TEXT,
				 BC				TEXT,
				 Length_Inch	TEXT,
				 Notes			LONGTEXT,
				 Picture		LONGTEXT
					);''')
		print("Table created successfully")
	except sqlite3.Error as error:
		print("Failed to read data from sqlite table  - ", error)

def case_table():
	try:
		conn.execute('''CREATE TABLE Case_table
				 (case_id 	INT PRIMARY KEY     NOT NULL,
				 Name           TEXT,
				 Manufacturer   TEXT,
				 Size_Inch      TEXT,
				 Size_mm		TEXT,
				 Weight			INT,
				 Type			TEXT,
				 SKU			TEXT,
				 Caliber		TEXT,
				 Bullet_Base	TEXT,
				 BC				TEXT,
				 Length_Inch	TEXT,
				 Notes			LONGTEXT,
				 Picture		LONGTEXT
					);''')
		print("Table created successfully")
	except sqlite3.Error as error:
		print("Failed to read data from sqlite table  - ", error)


# cursor = conn.execute('select * from bullet')
# print(cursor.description)

bullet_table()
case_table()

conn.close()
