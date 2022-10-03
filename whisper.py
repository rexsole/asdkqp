import logging
from pyrogram import Client, idle
import Config
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    "Whisper-Bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="WhisperBot"),
)


# Run Bot
print("bot online")
app.start()
pyrogram.idle()

