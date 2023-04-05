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
    
@dp.message_handler(commands = ['frontend'])
async def back(message:types.Message):
    await message.answer(f'Fronted — это внешняя часть сайта и сервера и т.д\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')
    
@dp.message_handler(commands = ['uiux'])
async def back(message:types.Message):
    await message.answer(f'UIUX — это дизайн сайта и сервера и т.д\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')
    
@dp.message_handler(commands = ['android'])
async def back(message:types.Message):
    await message.answer(f'Android — это создание приложения для устройств на операционной системе Android\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')
    
@dp.message_handler(commands = ['ios'])
async def back(message:types.Message):
    await message.answer(f'IOS — это это создание приложения для устройств на операционной системе IOS\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')

executor.start_polling(dp)