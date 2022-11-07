from fastapi.testclient import TestClient
import time

from .main import app

client = TestClient(app)

url_login = "http://localhost:6969/login/"
url_create = "http://localhost:6969/create_customer/"

#test 1
#creacion de cuenta
#verifica respuesta http 200
#verifica consistencia del json devuelto
def test_create_user_ok():
    response = client.post(url_create,headers={"accept": "application/json","Content-Type": "application/json"},
    json={"name": "ernesto","last_name": "perez","year_old": 100,"identification": "87654321","email": "el@correo.com",
    "password": "12345678","phone": "34567890"})
    assert response.json()['status'] == 200
    assert response.json() == {'status': 200, 'details': [],
    'data': [{'name': 'ernesto perez', 'email': 'el@correo.com', 'phone': '34567890'}]}




#test 2
#creacion de cuenta error, el usuario ya ha sido creado
#verifica respuesta http 400
#verifica consistencia del json devuelto
def test_create_user_bad1():
    response = client.post(url_create,headers={"accept": "application/json","Content-Type": "application/json"},
    json={"name": "ernesto","last_name": "perez","year_old": 100,"identification": "87654321","email": "el@correo.com",
    "password": "12345678","phone": "34567890"})
    assert response.json()['status'] == 400
    assert response.json() == {'status': 400, 'details': [{'status': 'Error', 'message': 'El correo ya se encuentra en uso'}], 'data': []}




#test 3
#creacion de segunda cuenta
#verifica respuesta http 200
#verifica consistencia del json devuelto
def test_create_2_user_ok():
    response = client.post(url_create,headers={"accept": "application/json","Content-Type": "application/json"},
    json={"name": "Charles Arturo","last_name": "Ocoró","year_old": 67,"identification": "007006","email": "elprofe@super_o.com",
    "password": "12345678","phone": "9876543"})
    assert response.json()['status'] == 200
    assert response.json() == {'status': 200, 'details': [],
    'data': [{'name': 'Charles Arturo Ocoró', 'email': 'elprofe@super_o.com', 'phone': '9876543'}]}



#test 4
#Login
#verifica respuesta http 200
#verifica consistencia del json devuelto
def test_login():
    response = client.post("http://localhost:6969/login/",
    headers={"accept": "application/json","Content-Type": "application/json"},
    json={"user": "el@correo.com","password": "12345678"})
    assert response.json()['status'] == 200
    global tok
    tok = response.json()["data"][0]["token"]




#test 5
#Lista de usuarios registrados
#verifica respuesta http 200
#verifica consistencia del json devuelto
def test_lista_usr():
    response = client.get('http://localhost:6969/get_customers/',
    headers={"accept": "application/json","token-passed": tok})
    assert response.json()['status'] == 200
    assert response.json() == {'status': 200, 'details': [], 
    'data': [[{'name': 'ernesto', 'last_name': 'perez', 'year_old': 100, 
    'identification': '87654321', 'email': 'el@correo.com', 'password': '', 'phone': '34567890'}, 
    {'name': 'Charles Arturo', 'last_name': 'Ocoró', 'year_old': 67,
     'identification': '007006', 'email': 'elprofe@super_o.com', 'password': '', 'phone': '9876543'}]]}
    print(response.json())




