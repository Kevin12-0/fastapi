from fastapi import *
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

class Registro(BaseModel):
	nombre : str
	email : str

app = FastAPI()

@app.get("/", response_model=Request)
async def Index():
    return {"message": 'API REST'}

@app.get('/clientes/',response_model=List[Cliente])
async def Cliente(offset:int = 0, limit:int = 3):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes LIMIT ? OFFSET ? ',(limit,offset))
        respose = cursor.fetchall()
        return respose

'''
    consulta pasando paramtros desde url a una base de datos
'''
@app.get("/consulta/{id}")
async def fetch_data(id:int):
    id_client = id
    consulta = 'SELECT * FROM clientes WHERE id_cliente ={}'.format((int(id_client)))
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(consulta)
        respose = cursor.fetchall()
        return respose
'''
	insertar registros en una tabla
'''
@app.post('/insertar/{nombre}/{email}')
async def Insertar(nombre:str,email:str):
	with sqlite3.connect('sql/clientes.sqlite') as connection:
		connection.row_factory = sqlite3.Row
		cursor = connection.cursor()
		cursor.execute('INSERT INTO clientes (nombre,email) VALUES (?,?)',(nombre,email))
		cursor.fetchall()
		return {"mensaje":"Cliente agregado"}

'''
	Actualizar registros de una tabla
'''
@app.put('/actulizar/{id}/{nombre}/{email}')
async def actulizar(id:str, nombre:str, email:str):
	with sqlite3.connect('sql/clientes.sqlite') as connection:
		connection.row_factory = sqlite3.Row
		cursor = connection.cursor()
		cursor.execute('UPDATE clientes SET nombre = ?, email = ? WHERE id_cliente = ?',(nombre,email,id))
		cursor.fetchall()
		return {"mensaje":"Cliente Actualizado"}
'''
	Eliminar un registro
'''
@app.delete('/eliminar/{id}')
async def eliminar(id:int):
	with sqlite3.connect('sql/clientes.sqlite') as connection:
		connection.row_factory = sqlite3.Row
		cursor = connection.cursor()
		cursor.execute('DELETE FROM clientes WHERE id_cliente= {}'.format(int(id)))
		cursor.fetchall()
		return {"mensaje":"Cliente borrado"}




