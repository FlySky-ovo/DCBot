from core.classes import Cog_Ext
from discord.ext.commands import command, has_permissions
from function.time import now_time

class Purge(Cog_Ext):

	@command
	@has_permissions(administrator=True)
	async def purge(self, ctx, count: int):
		await ctx.channel.purge(limit=count+1)
		await ctx.send(f'Done')
		now_time()
		print('mod.purge')

def setup(client):
	client.add_cog(Purge(client))