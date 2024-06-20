from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yoq = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Yo'q"),
            KeyboardButton(text="Bekor qilish 🚫")
        ],
    ],
    resize_keyboard=True
)

yoq_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Нет"),
            KeyboardButton(text="Отменить 🚫")
        ],
    ],
    resize_keyboard=True
)

yoq_eng = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="No"),
            KeyboardButton(text="Cancel 🚫")
        ],
    ],
    resize_keyboard=True
)
