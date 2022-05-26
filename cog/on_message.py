from discord.ext.commands import command
from core.classes import Cog_Ext
from function.time import now_time
from discord.ext.commands import Cog as cog

class OnMessage(Cog_Ext):

	@cog.listener()
	async def on_message(self, msg):

		if msg.startswith('幹') or msg.endswith('幹'):
			await msg.channel.send('兇殺小 誰說你可以兇的')

def setup(client):
	client.add_cog(OnMessage(client))