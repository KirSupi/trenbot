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
BUTTON_FEEDBACK = "Обратная связь"
BUTTON_BONUS = "Бонусы(реферальная система)"
BUTTON_PAYMENT = "Оплата подписки на тренировки"
# \

#/
BUTTON_BACK = "Назад⬅️"
#\
# Меню по оплате подписки/
BUTTON_1M = "1 месяц"
BUTTON_3M = "3 месяца"
BUTTON_1Y = "1 год"
# \
# Меню по оплате подписки/
BUTTON_NUMBER_OF_REFERRALS = "Кол-во рефералов"
BUTTON_BONUS_PACKAGE = "Размер бонуса"
BUTTON_LINK = "Получить ссылку"


# \


def get_main_menu_bot_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON_PAYMENT),
            KeyboardButton(BUTTON_BONUS),
            KeyboardButton(BUTTON_FEEDBACK),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def get_PAYMENT_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON_1M),
            KeyboardButton(BUTTON_3M),
            KeyboardButton(BUTTON_1Y),

        ],
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
