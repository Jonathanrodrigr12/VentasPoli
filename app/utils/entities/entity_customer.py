from typing import List
from pydantic import BaseModel

#Las entidades se pueden crear en una sola clase por clase, es decir 
# Dejar en una sola clase, todas las entidades posibles. Sea de respuesta o de ingreso
class CustomerEntity(BaseModel):
    name: str = ''
    last_name: str = ''
    year_old: int = 0
    identification: str = ''       
    email: str = ''
    password: str = ''
    phone: str = ''

class ErrorCustomer(BaseModel):
    status: str = ''
    message: str = ''

class SuccesfulRegiser(BaseModel):
    token: str = ''
    name: str = ''

class LoginCustomer(BaseModel):
    user: str = ''
    password: str = ''

class RestorePassword(BaseModel):
    user: str = ''
    restore_form: str = ''

class ResetPassword(BaseModel):
    user: str = ''
    password: str = ''

class ResponseModel(BaseModel):
    status: int
    details: List[ErrorCustomer] 
    data: List

class ResponseException(Exception):
    status: int
    details: List[ErrorCustomer] 
    data: List
    def __init__(self, status: str, details: List[ErrorCustomer], data: List):
        self.status = status
        self.details = details
        self.data = data