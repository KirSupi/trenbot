import datetime
import sqlalchemy
from sqlalchemy import orm

from data import db_session
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy import orm
# from werkzeug.security import generate_password_hash, check_password_hash
import time


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    age = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    sex = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    weight = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    height = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    balance = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
    telegram_id = sqlalchemy.Column(sqlalchemy.String, default="", nullable=True)
    referals_count = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=True)
    referal_owner = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=True)
    referals = sqlalchemy.Column(sqlalchemy.String, default="", nullable=True)
    last_payment_date = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
    date_to_payment = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)

    def repr(self):
        return f'<User> id:{self.id}, balance:{self.balance}'

    # def get(id):
    #     return User.query.get(id)
    #
    # def new(id, ref_owner=None):
    #     user = User.get(id)
    #     if user:
    #         return None
    #
    #     if not user:
    #         if ref_owner:
    #             user = User(id=id, balance=0, referal_owner=ref_owner)
    #         else:
    #             user = User(id=id, balance=0)
    #         session = db_session.create_session()
    #         session.add(user)
    #         session.commit()
    #         return True