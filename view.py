from bot import bot

async def start_game(message):
	await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}!\n\nДавай сыграем в игру!\n\nНа столе лежит n-ое количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.\n\nВведите /play, чтобы начать игру.')

async def player_take(message):
	await bot.send_message(message.from_user.id, f'Возьми не более 28 конфет: ')

async def table_info(message, name1, take, total_count, name2):
	await bot.send_message(message.from_user.id, f'{name1} взял {take} конфет, на столе осталось {total_count} конфет. Ход {name2}')
