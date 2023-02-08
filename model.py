import random


game = False
player_name = ''
total = 2023

async def set_game():
	global game
	global player_name
	global total
	if game == False:
		game == True
	else:
		player_name = ''
		total = 2023
		game = False

async def set_player_name(name):
	global player_name
	player_name = name

async def bot_take():
	global total
	take = total % 29 if total % 29 != 0 else random.randint(1, 28)
	return take

async def take_total_count(take):
	global total
	total -= take

async def get_player_name():
	global player_name
	return player_name

async def get_total_count():
	global total_count
	return total_count
