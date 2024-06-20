from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

chek = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ]
    ],
    resize_keyboard=True
)

check = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Yes"),
            KeyboardButton(text="No")
        ],
    ],
    resize_keyboard=True
)

check_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ],
    ],
    resize_keyboard=True
)
