from fastapi.middleware.cors import CORSMiddleware
from fastapi import *
from typing import List
from pydantic import BaseModel
import sqlite3
import os
from typing import Union

DATABASE_URL = os.path.join("sql/clientes.sqlite")


class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/clientes", response_model=List[Cliente])
async def list_clientes():
    with sqlite3.connect(DATABASE_URL) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        response = cursor.fetchall()
        return response
