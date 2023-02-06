from aiogram import Bot, Dispatcher, executor, types

bot = Bot('5991142887:AAEJV3_GCwIK8jqVh8lPnnkzi2s0KnD_erM')

dp = Dispatcher(bot)

total = 150

async def on_start(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer('Привет тебе')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Пока я ничего не умею, но обязательно нучусь')

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.text.isdigit():
        total -= int(message.text)
    await message.answer(f'На столе осталось {total} конфет')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)