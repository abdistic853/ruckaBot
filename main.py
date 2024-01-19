import asyncio
import random

import discord
from discord import Embed
from discord.ext import commands


from keep_alive import keep_alive
keep_alive()


snipe_author = {}
snipe_msg = {}
snipe_reply = {}
snipe_time = {}
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

snipe_message_content = None
snipe_message_author = None

@bot.event
async def on_message_delete(message):
  global snipe_message_content
  global snipe_message_author
  snipe_message_content = message.content
  snipe_message_author = message.author.name
  await asyncio.sleep(60)
  snipe_message_author = None
  snipe_message_content = None
@bot.command()
async def snipe(message):
  if snipe_message_content is None:
    await message.channel.send("cant snipe")
  else:
    embed = discord.Embed(color=discord.Color.random(), description=f"{snipe_message_content}")
    embed.set_footer(text=f"Requested by {message.author.name}#{message.author.discriminator}")
    embed.set_author(name=f"Sniped the message deleted by {snipe_message_author}")
    await message.channel.send(embed=embed)
    await message.message.delete()
@bot.command(name='delete', brief='Deletes a specified number of messages from the current channel')

async def delete(ctx, amount: int):
  # Delete the specified number of messages
  deleted = await ctx.channel.purge(limit=amount)
  if len(deleted) == 0:
    # If no messages were deleted, create an embed message with a custom color and text
    embed = discord.Embed(title='Purge complete', color=0xFFFF00)
    embed.description = 'No messages were deleted'
    # Set the user's profile picture as the thumbnail of the embed
    embed.set_thumbnail(url=ctx.author.avatar.url)
    # Send the embed message
    await ctx.send(embed=embed)
  else:
    # Create an embed message with a custom color and text
    embed = discord.Embed(title='Purge complete', color=0xFFFF00)
    if len(deleted) == 1:
      # If only one message was deleted, use singular text
      embed.description = '1 message was deleted'
    else:
      # If more than one message was deleted, use plural text
      embed.description = f'{len(deleted)} messages were deleted'
    # Set the user's profile picture as the thumbnail of the embed
    embed.set_thumbnail(url=ctx.author.avatar.url)
    # Send the embed message
    await ctx.send(embed=embed)
@bot.command()
async def rucka(ctx):
    await ctx.send('I am rucka rucka ali I can say whatever I want')
  
@bot.command()
async def say(ctx, *, msg):
  await ctx.send(msg)
  await ctx.message.delete()
isis = r"https://watchpeopledie.tv/h/isis"
isisname = ["sounding you"]
@bot.command()
async def echo(ctx, *, msg):
  await ctx.send(msg)
  await ctx.message.delete()
class ActionGifs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rag(self, ctx: commands.Context,):
        embed = discord.Embed(
            colour=discord.Colour(0xCE3011),
            description=f"{ctx.author.mention} {(random.choice(isisname))}"

        )
        embed.set_image(url=(random.choice(isis)))

        await ctx.send(embed=embed)



bot.run('MTE5NzU2NzU4OTQzMDM0OTkwNg.GnGF6f.lH2Jt3lrO_I4g4c2mPwTBcRQZ8_0lb-n_FxoDk')