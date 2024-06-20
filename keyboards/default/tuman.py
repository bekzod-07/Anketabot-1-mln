from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tum = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Shofirkon tumani"),
            KeyboardButton(text="Romitan tumani")
        ],
        [
            KeyboardButton(text="Bekor qilish 🚫")
        ]
    ],
    resize_keyboard=True
)

tum_eng = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Shafirkan district"),
            KeyboardButton(text="Romitan district")
        ],
        [
            KeyboardButton(text="Cancel 🚫")
        ]
    ],
    resize_keyboard=True
)

tum_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Шафирканский район"),
            KeyboardButton(text="Ромитанский район")
        ],
        [
            KeyboardButton(text="Отменить 🚫")
        ]
    ],
    resize_keyboard=True
)
