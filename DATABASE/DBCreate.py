import sqlite3

conn = sqlite3.connect('TrackerDB.db')
print("Opened database successfully")


def bullet_table():
	try:
		conn.execute('''CREATE TABLE Bullet
						 (Bullet_id 	INT PRIMARY KEY NOT NULL,
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
		print("Failed to build sqlite table  -", error)

def case_table():
	try:
		conn.execute('''CREATE TABLE Case_tbl
				 (Case_id 	INT PRIMARY KEY     NOT NULL,
				 Name           TEXT,
				 Manufacturer   TEXT,
				 Caliber		TEXT,
				 Finish			TEXT,
				 Primer_Size	TEXT
					);''')
		print("Table created successfully")
	except sqlite3.Error as error:
		print("Failed to build sqlite table  -", error)

def config_table():
	try:
		conn.execute('''CREATE TABLE Config
		(Config_id	INT	PRIMARY KEY	NOT NULL,
				  Config_Name			TEXT,
				  Firearm_Name			TEXT,
				  Bullet_Name			TEXT,
				  Case_Name				TEXT,
				  Powder_Name			TEXT,
				  Primer_Name			TEXT,
				  Powder_Weight			TEXT,
				  CBTO					DOUBLE,
				  COL					DOUBLE,
				  Notes					LONGTEXT,
				  Picture				LONGTEXT
				  );''')
		print("Table created successfully")
	except sqlite3.Error as error:
		print("Failed to build sqlite table  -", error)

def data_table():
	try:
		conn.execute('''CREATE TABLE Data
		(Data_id	INT	PRIMARY KEY	NOT NULL,
				  Group_MOA				DOUBLE,
				  Shot_1				DOUBLE,
				  Shot_2				DOUBLE,
				  Shot_3				DOUBLE,
				  Shot_4				DOUBLE,
				  Shot_5				DOUBLE,
				  Shot_6				DOUBLE,
				  Shot_7				DOUBLE,
				  Shot_8				DOUBLE,
				  Shot_9				DOUBLE,
				  Shot_10				DOUBLE,
				  Data_Date				DATETIME,
				  Config_ID				INT,
				  Notes					LONGTEXT,
				  Picture				LONGTEXT
				  );''')
		print("Table created successfully")
	except sqlite3.Error as error:
		print("Failed to build sqlite table  -", error)

def firearm_table():
	try:
		conn.execute('''CREATE TABLE Firearm
		(Firearm_id	INT	PRIMARY KEY	NOT NULL,
				  Firearm_Type			TEXT,
				  Name					TEXT,
				  Manufacturer			TEXT,
				  Model					TEXT,
				  SKU					TEXT,
				  Action_Type			TEXT,
				  Caliber				TEXT,
				  Overall_Length_Inch	DOUBLE,
				  Weight_Lb				DOUBLE,
				  Twist_Rate			TEXT,
				  Barrel_Len_Inch		DOUBLE,
				  Notes					LONGTEXT,
				  Picture				LONGTEXT
				  );''')
		print("Table created successfully")
	except sqlite3.Error as error:
		print("Failed to build sqlite table  -", error)

def powder_table():
	try:
		conn.execute('''CREATE TABLE Powder
		(Powder_id	INT	PRIMARY KEY	NOT NULL,
				  Name					TEXT,
				  Manufacturer			TEXT,
				  SKU					TEXT,
				  Relative_Burn_Rate	INT,
				  Weapon_Use			TEXT,
				  Density_lb			DOUBLE,
				  Bulk_Density			DOUBLE,
				  Notes					LONGTEXT,
				  Picture				LONGTEXT
				  );''')
		print("Table created successfully")
	except sqlite3.Error as error:
		print("Failed to build sqlite table  -", error)

def primer_table():
	try:
		conn.execute('''CREATE TABLE Primer
		(Primer_id	INT	PRIMARY KEY	NOT NULL,
				  Name					TEXT,
				  Manufacturer			TEXT,
				  Model					TEXT,
				  SKU					TEXT,
				  Size					TEXT,
				  Type					TEXT,
				  Notes					LONGTEXT,
				  Picture				LONGTEXT
				  );''')
		print("Table created successfully")
	except sqlite3.Error as error:
		print("Failed to build sqlite table  -", error)

def silencer_table():
	try:
		conn.execute('''CREATE TABLE Silencer
		(Silencer_id	INT	PRIMARY KEY	NOT NULL,
				  Name					TEXT,
				  Manufacturer			TEXT,
				  Model					TEXT,
				  SKU					TEXT,
				  Caliber				TEXT,
				  Overall_Len_Inch		DOUBLE,
				  Weight_lb				DOUBLE,
				  Diameter_Inch			DOUBLE,				
				  Notes					LONGTEXT,
				  Picture				LONGTEXT
				  );''')
		print("Table created successfully")
	except sqlite3.Error as error:
		print("Failed to build sqlite table  -", error)

def verify():
	table_list = ['Bullet', 'Case_tbl', 'Config', 'Data', 'Firearm', 'Powder',
				  'Primer', 'Silencer']
	for name in table_list:
		select_table = ('{}{}').format('select * from ', name)
		print(select_table)
		cursor = conn.execute(select_table)
		colnames = cursor.description
		for row in colnames:
			print(row[0])


bullet_table()
case_table()
config_table()
data_table()
firearm_table()
powder_table()
primer_table()
silencer_table()
#verify()


