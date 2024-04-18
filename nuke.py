import discord
from discord.ext import commands

import colorama
from colorama import Fore, Style

bot = commands.Bot(command_prefix="?",  intents=discord.Intents.all())



@bot.event
async def on_ready():    
    print('Bot is ready.')


@bot.command(name="spamch")
async def spamch(ctx, name: str, amount: int):
    for i in range(amount):
        print(Fore.CYAN + f"Created Channel {name}")
        await ctx.guild.create_text_channel(name)
        

@bot.command()
async def nuke(ctx):
    # Iterate over all channenels in the guild
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(Fore.CYAN + f"Deleted channel {channel.name}")
        except Exception as e:
            print(f"Error deleting channel {channel.name}: {e}")

    


# Avvia il bot e l'interfaccia sulla shell
async def main():
    await bot.start("paste  ur bot token")
    

# Esegue il loop principale
import asyncio
asyncio.run(main())





