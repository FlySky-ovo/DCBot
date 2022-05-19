from discord.ext.commands import command
from core.classes import Cog_Ext
from function.time import now_time

class Say(Cog_Ext):

	@command(
		name='say',
		description='請<@946421952619360317>幫忙你說出這句話',
		guild_ids=[894926051254362133]
	)

	async def say(self, ctx, *, msg):
		await ctx.message.delete()
		await ctx.send(msg)
		now_time()
		print('mod.say')

def setup(client):
	client.add_cog(Say(client))