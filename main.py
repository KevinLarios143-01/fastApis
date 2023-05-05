from typing import Union

from fastapi import FastAPI

# Creación de la app
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel): # Se crea la clase Item que hereda de BaseModel
    name: str # El campo name es obligatorio
    price: float # El campo price es obligatorio
    is_offer: Union[bool , None]=None #Union permite que el campo sea de tipo booleano o nulo

@app.get("/") # Decorador que indica que la función read_root() se ejecutará cuando se haga una petición GET a la ruta /
def read_root():
    return {"Hello": "World"}

@app.get("/hola") # Decorador que indica que la función hola() se ejecutará cuando se haga una petición GET a la ruta /hola
def hola():
    return {"Hola": "Mundo"}

@app.get("/items/{item_id}") # Decorador que indica que la función read_item() se ejecutará cuando se haga una petición GET a la ruta /items/{item_id}
def read_item(item_id: int, q: Union[str, None]=None):
    return {"item_id": item_id, "q": q}

@app.get("/calculadora") # Decorador que indica que la función calcular() se ejecutará cuando se haga una petición GET a la ruta /calculadora
def calcular(num1: int, num2: int): 
    return {"Calculadora": num1 + num2}     

@app.put("/items/{item_id}") # Decorador que indica que la función update_item() se ejecutará cuando se haga una petición PUT a la ruta /items/{item_id}
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

