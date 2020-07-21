# coding: utf8
from buttons_and_texts import *
from bot_configuration import *
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from data import db_session
from data.admins import Admin
from data.users import User
import time
import os
from data.db_session import db_path
from data.payments import Payment

db_session.global_init(db_path)

OTHER_BODY, QUESTIONNAIRE_2, QUESTIONNAIRE_3, QUESTIONNAIRE_4, \
QUESTIONNAIRE_5, QUESTIONNAIRE_END, OTHER_BODY_QUESTION = range(
    7)


def answer_to_question_other(update, context):
    query = update.callback_query
    data = query.data
    if data == CALLBACK_BUTTON_I_DONT_WANT:
        update.effective_message.reply_text("Мы все равно покажем результаты,"
                                            " чтобы сильнее вас мотивировать для грядующих тренировок!")
    if context.user_data['kind of training'] == CALLBACK_BUTTON_GAIN_WEIGHT:
        update.effective_message.reply_text("До")
        update.effective_message.reply_photo(open('src\img\p1.jpg', 'rb'))
        update.effective_message.reply_text("После")
        update.effective_message.reply_photo(open('src\img\p2.jpg', 'rb'))
    if context.user_data['kind of training'] == CALLBACK_BUTTON_LOSE_WEIGHT:
        update.effective_message.reply_text("До")
        update.effective_message.reply_photo(open('src\img\p3.jpg', 'rb'))
        update.effective_message.reply_text("После")
        update.effective_message.reply_photo(open('src\img\p4.jpg', 'rb'))
    start_text = "Теперь нужно пройти небольшой опрос," \
                 " чтобы мы подобрали для тебя оптимальный курс тренировок✅)"
    update.effective_message.reply_text(text=start_text)
    question = "Как вас зовут?"
    update.effective_message.reply_text(text=question)
    return QUESTIONNAIRE_2


def second_quest(update, context):
    context.user_data['ques1'] = update.message.text
    question = "Сколько вам лет?"
    update.effective_message.reply_text(text=question)
    return QUESTIONNAIRE_3


def third_quest(update, context):
    context.user_data['ques2'] = update.message.text
    question = "Какой у вас пол?"
    update.effective_message.reply_text(text=question)
    return QUESTIONNAIRE_4


def fourth_quest(update, context):
    context.user_data['ques3'] = update.message.text
    question = "Какой вес?"
    update.effective_message.reply_text(text=question)
    return QUESTIONNAIRE_5


def fifth_quest(update, context):
    context.user_data['ques4'] = update.message.text
    question = "Какой рост?"
    update.effective_message.reply_text(text=question)
    return QUESTIONNAIRE_END


def end_of_questionnaire(update, context):
    context.user_data['ques5'] = update.message.text
    update.effective_message.reply_text(text=f"Имя:{context.user_data['ques1']}, \n"
                                             f"Возраст:{context.user_data['ques2']}, \n"
                                             f"Пол:{context.user_data['ques3']}, \n"
                                             f"Вес:{context.user_data['ques4']}, \n"
                                             f"Рост{context.user_data['ques5']}, \n")
    referal_id = 0
    if context.user_data['ref']:
        referal_id = int(context.user_data['ref'])
    # ДОбавляем юзера в БД после опроса
    session = db_session.create_session()
    user = User(
        referal_owner=int(referal_id),
        telegram_id=str(update.effective_message.chat_id),
        weight=str(context.user_data['ques4']),
        height=str(context.user_data['ques5']),
        sex=str(context.user_data['ques3']),
        age=str(context.user_data['ques2']),
        name=str(context.user_data['ques1']))
    session.add(user)
    session.commit()
    # ДОбавляем юзера в БД после опроса
    update.effective_message.reply_text(text="⏳Подбираем тренировки....")
    chat_id = update.message.chat_id
    try:
        delay = 5
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(task, delay, context=chat_id)
        # Запоминаем созданную задачу в данных чата.
        context.chat_data['job'] = new_job
        # Присылаем сообщение о том, что всё получилось.
        # update.message.reply_text(f'Вернусь через {delay} секунд')

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set_timer <секунд>')

    return ConversationHandler.END


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='✅Оптимальный курс тренировок подобран!✅')
    context.bot.send_message(job.context, text=VIDEO_TEXT)
    context.bot.forward_message(job.context, group_with_video_id, 611)
    welcome_text = "Меню бота"
    context.bot.send_message(job.context, text=welcome_text, reply_markup=get_main_menu_bot_keyboard())
    return ConversationHandler.END


