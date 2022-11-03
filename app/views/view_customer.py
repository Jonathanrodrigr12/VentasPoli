from fastapi import APIRouter, Depends
from app.utils.entities.entity_customer import *
from sqlalchemy.orm import Session
from app.services.customer import Customer as CustomerService
from app.resources.context.context import get_db
from app.utils.security.security_util import SecurityUtil

router = APIRouter()

@router.post("/create_customer/", tags=["customer"], response_model=ResponseModel)
async def create_customer(data: CustomerEntity, db: Session = Depends(get_db)):
    """End point for can create customer."""
    return await CustomerService.create(db, data)

@router.get("/get_customers/", tags=["customer"], response_model=ResponseModel)
async def get_customers(db: Session = Depends(get_db), token = Depends(SecurityUtil.validate_token)):
    """End point that get all customers."""
    return CustomerService.fetch_all(db)

@router.post("/login/", tags=["customer"], response_model=ResponseModel)
async def login(data: LoginCustomer, db: Session = Depends(get_db)):
    """End point for get access the application."""
    return CustomerService.login(data, db)