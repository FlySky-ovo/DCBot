from json import load
from os import getenv, listdir
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
from function.clear_console import clear_console
from function.statue import change_presence
from function.time import now_time

clear_console()

now_time()
print('Starting bot...')

intent = Intents.all()

with open('cfg.json', 'r') as jcfg:
	cfg = load(jcfg)

load_dotenv()

client = commands.Bot(command_prefix=cfg['prefix'])

client.remove_command('help')

@client.event
async def on_ready():
	now_time()
	print('Ready!')
#	change_presence()


@client.command()
async def load(ctx, ext):
	if ctx.author.message.id == '745187705075531778':
		msg = await ctx.send('Loading...')
		client.load_extension(f'cog.{ext}')
		await msg.edit(content='Loaded Sucessful')
		now_time()
		print('load')
	else:
		await ctx.send('請勿操作核心！')

@client.command()
async def reload(ctx, ext):
	if ctx.message.author.id == '745187705075531778':
		msg = await ctx.send('Reloading...')
		client.reload_extension(f'cog.{ext}')
		await msg.edit(content='Reloaded Sucessful')
		now_time()
		print('reload')
	else:
		await ctx.send('請勿操作核心！')

@client.command()
async def unload(ctx, ext):
	if ctx.message.author.id == '745187705075531778':
		msg = await ctx.send('Unloading...')
		client.unload_extension(f'cog.{ext}')
		await msg.edit(content='Unloaded!')
		now_time()
		print('unload')
	else:
		await ctx.send('請勿操作核心！')

for filename in listdir('./cog'):
	if filename.endswith('.py'):
		client.load_extension(f'cog.{filename[:-3]}')

if __name__ == '__main__':
	client.run(getenv('token'))
