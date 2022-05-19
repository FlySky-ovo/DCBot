from core.classes import Cog_Ext
from discord import Embed
from discord.ext.commands import command
from function.time import now_time

class Ping(Cog_Ext):

	@command(
		name='ping',
		description='查看機器人延遲',
		guild_ids=[894926051254362133]
	)

	async def ping(self, ctx):
		await ctx.send(f'{round(self.client.latency*1000)} ms')
		now_time()
		print('>|> Ping')

def setup(client):
	client.add_cog(Ping(client))
