from aiogram import Dispatcher, Bot, types
from aiogram import Router
from main2 import RandomPassGenerator
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import config
import keyboard
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.command import \
    CommandStart, Command
from aiogram.types import Message

def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
available_lenght_sizes = [i for i in range(1,200)]
class PasswordLenght(StatesGroup):
    lenght = State()
router = Router()
bot = Bot(token=config.configuration["bot_token"])
dp = Dispatcher(bot)
@router.message(Command(commands=["lenght"]))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите длину пароля:",
        reply_markup=make_row_keyboard(available_lenght_sizes)
    )
    # Устанавливаем пользователю состояние "выбирает название"
    await state.set_state(PasswordLenght.lenght)

r = RandomPassGenerator(17)
@dp.message_handler(commands=['start'], commands_prefix='/!')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await bot.send_message(message.chat.id, config.configuration["start"], reply_markup=keyboard.start)

@dp.message_handler(content_types=['text'])
async def text_filter(message: types.Message):
    if message.text == "🎲Рандомный пароль":
        await bot.send_message(message.chat.id, "🔑Выбор пароля: ", reply_markup=keyboard.password_1_inline)
@dp.callback_query_handler(text='numbers')
async def numpass(call: types.CallbackQuery):
    await call.message.edit_text(text=r.numbers())
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='letters')
async def numpass(call: types.CallbackQuery):
    await call.message.edit_text(text=r.letters())
    await bot.answer_callback_query(callback_query_id=call.id)

@dp.callback_query_handler(text='mixed')
async def numpass(call: types.CallbackQuery):
    await call.message.edit_text(text=r.mixed())
    await bot.answer_callback_query(callback_query_id=call.id)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)