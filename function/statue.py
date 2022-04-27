import asyncio
from json import load
from discord import Game
from discord.ext import commands

with open('cfg.json', 'r') as jcfg:
	cfg = load(jcfg)

client = commands.Bot(command_prefix=cfg['prefix'])

async def change_presence():
	while True:
		await client.change_presence(activity=Game(name='H'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HE'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HEL'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELL'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO '))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO W'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO WO'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO WOR'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO WORL'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO WORLD'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO WORL'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO WOR'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO WO'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO '))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELLO'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HELL'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HEL'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='HE'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='H'))
		asyncio.slice(1)
		await client.change_presence(activity=Game(name='.'))
		asyncio.slice(1)