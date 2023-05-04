from typing import Union

from fastapi import FastAPI

# Path: main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
@app.get("/hello")
@app.get("/hello/{name}")