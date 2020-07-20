# from data import db_session
# from data.users import User
# from data.admins import Admin
#
# db_session.global_init("db/users.sqlite")
# session = db_session.create_session()
# # admin1 = Admin(telegram_id=419453249, name="Vupsin228", priority="admin")
# # admin2 = Admin(telegram_id=451957793, name="Pupsin228", priority="admin")
# # session.add(admin1)
# # session.add(admin2)
# # session.commit()
# all_users = session.query(User).all()[::-1]
# for user in all_users:
#     print(f"ID юзера(id): {user.id} \n"
#           f"Имя(name): {user.name} \n"
#           f"Возраст(age): {user.age} \n"
#           f"Пол(sex): {user.sex} \n"
#           f"Вес(weight): {user.weight} \n"
#           f"Рост(height): {user.height} \n"
#           f"Баланс(balance): {user.balance} \n"
#           f"Телеграм_ID(telegram_id): {user.telegram_id} \n"
#           f"Кол-во рефералов(referals_count): {user.referals_count} \n"
#           f"Хозяин реферала telegram_id(referal_owner): {user.referal_owner} \n"
#           f"Мои люди-рефералы(referals): {user.referals} \n"
#           f"Последний платеж(дата)(last_payment_date): {user.last_payment_date} \n"
#           f"Дата оплаты(date_to_payment): {user.date_to_payment} \n")
import datetime
import time

date = str(datetime.date.today()).split("-")
# count = float(int(date[0]) * 365 * 24 * 60 * 60 + int(date[1]) * 30 * 24 * 60 * 60 + int(date[2]) * 24 * 60 * 60)
# print(count)
# print(time.ctime(count))
print(float(int(date[0]) * 365 * 24 * 60))

# секунды прошли с эпох
seconds = 13722592000
# seconds = 1575721830.711298
local_time = time.ctime(seconds)
print("Местное время:", local_time)