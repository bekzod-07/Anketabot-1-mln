from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mall = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Oily"),
            KeyboardButton(text="Magistratura")
        ],
        [
            KeyboardButton(text="Talaba"),
            KeyboardButton(text="O'rta maxsus")
        ],
        [
            KeyboardButton(text="O'rta"),
            KeyboardButton(text="Bekor qilish 🚫")
        ],
    ],
    resize_keyboard=True
)

mall_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Высшее образование"),
            KeyboardButton(text="Магистратура")
        ],
        [
            KeyboardButton(text="Студент"),
            KeyboardButton(text="Среднее специальное")
        ],
        [
            KeyboardButton(text="Среднее"),
            KeyboardButton(text="Отменить 🚫")
        ],
    ],
    resize_keyboard=True
)