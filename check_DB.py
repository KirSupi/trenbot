from data import db_session
from data.users import User

# id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
# name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
# age = sqlalchemy.Column(sqlalchemy.String, nullable=False)
# sex = sqlalchemy.Column(sqlalchemy.String, nullable=False)
# weight = sqlalchemy.Column(sqlalchemy.String, nullable=False)
# height = sqlalchemy.Column(sqlalchemy.String, nullable=False)
# balance = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
# telegram_id = sqlalchemy.Column(sqlalchemy.String, default="", nullable=True)
# referals_count = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
# referal_owner = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
# referals = sqlalchemy.Column(sqlalchemy.String, nullable=True)
# last_payment_date = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
# date_to_payment = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)


db_session.global_init("db/users.sqlite")
session = db_session.create_session()
all_users = session.query(User).all()[::-1]
for user in all_users:
    print(f"ID юзера(id): {user.id} \n"
          f"Имя(name): {user.name} \n"
          f"Возраст(age): {user.age} \n"
          f"Пол(sex): {user.sex} \n"
          f"Вес(weight): {user.weight} \n"
          f"Рост(height): {user.height} \n"
          f"Баланс(balance): {user.balance} \n"
          f"Телеграм_ID(telegram_id): {user.telegram_id} \n"
          f"Кол-во рефералов(referals_count): {user.referals_count} \n"
          f"Хозяин реферала telegram_id(referal_owner): {user.referal_owner} \n"
          f"Мои люди-рефералы(referals): {user.referals} \n"
          f"Последний платеж(дата)(last_payment_date): {user.last_payment_date} \n"
          f"Дата оплаты(date_to_payment): {user.date_to_payment} \n")
