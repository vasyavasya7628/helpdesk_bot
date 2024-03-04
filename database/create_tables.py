from sqlalchemy import Integer, Column, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

from database.base import connect_to_db, Base


class District(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True)
    district_name = Column(Text, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    district_id = Column(Integer, ForeignKey('districts.id'))
    user_id = Column(Integer)
    user_name = Column(Text)
    user_nickname = Column(Text)
    role = Column(Text)

    district = relationship('District')


class OrderNumber(Base):
    __tablename__ = 'order_number'

    id = Column(Integer, primary_key=True)
    order_number = Column(Integer)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    district_id = Column(Integer, ForeignKey('districts.id'))
    order_number = Column(Integer)
    user_problem_description = Column(Text)
    admin_comment = Column(Text)
    from_user = Column(Text)
    to_admin = Column(Text)
    date_create = Column(Text)
    time_taken = Column(Text)
    date_close = Column(Text)
    status = Column(Text)
    admin_telegram_id = Column(Integer)

    district = relationship('District')


Base.metadata.create_all(bind=connect_to_db())

