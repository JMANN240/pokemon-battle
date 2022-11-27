# This is a file that should be run every time there is a change in the database schemas or when one wants to clear their copy of the database

import sqlite3

with sqlite3.connect("database.db") as connection: # Get a connection to the database file
	cursor = connection.cursor() # Get a cursor so we can modify the database

	# For every table we need to drop it if it exists and then create it.

	cursor.execute('DROP TABLE IF EXISTS item_types')
	cursor.execute('DROP TABLE IF EXISTS item')
	cursor.execute('DROP TABLE IF EXISTS player')
	cursor.execute('DROP TABLE IF EXISTS pokemon_types')
	cursor.execute('DROP TABLE IF EXISTS player_item')
	cursor.execute('DROP TABLE IF EXISTS team')
	cursor.execute('DROP TABLE IF EXISTS pokemon')
	cursor.execute('DROP TABLE IF EXISTS pokemon_type')

	cursor.execute('''
		
		CREATE TABLE item_types
		(
			type_id INT NOT NULL,
			type_name TEXT NOT NULL,
			type_display_name TEXT NOT NULL,
			PRIMARY KEY (type_ID)
		)
	''')

	cursor.execute('''
		CREATE TABLE item
		(
  			item_id INT NOT NULL,
  			item_name TEXT NOT NULL,
			item_display_name TEXT NOT NULL,
  			color TEXT NOT NULL,
			times_used INT NOT NULL,
			description TEXT NOT NULL,
			icon TEXT NOT NULL,
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
			p_type_color TEXT NOT NULL,
  			PRIMARY KEY (p_type_id)
		)

	''')

	cursor.execute('''
		CREATE TABLE player_item
		(
  			quantity INT NOT NULL,
  			player_id INT NOT NULL,
  			item_id INT NOT NULL,
  			PRIMARY KEY (player_id, item_id),
  			FOREIGN KEY (player_id) REFERENCES player(player_id),
  			FOREIGN KEY (item_id) REFERENCES item(item_id)
		)
	''')

	cursor.execute('''
		CREATE TABLE team
		(
  			team_id INT NOT NULL,
  			team_name TEXT NOT NULL,
  			player_id INT NOT NULL,
			active_id INT NOT NULL,
  			PRIMARY KEY (team_id),
  			FOREIGN KEY (player_id) REFERENCES player(player_id)
			FOREIGN KEY(active_id) REFERENCES pokemon(pokemon_id)
		)
	''')
	
	cursor.execute('''
		CREATE TABLE pokemon
		(
  			pokemon_id INT NOT NULL,
  			p_name TEXT NOT NULL,
  			health INT NOT NULL,
  			hype INT NOT NULL,
			sprite_path TEXT NOT NULL,
			holding TEXT,
			attack INT NOT NULL,
			defense INT NOT NULL,
			speed INT NOT NULL,
			caught_date TEXT NOT NULL,
  			team_id INT,
  			PRIMARY KEY (pokemon_id),
  			FOREIGN KEY (team_id) REFERENCES team(team_id)
		)
	''')

	cursor.execute('''
		CREATE TABLE pokemon_type
		(
  			pokemon_id INT NOT NULL,
  			p_type_id INT NOT NULL,
  			PRIMARY KEY (pokemon_id, p_type_id),
  			FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
  			FOREIGN KEY (p_type_id) REFERENCES pokemon_types(p_type_id)
		)

	''')

	# Then fill in our entries

	cursor.execute('INSERT INTO item_types (type_id, type_name, type_display_name) VALUES (0, "potions", "Potion")')
	cursor.execute('INSERT INTO item_types (type_id, type_name, type_display_name) VALUES (1, "balls", "Ball")')
	cursor.execute('INSERT INTO item_types (type_id, type_name, type_display_name) VALUES (2, "special", "Special")')

	cursor.execute('INSERT INTO item (item_id, item_name, item_display_name, color, times_used, description, icon, type_id) VALUES (1, "health_potion", "Health Potion", "FF0000", 0, "Health regeneration!", "fa-solid fa-flask-round-potion", 0)')
	cursor.execute('INSERT INTO item (item_id, item_name, item_display_name, color, times_used, description, icon, type_id) VALUES (2, "speed_potion", "Speed Potion", "0000FF", 0, "Speed Potion go zooom!", "fa-solid fa-flask-round-potion", 0)')
	cursor.execute('INSERT INTO item (item_id, item_name, item_display_name, color, times_used, description, icon, type_id) VALUES (0, "regular_ball", "Regular Ball", "red", 0, "The Classic Pokemon Ball!", "fa-solid fa-flask-round-potion", 1)')

	cursor.execute('INSERT INTO player (player_id, player_name) VALUES (0, "bob")')

	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (0, "bug", "A6B91A")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (1, "dark", "705746")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (2, "dragon", "6F35FC")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (3, "electric", "F7D02C")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (4, "fairy", "D685AD")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (5, "fighting", "C22E28")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (6, "fire", "EE8130")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (7, "flying", "A98FF3")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (8, "ghost", "735797")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (9, "grass", "7AC74C")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (10, "ground", "E2BF65")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (11, "ice", "96D9D6")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (12, "normal", "A8A77A")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (13, "poison", "A33EA1")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (14, "psychic", "F95587")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (15, "rock", "B6A136")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (16, "steel", "B7B7CE")')
	cursor.execute('INSERT INTO pokemon_types (p_type_id, p_type_name, p_type_color) VALUES (17, "water", "6390F0")')

	cursor.execute('INSERT INTO player_item (quantity, player_id, item_id) VALUES (5, 0, 0)')

	cursor.execute('INSERT INTO team (team_id, team_name, player_id, active_id) VALUES (0, "bobs_minions", 0, 0)')

	cursor.execute('''
		INSERT INTO pokemon
			(pokemon_id, p_name, health, hype, sprite_path, holding, attack, defense, speed, caught_date, team_id)
		VALUES
			(0, "pikachu", 100, 100, "/static/pikachu_icon.png", "Fire Stone", 12, 34, 15, "11/18/2022", 0)
		''')

	cursor.execute('''
		INSERT INTO pokemon
			(pokemon_id, p_name, health, hype, sprite_path, attack, defense, speed, caught_date, team_id)
		VALUES
			(1, "arceus", 100, 1000, "/static/arceus_icon.png", 100, 25, 50, "11/22/2022", 0)
		''')

	cursor.execute('''
		INSERT INTO pokemon
			(pokemon_id, p_name, health, hype, sprite_path, attack, defense, speed, caught_date, team_id)
		VALUES
			(2, "bidoof", 20, 50, "/static/bidoof_icon.png", 200, 0, 0, "11/21/2022", 0)
		''')
	
	cursor.execute('INSERT INTO pokemon_type (pokemon_id, p_type_id) VALUES (0, 3)')
	cursor.execute('INSERT INTO pokemon_type (pokemon_id, p_type_id) VALUES (1, 12)')
	cursor.execute('INSERT INTO pokemon_type (pokemon_id, p_type_id) VALUES (2, 12)')

	connection.commit()
