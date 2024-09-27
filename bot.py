# bot.py
import discord
from discord.ext import commands

TOKEN = 'DEIN_DISCORD_BOT_TOKEN'

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user.name}')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Starte den Bot
bot.run(TOKEN)
