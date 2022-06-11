from fastapi import FastAPI

import sqlite3
from typing import List
from pydantic import BaseModel

class Request(BaseModel):
    message: str

class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str

class ClienteID(BaseModel):
    id_cliente: int
    nombre: str
    email: str

app = FastAPI()


@app.get("/", response_model=Request)
async def Index():
    return {"message": 'Hola Mundo'}

@app.get('/clientes/',response_model=List[Cliente])
async def Cliente():
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes')
        respose = cursor.fetchall()
        return respose

@app.post("/test")
async def fetch_data(id_cliente: int):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        query = "SELECT * FROM tablename WHERE ID={}".format(str(id))
        results = await database.fetch_all(query=query)
    return  results