from fastapi import FastAPI

app = FastAPI()

app = FastAPI(title='PRACTICA FASTAPI',
	description= 'Realizando una prueba API',
	version= '1.0')

@app.get('/')
def index():
    return 'WELCOME TO MY WEBSITE'

@app.get('/about')
def about():
    return 'My name is, FABIAN CRUZ GOMEZ'
