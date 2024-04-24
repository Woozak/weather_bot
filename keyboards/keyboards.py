from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

geo_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Отправить геолокацию', request_location=True)]],
    resize_keyboard=True
)
