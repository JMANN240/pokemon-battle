import sqlite3
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

app = FastAPI()
api = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/api', api, name='api')

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def battle(request: Request):
	return templates.TemplateResponse('battle.html', {'request': request})

@app.get('/items', response_class=HTMLResponse)
async def items(request: Request):
	return templates.TemplateResponse('items.html', {
		'request': request,
		'back_url': '/'
	})

@app.get('/team', response_class=HTMLResponse)
async def team(request: Request):
	return templates.TemplateResponse('team.html', {'request': request})

@app.get('/team/{pokemon_name}', response_class=HTMLResponse)
async def team_member(request: Request, pokemon_name: str):
	return templates.TemplateResponse('team_member.html', {'request': request})

@app.get('/items/{item_type}', response_class=HTMLResponse)
async def item_list(request: Request, item_type: str):	
	with sqlite3.connect("database.db") as connection:
		connection.row_factory = dict_factory
		cursor = connection.cursor()
		print(item_type)
		res = cursor.execute("SELECT type_id FROM item_types WHERE type_name=?", (item_type,))
		type_id = cursor.fetchone()['type_id']
		res = cursor.execute("SELECT * FROM item WHERE type_id=?", (type_id,))
		items = res.fetchall()
		print(items)
	return templates.TemplateResponse('item_list.html', {'request': request, 'items': items, 'type': item_type})

@app.get('/items/{item_type}/{item_name}', response_class=HTMLResponse)
async def item(request: Request, item_type: str, item_name: str):
	return templates.TemplateResponse('item.html', {'request': request})

@app.get('/map', response_class=HTMLResponse)
async def map(request: Request):
	return templates.TemplateResponse('map.html', {
		'request': request,
		'back_url': '/'
	})
