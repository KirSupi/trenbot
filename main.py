import os

from telegram import InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from PIL import Image

TOKEN = "1124731420:AAGQa5H0sNRbumQJI2pqNJmtpct97Hhcgn8"

OTHER_BODY, QUESTIONNAIRE_2, QUESTIONNAIRE_3, QUESTIONNAIRE_4, \
QUESTIONNAIRE_5, QUESTIONNAIRE_END, OTHER_BODY_QUESTION = range(
    7)

CALLBACK_BUTTON_GAIN_WEIGHT = "CALLBACK_BUTTON_GAIN_WEIGHT"
CALLBACK_BUTTON_LOSE_WEIGHT = "CALLBACK_BUTTON_LOSE_WEIGHT"
CALLBACK_BUTTON_I_WANT = "CALLBACK_BUTTON_I_WANT"
CALLBACK_BUTTON_I_DONT_WANT = "CALLBACK_BUTTON_I_DONT_WANT"
CALLBACK_BUTTON_NEXT = "CALLBACK_BUTTON_NEXT"

TITLES = {
    CALLBACK_BUTTON_NEXT: "Далее➡️",
    CALLBACK_BUTTON_GAIN_WEIGHT: "🏋️‍Накачаться",
    CALLBACK_BUTTON_LOSE_WEIGHT: "🤸Похудеть",
    CALLBACK_BUTTON_I_WANT: "Да, хочу",
    CALLBACK_BUTTON_I_DONT_WANT: "Нет, не хочу"
}


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


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='✅Оптимальный курс тренировок подобран!✅')
    context.bot.send_message(job.context, text='❗️Пора начинать добиваться цели, буквально через неделю ты увидишь'
                                               ' отличные результаты, смотри видео ниже'
                                               ' и забирай первую бесплатную тренировку ПРЯМО СЕЙЧАС❗️')
    context.bot.send_message(job.context, text='+видео с предлогом начать первую бесплатную тренировку')


def key_button_handler(update, context):
    print("!!!!", dir(context.bot))
    print("???", dir(update.effective_message.chat_id))

    query = update.callback_query
    data = query.data
    if data in [CALLBACK_BUTTON_GAIN_WEIGHT, CALLBACK_BUTTON_LOSE_WEIGHT]:
        context_text = "Ты сделала еще один шаг на встречу телу своей мечты, а это значит," \
                       " что ты на верном пути и совсем скоро получишь желаемый результат🏃‍♀️"
        context.user_data['kind of training'] = data
        update.effective_message.reply_text(text=context_text)
        context.bot.send_video(chat_id=update.effective_message.chat_id, video=open("takoe.mp4", 'rb'),
                               supports_streaming=True)
        update.effective_message.reply_text("какие-то видео", reply_markup=get_next_inline_keyboard())
    if data == CALLBACK_BUTTON_NEXT:
        print("!!!!")
        return throw_question_body(update=update, context=context)
        # return OTHER_BODY_QUESTION


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
    welcome_text = "Привет! Ты на верном пути и теперь ты точно сможешь достигнуть тела своей мечты!🥇"
    update.message.reply_text(text=welcome_text, reply_markup=get_base_inline_keyboard())


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
    text_handler = MessageHandler(Filters.text, take_message)

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
