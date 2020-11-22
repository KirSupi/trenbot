# coding=utf-8
import math
import os
import random
import json
from pickle import loads, dumps
from datetime import date, time

import requests
from werkzeug.utils import redirect

from data import db_session
from data.users import User
from data.payments import Payment
from flask import Flask, render_template, request
from tariffs import tariffs
from data.db_session import db_path

# {
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# }

db_session.global_init(db_path)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


# обрабатывает POST-запрос и записывает оплату
@app.route('/result', methods=['POST'])
def get_payment():
    data = request.get_data()
    data = json.loads(data)
    session = db_session.create_session()
    user_id, payNum = data['InvId'].split('!') # e.g. 111111!2
    user = session.query(User).filter(User.id == user_id).first()
    time_now = int(time.time())
    if user.date_to_payment <= time_now:
        user.date_to_payment = time_now + tariffs[str(data['OutSum'])]
    else:
        user.date_to_payment += tariffs[str(data['OutSum'])]
    session.add(user)
    session.commit()

    session = db_session.create_session()
    payment = Payment(telegram_id=user_id, amount=int(data['OutSum']), date=time_now)
    session.add(payment)
    session.commit()

    return 'ok'


@app.route('/test')
def test():
    return render_template("base.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='194.67.86.81', port=port)
