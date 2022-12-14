from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.constants_file import Constants

engine = create_engine(
    Constants.SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    """Create connection with the data base"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()