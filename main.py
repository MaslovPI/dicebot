# import argparse
import os
import discord

from dotenv import load_dotenv
from functions.roll import roll_multiple
from discord.ext import commands


def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        raise ValueError("Discord token is not provided")
    intents = discord.Intents()
    intents.message_content = True

    bot = commands.Bot(command_prefix="/", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} has connected to Discord!")

    bot.run(str(TOKEN))


def roll_dice(dice_to_roll):
    dice_info = dice_to_roll.split("d")
    if not len(dice_info) == 2:
        raise ValueError("Incorrect dice info")

    number = int(dice_info[0]) if dice_info[0] else 1
    dimensions = int(dice_info[1])
    result = roll_multiple(number, dimensions)
    return f"{dice_to_roll} roll result: {result.describe()}"


if __name__ == "__main__":
    main()
