import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from functions.roll import roll_multiple


def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        raise ValueError("Discord token is not provided")
    intents = discord.Intents()
    intents.message_content = True

    bot = Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} has connected to Discord!")

    @bot.tree.command(name="roll", description="Roll dice in NdM format")
    async def roll(interaction: discord.Interaction, dice: str):
        await interaction.response.send_message(roll_dice(dice))

    bot.run(str(TOKEN))


class Bot(commands.Bot):
    async def setup_hook(self):
        await self.tree.sync()


def roll_dice(dice_to_roll):
    dice_info = dice_to_roll.split("d")
    if not len(dice_info) == 2:
        return "Invalid format. Use NdM (e.g. 2d6)"

    number = int(dice_info[0]) if dice_info[0] else 1
    dimensions = int(dice_info[1])
    result = roll_multiple(number, dimensions)
    return f"{dice_to_roll} roll result: {result.describe()}"


if __name__ == "__main__":
    main()
