# import tdlib
from telegram import InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler

from data import db_session

db_session.global_init("db/users.sqlite")
TOKEN = "1124731420:AAGQa5H0sNRbumQJI2pqNJmtpct97Hhcgn8"

OTHER_BODY, QUESTIONNAIRE_2, QUESTIONNAIRE_3, QUESTIONNAIRE_4, \
QUESTIONNAIRE_5, QUESTIONNAIRE_END, OTHER_BODY_QUESTION = range(
    7)
CALLBACK_BUTTON_1_MONTH = "CALLBACK_BUTTON_1_MONTH"
CALLBACK_BUTTON_3_MONTH = "CALLBACK_BUTTON_3_MONTH"
CALLBACK_BUTTON_1_YEAR = "CALLBACK_BUTTON_1_YEAR"

CALLBACK_BUTTON_NUMBER_OF_REFERRALS = "CALLBACK_BUTTON_NUMBER_OF_REFERRALS"
CALLBACK_BUTTON_BONUS_PACKAGE = "CALLBACK_BUTTON_BONUS_PACKAGE"
CALLBACK_BUTTON_CANCEL = "CALLBACK_BUTTON_CANCEL"
CALLBACK_BUTTON_PAYMENT = "CALLBACK_BUTTON_PAYMENT"
CALLBACK_BUTTON_BONUS = "CALLBACK_BUTTON_BONUS"
CALLBACK_BUTTON_FEEDBACK = "CALLBACK_BUTTON_FEEDBACK"
CALLBACK_BUTTON_GAIN_WEIGHT = "CALLBACK_BUTTON_GAIN_WEIGHT"
CALLBACK_BUTTON_LOSE_WEIGHT = "CALLBACK_BUTTON_LOSE_WEIGHT"
CALLBACK_BUTTON_I_WANT = "CALLBACK_BUTTON_I_WANT"
CALLBACK_BUTTON_I_DONT_WANT = "CALLBACK_BUTTON_I_DONT_WANT"
CALLBACK_BUTTON_NEXT = "CALLBACK_BUTTON_NEXT"

TITLES = {
    CALLBACK_BUTTON_CANCEL: "Назад ↩",
    CALLBACK_BUTTON_1_MONTH: "1 месяц",
    CALLBACK_BUTTON_3_MONTH: "3 месяца",
    CALLBACK_BUTTON_1_YEAR: "1 год",
    CALLBACK_BUTTON_NUMBER_OF_REFERRALS: "Кол-во рефералов",
    CALLBACK_BUTTON_BONUS_PACKAGE: "Размер бонуса",
    CALLBACK_BUTTON_FEEDBACK: "Обратная связь",
    CALLBACK_BUTTON_BONUS: "Бонусы(реферальная система)",
    CALLBACK_BUTTON_PAYMENT: "Оплата подписки на тренировки",
    CALLBACK_BUTTON_NEXT: "Далее➡️",
    CALLBACK_BUTTON_GAIN_WEIGHT: "🏋️‍Накачаться",
    CALLBACK_BUTTON_LOSE_WEIGHT: "🤸Похудеть",
    CALLBACK_BUTTON_I_WANT: "Да, хочу",
    CALLBACK_BUTTON_I_DONT_WANT: "Нет, не хочу"
}

BONUS = 1
def get_cancel_inline_keyboard():
    keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_CANCEL], callback_data=CALLBACK_BUTTON_CANCEL)]]
    return InlineKeyboardMarkup(keyboard)


def get_FEEDBACK_inline_keyboard():
    keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_CANCEL], callback_data=CALLBACK_BUTTON_CANCEL)]]
    return InlineKeyboardMarkup(keyboard)


def get_PAYMENT_inline_keyboard():
    keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_1_MONTH], callback_data=CALLBACK_BUTTON_1_MONTH), ],
                [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_3_MONTH], callback_data=CALLBACK_BUTTON_3_MONTH), ],
                [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_1_YEAR], callback_data=CALLBACK_BUTTON_1_YEAR), ],
                [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_CANCEL], callback_data=CALLBACK_BUTTON_CANCEL)],
                ]
    return InlineKeyboardMarkup(keyboard)


