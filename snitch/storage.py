# coding: utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_email = Column(String(50))
    user_passwd = Column(String(50))
    user_full_name = Column(String(50))
    user_is_active = Column(Boolean(1))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                         self.name, self.fullname, self.password)
