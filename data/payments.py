import datetime
import sqlalchemy
from sqlalchemy import orm

from data import db_session
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy import orm
# from werkzeug.security import generate_password_hash, check_password_hash
import time


class Payment(SqlAlchemyBase, UserMixin):
    __tablename__ = 'payments'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    telegram_id = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
    amount = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
    date = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)


    def repr(self):
        return f'<Payment> id:{self.id}, telegram_id:{self.telegram_id}, amount:{self.amount}'

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