def get_BONUS_inline_keyboard():
    keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_NUMBER_OF_REFERRALS],
                                      callback_data=CALLBACK_BUTTON_NUMBER_OF_REFERRALS), ],
                [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_BONUS_PACKAGE],
                                      callback_data=CALLBACK_BUTTON_BONUS_PACKAGE), ],
                [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_CANCEL], callback_data=CALLBACK_BUTTON_CANCEL)],
                ]
    return InlineKeyboardMarkup(keyboard)


def get_main_menu_inline_keyboard():
    keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_PAYMENT], callback_data=CALLBACK_BUTTON_PAYMENT),
                 InlineKeyboardButton(TITLES[CALLBACK_BUTTON_BONUS], callback_data=CALLBACK_BUTTON_BONUS),
                 InlineKeyboardButton(TITLES[CALLBACK_BUTTON_FEEDBACK], callback_data=CALLBACK_BUTTON_FEEDBACK),
                 ]
                ]
    return InlineKeyboardMarkup(keyboard)


def get_next_inline_keyboard():
    keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_NEXT], callback_data=CALLBACK_BUTTON_NEXT), ]]
    return InlineKeyboardMarkup(keyboard)


def get_base_inline_keyboard():
    keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_GAIN_WEIGHT], callback_data=CALLBACK_BUTTON_GAIN_WEIGHT),
                 InlineKeyboardButton(TITLES[CALLBACK_BUTTON_LOSE_WEIGHT], callback_data=CALLBACK_BUTTON_LOSE_WEIGHT),
                 ]
                ]
    return InlineKeyboardMarkup(keyboard)


def get_question_other_body_inline_keyboard():
    keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_I_WANT], callback_data=CALLBACK_BUTTON_I_WANT),
                 InlineKeyboardButton(TITLES[CALLBACK_BUTTON_I_DONT_WANT], callback_data=CALLBACK_BUTTON_I_DONT_WANT),
                 ]
                ]
    return InlineKeyboardMarkup(keyboard)


def answer_to_question_other(update, context):
    print("))000")
    query = update.callback_query
    data = query.data
    path_1, path_2 = "", ""
    # if data == CALLBACK_BUTTON_I_WANT:
    #     update.effective_message.reply_text("До")
    #     update.message.reply_photo(open('scale_1200.jpg', 'rb'))
    #     update.effective_message.reply_text("После")
    #     update.message.reply_photo(open('scale_1200.jpg', 'rb'))
    # update.effective_message.reply_text("ФОТИ ДО/ПОСЛЕ")
    if data == CALLBACK_BUTTON_I_DONT_WANT:
        # update.effective_message.reply_text("ФОТИ ДО/ПОСЛЕ")
        update.effective_message.reply_text("Мы все равно покажем результаты,"
                                            " чтобы сильнее вас мотивировать для грядующих тренировок!")
    print(context.user_data['kind of training'])
    if context.user_data['kind of training'] == CALLBACK_BUTTON_GAIN_WEIGHT:
        update.effective_message.reply_text("До")
        update.effective_message.reply_photo(open('p1.jpg', 'rb'))
        update.effective_message.reply_text("После")
        update.effective_message.reply_photo(open('p2.jpg', 'rb'))
    if context.user_data['kind of training'] == CALLBACK_BUTTON_LOSE_WEIGHT:
        update.effective_message.reply_text("До")
        update.effective_message.reply_photo(open('p3.jpg', 'rb'))
        update.effective_message.reply_text("После")
        update.effective_message.reply_photo(open('p4.jpg', 'rb'))
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
    update.effective_message.reply_text(text="⏳Подбираем тренировки....")
    chat_id = update.message.chat_id
    try:
        delay = 2
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
    welcome_text = "Меню бота"
    context.bot.send_message(job.context, text=welcome_text, reply_markup=get_main_menu_inline_keyboard())
    # context.bot.send_message(job.context, text='+видео с предлогом начать первую бесплатную тренировку')
    videos_group = "-368870653"
    main_chat = "419453249"
    # print(update.effective_message.message_id)
    # print(update.effective_message.chat_id)
    print(dir(context.chat_data))
    print(dir(context.user_data))
    print(dir(context.bot), "!@!@@!@")
    print(context.bot.last_name)
    print(context.bot.id)
    # update.effective_message.reply_text(text=update.effective_message.message_id)
    # context.bot.forward_message(context.bot.chat_id, videos_group, 602)
    return ConversationHandler.END


