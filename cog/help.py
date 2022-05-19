from core.classes import Cog_Ext
from discord import Embed
from discord.ext.commands import command
from function.time import now_time

class Help(Cog_Ext):

	@command(
		name='help',
		description='叫出沒啥用的幫助區',
		guild_ids=[894926051254362133]
	)

	async def help(self, ctx):
		emb = Embed(title = '幫助區　//　飛翔小助手')
		emb.add_field(name='prefix `^`', value='> 前綴', inline=False)

		emb.add_field(name='————　C　————', value='*`指令排序用`*', inline=False)
		emb.add_field(name='check_per', value='> 檢查是否有管理員權限', inline=True)

		emb.add_field(name='————　P　————', value='*`指令排序用`*', inline=False)
		emb.add_field(name='ping', value='> 查看機器人延遲', inline=True)
		emb.add_field(name='purge <count>', value='> 清除指定數量的訊息\n> **`需求：管理員`**', inline=True)

		emb.add_field(name='————　H　————', value='*`指令排序用`*', inline=False)
		emb.add_field(name='help', value='> 叫出沒啥用的幫助區', inline=True)

		emb.add_field(name='————　S　————', value='*`指令排序用`*', inline=False)
		emb.add_field(name='say', value='> 請<@946421952619360317>幫忙你說出這句話', inline=True)

		await ctx.send(embed = emb)
		now_time()
		print('main.help')

def setup(client):
	client.add_cog(Help(client))
