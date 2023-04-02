from aiogram import Dispatcher, Bot, executor, types
from config import token

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start(message:types.Message):
    await message.answer(f'Здраствуйте {message.from_user.full_name}\nВыберите направление:\n/backend\n/frontend\n/uiux\n/android\n/ios')

@dp.message_handler(commands = ['backend'])
async def back(message:types.Message):
    await message.answer(f'Backend — это внутренняя часть сайта и сервера и т.д\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')

executor.start_polling(dp)