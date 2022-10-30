from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
start = ReplyKeyboardMarkup(resize_keyboard=True)
start.add(KeyboardButton('🎲Рандомный пароль'))
start.add(KeyboardButton('ℹ️ FAQ'))