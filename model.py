import random


game = False
player_name = ''
total_count = 150

async def set_game():
	global game
	global player_name
	global total_count
	if game == False:
		game == True
	else:
		player_name = ''
		total_count = 150
		game = False

async def set_player_name(name):
	global player_name
	player_name = name

async def bot_take():
	global total_count
	take = total_count % 29 if total_count % 29 != 0 else random.randint(1, 28)
	return take

async def set_total_count(take):
	global total_count
	total_count -= take

async def get_player_name():
	global player_name
	return player_name

async def get_total_count():
	global total_count
	return total_count

async def get_game():
	global game
	return game
