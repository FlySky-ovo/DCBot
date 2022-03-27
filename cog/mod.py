from core.classes import Cog_Extension
from discord.ext.commands import command

class Mod(Cog_Extension):

	@command()
	async def say(self, ctx, *, msg):
		await ctx.message.delete()
		await ctx.send(msg)

	@command()
	async def purge(self, ctx, count: int):
		await ctx.channel.purge(limit=count+1)
		await ctx.send(f'Done')

def setup(client):
	client.add_cog(Mod(client))