from typing import List
from pydantic import BaseModel

class CustomerEntity(BaseModel):
    """Customer Entity for able register new customer"""
    name: str = ''
    last_name: str = ''
    year_old: int = 0
    identification: str = ''       
    email: str = ''
    password: str = ''
    phone: str = ''

class ErrorCustomer(BaseModel):
    """Client error for handling all types of errors."""
    status: str = ''
    message: str = ''

class ResponseModel(BaseModel):
    """Response Model that help handling one only response."""
    status: int
    details: List[ErrorCustomer] 
    data: List

class LoginCustomer(BaseModel):
    """Model that allow access the application."""
    user: str = ''
    password: str = ''

class ResponseException(Exception):
    """Hanlder message exception"""
    status: int
    details: List[ErrorCustomer] 
    data: List
    def __init__(self, status: str, details: List[ErrorCustomer], data: List):
        self.status = status
        self.details = details
        self.data = data