def key_button_handler(update, context):
    query = update.callback_query
    data = query.data
    if data in [CALLBACK_BUTTON_GAIN_WEIGHT, CALLBACK_BUTTON_LOSE_WEIGHT]:
        context_text = "Ты сделала еще один шаг на встречу телу своей мечты, а это значит," \
                       " что ты на верном пути и совсем скоро получишь желаемый результат🏃‍♀️"
        context.user_data['kind of training'] = data
        update.effective_message.reply_text(text=context_text)
        context.bot.forward_message(update.effective_message.chat_id, group_with_video_id, 611)
        update.effective_message.reply_text("какие-то видео", reply_markup=get_next_inline_keyboard())
    if data == CALLBACK_BUTTON_NEXT:
        return throw_question_body(update=update, context=context)


def throw_question_body(update, context):
    question_text = "Хочешь увидеть результаты людей, которые начали тренировки вместе со мной?"
    update.effective_message.reply_text(text=question_text, reply_markup=get_question_other_body_inline_keyboard())
    return OTHER_BODY


def make_payment(update, context, type_pay):
    update.message.reply_text(text=f"Вы произвели оплату на {type_pay}")


def start_training(update, context):
    session = db_session.create_session()
    current_user = session.query(User).filter(User.telegram_id == update.message.chat_id).first()
    if current_user.date_to_payment > int(time.time()):
        update.message.reply_text("Кнопки с видео")
    else:
        update.message.reply_text("У вас не оплачена подписка !")
        update.message.reply_text(text=PAYMENT_TEXT, reply_markup=get_PAYMENT_keyboard())


def get_res_people(update, context, type_training):
    if type_training == BUTTON_GET_WEIGHT:
        update.message.reply_text("До")
        update.message.reply_photo(open('src\img\p1.jpg', 'rb'))
        update.message.reply_text("После")
        update.message.reply_photo(open('src\img\p2.jpg', 'rb'))
    elif type_training == BUTTON_LOSE_WEIGHT:
        update.message.reply_text("До")
        update.message.reply_photo(open('src\img\p3.jpg', 'rb'))
        update.message.reply_text("После")
        update.message.reply_photo(open('src\img\p4.jpg', 'rb'))


def make_BONUS(update, context, type_):
    session = db_session.create_session()
    if type_ == BUTTON_NUMBER_OF_REFERRALS:
        current_user = session.query(User).filter(User.telegram_id == update.message.chat_id).first()
        update.message.reply_text(text=f"{current_user.referals_count}шт.")

    elif type_ == BUTTON_BONUS_PACKAGE:
        current_user = session.query(User).filter(User.telegram_id == update.message.chat_id).first()
        update.message.reply_text(text=f"{current_user.balance}руб.")
    elif type_ == BUTTON_LINK:
        update.message.reply_text(
            text=f"Ссылка:http://t.me/trenirovki_test228bot?start=871qXoi359ref={update.message.chat_id} \n"
                 f"Отправив ее знакомым, вы получите бонусные 10р!")
    session.commit()


def add_most_people(update, context):
    update.message.reply_text("Перешлите сообщение человека, которого хотите сделать модератором",
                              reply_markup=get_cancel_keyboard())
    return get_forward_message


def add_most_people_end(update, context):
    if update.message.text == "/CANCEL":
        update.message.reply_text("Введите любой текст, для вызова меню")
        return ConversationHandler.END
    moder = update.message.forward_from
    session = db_session.create_session()
    moder1 = Admin(telegram_id=moder['id'], name=moder['first_name'], priority="moder")
    session.add(moder1)
    session.commit()
    update.message.reply_text(text=f"Модератор {moder1.name} успешно добавлен!")
    return ConversationHandler.END


def delete_user(update, context):
    update.message.reply_text("Перешлите сообщение человека, которого хотите удалить",
                              reply_markup=get_cancel_keyboard())
    return delete


