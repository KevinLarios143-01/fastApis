# Creación de la app
from fastapi import FastAPI
from typing import Union, Optional
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):# Clase que hereda de BaseModel y que define los atributos de un item
    id: int
    name: str
    description: str
    price: float
    on_offer: bool
    
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
def calcular(num1: float, num2: float): 
    return {"Calculadora": num1 + num2}     


@app.get("/greet")
def greet_optional_name(name: Optional[str] = "user"):
    if name:
        return f"Hello, {name}"
    else:
        return "Hello, World"

@app.put("/items/{item_id}") # Decorador que indica que la función update_item() se ejecutará cuando se haga una petición PUT a la ruta /items/{item_id}
def update_item(item_id: int, item: Item):
    return {"name": item.name, "description": item.description, "price": item.price, "on_offer": item.on_offer}

