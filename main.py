print('Starting bot...')
from json import load
from os import listdir, getenv
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
from clear_console import clear_console

intent = Intents.all()

with open('cfg.json', 'r') as jcfg:
	cfg = load(jcfg)

load_dotenv()

client = commands.Bot(command_prefix=cfg['prefix'])

client.remove_command('help')

@client.event
async def on_ready():
	clear_console()
	print('Ready!')

@client.command()
async def load(ctx, ext):
	msg = await ctx.send('Loading...')
	client.load_extension(f'cog.{ext}')
	await msg.edit(content='Loaded Sucessful')

@client.command()
async def reload(ctx, ext):
	msg = await ctx.send('Reloading...')
	client.reload_extension(f'cog.{ext}')
	await msg.edit(content='Reloaded Sucessful')

@client.command()
async def unload(ctx, ext):
	msg = await ctx.send('Unloading...')
	client.unload_extension(f'cog.{ext}')
	await msg.edit(content='Unloaded!')

for filename in listdir('./cog'):
	if filename.endswith('.py'):
		client.load_extension(f'cog.{filename[:-3]}')

if __name__ == '__main__':
	client.run(getenv('token'))