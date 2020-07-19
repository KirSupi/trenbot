import datetime
import sqlalchemy
from sqlalchemy import orm

from data import db_session
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy import orm
# from werkzeug.security import generate_password_hash, check_password_hash
import time


class Admin(SqlAlchemyBase, UserMixin):
    __tablename__ = 'admins'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    telegram_id = sqlalchemy.Column(sqlalchemy.String, default="", nullable=True)
    priority = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    #priority = admin / moder

    def repr(self):
        return f'<Admin> id:{self.id}, balance:{self.balance}'