def delete_user_end(update, context):
    if update.message.text == "/CANCEL":
        update.message.reply_text("Введите любой текст, для вызова меню")
        return ConversationHandler.END
    else:
        session = db_session.create_session()
        admin_moder = session.query(Admin).filter(Admin.telegram_id == update.message.chat_id).first()
        if admin_moder.priority == "admin":
            moder = session.query(Admin).filter(Admin.telegram_id == update.message.forward_from['id']).first()
            session.delete(moder)
            session.commit()
            update.message.reply_text("Успешно!")
        elif admin_moder.priority == "moder":
            pass
        return ConversationHandler.END


def change_balance(update, context):
    update.message.reply_text("Перешлите сообщение человека, у которого хотите изменить баланс",
                              reply_markup=get_cancel_keyboard())
    return get_balance_id


def change_balance_id(update, context):
    if update.message.text == "/CANCEL":
        update.message.reply_text("Введите любой текст, для вызова меню")
        return ConversationHandler.END
    print(update.message.text)
    print(update.message.forward_from, "!")
    context.user_data['balance_id'] = update.message.forward_from
    update.message.reply_text(f"Введите новое значение баланса для юзера {context.user_data['balance_id'].first_name}")
    # user_info =
    # session = db_session.create_session()
    # user = session.query(User).filter(User.telegram_id == user_info['id']).first()
    # user.balance =
    # session.commit()
    return get_balance


def change_balance_end(update, context):
    if update.message.text == "/CANCEL":
        update.message.reply_text("Введите любой текст, для вызова меню")
        return ConversationHandler.END
    else:
        session = db_session.create_session()
        user = session.query(User).filter(User.telegram_id == context.user_data['balance_id'].id).first()
        user.balance = int(update.message.text)
        session.commit()
        update.message.reply_text("Успешно!")
        return ConversationHandler.END


def change_text(update, context):
    update.message.reply_text("Введите новый текст:")
    # with open("feedback.txt", 'w', encoding='utf-8') as f:
    #     f.write("my first filen")
    #     f.write("This filenn")
    #     f.write("contains three linesn")
    return get_text


def change_text_end(update, context):
    if update.message.text == "/CANCEL":
        update.message.reply_text("Введите любой текст, для вызова меню")
        return ConversationHandler.END
    else:
        with open("feedback.txt", 'w', encoding='utf-8') as f:
            f.write(update.message.text)
        f.close()
        update.message.reply_text("Текст успешно изменен!")
        return ConversationHandler.END


def renewed_sub(update, context):
    update.message.reply_text("Перешлите сообщение человека, у которого хотите продлить подписку",
                              reply_markup=get_cancel_keyboard())
    return sub


def renewed_sub_id(update, context):
    if update.message.text == "/CANCEL":
        update.message.reply_text("Введите любой текст, для вызова меню")
        return ConversationHandler.END
    else:
        context.user_data['sub'] = update.message.forward_from
        # if admin_moder.priority == "admin":
        #     # moder = session.query(Admin).filter(Admin.telegram_id == update.message.forward_from['id']).first()
        #     # session.delete(moder)
        #     # session.commit()
        update.message.reply_text("Введите набор цыфр для продления подписки")
        text_ = "1 - день \n" \
                "2 - месяц \n" \
                "3 - год \n" \
                "4 - навсегда \n" \
                "Первоа цифры - тип множителя. \n" \
                "Второе число - кол-во. \n" \
                "___________________ \n" \
                "Пример: 1230 = 230 дней, 34 = 4 года"
        update.message.reply_text(text=text_)
        # update.message.reply_text("Типо успешно прошло продление подпски!")
        # update.message.reply_text("Успешно!")
        return sub_end


def renewed_sub_end(update, context):
    if update.message.text == "/CANCEL":
        update.message.reply_text("Введите любой текст, для вызова меню")
        return ConversationHandler.END
    code = update.message.text
    type_ = int(code[0])
    counts = int(code[1:])
    info_user = context.user_data['sub']
    session = db_session.create_session()
    user = session.query(User).filter(User.telegram_id == info_user.id).first()
    if type_ == 1:
        user.date_to_payment += counts * 60 * 60 * 24 * 1
    elif type_ == 2:
        user.date_to_payment += counts * 60 * 60 * 24 * 30
    elif type_ == 3:
        user.date_to_payment += counts * 60 * 60 * 24 * 30 * 12
    elif type_ == 4:
        user.date_to_payment += counts * 60 * 60 * 24 * 30 * 12 * 50

    session.commit()
    update.message.reply_text(f"Успешно! Подписка для {user.name} продлина до {user.date_to_payment}")
    return ConversationHandler.END


