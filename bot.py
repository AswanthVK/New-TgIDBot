import os
import string
import asyncio
from pyrogram import Client, filters


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

app = Client("tgid", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID)


@app.on_message(filters.command(['start']))
async def start(c, m):
    await m.reply_text(text=f"Hello 👋", reply_to_message_id=m.message_id)


@app.on_message(filters.command(['id']))
async def id(c, m):
    await c.send_chat_action(m.chat.id, "typing")
    await m.reply_text(text=f"`{m.chat.id}`", reply_to_message_id=m.message_id)


app.run()
