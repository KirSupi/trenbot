from buttons_and_texts import *
from bot_configuration import *
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from data import db_session
from data.users import User
import time
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


def make_payment(update, context, type_pay):
    update.message.reply_text(text=f"Вы произвели оплату на {type_pay}")


def start_training(update, context):
    session = db_session.create_session()
    current_user = session.query(User).filter(User.telegram_id == update.message.chat_id).first()
    if current_user.date_to_payment > int(time.time()):
        update.message.reply_text("Кнопки с видео")
    else:

        update.message.reply_text("У вас не оплачена подписка !")
        text_context = "❗️ВНИМАНИЕ ПРЯМО СЕЙЧАС ДЕЙСТВУЮТ  СКИДКИ❗️ Оплачивая подписку вы получаете ежедневные эффективные тренировки, которые" \
                       " гарантируют вам быстрый и стабильный результат." \
                       " Покупая тарифные планы '💳 90 дней', '💳Безлимит'" \
                       " или '💳180 дней' вы так же получите доступ к VIP консультациям," \
                       " нутрициолога и личного фитнес тренера, которые будут помогать и отвечать на ваши вопросы 24/7!"
        update.message.reply_text(text=text_context, reply_markup=get_PAYMENT_keyboard())


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


def take_message(update, context):
    print(update.message.chat_id, group_with_video_id)
    if str(update.message.chat_id) == str(group_with_video_id):
        print("!!!!")
        update.message.reply_text(text=f"Видео ID: {update.message.message_id}")
    else:
        print(",,,,,")
        if update.message.text == BUTTON_BACK:
            update.message.reply_text(text="Меню бота", reply_markup=get_main_menu_bot_keyboard())
        elif update.message.text == BUTTON_STARTTRAINING:
            text_context = "Самое время начинать тренироваться!" \
                           " Жми на кнопку ниже и выбирай нужную тебе тренировку."
            update.message.reply_text(text=text_context, reply_markup=get_training())
        #      return start_training(update=update, context=context)
        elif update.message.text == BUTTON_PAYMENT:
            text_context = "❗️ВНИМАНИЕ ПРЯМО СЕЙЧАС ДЕЙСТВУЮТ  СКИДКИ❗️ Оплачивая подписку вы получаете ежедневные эффективные тренировки, которые" \
                           " гарантируют вам быстрый и стабильный результат." \
                           " Покупая тарифные планы '💳 90 дней', '💳Безлимит'" \
                           " или '💳180 дней' вы так же получите доступ к VIP консультациям," \
                           " нутрициолога и личного фитнес тренера, которые будут помогать и отвечать на ваши вопросы 24/7!"
            update.message.reply_text(text=text_context, reply_markup=get_PAYMENT_keyboard())
        elif update.message.text in [BUTTON_GW, BUTTON_LW]:
            return start_training(update=update, context=context)
        elif update.message.text in [BUTTON_1P, BUTTON_2P, BUTTON_3P, BUTTON_4P, BUTTON_5P]:
            return make_payment(update=update, context=context, type_pay=update.message.text)
        elif update.message.text == BUTTON_BONUS:
            text_current = "Вы можете поделиться в своих соц. сетях нашим" \
                           " проектом и получать деньги на баланс, которыми вы сможете оплатить подписку на тренировки!"
            update.message.reply_text(text=text_current, reply_markup=get_BONUS_keyboard())
        elif update.message.text == BUTTON_FEEDBACK:
            text_context = "Остались вопросы? Напишите нашему менеджеру," \
                           " он обязательно поможет вам и быстро ответит на все ваши вопросы! @ахуенный манагер"
            update.message.reply_text(text=text_context)
        elif update.message.text == BUTTON_USERRESULTS:
            text_context = "Жми на кнопку и смотри еще больше результатов людей," \
                           " которые воспользовались нашими тренировочными курсами!"
            update.message.reply_text(text=text_context, reply_markup=get_user_results())
        elif update.message.text == BUTTON_RESULTS:
            update.message.reply_text(text="Результаты какого вида тренировок,"
                                           " вы хотите посмотреть?", reply_markup=get_user_res_type())
        elif update.message.text in [BUTTON_GET_WEIGHT, BUTTON_LOSE_WEIGHT]:
            get_res_people(update=update, context=context, type_training=update.message.text)
        elif update.message.text == BUTTON_NUMBER_OF_REFERRALS:
            session = db_session.create_session()
            current_user = session.query(User).filter(User.telegram_id == update.message.chat_id).first()
            update.message.reply_text(text=f"{current_user.referals_count}шт.")
            session.commit()
        elif update.message.text == BUTTON_BONUS_PACKAGE:
            session = db_session.create_session()
            current_user = session.query(User).filter(User.telegram_id == update.message.chat_id).first()
            update.message.reply_text(text=f"{current_user.balance}руб.")
            session.commit()
        elif update.message.text == BUTTON_LINK:
            update.message.reply_text(
                text=f"Ссылка:http://t.me/trenirovki_test228bot?start=871qXoi359ref={update.message.chat_id} \n"
                     f"Отправив ее друзьям, вы получите бонусные 10р!")
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
    session = db_session.create_session()
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
