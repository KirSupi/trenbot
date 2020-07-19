from telegram import InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

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


# def get_cancel_inline_keyboard():
#     keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_CANCEL], callback_data=CALLBACK_BUTTON_CANCEL)]]
#     return InlineKeyboardMarkup(keyboard)


# def get_FEEDBACK_inline_keyboard():
#     keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_CANCEL], callback_data=CALLBACK_BUTTON_CANCEL)]]
#     return InlineKeyboardMarkup(keyboard)


# def get_PAYMENT_inline_keyboard():
#     keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_1_MONTH], callback_data=CALLBACK_BUTTON_1_MONTH), ],
#                 [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_3_MONTH], callback_data=CALLBACK_BUTTON_3_MONTH), ],
#                 [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_1_YEAR], callback_data=CALLBACK_BUTTON_1_YEAR), ],
#                 [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_CANCEL], callback_data=CALLBACK_BUTTON_CANCEL)],
#                 ]
#     return InlineKeyboardMarkup(keyboard)

#
# def get_BONUS_inline_keyboard():
#     keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_NUMBER_OF_REFERRALS],
#                                       callback_data=CALLBACK_BUTTON_NUMBER_OF_REFERRALS), ],
#                 [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_BONUS_PACKAGE],
#                                       callback_data=CALLBACK_BUTTON_BONUS_PACKAGE), ],
#                 [InlineKeyboardButton(TITLES[CALLBACK_BUTTON_CANCEL], callback_data=CALLBACK_BUTTON_CANCEL)],
#                 ]
#     return InlineKeyboardMarkup(keyboard)


# def get_main_menu_inline_keyboard():
#     keyboard = [[InlineKeyboardButton(TITLES[CALLBACK_BUTTON_PAYMENT], callback_data=CALLBACK_BUTTON_PAYMENT),
#                  InlineKeyboardButton(TITLES[CALLBACK_BUTTON_BONUS], callback_data=CALLBACK_BUTTON_BONUS),
#                  InlineKeyboardButton(TITLES[CALLBACK_BUTTON_FEEDBACK], callback_data=CALLBACK_BUTTON_FEEDBACK),
#                  ]
#                 ]
#     return InlineKeyboardMarkup(keyboard)


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
