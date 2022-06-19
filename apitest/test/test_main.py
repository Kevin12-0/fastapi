from fastapi.testclient import TestClient
from code.main import app

clientes = TestClient(app)

def test_index():
	response = clientes.get('/')
	data = {"message": 'Hola Mundo'}
	assert response.status_code == 200
	assert response.json()==data

def test_consulta():
	response = clientes.get('/consulta/2?short=1')
	data = {"id_cliente":2,"nombre":"John","email":"john@gmail.com"}
	assert response.status_code == 200
	assert response.json()==data

#python3 -m pytest -u