def key_button_handler(update, context):
    # print("!!!!", dir(context.bot))
    # print("???", dir(update.effective_message.chat_id))

    query = update.callback_query
    data = query.data
    if data in [CALLBACK_BUTTON_GAIN_WEIGHT, CALLBACK_BUTTON_LOSE_WEIGHT]:
        context_text = "Ты сделала еще один шаг на встречу телу своей мечты, а это значит," \
                       " что ты на верном пути и совсем скоро получишь желаемый результат🏃‍♀️"
        context.user_data['kind of training'] = data
        update.effective_message.reply_text(text=context_text)
        # context.bot.send_video(chat_id=update.effective_message.chat_id, video=open("takoe.mp4", 'rb'),
        #                        supports_streaming=True)
        videos_group = "-368870653"
        main_chat = "419453249"
        # print(update.effective_message.message_id)
        # print(update.effective_message.chat_id)
        # print(dir(context.chat_data))
        # print(dir(context.user_data))
        # print(dir(context.bot))
        # update.effective_message.reply_text(text=update.effective_message.message_id)
        print("!!!!", update.effective_message.chat_id)
        context.bot.forward_message(update.effective_message.chat_id, videos_group, 611)
        update.effective_message.reply_text("какие-то видео", reply_markup=get_next_inline_keyboard())
    if data == CALLBACK_BUTTON_NEXT:
        # print("!!!!")
        return throw_question_body(update=update, context=context)
        # return OTHER_BODY_QUESTION
    # CALLBACK_BUTTON_FEEDBACK: "Обратная связь",
    # CALLBACK_BUTTON_BONUS: "Бонусы(реферальная система)",
    # CALLBACK_BUTTON_PAYMENT: "Оплата подписки на тренировки",
    if data == CALLBACK_BUTTON_FEEDBACK:
        # update.effective_message.reply_text("Обратная связь, и тут что-то должно быть....", reply_markup=get_cancel_inline_keyboard())
        context.bot.edit_message_text(chat_id=update.effective_message.chat_id,
                                      message_id=update.effective_message.message_id,
                                      text="Обратная связь.......", reply_markup=get_FEEDBACK_inline_keyboard())
    if data == CALLBACK_BUTTON_BONUS:
        context.bot.edit_message_text(chat_id=update.effective_message.chat_id,
                                      message_id=update.effective_message.message_id,
                                      text="Бонусы(реферальная система)", reply_markup=get_BONUS_inline_keyboard())
        # return BONUS
        # update.effective_message.reply_text("Бонусы(реферальная система)", reply_markup=get_BONUS_inline_keyboard())
    if data == CALLBACK_BUTTON_PAYMENT:
        context.bot.edit_message_text(chat_id=update.effective_message.chat_id,
                                      message_id=update.effective_message.message_id,
                                      text="Оплата подписки на тренировки", reply_markup=get_PAYMENT_inline_keyboard())

    if data == CALLBACK_BUTTON_CANCEL:
        context.bot.edit_message_text(chat_id=update.effective_message.chat_id,
                                      message_id=update.effective_message.message_id,
                                      text="Меню бота", reply_markup=get_main_menu_inline_keyboard())
        return ConversationHandler.END

    if data == CALLBACK_BUTTON_BONUS_PACKAGE:
        update.effective_message.reply_text("0 руб.", reply_markup=get_cancel_inline_keyboard())
    if data == CALLBACK_BUTTON_NUMBER_OF_REFERRALS:
        update.effective_message.reply_text("0 шт.", reply_markup=get_cancel_inline_keyboard())