# 419453249
# 419453249
def take_message(update, context):
    print("update.message", dir(update.message))
    print(update.message.from_user)
    print("forward_from", update.message.forward_from)
    print(update.message.chat_id, group_with_video_id)
    session = db_session.create_session()
    check_user = session.query(Admin).filter(Admin.telegram_id == update.message.chat_id).first()
    session.commit()
    if check_user:
        if check_user.priority == "admin":
            update.message.reply_text(text="Меню админа", reply_markup=get_admin_keyboard())
        elif check_user.priority == "moder":
            update.message.reply_text(text="Меню модератора", reply_markup=get_moder_keyboard())
    else:
        if str(update.message.chat_id) == str(group_with_video_id):
            update.message.reply_text(text=f"Видео ID: {update.message.message_id}")
        else:
            if update.message.text == BUTTON_BACK:
                update.message.reply_text(text="Меню бота", reply_markup=get_main_menu_bot_keyboard())
            elif update.message.text == BUTTON_STARTTRAINING:
                update.message.reply_text(text=STARTTRAINING, reply_markup=get_training())
            elif update.message.text == BUTTON_PAYMENT:
                update.message.reply_text(text=PAYMENT_TEXT, reply_markup=get_PAYMENT_keyboard())
            elif update.message.text in [BUTTON_GW, BUTTON_LW]:
                return start_training(update=update, context=context)
            elif update.message.text in [BUTTON_1P, BUTTON_2P, BUTTON_3P, BUTTON_4P, BUTTON_5P]:
                return make_payment(update=update, context=context, type_pay=update.message.text)
            elif update.message.text == BUTTON_BONUS:
                update.message.reply_text(text=BONUS_TEXT, reply_markup=get_BONUS_keyboard())
            elif update.message.text == BUTTON_FEEDBACK:
                update.message.reply_text(text=get_feedback_text())
            elif update.message.text == BUTTON_USERRESULTS:
                update.message.reply_text(text=USERRESULTS_TEXT, reply_markup=get_user_results())
            elif update.message.text == BUTTON_RESULTS:
                update.message.reply_text(text="Результаты какого вида тренировок,"
                                               " вы хотите посмотреть?", reply_markup=get_user_res_type())
            elif update.message.text in [BUTTON_GET_WEIGHT, BUTTON_LOSE_WEIGHT]:
                return get_res_people(update=update, context=context, type_training=update.message.text)
            elif update.message.text in [BUTTON_NUMBER_OF_REFERRALS, BUTTON_BONUS_PACKAGE, BUTTON_LINK]:
                return make_BONUS(update=update, context=context, type_=update.message.text)
            else:
                session = db_session.create_session()
                if session.query(User).filter(User.telegram_id == update.message.chat_id).first():
                    session.commit()
                    welcome_text = "Меню бота"
                    update.message.reply_text(text=welcome_text, reply_markup=get_main_menu_bot_keyboard())
                else:
                    welcome_text = "Привет! Ты на верном пути и теперь ты точно сможешь достигнуть тела своей мечты!🥇"
                    update.message.reply_text(text=welcome_text, reply_markup=get_base_inline_keyboard())


def cancel(update, context):
    return ConversationHandler.END


def start(update, context):
    session = db_session.create_session()
    check_user = session.query(Admin).filter(Admin.telegram_id == update.message.chat_id).first()
    if check_user:
        context.user_data['admin'] = True
        welcome_text = f"Добро пожаловать, {check_user.name}. Вы {check_user.priority}"
        update.message.reply_text(text=welcome_text)
        session.commit()
        if check_user.priority == "admin":
            update.message.reply_text(text="Меню админа", reply_markup=get_admin_keyboard())
        elif check_user.priority == "moder":
            update.message.reply_text(text="Меню модератора", reply_markup=get_moder_keyboard())
    else:
        context.user_data['admin'] = False
        context.user_data['ref'] = ""
        # session = db_session.create_session()
        if "/start 871qXoi359ref=" in update.message.text:
            id_boss_ref = update.message.text.split("ref=")[-1]
            current_user = session.query(User).filter(User.telegram_id == id_boss_ref).first()
            if current_user and str(update.message.chat_id) not in current_user.referals:
                current_user.referals_count += 1
                current_user.referals += f" {id_boss_ref}"
                current_user.balance += 10
                session.commit()
                context.user_data['ref'] = id_boss_ref
        else:
            if session.query(User).filter(User.telegram_id == update.message.chat_id).first():
                welcome_text = "Меню бота"
                update.message.reply_text(text=welcome_text, reply_markup=get_main_menu_bot_keyboard())
            else:
                welcome_text = "Привет! Ты на верном пути и теперь ты точно сможешь достигнуть тела своей мечты!🥇"
                update.message.reply_text(text=welcome_text, reply_markup=get_base_inline_keyboard())
            session.commit()


