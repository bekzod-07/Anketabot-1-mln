from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

til = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbek tili 🇺🇿"),
            KeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English language 🏴󠁧󠁢󠁥󠁮󠁧󠁿")
        ],
        [
            KeyboardButton(text="🇷🇺 Русский язык 🇷🇺"),
            KeyboardButton(text="Bekor qilish 🚫")
        ]
    ],
    resize_keyboard=True
)
