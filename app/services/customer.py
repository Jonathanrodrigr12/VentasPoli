from http import HTTPStatus
from sqlalchemy.orm import Session
from app.utils.models.model_customer import CustomerModel
from app.utils.encryption.encryption_utils import Encryption
from app.utils.entities.entity_customer import CustomerEntity, ErrorCustomer, ResponseModel
from app.utils.constans.utils_constans import *
from app.utils.entities.entity_customer import *
from app.utils.security.security_util import SecurityUtil

class Customer:
    """Customer that contain all the services for the customer."""

    def fetch_all(db: Session):
        """Get all customer created."""
        result = (list(map(lambda register:CustomerEntity(name=register.name, last_name=register.last_name,
                year_old=register.year_old, identification=register.identification, email=register.email, phone=register.phone)
            , db.query(CustomerModel).all())))
        return ResponseModel(status=HTTPStatus.OK, details=[], data=[result])

    async def create(db: Session, item: CustomerEntity):
        """Create customer when it doesn't exist in the database."""
        find_user = Customer.fetch_by_name(db, item.email)
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
        return ResponseModel(status=HTTPStatus.OK,details=[], data=[
            {'name': f'{item.name} {item.last_name}', 
            'email': item.email,
            'phone': item.phone
            }])
    
    def fetch_by_name(db: Session, email: str):
        """Get customer across the email address."""
        user = db.query(CustomerModel).filter(
            CustomerModel.email == email.lower()).first()
        return user

    def login(data: LoginCustomer, db: Session):
        userdata = db.query(CustomerModel).filter(
            CustomerModel.email == data.user.lower()).first()
        if userdata is None:
            return ResponseModel(status=HTTPStatus.BAD_REQUEST, details=data, data=[])

        password = Encryption.decrypt_value(userdata.password).decode("utf-8")

        if data.password != password:
            data = []
            data.append(ErrorCustomer(status=error, message=login_error))
            return ResponseModel(status=HTTPStatus.BAD_REQUEST, details=data, data=[])
        token = SecurityUtil.get_token({
            'user': userdata.email
        })
        return ResponseModel(status=HTTPStatus.OK, details=[], data=[
            {
             'token': token,
             'name': f'{userdata.name} {userdata.last_name}',
             'email': userdata.email,
             'phone': userdata.phone
             }])    