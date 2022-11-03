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

@app.get('/items', response_class=HTMLResponse)
async def index(request: Request):
	return templates.TemplateResponse('items.html', {'request': request})
