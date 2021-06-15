from fastapi import FastAPI

app = FastAPI ()

@app.get("/")
def home():
	return {"Claudia Arely"}

Datos = {
	1: {
		"nombre": "Claudia",
		"matrícula":"091810190",
		"edad": "20"
	}
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
	return Datos[item_id]
	

