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
	await model.set_total_count(take)
	name = await model.get_player_name()
	total_count = await model.get_total_count()
	if await model.get_total_count() > 0:
		await view.table_info(message, 'Бот', take, total_count, name)
	if await model.get_total_count() <= 0:
		await view.win(message, 'Бот', take, total_count)
		await model.set_game()


async def player_turn(message: types.Message):
	game = await model.get_game()
	if game:
		if message.text == '/start':
			return
		else:
			take = int(message.text)
		if (take <= 28) and (take > 0):
			await model.set_total_count(take)
		else:
			await view.wrong_take(message)
		name = await model.get_player_name()
		total_count = await model.get_total_count()
		if await model.get_total_count() > 0:
			await view.table_info(message, name, take, total_count, "Бот")
		if await model.get_total_count() <= 0:
			await view.win(message, name, take, total_count)
			await model.set_game()
	await bot_turn(message)