from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    gio = "gio"
    sdc = "sdc"
    mayick = "mayick"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.gio:
        return {"model_name": model_name, "message": "Nombre"}

    if model_name.value == "mayick":
        return {"model_name": model_name, "message": "Apodo"}

    return {"model_name": model_name, "message": "Mis apellidos son Sanchez de la cruz"}