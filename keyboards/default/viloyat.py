from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

vil = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Buxoro viloyati"),
            KeyboardButton(text="Bekor qilish 🚫")
        ],
    ],
    resize_keyboard=True
)

vil_eng = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Bukhara region"),
            KeyboardButton(text="Cancel 🚫")
        ],
    ],
    resize_keyboard=True
)

vil_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Бухарская область"),
            KeyboardButton(text="Отменить 🚫")
        ],
    ],
    resize_keyboard=True
)
