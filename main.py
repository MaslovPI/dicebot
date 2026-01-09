import logging
import os

from dotenv import load_dotenv

from classes.discordclient import DiscordClient
from functions.logging import configure_logger

logger = logging.getLogger(__name__)
configure_logger(logger)


def main():
    logger.info("Started")
    try:
        load_dotenv()
        TOKEN = os.getenv("DISCORD_TOKEN")
        if not TOKEN:
            msg = "Discord token is not provided"
            logger.error(msg)
            raise ValueError(msg)

        client = DiscordClient(TOKEN)
        client.run_bot()
    finally:
        logger.info("Finished")


if __name__ == "__main__":
    main()
