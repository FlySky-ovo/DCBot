from core.classes import Cog_Ext
from discord.ext.commands import command, has_permissions
from function.time import now_time

class Purge(Cog_Ext):

	@command(
		name='purge',
		description='清除指定數量的訊息',
		guild_ids=[894926051254362133]
	)

	async def purge(self, ctx, count: int):

		if ctx.author.guild_permissions.administrator:
			await ctx.channel.purge(limit = count + 1)
			await ctx.send(f'Done')
			now_time()
			print('>|> Purge\n>|>Admin')

		else:
			await ctx.send(f'你沒有權限')
			now_time()
			print('>|> Purge\n>|>Normal')

def setup(client):
	client.add_cog(Purge(client))