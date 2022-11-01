from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
start = ReplyKeyboardMarkup(resize_keyboard=True)
start.add(KeyboardButton('🎲Рандомный пароль'))
start.add(KeyboardButton('ℹ️ FAQ'))

password_1_inline = InlineKeyboardMarkup()
psw_1 = InlineKeyboardButton(text='📝Буквы(анг)', callback_data="letters")
psw_2 = InlineKeyboardButton(text='🖊Цифры', callback_data="numbers")
password_1_inline.add(psw_1, psw_2)
psw_3 = InlineKeyboardButton(text='📊Буквы с цифрами', callback_data="letters_with_num")
password_1_inline.add(psw_3)
psw_4 = InlineKeyboardButton(text='🖇Смешанный', callback_data="mixed")
password_1_inline.add(psw_4)