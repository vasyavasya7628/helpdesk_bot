from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


def connect_to_db():
    conn = "postgresql://postgres:crjkmrj@localhost:5432/postgres"
    engine = create_engine(conn)
    return engine
