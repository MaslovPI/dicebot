import discord
from discord.ext import commands
from functions.roll import roll_dice


class DiscordClient(commands.Bot):
    def __init__(self, token: str):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix="", intents=intents)
        self.token = token

    async def setup_hook(self):
        @self.tree.command(
            name="roll", description="Roll dice in NdM format (e.g. 2d6)"
        )
        async def roll(interaction: discord.Interaction, dice: str):
            try:
                result = roll_dice(dice)
            except ValueError as e:
                await interaction.response.send_message(f"❌ {e}", ephemeral=True)
                return

            await interaction.response.send_message(result)

        await self.tree.sync()

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

    def run_bot(self):
        self.run(self.token)
