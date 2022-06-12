from fastapi import FastAPI, APIRouter
from typing import List
from pydantic import BaseModel
import sqlite3
from typing import Union

class Request(BaseModel):
    message: str

class Cliente(BaseModel):
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

'''
    consulta por medio de metodo de cursor muestra todos los datos
'''
@app.get("/test/")
async def fetch_data():
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id_cliente = 1')
        respose = cursor.fetchall()
        return respose
'''
    consulta pasando paramtros desde url a una base de datos
'''
@app.get("/consulta/{id}")
async def fetch_data(id:int, q: Union[int, None] = None, short: bool = False):
    id_client = id
    consulta = 'SELECT * FROM clientes WHERE id_cliente ='+str(id_client)
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(consulta)
        respose = cursor.fetchall()
        return respose
'''
    paso de paarametros por url
'''
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = item_id
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item