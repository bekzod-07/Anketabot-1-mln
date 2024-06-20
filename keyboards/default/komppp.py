from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

komp = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ],
        [
            KeyboardButton(text="Bekor qilish 🚫")
        ]
    ],
    resize_keyboard=True
)

komp_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ],
        [
            KeyboardButton(text="Отменить 🚫")
        ]
    ],
    resize_keyboard=True
)

komp_eng = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Yes"),
            KeyboardButton(text="No")
        ],
        [
            KeyboardButton(text="Cancel 🚫")
        ]
    ],
    resize_keyboard=True
)