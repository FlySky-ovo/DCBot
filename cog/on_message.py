from discord.ext.commands import command
from core.classes import Cog_Ext
from function.time import now_time
from discord.ext.commands import Cog as cog

class OnMessage(Cog_Ext):

	@cog.listener()
	async def on_message(self, msg):

		if msg.startswith('幹') or msg.endswith('幹'):
			await msg.channel.send('很兇誒...')

		elif msg.startswith('早安') or msg.endswith('早安'):
			await msg.channel.send('早安')

def setup(client):
	client.add_cog(OnMessage(client))