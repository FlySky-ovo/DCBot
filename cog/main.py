from discord import Embed
from discord.ext.commands import command
from core.classes import Cog_Extension

class Main(Cog_Extension):

	@command()
	async def ping(self, ctx):
		await ctx.send(f'{round(self.client.latency*1000)} ms')

	@command()
	async def help(self, ctx):
		emb = Embed(title = '幫助區 // 飛翔小助手')
		emb.add_field(name='prefix `^`', value='前綴', inline=True)
		emb.add_field(name='◁▶——————————機器人 // Bot ——————————◀▷', value='> 關於機器人的一些資訊。', inline=False)
		emb.add_field(name='help', value='> 叫出這個沒啥用的幫助區', inline=True)
		await ctx.send(embed = emb)

def setup(client):
	client.add_cog(Main(client))