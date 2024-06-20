from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

talim_shakli = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kunduzgi"),
            KeyboardButton(text="Sirtqi")
        ],
        [
            KeyboardButton(text="O'qimayman")
        ],
        [
            KeyboardButton(text="Bekor qilish 🚫")
        ]
    ],
    resize_keyboard=True
)

talim_shakli_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ежедневный"),
            KeyboardButton(text="Дистанционный")
        ],
        [
            KeyboardButton(text="I do not study")
        ],
        [
            KeyboardButton(text="Отменить 🚫")
        ]
    ],
    resize_keyboard=True
)

talim_shakli_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Daily"),
            KeyboardButton(text="Remote")
        ],
        [
            KeyboardButton(text="Я не учусь")
        ],
        [
            KeyboardButton(text="Cancel 🚫")
        ]
    ],
    resize_keyboard=True
)
