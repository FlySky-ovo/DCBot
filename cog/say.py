from discord.ext.commands import command
from core.classes import Cog_Ext
from function.time import now_time

class Say(Cog_Ext):

	@command
	async def say(self, ctx, *, msg):
		await ctx.message.delete()
		await ctx.send(msg)
		now_time()
		print('mod.say')

def setup(client):
	client.add_cog(Say(client))