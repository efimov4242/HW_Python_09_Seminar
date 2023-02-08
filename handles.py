from create import dp
from aiogram import types
import random
import model
import view

async def start_game(message: types.Message):
	await model.set_game()
	await view.start_game(message)
	name = message.from_user.first_name
	await model.set_player_name(name)
	first_turn = random.randint(0, 1)
	if first_turn == 1:
		await view.player_take(message)
	else:
		await bot_turn(message)

async def bot_turn(message):
	take = await model.bot_take()
	await model.take_total_count(take)
	name = await model.get_player_name()
	total_count = await model.get_total_count()
	if await model.get_total_count() > 0:
		await view.table_info(message, 'Бот', take, total_count, name)
	if await model.get_total_count() <= 0:
		await view.win(message, 'Бот', take, total_count)
		await model.set_game()



@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
	await message.answer(f'Приветствую тебя {message.from_user.first_name}!\n\nДавай сыграем в игру!\n\nНа столе лежит n-ое количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.\n\nВведите /play, чтобы начать игру.')


@dp.message_handler(commands=['play'])
async def count(message: types.Message):
	count = int(message.text)
	if count >= 28:
		await message.answer(f'Общее количество конфет {str(count)}')
	else:
		await message.answer('Введите число не менее 28')
	p_name = []
	p_name.append("Бот")
	p_name.append(message.from_user.first_name)
	in_game_player = random.randint(0,1)
	await message.answer(f'Первым ходит {p_name[in_game_player]}')


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Пока я ничего не умею, но обязательно нучусь')


@dp.message_handler()
async def mes_all(message: types.Message):
	global total
	if message.text.isdigit():
		total -= int(message.text)
		await message.answer(f'На столе осталось {total} конфет')