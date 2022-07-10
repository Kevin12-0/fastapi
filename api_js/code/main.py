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


@app.get("/cliente/{id}")
async def get_cliente(id: int):
    with sqlite3.connect(DATABASE_URL) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id_cliente ="+str(id))
        response = cursor.fetchall()
        return response


@app.post('/insertar/{nombre}/{email}')
async def Insertar(nombre: str, email: str):
    with sqlite3.connect(DATABASE_URL) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO clientes (nombre,email) VALUES (?,?)', (nombre, email))
        cursor.fetchall()
        return {"mensaje": "Cliente agregado"}


@app.put('/actulizar/{id}/{nombre}/{email}')
async def actulizar(id: str, nombre: str, email: str):
    with sqlite3.connect(DATABASE_URL) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE clientes SET nombre = ?, email = ? WHERE id_cliente = ?', (nombre, email, id))
        cursor.fetchall()
        return {"mensaje": "Cliente Actualizado"}


@app.delete('/eliminar/{id}')
async def eliminar(id: int):
    with sqlite3.connect(DATABASE_URL) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(
            'DELETE FROM clientes WHERE id_cliente= {}'.format(int(id)))
        cursor.fetchall()
        return {"mensaje": "Cliente borrado"}
