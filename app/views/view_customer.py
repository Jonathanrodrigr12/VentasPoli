from http import HTTPStatus
from fastapi import APIRouter, Depends, Header
from app.utils.models.enum.user_roles import UserRoles
from app.utils.entities.entity_customer import *
from sqlalchemy.orm import Session
from app.services.customer import Customer as CustomerService
from app.resources.context.context import get_db
from app.constants_file import Constants

router = APIRouter()

@router.post("/create_customer/", tags=["customer"], response_model=ResponseModel)
async def create_customer(data: CustomerEntity, db: Session = Depends(get_db)):
    return await CustomerService.create(db, data)

# @router.get("/get_iva/", tags=["customer"])
# async def get_iva(db: Session = Depends(get_db), token = Depends(SecurityUtil.verify_customer_token)):
#     return ResponseModel(status=HTTPStatus.OK, details=[], data=[{
#         "IVA": Constants.IVA
#     }])

@router.post("/login/", tags=["customer"], response_model=ResponseModel)
async def login(data: LoginCustomer, db: Session = Depends(get_db)):
    return CustomerService.login(data, db)

# @router.get("/get_tables_customer/", tags=["customer"])
# async def get_tables_customer(db: Session = Depends(get_db), token = Depends(SecurityUtil.verify_customer_token)):
#     return CustomerService.get_tables_customer(db)

# @router.put("/update_table_customer/{table_id}", tags=["customer"], response_model=ResponseModel)
# def update_table_customer(table_id, db: Session = Depends(get_db), token = Depends(SecurityUtil.verify_customer_token)):
#     return CustomerService.update_table(table_id, db)

# @router.get("/auth_method/", tags=["Validation_login"])
# def auth_method(x_token: str = Header("token")):
#     return CustomerService.validation_user(x_token)

# @router.post("/restore_password/", tags=["customer"], response_model=ResponseModel)
# async def restore_password(brestorUser: RestorePassword, db: Session = Depends(get_db)):
#     return await CustomerService.restore_password(brestorUser, db)

# @router.put("/reset_password/", tags=["customer"], response_model=ResponseModel)
# def reset_password(brestorUser: ResetPassword, db: Session = Depends(get_db), 
#                            token = Depends(ProfileEmployeChecker([UserRoles.table_coordinator,
#                                                                                                UserRoles.chef,
#                                                                                                UserRoles.customer,
#                                                                                                UserRoles.waiter,
#                                                                                                UserRoles.manager]))):
#     return CustomerService.reset_password(brestorUser, token, db)

# @router.post("/logout/", tags=["customer"], response_model=ResponseModel)
# def logout(token = Depends(ProfileEmployeChecker([UserRoles.table_coordinator,
#                                                   UserRoles.chef,
#                                                   UserRoles.customer,
#                                                   UserRoles.waiter,
#                                                   UserRoles.manager]))):
#     return CustomerService.close_session(token['token'])
