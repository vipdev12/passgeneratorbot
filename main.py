from aiogram import Dispatcher, executor, Bot, types
import config
bot = Bot(token=config.configuration["bot_token"])
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'], commands_prefix='/!')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await bot.send_message(message.chat.id, config.configuration["start"])




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)