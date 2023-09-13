import discord
from discord.member import flatten_user

import config

intents = discord.Intents.default()
intents.message_content = False

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """Prints the information that the bot is ready."""

    print(f'-------------------- Bot is ready! --------------------')
    print(f'Logged in as {client.user}'.center(55))
    print(f'-------------------------------------------------------')


@client.event
async def on_message(message: discord.Message):
    """Detects a message in the announcements channel."""

    if message.channel.id != config.ANNOUNCEMENTS_CHANNEL_ID:
        return

    if '@everyone' in message.content or '@here' in message.content:
        return

    try:
        await message.delete()
    except discord.HTTPException:
        print(f'Error: Couldn\'t delete a message in {message.channel}: {message.content}')


client.run(config.TOKEN)
