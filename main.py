import sqlite3
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
	return templates.TemplateResponse('items.html', {'request': request})

@app.get('/team', response_class=HTMLResponse)
async def team(request: Request):
	return templates.TemplateResponse('team.html', {'request': request})

@app.get('/team/{pokemon_name}', response_class=HTMLResponse)
async def team_member(request: Request, pokemon_name: str):
	return templates.TemplateResponse('team_member.html', {'request': request})

@app.get('/items/{item_type}', response_class=HTMLResponse)
async def item_list(request: Request, item_type: str):
	return templates.TemplateResponse('item_list.html', {'request': request})

@app.get('/items/{item_type}/{item_name}', response_class=HTMLResponse)
async def item(request: Request, item_type: str, item_name: str):
	return templates.TemplateResponse('item.html', {'request': request})

@app.get('/map', response_class=HTMLResponse)
async def map(request: Request):
	return templates.TemplateResponse('map.html', {'request': request})