def BONUS_menu(update, context):
    print("QWERTY")
    query = update.callback_query
    data = query.data
    print(data)
    if data == CALLBACK_BUTTON_BONUS_PACKAGE:
        update.effective_message.reply_text("0 руб.", reply_markup=get_cancel_inline_keyboard())
        # context.bot.edit_message_text(chat_id=update.effective_message.chat_id,
        #                               message_id=update.effective_message.message_id,
        #                               text="Меню бота", reply_markup=get_main_menu_inline_keyboard())
    if data == CALLBACK_BUTTON_NUMBER_OF_REFERRALS:
        update.effective_message.reply_text("0 шт.", reply_markup=get_cancel_inline_keyboard())



def throw_question_body(update, context):
    question_text = "Хочешь увидеть результаты людей, которые начали тренировки вместе со мной?"
    update.effective_message.reply_text(text=question_text, reply_markup=get_question_other_body_inline_keyboard())
    return OTHER_BODY


def take_message(update, context):
    # print(dir(update.message))
    # # im = Image.open("scale_1200.jpg")
    # # photo = r'{}\utils\scale_1200.jpg'.format(os.getcwd())
    # # # with open(
    # # #         "scale_1200.jpg", "rb") as file:
    # # #     data = file.read()
    # update.message.reply_photo(open('scale_1200.jpg', 'rb'))
    # videos_group = "-368870653"
    # main_chat = "419453249"
    # print(update.message.message_id)
    # print(update.message.chat_id)
    # print(dir(context.chat_data))
    # print(dir(context.user_data))
    # print(dir(context.bot))
    # update.message.reply_text(text=update.message.message_id)
    # context.bot.forward_message(main_chat, videos_group, update.message.message_id)
    welcome_text = "Меню бота"
    update.message.reply_text(text=welcome_text, reply_markup=get_main_menu_inline_keyboard())


def start(update, context):
    welcome_text = "Привет! Ты на верном пути и теперь ты точно сможешь достигнуть тела своей мечты!🥇"
    update.message.reply_text(text=welcome_text, reply_markup=get_base_inline_keyboard())


def main():
    updater = Updater(TOKEN, use_context=True, request_kwargs={'read_timeout': 1000, 'connect_timeout': 1000323})
    dispatcher = updater.dispatcher
    questionnaireANDtraining_selection = ConversationHandler(
        entry_points=[CallbackQueryHandler(key_button_handler, pass_chat_data=True)],
        states={
            # OTHER_BODY_QUESTION: [MessageHandler(Filters.text, throw_question_body, pass_user_data=True)],
            BONUS: [CallbackQueryHandler(BONUS_menu, pass_chat_data=True)],
            OTHER_BODY: [CallbackQueryHandler(answer_to_question_other, pass_chat_data=True)],
            QUESTIONNAIRE_2: [MessageHandler(Filters.text, second_quest, pass_user_data=True)],
            QUESTIONNAIRE_3: [MessageHandler(Filters.text, third_quest, pass_user_data=True)],
            QUESTIONNAIRE_4: [MessageHandler(Filters.text, fourth_quest, pass_user_data=True)],
            QUESTIONNAIRE_5: [MessageHandler(Filters.text, fifth_quest, pass_user_data=True)],
            QUESTIONNAIRE_END: [MessageHandler(Filters.text, end_of_questionnaire, pass_user_data=True)],

            # FINAL_ADDING_USER: [
            #     MessageHandler(Filters.photo, add_user_final, pass_chat_data=True)],
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
