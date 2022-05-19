from discord.ext.commands import command, has_permissions
from core.classes import Cog_Ext
from function.time import now_time

class CheckPer(Cog_Ext):

	@command
	async def say(self, ctx, *, msg):
		await ctx.message.delete()
		await ctx.send(msg)
		now_time()
		print('mod.say')

	@command
	@has_permissions(administrator=True)
	async def purge(self, ctx, count: int):
		await ctx.channel.purge(limit=count+1)
		await ctx.send(f'Done')
		now_time()
		print('mod.purge')

	@command
	async def check_per(self, ctx):
		if ctx.author.guild_permissions.administrator:
			await ctx.send(f'你有管理員權限，可以操作大部分的指令！')
		else:
			await ctx.send(f'你沒有管理員權限，只能使用安全的指令。')
		now_time()
		print('mod.check_per')

def setup(client):
	client.add_cog(CheckPer(client))