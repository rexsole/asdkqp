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
    api_id=14724834,
    api_hash="837e89b4fad3c162e1aeb28b25205805",
    bot_token="5405130503:AAGav8Nj_blK6od0XmfDvIiT8mFWhM8EX3k",
    plugins=dict(root="WhisperBot"),
)


# Run Bot
print("bot online")
app.start()
pyrogram.idle()

