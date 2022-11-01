from email.policy import strict
from http import HTTPStatus
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy.sql.expression import and_, true, update
from sqlalchemy.sql.functions import user
from app.utils.models.enum.user_roles import UserRoles
from app.utils.models.model_customer import CustomerModel
from app.utils.constans.utils_constans import *
from app.utils.entities.entity_customer import *
from app.utils.encryption.encryption_utils import Encryption


class Customer:

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(CustomerModel).offset(skip).limit(limit).all()

    async def create(db: Session, item: CustomerEntity):
        find_user = None
        if find_user is not None:
            data = []
            data.append(ErrorCustomer(status=error, message=message_email))
            return ResponseModel(status=HTTPStatus.BAD_REQUEST, details=data, data=[])
        password_encrypt = Encryption.encrypt_value(
            item.password).decode("utf-8")
        db_item = CustomerModel(name=item.name, last_name=item.last_name, year_old=item.year_old,
                                identification=item.identification, email=item.email.lower(),
                                password=password_encrypt,
                                phone=item.phone)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        roles = UserRoles.customer.value
        return ResponseModel(status=HTTPStatus.OK,details=[], data=[
            {'role': roles, 
            'name': f'{item.name} {item.last_name}', 
            'email': item.email,
            'phone': item.phone
            }])

    def fetch_by_id(db: Session, id: int):
        return db.query(CustomerModel).filter(CustomerModel.id == id).first()

    def login(data: LoginCustomer, db: Session):
        userdata = db.query(CustomerModel).filter(
            CustomerModel.email == data.user.lower()).first()
        roles = UserRoles.customer.value
        if userdata is None:
            return ResponseModel(status=HTTPStatus.BAD_REQUEST, details=data, data=[])

        password = Encryption.decrypt_value(userdata.password).decode("utf-8")

        if data.password != password:
            data = []
            data.append(ErrorCustomer(status=error, message=login_error))
            return ResponseModel(status=HTTPStatus.BAD_REQUEST, details=data, data=[])

        return ResponseModel(status=HTTPStatus.OK, details=[], data=[
            {'role': roles,
             'name': f'{userdata.name} {userdata.last_name}',
             'email': userdata.email,
             'phone': userdata.phone
             }])

    # async def restore_password(data: RestorePassword, db: Session):
    #     result = db.query(CustomerModel).filter(
    #         CustomerModel.email == data.user.lower()).first()
    #     role = UserRoles.customer.value

    #     if result is None:
    #         result = db.query(ProfilesUserModel).filter(
    #             ProfilesUserModel.email == data.user.lower()).first()
    #         role = result.identifier_user

    #     if(result is not None):
    #         token = token = SecurityUtil.get_token({
    #             'user': data.user,
    #             'role': role
    #         })
    #         url = '{}?mail={}&token={}'.format(
    #             data.restore_form, data.user, token)
    #         body = "Hola,\nEste es el link para generar una nueva contraseña:\n{}".format(
    #             url)
    #         await Mail.send_email_async("Reestablecer contraseña", data.user, body)
    #     else:
    #         data = []
    #         data.append(ErrorCustomer(status=error, message=user_no_create))
    #         return ResponseModel(status=HTTPStatus.BAD_REQUEST, details=data, data=[])
    #     return ResponseModel(status=HTTPStatus.OK, details=[], data=[{"message": "Send Email"}])

    # def reset_password(data: ResetPassword, token: str, db: Session):
    #     result = db.query(CustomerModel).filter(
    #         CustomerModel.email == data.user.lower()).first()
    #     if result is None:
    #         result = db.query(ProfilesUserModel).filter(
    #             ProfilesUserModel.email == data.user.lower()).first()
    #         if result is None:
    #             data = []
    #             data.append(ErrorCustomer(status=error, message=login_error))
    #             return ResponseModel(status=HTTPStatus.BAD_REQUEST, details=data, data=[])

    #     result.password = Encryption.encrypt_value(
    #         data.password).decode("utf-8")
    #     db.commit()
    #     db.refresh(result)
    #     token = token = SecurityUtil.get_token({
    #         'user': token['val']['user'],
    #         'role': token['val']['role']
    #     })
    #     return ResponseModel(status=HTTPStatus.OK, details=[], data=[{'token': token}])

    # def validation_user(x_token: str):
    #     validation_token = SecurityUtil.validate_token(x_token)
    #     if not validation_token[0]:
    #         return ResponseModel(status=HTTPStatus.OK, details=[], data=[{'authenticator': False}])
    #     else:
    #         return ResponseModel(status=HTTPStatus.OK, details=[], data=[{'authenticator': True}])

    # def close_session(x_token: str):
    #     SecurityUtil.delete_token(x_token)
    #     return ResponseModel(status=HTTPStatus.OK, details=[], data=[{'logout': True}])

    # def get_tables_customer(db: Session):
    #     return ResponseModel(status=HTTPStatus.OK, details=[], data=[
    #         list(map(lambda x: {
    #             'id': x.id,
    #             'name': x.name,
    #             'reserved': x.reserved
    #         },
    #             db.query(TablesModel).all()
    #         ))])

    # def update_table(table_id, db: Session):
    #     result = db.query(TablesModel).filter(
    #         TablesModel.id == table_id).first()
    #     result.reserved = not result.reserved
    #     db.commit()
    #     db.refresh(result)
    #     return ResponseModel(status=HTTPStatus.OK, details=[], data=[{'message': 'Table state change'}])
