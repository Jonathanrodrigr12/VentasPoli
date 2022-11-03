from sqlalchemy import Column, Integer, VARCHAR

from app.resources.context.context import Base

class CustomerModel(Base):
    """Columns of the Model Customer."""
    __tablename__ = "customer"
    
    id = Column(Integer, autoincrement=True ,primary_key=True,index=True)
    name = Column(VARCHAR, nullable=False, unique=False)
    last_name = Column(VARCHAR, nullable=False, unique=False)
    year_old = Column(Integer, nullable=False, unique=False)
    identification = Column(VARCHAR, nullable=False, unique=False)
    email = Column(VARCHAR, nullable=False, unique=False)
    password = Column(VARCHAR, nullable=False, unique=False)
    phone = Column(VARCHAR, nullable=False, unique=False)