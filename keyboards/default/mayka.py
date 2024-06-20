from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mayka = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="XS / 44 / 37"),
            KeyboardButton(text="S / 46 / 38")
        ],
        [
            KeyboardButton(text="M / 48 / 39"),
            KeyboardButton(text="L / 50 / 40")
        ],
        [
            KeyboardButton(text="XL / 52 / 41"),
            KeyboardButton(text="XXL / 54 / 41-42")
        ],
        [
            KeyboardButton(text="XXXL / 56 / 43-44"),
            KeyboardButton(text="4XL / 58 / 45-46")
        ],
        [
            KeyboardButton(text="5XL / 60 / 47-48"),
            KeyboardButton(text="Bekor qilish 🚫")
        ]
    ],
    resize_keyboard=True
)

mayka_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="XS / 44 / 37"),
            KeyboardButton(text="S / 46 / 38")
        ],
        [
            KeyboardButton(text="M / 48 / 39"),
            KeyboardButton(text="L / 50 / 40")
        ],
        [
            KeyboardButton(text="XL / 52 / 41"),
            KeyboardButton(text="XXL / 54 / 41-42")
        ],
        [
            KeyboardButton(text="XXXL / 56 / 43-44"),
            KeyboardButton(text="4XL / 58 / 45-46")
        ],
        [
            KeyboardButton(text="5XL / 60 / 47-48"),
            KeyboardButton(text="Отменить 🚫")
        ]
    ],
    resize_keyboard=True
)

mayka_eng = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="XS / 44 / 37"),
            KeyboardButton(text="S / 46 / 38")
        ],
        [
            KeyboardButton(text="M / 48 / 39"),
            KeyboardButton(text="L / 50 / 40")
        ],
        [
            KeyboardButton(text="XL / 52 / 41"),
            KeyboardButton(text="XXL / 54 / 41-42")
        ],
        [
            KeyboardButton(text="XXXL / 56 / 43-44"),
            KeyboardButton(text="4XL / 58 / 45-46")
        ],
        [
            KeyboardButton(text="5XL / 60 / 47-48"),
            KeyboardButton(text="Cancel 🚫")
        ]
    ],
    resize_keyboard=True
)