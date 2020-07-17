from buttons_and_texts import *
from bot_configuration import *
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from data import db_session
from data.users import User
from data.payments import Payment

db_session.global_init("db/users.sqlite")

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
    context.bot.send_message(job.context, text='❗️Пора начинать добиваться цели, буквально через неделю ты увидишь'
                                               ' отличные результаты, смотри видео ниже'
                                               ' и забирай первую бесплатную тренировку ПРЯМО СЕЙЧАС❗️')
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


def take_message(update, context):
    if update.message.text == BUTTON_PAYMENT:
        update.message.reply_text(text="Оплата подписки на тренировки", reply_markup=get_PAYMENT_keyboard())
    elif update.message.text == BUTTON_BONUS:
        update.message.reply_text(text="Бонусы(реферальная система)", reply_markup=get_BONUS_keyboard())
    elif update.message.text == BUTTON_FEEDBACK:
        update.message.reply_text(text="О себе", reply_markup=get_main_menu_bot_keyboard())
    elif update.message.text == BUTTON_NUMBER_OF_REFERRALS:
        session = db_session.create_session()
        current_user = session.query(User).filter(User.telegram_id == update.message.chat_id).first()
        update.message.reply_text(text=f"{current_user.referals_count}шт.", reply_markup=get_main_menu_bot_keyboard())
        session.commit()
    elif update.message.text == BUTTON_BONUS_PACKAGE:
        session = db_session.create_session()
        current_user = session.query(User).filter(User.telegram_id == update.message.chat_id).first()
        update.message.reply_text(text=f"{current_user.balance}руб.", reply_markup=get_main_menu_bot_keyboard())
        session.commit()
    elif update.message.text == BUTTON_LINK:
        update.message.reply_text(
            text=f"Ссылка:http://t.me/trenirovki_test228bot?start=871qXoi359ref={update.message.chat_id} \n"
                 f"Отправив ее друзьям, вы получите бонусные 10р!",
            reply_markup=get_main_menu_bot_keyboard())
    else:
        session = db_session.create_session()
        if session.query(User).filter(User.telegram_id == update.message.chat_id).first():
            session.commit()
            welcome_text = "Меню бота"
            update.message.reply_text(text=welcome_text, reply_markup=get_main_menu_bot_keyboard())
        else:
            welcome_text = "Привет! Ты на верном пути и теперь ты точно сможешь достигнуть тела своей мечты!🥇"
            update.message.reply_text(text=welcome_text, reply_markup=get_base_inline_keyboard())


def start(update, context):
    context.user_data['ref'] = ""
    if "/start 871qXoi359ref=" in update.message.text:
        session = db_session.create_session()
        id_boss_ref = update.message.text.split("ref=")[-1]
        current_user = session.query(User).filter(User.telegram_id == id_boss_ref).first()
        if current_user and str(update.message.chat_id) not in current_user.referals:
            current_user.referals_count += 1
            current_user.referals += f" {id_boss_ref}"
            current_user.balance += 10
            session.commit()
            context.user_data['ref'] = id_boss_ref
    welcome_text = "Привет! Ты на верном пути и теперь ты точно сможешь достигнуть тела своей мечты!🥇"
    update.message.reply_text(text=welcome_text, reply_markup=get_base_inline_keyboard())


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
            CallbackQueryHandler(key_button_handler, pass_chat_data=True),

        ],
    )
    text_handler = MessageHandler(Filters.all, take_message)

    # Регистрируем обработчик в диспетчере.

    buttons_handler = CallbackQueryHandler(callback=key_button_handler, pass_chat_data=True)
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(questionnaireANDtraining_selection)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_handler)
    dispatcher.add_handler(buttons_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
