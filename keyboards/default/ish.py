from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ish_uz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Sotuvchi"),
            KeyboardButton(text="Qoʻriqlash xizmati")
        ],
        [
            KeyboardButton(text="Kassir"),
            KeyboardButton(text="Haydovchi")
        ],
        [
            KeyboardButton(text="Novoy"),
            KeyboardButton(text="Operator")
        ],
        [
            KeyboardButton(text="Bekor qilish 🚫")
        ]
    ],
    resize_keyboard=True
)

ish_eng = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Seller"),
            KeyboardButton(text="Security Service")
        ],
        [
            KeyboardButton(text="Cashier"),
            KeyboardButton(text="Driver")
        ],
        [
            KeyboardButton(text="Baker"),
            KeyboardButton(text="Operator")
        ],
        [
            KeyboardButton(text="Cancel 🚫")
        ]
    ],
    resize_keyboard=True
)

ish_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Продавец"),
            KeyboardButton(text="Охранная служба")
        ],
        [
            KeyboardButton(text="Кассир"),
            KeyboardButton(text="Водитель")
        ],
        [
            KeyboardButton(text="Пекарь"),
            KeyboardButton(text="Оператор")
        ],
        [
            KeyboardButton(text="Отменить 🚫")
        ]
    ],
    resize_keyboard=True
)
