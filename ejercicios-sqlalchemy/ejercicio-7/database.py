from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine("sqlite:///:memory:", echo=False)

class Base(DeclarativeBase):
    pass