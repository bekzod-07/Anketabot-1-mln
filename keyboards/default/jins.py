from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

jinss = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Erkak"),
            KeyboardButton(text="Ayol"),
        ],
        [
            KeyboardButton(text="Bekor qilish 🚫")
        ]
    ],
    resize_keyboard=True
)

jinss_eng = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Male"),
            KeyboardButton(text="Female"),
        ],
        [
            KeyboardButton(text="Cancel 🚫")
        ]
    ],
    resize_keyboard=True
)

jins_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Мужской"),
            KeyboardButton(text="Женский"),
        ],
        [
            KeyboardButton(text="Отменить 🚫")
        ]
    ],
    resize_keyboard=True
)
