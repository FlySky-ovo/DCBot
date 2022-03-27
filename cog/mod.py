from core.classes import Cog_Extension
from discord.ext.commands import command

class Mod(Cog_Extension):
	@command()
	async def purge(ctx, count):
		ctx.purge(count)
		await ctx.send(f'Done.')
		print('mod.purge >> done')

def setup(client):
	client.add_cog(Mod(client))