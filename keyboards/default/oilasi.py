from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

oil = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Turmush qurgan"),
            KeyboardButton(text="Turmush qurmagan")
        ],
        [
            KeyboardButton(text="Bekor qilish 🚫")
        ]
    ],
    resize_keyboard=True
)