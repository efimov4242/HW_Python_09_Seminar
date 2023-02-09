from aiogram.utils import executor
import handlers
from bot import dp


async def on_start(_):
    print('Бот запущен')


handlers.register_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_start)
