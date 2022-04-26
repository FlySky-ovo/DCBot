from core.classes import Cog_Extension
from discord.ext.commands import command, has_permissions

class Mod(Cog_Extension):

	@command()
	async def say(self, ctx, *, msg):
		await ctx.message.delete()
		await ctx.send(msg)

	@command()
	@has_permissions(administrator=True)
	async def purge(self, ctx, count: int):
		await ctx.channel.purge(limit=count+1)
		await ctx.send(f'Done')

	@command()
	@has_permissions(administrator=True)
	async def check_per(self, ctx):
		if ctx.author.guild_permissions.administrator:
			await ctx.send(f'你有管理員權限，可以操作大部分的指令！')
		else:
			await ctx.send(f'你沒有管理員權限，只能使用安全的指令。')

def setup(client):
	client.add_cog(Mod(client))