from json import load
from os import getenv, listdir
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
from function.clear_console import clear_console
from function.time import now_time

clear_console()

now_time()
print('Starting bot...')

intent = Intents.all()

with open('cfg.json', 'r') as jcfg:
	cfg = load(jcfg)

load_dotenv()

client = commands.Bot(command_prefix=cfg['prefix'], intents=intent)

client.remove_command('help')

@client.event
async def on_ready():
	now_time()
	print('>|> Bot is Ready!')

@client.command()
async def load(ctx, ext):
	if ctx.author.id == 745187705075531778:
		msg = await ctx.send('Loading...')
		client.load_extension(f'cog.{ext}')
		await msg.edit(content='Loaded Sucessful')
		now_time()
		print('>|> Load')
	else:
		await ctx.send('請勿操作核心！')

@client.command()
async def reload(ctx, ext):
	if ctx.author.id == 745187705075531778:
		msg = await ctx.send('Reloading...')
		client.reload_extension(f'cog.{ext}')
		await msg.edit(content='Reloaded Sucessful')
		now_time()
		print('>|> Reload')
	else:
		await ctx.send('請勿操作核心！')

@client.command()
async def unload(ctx, ext):
	if ctx.author.id == 745187705075531778:
		msg = await ctx.send('Unloading...')
		client.unload_extension(f'cog.{ext}')
		await msg.edit(content='Unloaded!')
		now_time()
		print('>|> Unload')
	else:
		await ctx.send('請勿操作核心！')

@client.event
async def on_error(ctx, error):
	print(error)
	ctx.send(error)

for filename in listdir('./cog'):
	if filename.endswith('.py'):
		client.load_extension(f'cog.{filename[:-3]}')
		print(f'>|> Loading {filename[:-3]}')

if __name__ == '__main__':
	client.run(getenv('token'))