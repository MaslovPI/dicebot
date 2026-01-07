import os
from dotenv import load_dotenv
from classes.discordclient import DiscordClient


def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        raise ValueError("Discord token is not provided")

    client = DiscordClient(TOKEN)
    client.run_bot()


if __name__ == "__main__":
    main()
