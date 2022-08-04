import os
import string
import asyncio
from pyrogram import Client, filters


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

app = Client("tgid", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID)


@app.on_message(filters.command(['start']))
async def start(client, message):
    await m.reply_text(text=f"Hello 👋", reply_to_message_id=message.message_id)


@app.on_message(filters.command(['id']))
async def id(client, message):
    await client.send_chat_action(message.chat.id, "typing")
    await message.reply_text(text=f"`{message.chat.id}`", reply_to_message_id=message.message_id)


app.run()
