# This is a file that should be run every time there is a change in the database schemas or when one wants to clear their copy of the database

import sqlite3

with sqlite3.connect("database.db") as connection: # Get a connection to the database file
	cursor = connection.cursor() # Get a cursor so we can modify the database

	# For every table we need to drop it if it exists and then create it.

	cursor.execute('DROP TABLE IF EXISTS blah')
	cursor.execute('''
		CREATE TABLE blah (
			col1 INTEGER PRIMARY KEY,
			col2 TEXT NOT NULL,
			col3 TEXT NOT NULL
		)
	''')

	# Then fill in our entries

	cursor.execute('INSERT INTO blah (col1, col2, col3) VALUES (1, "foo", "bar")')
	cursor.execute('INSERT INTO blah (col1, col2, col3) VALUES (2, "bat", "baz")')
	connection.commit()
