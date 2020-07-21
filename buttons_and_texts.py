# coding=utf-8
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

PAYMENT_TEXT = "❗️ВНИМАНИЕ ПРЯМО СЕЙЧАС ДЕЙСТВУЮТ  СКИДКИ❗" \
               "️ Оплачивая подписку вы получаете ежедневные эффективные тренировки, которые" \
               " гарантируют вам быстрый и стабильный результат." \
               " Покупая тарифные планы '💳 90 дней', '💳Безлимит'" \
               " или '💳180 дней' вы так же получите доступ к VIP консультациям," \
               " нутрициолога и личного фитнес тренера, которые будут помогать и отвечать на ваши вопросы 24/7!"

BONUS_TEXT = "Вы можете поделиться в своих соц. сетях нашим" \
             " проектом и получать деньги на баланс, которыми вы сможете оплатить подписку на тренировки!"
FEEDBACK_TEXT = "Остались вопросы? Напишите нашему менеджеру," \
                " он обязательно поможет вам и быстро ответит на все ваши вопросы! @ахуенный манагер"

USERRESULTS_TEXT = "Жми на кнопку и смотри еще больше результатов людей," \
                   " которые воспользовались нашими тренировочными курсами!"

STARTTRAINING = "Самое время начинать тренироваться!" \
                " Жми на кнопку ниже и выбирай нужную тебе тренировку."

VIDEO_TEXT = '❗️Пора начинать добиваться цели, буквально через неделю ты увидишь'
' отличные результаты, смотри видео ниже'
' и забирай первую бесплатную тренировку ПРЯМО СЕЙЧАС❗️'
# CALLBACK_BUTTON_1_MONTH = "CALLBACK_BUTTON_1_MONTH"
# CALLBACK_BUTTON_3_MONTH = "CALLBACK_BUTTON_3_MONTH"
# CALLBACK_BUTTON_1_YEAR = "CALLBACK_BUTTON_1_YEAR"


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
    # CALLBACK_BUTTON_1_MONTH: "1 месяц",
    # CALLBACK_BUTTON_3_MONTH: "3 месяца",
    # CALLBACK_BUTTON_1_YEAR: "1 год",
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
# Главное меню бота/

BUTTON_STARTTRAINING = "Начать тренироваться"
BUTTON_USERRESULTS = "Результаты клиентов"
BUTTON_FEEDBACK = "Обратная связь"
BUTTON_BONUS = "🎁Бонусы"
BUTTON_PAYMENT = "Оплата подписки на тренировки"
# \

# /
BUTTON_BACK = "⬅️Главное меню"
# \
# Меню по оплате подписки/
BUTTON_1P = "💳7 дней - 699р"
BUTTON_2P = "💳30 дней(-15%) - 2.399р"
BUTTON_3P = "💳90 дней(-40%) - 4.999р"
BUTTON_4P = "💳180 дней(-60%) - 9.999р"
BUTTON_5P = "💳Безлимит - 19.999р"
# \
# Меню по оплате подписки/
BUTTON_NUMBER_OF_REFERRALS = "👫Кол-во рефералов"
BUTTON_BONUS_PACKAGE = "💸Баланс"
BUTTON_LINK = "Получить ссылку"
# \
# Меню результаты клиентов/
BUTTON_RESULTS = "✅Результаты клиентов"

BUTTON_GET_WEIGHT = "Накачаться"
BUTTON_LOSE_WEIGHT = "Похудеть"

# \
# Меню "Начать тренироваться"/

BUTTON_GW = "🏋️‍♀️Тренировка на набор мышц"
BUTTON_LW = "🤸Тренировка на похудение"


# \


def get_main_menu_bot_keyboard():
    keyboard = [

        [KeyboardButton(BUTTON_STARTTRAINING),
         KeyboardButton(BUTTON_PAYMENT),
         KeyboardButton(BUTTON_BONUS),
         ],
        [

            KeyboardButton(BUTTON_USERRESULTS),
            KeyboardButton(BUTTON_FEEDBACK),
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def get_PAYMENT_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON_1P), KeyboardButton(BUTTON_2P), ],
        [KeyboardButton(BUTTON_3P), KeyboardButton(BUTTON_4P), ],
        [KeyboardButton(BUTTON_5P), ],

        [KeyboardButton(BUTTON_BACK)],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def get_BONUS_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON_NUMBER_OF_REFERRALS),
            KeyboardButton(BUTTON_BONUS_PACKAGE),
            KeyboardButton(BUTTON_LINK),
        ],
        [KeyboardButton(BUTTON_BACK)],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def get_user_results():
    keyboard = [
        [
            KeyboardButton(BUTTON_RESULTS),
        ],
        [KeyboardButton(BUTTON_BACK)],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def get_user_res_type():
    keyboard = [
        [
            KeyboardButton(BUTTON_GET_WEIGHT), KeyboardButton(BUTTON_LOSE_WEIGHT),
        ],
        [KeyboardButton(BUTTON_BACK)],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def get_training():
    keyboard = [
        [
            KeyboardButton(BUTTON_GW), KeyboardButton(BUTTON_LW),
        ],
        [KeyboardButton(BUTTON_BACK)],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


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


# __________________________________ADMIN&MODERNmode____________________________
get_forward_message, get_text, get_balance, get_balance_id, delete = 1, 2, 3, 4, 5
sub, sub_end = 6, 7
# ____________ADMIN_MODE___________________{
BUTTON_ADD = "/ADD_MOST_PEOPLE"
BUTTON_DELETE = "/DELETE_MOST_PEOPLE"
BUTTON_CHANGE_FEEDBACK_TEXT = "/CHANGE_FEEDBACK_TEXT"
BUTTON_RENEWED_SUBSCRIPTION = "/RENEWED_SUBSCRIPTION"
BUTTON_CHANGE_USER_BALANCE = "/CHANGE_USER_BALANCE"
BUTTON_CANCEL = "/CANCEL"


def get_cancel_keyboard():
    keyboard = [

        [
            KeyboardButton(BUTTON_CANCEL),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def get_feedback_text():
    f = open("feedback.txt", 'r', encoding='utf-8')
    return f.read()


def get_admin_keyboard():
    keyboard = [

        [
            KeyboardButton(BUTTON_ADD),
            KeyboardButton(BUTTON_DELETE),

        ],
        [
            KeyboardButton(BUTTON_RENEWED_SUBSCRIPTION),
            KeyboardButton(BUTTON_CHANGE_USER_BALANCE),
        ],
        [
            KeyboardButton(BUTTON_CHANGE_FEEDBACK_TEXT)
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


# ____________ADMIN_MODE___________________}
# ____________MODER_MODE___________________{
def get_moder_keyboard():
    keyboard = [

        [
            KeyboardButton(BUTTON_CHANGE_FEEDBACK_TEXT),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )

# ____________MODER_MODE___________________}
