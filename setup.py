# This is a file that should be run every time there is a change in the database schemas or when one wants to clear their copy of the database

import sqlite3

with sqlite3.connect("database.db") as connection: # Get a connection to the database file
	cursor = connection.cursor() # Get a cursor so we can modify the database

	# For every table we need to drop it if it exists and then create it.

	cursor.execute('DROP TABLE IF EXISTS item_types')
	cursor.execute('''
		CREATE TABLE item_types
		(
			type_id INT NOT NULL,
			type_name TEXT NOT NULL,
			PRIMARY KEY (type_ID)
		)
		CREATE TABLE item
		(
  			item_id INT NOT NULL,
  			item_name TEXT NOT NULL,
  			color TEXT NOT NULL,
  			type_id INT NOT NULL,
  			PRIMARY KEY (item_id),
  			FOREIGN KEY (type_id) REFERENCES item_types(type_ID)
		)

	''')

	# Then fill in our entries

	cursor.execute('INSERT INTO item_types (type_id, type_name) VALUES (0, "potions")')
	cursor.execute('INSERT INTO item_types (type_id, type_name) VALUES (1, "balls")')
	cursor.execute('INSERT INTO item_types (type_id, type_name) VALUES (2, "special")')
	cursor.execute('INSERT INTO item (item_id, item_name, color, type_id) VALUES (0, "regular_ball", "red", 1)
	connection.commit()
