from pyrogram import Client, filters
from pyrogram.types import Message, ChatMember
import logging
from Spy import app

logging.basicConfig(level=logging.INFO)

@app.on_message(filters.video_chat_started)
async def video_chat_started(client, message: Message):
    chat = message.chat
    await message.reply(
        f"🎥 𝗩𝗜𝗗𝗘𝗢 𝗖𝗛𝗔𝗧 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 🥹 𝗜𝗡 {chat.title}."
    )

@app.on_message(filters.video_chat_ended)
async def video_chat_ended(client, message: Message):
    chat = message.chat
    await message.reply(
        f"🎥 𝗩𝗜𝗗𝗘𝗢 𝗖𝗛𝗔𝗧 𝗛𝗔𝗦 𝗘𝗡𝗗𝗘𝗗 💔 𝗜𝗡 {chat.title}."
    )
