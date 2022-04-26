from discord import Embed
from discord.ext.commands import command
from core.classes import Cog_Extension
from function.time import now_time

class Main(Cog_Extension):

	@command()
	async def ping(self, ctx):
		await ctx.send(f'{round(self.client.latency*1000)} ms')

	@command()
	async def help(self, ctx):
		emb = Embed(title = '幫助區　//　飛翔小助手')
		emb.add_field(name='prefix `^`', value='> 前綴', inline=True)
		emb.add_field(name='help', value='> 叫出這個沒啥用的幫助區', inline=True)
		emb.add_field(name='ping', value='> 查看機器人延遲', inline=True)
		emb.add_field(name='purge <count>', value='> 清除指定數量的訊息\n> **`需求：管理員`**', inline=True)
		emb.add_field(name='check_per', value='> 檢查是否有管理員權限', inline=True)
		await ctx.send(embed = emb)
		now_time()
		print('main.help')

def setup(client):
	client.add_cog(Main(client))