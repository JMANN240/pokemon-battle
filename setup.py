# This is a file that should be run every time there is a change in the database schemas or when one wants to clear their copy of the database

import sqlite3

with sqlite3.connect("database.db") as connection: # Get a connection to the database file
	cursor = connection.cursor() # Get a cursor so we can modify the database

	# For every table we need to drop it if it exists and then create it.

	cursor.execute('DROP TABLE IF EXISTS item_types')
	cursor.execute('DROP TABLE IF EXISTS item')
	cursor.execute('DROP TABLE IF EXISTS player')
	cursor.execute('DROP TABLE IF EXISTS pokemon_types')

	cursor.execute('''
		
		CREATE TABLE item_types
		(
			type_id INT NOT NULL,
			type_name TEXT NOT NULL,
			PRIMARY KEY (type_ID)
		)
	''')

	cursor.execute('''
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
	
	cursor.execute('''
		CREATE TABLE player
		(
  			player_id INT NOT NULL,
  			player_name TEXT NOT NULL,
  			PRIMARY KEY (player_id)
		)
	''')

	cursor.execute('''
		CREATE TABLE pokemon_types
		(
  			p_type_id INT NOT NULL,
  			p_type_name TEXT NOT NULL,
  			PRIMARY KEY (p_type_id)
		)

	''')

	# Then fill in our entries

	cursor.execute('INSERT INTO item_types (type_id, type_name) VALUES (0, "potions")')
	cursor.execute('INSERT INTO item_types (type_id, type_name) VALUES (1, "balls")')
	cursor.execute('INSERT INTO item_types (type_id, type_name) VALUES (2, "special")')
	cursor.execute('INSERT INTO item (item_id, item_name, color, type_id) VALUES (0, "regular_ball", "red", 1)')
	cursor.execute('INSERT INTO player (player_id, player_name) VALUES (0, "bob")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (0, "bug")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (1, "dark")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (2, "dragon")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (3, "electric")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (4, "fairy")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (5, "fighting")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (6, "fire")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (7, "flying")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (8, "ghost")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (9, "grass")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (10, "ground")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (11, "ice")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (12, "normal")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (13, "poison")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (14, "psychic")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (15, "rock")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (16, "steel")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name) VALUES (17, "water")')
	connection.commit()
