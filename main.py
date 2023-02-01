import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

#To do: add checks for day of the week (not sat/sun), adjust nickname to be in format “<random prefix>.<random postfix>”

@client.event
async def on_message(message):
  t = message.created_at
  hour = t.hour
  channel = message.channel
  print(message.author.id == 263178859971608586)
  if message.author.id == 263178859971608586 and len(
      message.attachments) > 0 and (hour >= 15 and
                                    hour <= 23) and (channel.name == "memes"):
    await message.channel.send("<@263178859971608586> get a job")


keep_alive()
my_secret = os.environ['DISCORD_BOT_SECRET']
client.run(os.environ['DISCORD_BOT_SECRET'])