def main():
    updater = Updater(TOKEN, use_context=True, request_kwargs=request_)
    dispatcher = updater.dispatcher
    questionnaireANDtraining_selection = ConversationHandler(
        entry_points=[CallbackQueryHandler(key_button_handler, pass_chat_data=True)],
        states={
            OTHER_BODY: [CallbackQueryHandler(answer_to_question_other, pass_chat_data=True)],
            QUESTIONNAIRE_2: [MessageHandler(Filters.text, second_quest, pass_user_data=True)],
            QUESTIONNAIRE_3: [MessageHandler(Filters.text, third_quest, pass_user_data=True)],
            QUESTIONNAIRE_4: [MessageHandler(Filters.text, fourth_quest, pass_user_data=True)],
            QUESTIONNAIRE_5: [MessageHandler(Filters.text, fifth_quest, pass_user_data=True)],
            QUESTIONNAIRE_END: [MessageHandler(Filters.text, end_of_questionnaire, pass_user_data=True)],
        },
        fallbacks=[
            CommandHandler("CANCEL", cancel),

        ],
    )
    add_most_people_handler = ConversationHandler(
        entry_points=[CommandHandler("ADD_MOST_PEOPLE", add_most_people)],
        states={
            get_forward_message: [MessageHandler(Filters.text, add_most_people_end, pass_user_data=True)],
        },
        fallbacks=[
            CommandHandler("CANCEL", cancel),
        ],
    )
    change_balance_handler = ConversationHandler(
        entry_points=[CommandHandler("CHANGE_USER_BALANCE", change_balance)],
        states={
            get_balance_id: [MessageHandler(Filters.text, change_balance_id, pass_user_data=True)],
            get_balance: [MessageHandler(Filters.text, change_balance_end, pass_user_data=True)],
        },
        fallbacks=[
            CommandHandler("CANCEL", cancel),

        ],
    )
    change_text_handler = ConversationHandler(
        entry_points=[CommandHandler("CHANGE_FEEDBACK_TEXT", change_text)],
        states={
            get_text: [MessageHandler(Filters.text, change_text_end, pass_user_data=True)],
        },
        fallbacks=[
            CommandHandler("CANCEL", cancel),

        ],
    )
    delete_handler = ConversationHandler(
        entry_points=[CommandHandler("DELETE_MOST_PEOPLE", delete_user)],
        states={
            delete: [MessageHandler(Filters.all, delete_user_end, pass_user_data=True)],
        },
        fallbacks=[
            CommandHandler("CANCEL", cancel),

        ],
    )
    renewed_subscription = ConversationHandler(
        entry_points=[CommandHandler("RENEWED_SUBSCRIPTION", renewed_sub)],
        states={
            sub: [MessageHandler(Filters.all, renewed_sub_id, pass_user_data=True)],
            sub_end: [MessageHandler(Filters.all, renewed_sub_end, pass_user_data=True)],
        },
        fallbacks=[
            CallbackQueryHandler(key_button_handler, pass_chat_data=True),

        ],
    )
    text_handler = MessageHandler(Filters.all, take_message)

    # Регистрируем обработчик в диспетчере.

    buttons_handler = CallbackQueryHandler(callback=key_button_handler, pass_chat_data=True)
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(questionnaireANDtraining_selection)
    dispatcher.add_handler(add_most_people_handler)
    dispatcher.add_handler(change_text_handler)
    dispatcher.add_handler(delete_handler)
    dispatcher.add_handler(change_balance_handler)
    dispatcher.add_handler(renewed_subscription)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_handler)
    dispatcher.add_handler(buttons_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
