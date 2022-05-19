from discord.ext.commands import command, has_permissions
from core.classes import Cog_Ext
from function.time import now_time

class CheckPer(Cog_Ext):

	@command(
		name='check_per',
		description='檢查是否有管理員權限',
		guild_ids=[894926051254362133]
	)

	async def check_per(self, ctx):

		if ctx.author.guild_permissions.administrator:
			await ctx.send(f'你有管理員權限，可以操作大部分的指令！')

		else:
			await ctx.send(f'你沒有管理員權限，只能使用安全的指令。')

		now_time()
		print('mod.check_per')

def setup(client):
	client.add_cog(CheckPer(client))